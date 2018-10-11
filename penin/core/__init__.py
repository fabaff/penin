"""Init file for the core parts of PenIn."""
import platform
import socket
import hashlib


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


