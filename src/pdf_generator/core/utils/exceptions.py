"""PDF GENERATOR Exceptions"""
import logging

logger = logging.getLogger(__name__)


class PdfGeneratorException(Exception):
    """Exception raised by every module in the PFD Generator package."""

    def __init__(self, msg=None):
        """

        Args:
            msg (str): human friendly error message.
        """

        if msg is None:
            msg = "PDF GENERATOR Exception"
        logger.exception(msg)
        super().__init__(msg)


class DbException(PdfGeneratorException):
    """Exception raised by every function in the ServiceDB sub-module"""

    pass

class DataNotFoundException(PdfGeneratorException):
    """Exception raised by every function in the DataNotFound sub-module"""

    pass

