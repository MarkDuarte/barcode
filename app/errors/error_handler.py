from app.views.http_types.http_response import HttpResponse
from .erro_types.http_unprocessable_types import HttpUnprocessableEntityError

def handler_errors(error: Exception) -> HttpResponse:
  if isinstance(error, HttpUnprocessableEntityError):
    return HttpResponse(
      status_code=error.status_code,
      body={
        "errors": [{
          "title": error.name,
          "details": error.message
        }]
      }
    )

  return HttpResponse(
    status_code=500,
    body={
      "errors": [{
        "title": "Server Error",
        "detail": str(error)
      }]
    }
  )