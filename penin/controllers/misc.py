"""Support for various helper commands."""
import base64

from cement import Controller, ex
from penin.core import create_hash, get_host_details, identify_hash
from penin.core.mdns import discover_devices

ALGORITHMS = [
    "md5",
    "sha1",
    "sha256",
    "sha384",
    "sha512",
    "ripemd160",
    "whirlpool",
]


class Misc(Controller):
    """Representation of various helper commands."""

    class Meta:
        """Meta data for the IP support."""

        label = "misc"
        stacked_type = "nested"
        stacked_on = "base"

    @ex(help="retrieve the details about the host")
    def host(self):
        """Retrieve details about the host."""
        result = get_host_details()

        if result is None:
            self.app.log.error("Unable to get details about host")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")

    @ex(
        help="create a hash of the given string",
        arguments=[
            (["string"], {"help": "string to hash"}),
            (
                ["-a", "--algorithm"],
                {
                    "help": "algorithm to use",
                    "default": "sha256",
                    "choices": ALGORITHMS,
                },
            ),
        ],
    )
    def hash(self):
        """Create hash of a given string."""

        result = create_hash(self.app.pargs.string, self.app.pargs.algorithm)
        data = {"result": result}
        self.app.render(data, "default.jinja2")

    @ex(
        help="handles the encoding/decoding of a string",
        arguments=[
            (["string"], {"help": "string to hash"}),
            (
                ["-e", "--encode"],
                {"help": "encode the string", "action": "store_true"},
            ),
            (
                ["-d", "--decode"],
                {"help": "decode a string", "action": "store_true"},
            ),
        ],
    )
    def base64(self):
        """Decode or encode a string as Base64."""
        if self.app.pargs.decode:
            result = base64.b64decode(self.app.pargs.string).decode(
                "utf-8", "ignore"
            )
        if self.app.pargs.encode:
            result = base64.b64encode(self.app.pargs.string.encode()).decode(
                "utf-8", "ignore"
            )
        if result is None:
            self.app.log.error("Unable to handle the string")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")

    @ex(help="search for mDNS, Bonjour or ZeroConf capable devices")
    def discover(self):
        """Search for local devices and services."""
        result = discover_devices()

        if result is None:
            self.app.log.error("Unable to discover devices")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")

    @ex(
        help="perform a reverse lookup of an IP address",
        arguments=[(["input_hash"], {"help": "Hash to identify"})],
    )
    def ident_hash(self):
        """Retrieve details about the host."""
        result = identify_hash(self.app.pargs.input_hash)

        if result is None:
            self.app.log.error("Unable to get details about host")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")