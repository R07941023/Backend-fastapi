from fastapi import APIRouter, Depends, Header
from src.main.python.scheme.dataLoader import *
from src.main.python.errorHandle.handler import registerUID, handle_exceptions
from src.main.python.dataLoader.minIO import *
from src.main.python.dataLoader.db import *
from src.main.python.mail.mail import *
from src.main.python.log.logger import Logger as logger
logging = logger()

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



@appTest.post("/mail/sender")
@handle_exceptions
def mailSenderSystem(item: mailSenderFormat, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    res = mailSender(item)
    return res

@appTest.post("/mail/site/sender")
@handle_exceptions
def mailSiteSenderSystem(item: mailSiteSenderFormat, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    res = mailSiteSender(item)
    return res