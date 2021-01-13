"""
Tests for gracefull shutdown
"""
from gracefull_shutdown import ExitSignalHandler


def test_trigger_ok():
    """
    Check correct creation and triggering
    """
    shutdown = ExitSignalHandler()

    assert shutdown.triggered is False

    shutdown.exit_gracefully(None, None)

    assert shutdown.triggered is True
