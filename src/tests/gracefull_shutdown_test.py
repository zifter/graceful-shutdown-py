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

    shutdown.trigger()

    assert shutdown.triggered is True


def test_cast_to_bool_ok():
    """
    Check correctness of casting to bool
    """
    shutdown = ExitSignalHandler()

    assert bool(shutdown) is False

    shutdown.trigger()

    assert bool(shutdown) is True
