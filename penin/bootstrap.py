"""Load the PenIn framework."""
from penin.controllers.base import Base


def load(app):
    """Load the framework."""
    app.handler.register(Base)
