"""Support for dealing with DNS-related information."""
import ipaddress
import socket

from dns import flags, message, name, query, rdatatype, resolver, reversename

ADDITIONAL_RDCLASS = 65535


def forward_lookup(hostname):
    """Perform a forward lookup of a hostname."""
    ip_addresses = {}

    addresses = list(
        set(str(ip[4][0]) for ip in socket.getaddrinfo(hostname, None))
    )

    if addresses is None:
        return ip_addresses

    for address in addresses:
        if type(ipaddress.ip_address(address)) is ipaddress.IPv4Address:
            ip_addresses["ipv4"] = address
        if type(ipaddress.ip_address(address)) is ipaddress.IPv6Address:
            ip_addresses["ipv6"] = address

    return ip_addresses


def reverse_lookup(ip_address):
    """Perform a reverse lookup of an IP address."""
    try:
        type(ipaddress.ip_address(ip_address))
    except ValueError:
        return None

    record = reversename.from_address(ip_address)
    hostname = str(resolver.query(record, "PTR")[0])[:-1]
    return hostname


def get_records(domain, nameserver):
    """Retrieve the records of a nameserver."""
    try:
        request = message.make_query(domain, rdatatype.ANY)
        request.flags |= flags.AD
        request.find_rrset(
            request.additional,
            name.root,
            ADDITIONAL_RDCLASS,
            rdatatype.OPT,
            create=True,
            force_unique=True,
        )
        response = query.udp(request, nameserver)
        return response
    except OSError:
        return None
