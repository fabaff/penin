"""Helper to get the release right."""
from cement.utils.version import get_version as cement_get_version
from penin.constants import VERSION


def get_version(version=VERSION):
    """Get the current version of the framework."""
    return cement_get_version(version)
