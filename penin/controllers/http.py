"""Support for retrieving details about HTTP servers."""
from cement import Controller, ex

from penin.core.http import get_headers, get_options, get_subjugation, \
    get_tech, get_social_media


class Http(Controller):
    """Representation of all HTTP-related commands."""

    class Meta:
        """Metadata for the HTTP support."""

        label = "http"
        stacked_type = "nested"
        stacked_on = "base"

    @ex(
        help="retrieve the HTTP headers of a web server",
        arguments=[(["target"], {"help": "IP address of the target server"})],

    )
    def headers(self):
        """Retrieve the HTTP headers of a web server."""
        result = get_headers(self.app.pargs.target)

        if result is None:
            self.app.log.error("Unable to get headers")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")

    @ex(
        help="retrieve the HTTP options of a web server",
        arguments=[(["target"], {"help": "IP address of the target server"})],

    )
    def options(self):
        """Retrieve the HTTP options of a web server."""
        result = get_options(self.app.pargs.target)

        if result is None:
            self.app.log.error("Unable to get options")
            return

        data = {"result": result}
        self.app.render(data, "default.jinja2")

    @ex(
        help="retrieve the location of a subjugation",
        arguments=[(["target"], {"help": "IP address of the target server"})],

    )
    def subjugation(self):
        """Retrieve the location of a subjugation."""
        data = {}

        result = get_subjugation(self.app.pargs.target)

        if result is None:
            self.app.log.error("Unable to get subjugation")
            return

        if result is False:
            self.app.log.info("No subjugation present")
            data = {"result": None}
        else:
            data = {"result": result}

        self.app.render(data, "default.jinja2")

    @ex(
        help="identify the used technology of a web server",
        arguments=[(["target"], {"help": "IP address of the target server"})],

    )
    def tech(self):
        """Identify the used technology of the web server."""
        result = get_tech(self.app.pargs.target)

        if result is None:
            self.app.log.error("Unable to determine the technology")
            return

        data = {"result": result}

        self.app.render(data, "default.jinja2")

    @ex(
        help="identify listed social media accounts",
        arguments=[(["target"], {"help": "The URL to check"})],

    )
    def social_media(self):
        """Extract social media accounts from a website."""
        result = get_social_media(self.app.pargs.target)

        if result is None:
            self.app.log.error("Unable to determine the technology")
            return

        data = {"result": {'accounts': result}}

        self.app.render(data, "default.jinja2")
