"""
Package with gracefull shutdown functionality
"""
import signal
from logging import getLogger

_logger = getLogger("gracefull-shutdown")


class ExitSignalHandler:
    """
    Simple exit signal handler
    """

    def __init__(self):
        """
        Initialization for signal handling
        """
        self._triggered: bool = False

        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, _signum, _frame):
        """
        Signal handler
        """
        _logger.warning("[!] got exit signal")

        self._triggered = True

    @property
    def triggered(self) -> bool:
        """
        Check if exit signal triggered
        """
        return self._triggered


__all__ = [
    "ExitSignalHandler",
]
