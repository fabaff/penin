"""Support for retrieving details about IP addresses in use."""
from cement import Controller, ex

from penin.core.ip import (
    get_external_ip, get_gateways, get_internal_ip,
    get_location, get_asn)


class Ip(Controller):
    """Representation of all IP-related commands."""

    class Meta:
        """Metadata for the IP support."""

        label = "ip"
        stacked_type = "nested"
        stacked_on = "base"

    @ex(
        help="retrieve the local IP address",
    )
    def local(self):
        """Retrieve the local IP address."""
        result = get_internal_ip()

        if result is None:
            self.app.log.error("Unable to get details about the local NICs")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")

    @ex(
        help="retrieve the external IP address",
    )
    def external(self):
        """Retrieve the external IP address."""
        result = get_external_ip()

        if result is None:
            self.app.log.error("Unable to get the external IP address")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")


    @ex(
        help="perform a reverse lookup of an IP address",
        arguments=[(["ip_address"], {"help": "IP address to lookup"})],
    )
    def geolocation(self):
        """Get the geolocation of an IP address."""
        result = get_location(self.app.pargs.ip_address)

        if result is None:
            self.app.log.error("Unable to get location of IP address")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")


    @ex(
        help="perform a reverse lookup of an IP address",
    )
    def gateways(self):
        """Get all gateways for the interfaces."""
        result = get_gateways()

        if result is None:
            self.app.log.error("Unable to get the gateways")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")

    @ex(
        help="perform a reverse lookup of an IP address",
        arguments=[(["ip_address"], {"help": "IP address to lookup"})],
    )
    def asn(self):
        """Get the ASN detail of an IP address."""
        result = get_asn(self.app.pargs.ip_address)

        if result is None:
            self.app.log.error("Unable to get the ASN details")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")
