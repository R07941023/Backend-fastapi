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

dataAccess = APIRouter()


@dataAccess.post("/get/data/site/mariadb/query", tags=["Data"])
@handle_exceptions
def getDataSiteMariadbQuery(item: connSQLSite, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    res = mariadbSiteQuery(item)
    return res

@dataAccess.post("/get/data/site/mariadb/nonquery", tags=["Data"])
@handle_exceptions
def getDataSiteMariadbNonquery(item: connSQLSite, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    res = mariadbSiteNonquery(item)
    return res


@dataAccess.post("/get/data/site/minIO/objKeys", tags=["Data"])
@handle_exceptions
def getDataSiteMinIOObjKeys(item: GetDataSiteMinIOObjKeys, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    res = findListFromSiteMinIO(item)
    return res

@dataAccess.post("/get/data/site/minIO/obj", tags=["Data"])
@handle_exceptions
def getDataSiteMinIOObj(item: GetDataSiteMinIOObj, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    res = getObjFromSiteMinIO(item)
    return res

@dataAccess.post("/get/data/mariadb/query", tags=["Infra"])
@handle_exceptions
def getDataMariadbQuery(item: connSQLInfra, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    logging.info('[START] getDataMariadbQuery: ' + str(item))
    res = mariadbQuery(item)
    return res

@dataAccess.post("/get/data/mariadb/nonquery", tags=["Infra"])
@handle_exceptions
def getDataMariadbNonquery(item: connSQLInfra, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    logging.info('[START] getDataMariadbNonquery: ' + str(item))
    res = mariadbNonquery(item)
    return res

@dataAccess.post("/get/data/minIO/objKeys", tags=["Infra"])
@handle_exceptions
def getDataMinIOObjKeys(item: GetDataMinIOObjKeys, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    logging.info('[START] getDataMinIOObjKeys: ' + str(item))
    res = findListFromMinIO(item)
    return res

@dataAccess.post("/get/data/minIO/obj", tags=["Infra"])
@handle_exceptions
def getDataMinIOObj(item: GetDataMinIOObj, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    logging.info('[START] getDataMinIOObj: ' + str(item))
    res = getObjFromMinIO(item)
    return res

@dataAccess.post("/get/data/minIO/obj/download", tags=["Infra"])
@handle_exceptions
def getDataMinIOObjDownload(item: GetDataMinIOObjDownload, uid: str = Depends(get_uid)): 
    logging.info(f'[{uid}]: Welocime')
    item = registerUID(item, uid)
    logging.info('[START] getDataMinIOObjDownload: ' + str(item))
    res = downloadObjFromMinIO(item)
    return res