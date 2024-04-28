import logging
import os
import sys

# Set styling tags
HEADER = '\033[95m'
TIMESTAMP = '\033[90m'
ORIGIN = '\033[94m'
DEBUG = '\033[96m'
INFO = '\033[92m'
WARNING = '\033[93m'
ERROR = '\033[91m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
ENDC = '\033[0m'

# Get logger
logger = logging.getLogger()

# Set labels
timestamp_format = '%Y-%m-%d %H:%M:%S'
timestamp = '[%(asctime)s.%(msecs)03d]'
origin_label = '[%(filename)-18.18s:%(lineno)-4.4d] [%(funcName)-30.30s]'
level_label = '[%(levelname)-4.4s]'


# Create formatters
level = '(LEVEL)'
stream_formatter_template = f'{TIMESTAMP}{timestamp}{ENDC} {ORIGIN}{origin_label}{ENDC} {level}{level_label}{ENDC}  %(message)s'

stream_debug_format = stream_formatter_template.replace(level, DEBUG)
stream_info_format = stream_formatter_template.replace(level, INFO)
stream_warning_format = stream_formatter_template.replace(level, WARNING)
stream_error_format = stream_formatter_template.replace(level, ERROR)

stream_debug_formatter = logging.Formatter(stream_debug_format, datefmt=timestamp_format)
stream_info_formatter = logging.Formatter(stream_info_format, datefmt=timestamp_format)
stream_warning_formatter = logging.Formatter(stream_warning_format, datefmt=timestamp_format)
stream_error_formatter = logging.Formatter(stream_error_format, datefmt=timestamp_format)


# Create handlers
stream_debug_handler = logging.StreamHandler(sys.stdout)
stream_info_handler = logging.StreamHandler(sys.stdout)
stream_warning_handler = logging.StreamHandler(sys.stderr)
stream_error_handler = logging.StreamHandler(sys.stderr)

# Set formatters
stream_debug_handler.setFormatter(stream_debug_formatter)
stream_info_handler.setFormatter(stream_info_formatter)
stream_warning_handler.setFormatter(stream_warning_formatter)
stream_error_handler.setFormatter(stream_error_formatter)

# Set logging levels
stream_debug_handler.setLevel(logging.DEBUG)
stream_info_handler.setLevel(logging.INFO)
stream_warning_handler.setLevel(logging.WARNING)
stream_error_handler.setLevel(logging.ERROR)


# Create filters
class DebugFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.DEBUG


class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO


class WarningFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.WARNING


class ErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR


# Set filters
stream_debug_handler.addFilter(DebugFilter())
stream_info_handler.addFilter(InfoFilter())
stream_warning_handler.addFilter(WarningFilter())
stream_error_handler.addFilter(ErrorFilter())


# Add handlers to logger
logger.handlers = [
    stream_debug_handler,
    stream_info_handler,
    stream_warning_handler,
    stream_error_handler
]

# Set logger level
logger.setLevel(logging.DEBUG)
logger.propagate = False

# Mute pypdf._reader
logging.getLogger('pypdf._reader').setLevel(logging.CRITICAL)
