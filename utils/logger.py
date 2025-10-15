"""
This will contain logging for the launcher only.
All other projects will have their own logger.
"""

import logging
import os

from constants import CONSOLE_LOGGING_ENABLED, LOG_DATE_FORMAT, LOG_DIRECTORY, LOG_FORMAT, LOGS_FILE_NAME


class Logger:
    """
    This class handles the logger for the launcher.
    """
    def __init__(self):
        """
        This method initializes the logger.
        """
        self._loggers = {}

    def get_logger(self, name):
        """
        This method returns or creates a logger with proper setup.
        """
        if name not in self._loggers:
            logger = logging.getLogger(name)
            logger.setLevel(logging.DEBUG)

            # Create formatters
            formatter = logging.Formatter(
                LOG_FORMAT,
                datefmt=LOG_DATE_FORMAT
            )

            # Console handler (only if enabled)
            if CONSOLE_LOGGING_ENABLED:
                console_handler = logging.StreamHandler()
                console_handler.setFormatter(formatter)
                logger.addHandler(console_handler)

            # File handler
            # TODO: Add rotation to the file handler
            if not os.path.exists(LOG_DIRECTORY):
                os.makedirs(LOG_DIRECTORY)
            file_handler = logging.FileHandler(
                os.path.join(LOG_DIRECTORY, LOGS_FILE_NAME),
                mode='a'
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            self._loggers[name] = logger

        return self._loggers[name]

    def log(self, message, level, name):
        """
        This method logs a message.
        """
        logger = self.get_logger(name)
        logger.log(level, message)

    def debug(self, message, name):
        """Log a debug message."""
        self.log(message, logging.DEBUG, name)

    def info(self, message, name):
        """Log an info message."""
        self.log(message, logging.INFO, name)

    def warning(self, message, name):
        """Log a warning message."""
        self.log(message, logging.WARNING, name)

    def error(self, message, name):
        """Log an error message."""
        self.log(message, logging.ERROR, name)

    def critical(self, message, name):
        """Log a critical message."""
        self.log(message, logging.CRITICAL, name)
