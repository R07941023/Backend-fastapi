from fastapi import APIRouter, Depends, Header
from src.main.python.scheme.dataLoader import GetUserID
from src.main.python.errorHandle.handler import registerUID, handle_exceptions
import logging

# build the logger
logger = logging.getLogger('myLoger')

# get UID
def get_uid(uid: str = Header('admin')):
    return uid

appTest = APIRouter()
@appTest.get("/") 
async def read_root():
    return {"Hello": "World"}

@appTest.post("/users")
@handle_exceptions
def read_user(item: GetUserID, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    res = {'statusCode': 200, "data": item, "info": 'welcome'}
    return res