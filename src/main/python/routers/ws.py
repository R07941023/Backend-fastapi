from fastapi import APIRouter, Depends, Header
from src.main.python.scheme.dataLoader import *
from src.main.python.errorHandle.handler import registerUID, handle_exceptions
from src.main.python.dataLoader.minIO import *
from src.main.python.dataLoader.db import *
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


@appTest.post("/get/data/minIO/objKeys")
@handle_exceptions
def getDataMinIOObjKeys(item: GetDataMinIOObjKeys, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    res = findListFromMinIO(item)
    return res

@appTest.post("/get/data/minIO/obj")
@handle_exceptions
def getDataMinIOObj(item: GetDataMinIOObj, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    res = getObjFromMinIO(item)
    return res

@appTest.post("/get/data/minIO/obj/download")
@handle_exceptions
def getDataMinIOObjDownload(item: GetDataMinIOObjDownload, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    res = downloadObjFromMinIO(item)
    return res

@appTest.post("/get/data/mariadb/query")
@handle_exceptions
def getDataMariadbQuery(item: sqlCommand, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    res = mariadbQuery(item)
    return res

@appTest.post("/get/data/mariadb/nonquery")
@handle_exceptions
def getDataMariadbNonquery(item: sqlCommand, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    res = mariadbNonquery(item)
    return res