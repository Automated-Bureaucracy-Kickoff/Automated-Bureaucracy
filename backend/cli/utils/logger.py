import logging
import os
from datetime import datetime


class Logger:
    """
    Utility class for centralized logging.
    """

    def __init__(self, log_file="app.log", log_level=logging.INFO):
        """
        Initialize the Logger instance.

        Args:
            log_file (str): Path to the log file.
            log_level (int): Logging level (e.g., logging.DEBUG, logging.INFO).
        """
        self.logger = logging.getLogger("AutomatedBureaucracyLogger")
        self.logger.setLevel(log_level)

        # Create log directory if it doesn't exist
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Configure file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)

        # Configure console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # Configure log formatting
        log_format = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(module)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(log_format)
        console_handler.setFormatter(log_format)

        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        """
        Retrieve the logger instance.

        Returns:
            logging.Logger: Configured logger instance.
        """
        return self.logger


# Example usage
if __name__ == "__main__":
    log_file_path = f"logs/app_{datetime.now().strftime('%Y%m%d')}.log"
    logger = Logger(log_file=log_file_path, log_level=logging.DEBUG).get_logger()

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
