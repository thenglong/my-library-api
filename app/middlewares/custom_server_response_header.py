from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


# this middleware is used to override "server: uvicorn" from response header
class CustomServerResponseHeader(BaseHTTPMiddleware):
    def __init__(
            self,
            app,
            server_name: str = "avengers",
    ):
        super().__init__(app)
        self.server_name = server_name

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        if self.server_name == "" or self.server_name is None:
            del response.headers['server']
        else:
            response.headers['server'] = self.server_name
        return response
