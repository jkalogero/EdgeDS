from swagger_server.models.problem_details import ProblemDetails  # noqa: F401,E501
from flask_api import status

def problem():
    r = ProblemDetails()
    r.status = 0
    r.detail = "The provided URI that cannot be mapped to a valid resource URI."
    return r, status.HTTP_404_NOT_FOUND