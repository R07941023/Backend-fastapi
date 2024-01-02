from fastapi import APIRouter, Depends, Header
from src.main.python.scheme.dataLoader import GetUserID, tickerGetDataFormat
from src.main.python.errorHandle.handler import registerUID, handle_exceptions
from src.main.python.dataLoader.ticker import tickerGetData
import logging

# build the logger
logger = logging.getLogger('myLoger')

# get UID
def get_uid(uid: str = Header('admin')):
    return uid


appQuant = APIRouter()
@appQuant.post("/finance/history/getData")
@handle_exceptions
def read_user(item: tickerGetDataFormat, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    res = tickerGetData(item)
    return res