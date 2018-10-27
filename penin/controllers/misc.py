"""Support for retrieving details about IP addresses in use."""
from cement import Controller, ex

from penin.core import get_host_details, create_hash

ALGORITHMS = [
    'md5',
    'sha1',
    'sha256',
    'sha384',
    'sha512',
    'ripemd160',
    'whirlpool',
]


class Misc(Controller):
    """Representation of all IP-related commands."""

    class Meta:
        """Meta data for the IP support."""

        label = "misc"
        stacked_type = "nested"
        stacked_on = "base"

    @ex(
        help="retrieve the details about the host",
    )
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
        arguments=[(["string"], {"help": "string to hash"}),
            (
            ["-a", "--algorithm"],
            {
                "help": "algorithm to use",
                "default": 'sha256',
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