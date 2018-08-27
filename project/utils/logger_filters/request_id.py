import logging

import aiotask_context as context


class RequestIdLogFilter(logging.Filter):
    """Filter for X-Request-ID"""

    def filter(self, log_record):
        """Filter implementation"""
        log_record.request_id = context.get("X-Request-ID")
        return True
