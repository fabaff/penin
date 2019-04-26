"""Support for retrieving details about HTTP servers."""
from cement import Controller, ex

from penin.core.port_scan import run_masscan


class PortSan(Controller):
    """Representation of all port scan-related commands."""

    class Meta:
        """Metadata for the port scanner support."""

        label = "port-scan"
        stacked_type = "nested"
        stacked_on = "base"

    @ex(
        help="run masscan",
        arguments=[(["target"], {"help": "IP address of the target server"}),
                   (["ports"], {"help": "Ports to scan", 'default': '1-65535'})],

    )
    def masscan(self):
        """Run masscan."""
        result = run_masscan(self.app.pargs.target, self.app.pargs.ports)

        if result is None:
            self.app.log.error("Unable to get results from masscan")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")
