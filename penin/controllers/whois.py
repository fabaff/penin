"""Support for retrieving whois information."""
from cement import Controller, ex

from penin.core.whois import get_whois


class Whois(Controller):
    """Representation of all whois-related commands."""

    class Meta:
        """Metadata for the whois support."""

        label = "whois"
        stacked_type = "nested"
        stacked_on = "base"

    @ex(
        help="retrieve whois details",
        arguments=[(["target"], {"help": "IP address/domain to lookup"})],

    )
    def info(self):
        """Retrieve the local IP address."""
        result = get_whois(self.app.pargs.target)

        if result is None:
            self.app.log.error("Unable to get details about the local NICs")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")
