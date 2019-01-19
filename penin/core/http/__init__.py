"""Support for getting information from HTTP servers."""
import requests
import urllib3

urllib3.disable_warnings()


def get_headers(server):
    """Retrieve all HTTP headers."""
    try:
        response = requests.head(
            server, allow_redirects=False, verify=False, timeout=5)
    except requests.exceptions.ConnectionError:
        return None

    return dict(response.headers)


def get_subjugation(server):
    """Check if the URL is redirected."""
    headers = get_headers(server)

    if 'Location' in headers:
        return headers['Location']
    else:
        return False


def get_options(server):
    """Retrieve all allowed HTTP verbs/methods."""
    try:
        response = requests.options(
            server, allow_redirects=False, verify=False, timeout=5)
    except (requests.exceptions.ConnectionError,
            requests.exceptions.MissingSchema):
        return None

    try:
        return response.headers['Allow']
    except KeyError:
        return None
