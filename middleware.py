import time
from flask import request

class RequestTimingMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        start_time = time.time()
        def custom_start_response(status, headers, exc_info=None):
            end_time = time.time()
            duration = end_time - start_time
            headers.append(('X-Request-Duration', str(duration)))
            print(f"Request took {duration:.4f} seconds")
            return start_response(status, headers, exc_info)
        return self.app(environ, custom_start_response)
