"""Init file for the core parts of PenIn."""
import platform
import socket
import hashlib

import hashid


def get_host_details():
    """Get details about the host that is executing PenIn."""
    try:
        data = {
            'arch': platform.machine(),
            'cpu': platform.processor(),
            'distribution': platform.linux_distribution(),
            'fqdn': socket.getfqdn(),
            'kernel': platform.uname(),
            'libc': platform.libc_ver(),
            'os_name': platform.system(),
            'python_version': platform.python_version(),
            'static_hostname': platform.node(),
        }
    except AttributeError:
        return None

    return data


def create_hash(data, algorithm):
    """Create the hash of a given string."""
    if algorithm not in hashlib.algorithms_available:
        return None

    try:
        _hash = hashlib.new(algorithm)
        _hash.update(data.encode())
        data = _hash.hexdigest()
    except UnicodeEncodeError:
        return None

    return data


def identify_hash(input_hash):
    """Identify a hash."""
    _hash = hashid.HashID()
    hash_details = _hash.identifyHash(input_hash)
    types = {}
    types_list = []
    for mode in hash_details:
        hash_type = {}
        if not mode.extended:
            hash_type['hash_type'] = mode.name
            formats = {}
            if mode.hashcat is not None:
                formats['hashcat'] = mode.hashcat
            if mode.john is not None:
                formats['john'] = mode.john
        hash_type['formats'] = formats
        types_list.append(hash_type)
        types['types']=types_list
    return types
