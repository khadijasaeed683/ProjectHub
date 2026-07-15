import logging
from datetime import datetime

logger = logging.getLogger("request_logger")


class RequestLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(">>> Logging Middleware Executed <<<")
        ip = request.META.get("REMOTE_ADDR")
        logger.info(f"{datetime.now()} | {ip} | {request.method} | {request.path}")
        response = self.get_response(request)
        return response
