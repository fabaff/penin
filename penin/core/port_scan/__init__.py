"""Support for performing port scans."""


def run_masscan(target, ports):
    """Create the hash of a given string."""
    import masscan

    mas = masscan.PortScanner()
    mas.scan(target, ports=ports)
    return mas.scan_result
