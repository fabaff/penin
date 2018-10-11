"""."""
from cement import Controller, ex
from cement.utils.version import get_version_banner
from penin.core.version import get_version

VERSION_BANNER = """
Information gathering and penetration testing framework {}
{}
""".format(
    get_version(), get_version_banner()
)


class Base(Controller):
    """Representation of a base controller."""

    class Meta:
        """Metadata for the BAse controller."""

        label = "base"

        # Text displayed at the top of --help output
        description = "Information gathering and penetration testing framework"

        # Text displayed at the bottom of --help output
        epilog = "Usage: penin command1 --foo bar"

        # Controller level arguments. ex: 'penin --version'
        arguments = [
            (
                ["-v", "--version"],
                {"action": "version", "version": VERSION_BANNER},
            )
        ]

    def _default(self):
        """Default action if no sub-command is passed."""
        self.app.args.print_help()
