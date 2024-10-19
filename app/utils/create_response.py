from app.models.response import ResponseModel


def create_response(status_code: int, message: str, data: any = None, error_code: str = None, success: bool = True):
    return ResponseModel.create_response(
        status_code=status_code,
        message=message,
        data=data,
        error_code=error_code,
        success=success
    )
