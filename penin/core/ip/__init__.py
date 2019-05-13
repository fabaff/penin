"""Support for retrieving details about IP addresses in use."""
import ipaddress

from netifaces import (
    AF_INET, AF_INET6, AF_LINK, gateways, ifaddresses, interfaces)
import requests


def get_external_ip():
    """Get the external IP address for the connection."""
    try:
        ip_address = requests.get("https://api.ipify.org", timeout=5).text
        return ip_address
    except requests.exceptions.ConnectionError:
        return None


def get_internal_ip():
    """Get the local IP addresses."""
    nics = {}
    for interface_name in interfaces():
        addresses = ifaddresses(interface_name)
        try:
            nics[interface_name] = {
                "ipv4": addresses[AF_INET],
                "link_layer": addresses[AF_LINK],
                "ipv6": addresses[AF_INET6],
            }
        except KeyError:
            pass

    return nics


def get_location(ip_address):
    """Get the geolocation of an IP address."""
    try:
        type(ipaddress.ip_address(ip_address))
    except ValueError:
        return {}
    try:
        data = requests.get(
            "https://ipapi.co/{}/json/".format(ip_address), timeout=5
        ).json()
        return data
    except requests.exceptions.ConnectionError:
        return None


def get_gateways():
    """Get all gateways for the interfaces."""
    return gateways()


def get_asn(ip_address):
    """Get the ASN details of a give IP address."""
    try:
        data = requests.get(
            "https://api.iptoasn.com/v1/as/ip/{}".format(ip_address), timeout=5
        ).text
        return data
    except requests.exceptions.ConnectionError:
        return None


def get_network_details(network):
    """List all IP addresses in the network."""
    from ipaddress import ip_network

    network_data = ip_network(network)
    data = {
        "network": network,
        "netmask": network_data.netmask,
        "hostmask": network_data.hostmask,
        "total_hosts": network_data.num_addresses,
        "network_address": network_data.network_address,
        "broadcast_address": network_data.broadcast_address,
        "private": network_data.is_private,
    }

    print(data)


def get_ips(network):
    """List all IP addresses in the network."""
    from ipaddress import ip_network

    data = list(ip_network(network).hosts())

    print(data)
