class APIError(Exception):
    pass

class AuthError(APIError):
    def __init__(self, status, response):
        message = f'Auth Error ({status}) - {response}'
        super().__init__(message)

class SessionError(APIError):
    def __init__(self, status, response):
        message = f'Session Error ({status}) - {response}'
        super().__init__(message)

class ApiConnectionError(APIError):
    def __init__(self, message):
        super().__init__(f'Connection Error: {message}')