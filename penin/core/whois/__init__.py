"""Support for retrieving whois information about sources."""
import ipaddress

from ipwhois import IPWhois
import whois


def get_whois(target):
    """Get the details of a domain."""
    try:
        if type(ipaddress.ip_address(target)) is ipaddress.IPv4Address:
            lookup = IPWhois(target)
            result = lookup.lookup_rdap()
            return result
        if type(ipaddress.ip_address(target)) is ipaddress.IPv6Address:
            return None
    except (ValueError, Exception):

        result = whois.query(target)
        return result.__dict__
