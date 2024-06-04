from fastapi import HTTPException
from fastapi.responses import JSONResponse
from functools import wraps
import sys
import traceback

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return resHandler(result)
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            error_message = {
                "error_type": str(exc_type),
                "error_message": str(exc_value),
                "traceback": [str(line) for line in traceback.format_tb(exc_traceback)],
            }
            return JSONResponse(content=error_message, status_code=500)
    return wrapper

def resHandler(datas):
    statusCode, info = datas['statusCode'], datas['info']
    if statusCode != 200:
        raise HTTPException(status_code=statusCode, detail=info)
    return datas

def registerUID(data, uid):
    data = dict(data)
    data.update({"uid": uid})
    return data