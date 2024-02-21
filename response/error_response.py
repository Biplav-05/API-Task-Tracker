from rest_framework import status
from rest_framework.response import Response

status_code_map = {
    200: status.HTTP_200_OK,
    201: status.HTTP_201_CREATED,
    204: status.HTTP_204_NO_CONTENT,
    400: status.HTTP_400_BAD_REQUEST,
    401: status.HTTP_401_UNAUTHORIZED,
    403: status.HTTP_403_FORBIDDEN,
    404: status.HTTP_404_NOT_FOUND,
    500: status.HTTP_500_INTERNAL_SERVER_ERROR,
}

class Error(Exception):
    def __init__(self):
        self.errors = []

    def add_errors(self, name, message):
        self.errors = {'title': name, 'message': message}
        return self.errors

class ErrorResponse(Response):

    def __init__(self, errors, status_code=400):
        self.status_code = status_code_map.get(status_code)
        self.errors = {'errors': errors}
        super().__init__(data=self.errors, status=self.status_code)