"""
Package with graceful shutdown functionality
"""
import signal
from logging import getLogger

_logger = getLogger("graceful-shutdown")


class ExitSignalHandler:
    """
    Simple exit signal handler
    """

    def __init__(self):
        """
        Initialization for signal handling
        """
        self._triggered: bool = False

        signal.signal(signal.SIGINT, self.exit_gracefuly)
        signal.signal(signal.SIGTERM, self.exit_gracefuly)

    def exit_gracefuly(self, _signum, _frame):
        """
        Signal handler
        """
        _logger.warning("[!] got exit signal")

        self.trigger()

    def trigger(self):
        """
        Signal handler
        """
        _logger.warning("Trigger shutdown")

        self._triggered = True

    @property
    def triggered(self) -> bool:
        """
        Check if exit signal triggered
        """
        return self._triggered

    def __bool__(self) -> bool:
        """
        Cast to bool
        """
        return self.triggered


__all__ = [
    "ExitSignalHandler",
]
