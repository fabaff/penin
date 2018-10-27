"""Main file for PenIn."""
from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from penin.controllers.base import Base
from penin.controllers.misc import Misc
from penin.core.exc import PenInError
from penin.helpers import extend_tinydb

# Configuration defaults
CONFIG = init_defaults('penin')
CONFIG['penin']['foo'] = 'bar'
CONFIG['penin']['db_file'] = '~/.penin/storage.json'


class PenIn(App):
    """PenIn primary application."""

    class Meta:
        """Meta handler for tasks to perform for initialisation."""
        label = 'penin'

        # Configuration defaults
        config_defaults = CONFIG

        # Call sys.exit() on close
        close_on_exit = True

        # Load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # Configuration handler
        config_handler = 'yaml'

        # Configuration file suffix
        config_file_suffix = '.yml'

        # Set the log handler
        log_handler = 'colorlog'

        # Set the output handler
        output_handler = 'jinja2'

        # Register handlers
        handlers = [
            Base,
            Misc,
        ]

        # Register hooks
        hooks = [
            ('post_setup', extend_tinydb),
        ]


class PenInTest(TestApp, PenIn):
    """A sub-class of PenIn that is better suited for testing."""

    class Meta:
        """Metadata for testing the framework."""
        label = 'penin'


def main():
    """Main part of PenIn."""
    with PenIn() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > {}'.format(e.args[0]))
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except PenInError as e:
            print('PenInError > %s'.format(e.args[0]))
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s'.format(e))
            app.exit_code = 0


if __name__ == '__main__':
    main()
