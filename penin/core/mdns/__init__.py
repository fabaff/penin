"""Support for discovering local devices and services."""
from netdisco.discovery import NetworkDiscovery


def discover_devices():
    """Discover local devices and services."""
    data = {}
    netdis = NetworkDiscovery()

    netdis.scan()

    for device_type in netdis.discover():
        data[device_type] = netdis.get_info(device_type)

    return data

    netdis.stop()
