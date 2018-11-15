"""Support for performing DNS queries and lookups."""
from cement import Controller, ex
from penin.core.dns import forward_lookup, get_records, reverse_lookup


class Dns(Controller):
    """Representation of all DNS-related commands."""

    class Meta:
        """Metadata for the DNS support."""

        label = "dns"
        stacked_type = "nested"
        stacked_on = "base"

    @ex(
        help="perform a forward lookup of a hostname",
        arguments=[(["hostname"], {"help": "hostname to lookup"})],
    )
    def forward(self):
        """Perform a forward lookup of a hostname."""
        ip_addresses = forward_lookup(self.app.pargs.hostname)

        data = {"result": ip_addresses}
        self.app.render(data, "default.jinja2")

    @ex(
        help="perform a reverse lookup of an IP address",
        arguments=[(["ip_address"], {"help": "IP address to lookup"})],
    )
    def reverse(self):
        """Perform a reverse lookup of an IP address."""
        ip_address = self.app.pargs.ip_address
        hostname = reverse_lookup(ip_address)

        if hostname is None:
            self.app.log.error("Unable to resolve {}".format(ip_address))
            return

        data = {"result": hostname}
        self.app.render(data, "default.jinja2")

    @ex(
        help="retrieve the records of a domain",
        arguments=[
            (["domain"], {"help": "domain to lookup"}),
            (
                ["-n", "--nameserver"],
                {
                    "help": "nameserver to use for " "the lookup",
                    "default": "8.8.8.8",
                },
            ),
        ],
    )
    def records(self):
        """Retrieve the records of a nameserver."""
        domain = self.app.pargs.domain
        nameserver = self.app.pargs.nameserver

        response = get_records(domain, nameserver)

        data = {"result": response}
        self.app.render(data, "default.jinja2")
