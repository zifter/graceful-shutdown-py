"""
Tests for graceful shutdown
"""
from graceful_shutdown import ExitSignalHandler


def test_trigger_like_signal_ok():
    """
    Check correct creation and trigger as signal handler
    """
    shutdown = ExitSignalHandler()

    assert shutdown.triggered is False

    shutdown.exit_gracefuly(None, None)

    assert shutdown.triggered is True


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
