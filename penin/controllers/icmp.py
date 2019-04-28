"""Support for performing ICMP requests."""
from cement import Controller, ex

from penin.core.icmp import create_icmp_request


class Icmp(Controller):
    """Representation of all ICMP-related commands."""

    class Meta:
        """Metadata for the ICMP support."""

        label = "icmp"
        stacked_type = "nested"
        stacked_on = "base"

    @ex(
        help="create an ICMP echo (type 0) request",
        arguments=[
            (
                ["destination"],
                {
                    "help": "destination for the request",
                },
            )
        ],
    )
    def echo(self):
        """Create an ICMP echo (type 0) request."""
        result = create_icmp_request(self.app.pargs.destination, 8)

        if result is None:
            self.app.log.error("Host doesn't respond or is offline")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")

    @ex(
        help="create an ICMP timestamp (type 13) request",
        arguments=[(["destination"], {"help": "destination for the request"})],
    )
    def timestamp(self):
        """Create an ICMP timestamp (type 13) request."""
        result = create_icmp_request(self.app.pargs.destination, 13)

        if result is None:
            self.app.log.error("Host doesn't respond or is offline")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")
