"""Support for retrieving whois information about sources."""
import ipaddress

import whois
from ipwhois import IPWhois


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
