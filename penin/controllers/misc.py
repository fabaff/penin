"""Support for various helper commands."""
import base64

from cement import Controller, ex

from penin.core import get_host_details, create_hash

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
    """Representation of all IP-related commands."""

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
        """Retrieve details about the host."""
        if self.app.pargs.decode:
            result = base64.b64decode(
                self.app.pargs.string).decode("utf-8", "ignore")
        if self.app.pargs.encode:
            result = base64.b64encode(
                self.app.pargs.string.encode()).decode("utf-8", "ignore")
        if result is None:
            self.app.log.error("Unable to handle the string")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")
