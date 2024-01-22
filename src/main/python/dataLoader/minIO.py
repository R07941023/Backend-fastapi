import boto3
from src.main.python.log.logger import Logger as logger
logging = logger()
import pandas as pd
from func_timeout import func_set_timeout
from io import BytesIO
import json
from src.main.python.InfraAPI.InfraAPI import *

def readConnMariadbSite(site):
    sql = f"""Select * from account where project = 'minIO' and site = '{site}'"""
    dbConn = {}
    dbConn['site'] = site
    dbConn['database'] = 'backend'
    dbConn['sql'] = sql        
    response = API_getDataSiteMariadbQuery(dbConn)
    logging.info(str(response))
    res = {}
    res['endpoint_url'] = json.loads(response['data'][0]['info'])['endpoint_url']
    res['access_key'] = response['data'][0]['account']
    res['secret_key'] = response['data'][0]['password']
    return res

@func_set_timeout(180)
def findListFromSiteMinIO(item):
    uid = item['uid']
    connInfo = readConnMariadbSite(item['site'])
    minIOConn = {}
    minIOConn['endpoint_url'] = connInfo['endpoint_url']
    minIOConn['access_key'] = connInfo['access_key']
    minIOConn['secret_key'] = connInfo['secret_key']
    minIOConn['bucket_name'] = item['bucket_name']
    res = API_getDataMinIOObjKeys(minIOConn)
    return res

@func_set_timeout(180)
def getObjFromSiteMinIO(item):
    uid = item['uid']
    connInfo = readConnMariadbSite(item['site'])
    minIOConn = {}
    minIOConn['endpoint_url'] = connInfo['endpoint_url']
    minIOConn['access_key'] = connInfo['access_key']
    minIOConn['secret_key'] = connInfo['secret_key']
    minIOConn['bucket_name'] = item['bucket_name']
    minIOConn['object_key'] = item['object_key']
    res = API_getDataMinIOObj(minIOConn)
    return res


@func_set_timeout(180)
def findListFromMinIO(item):
    uid = item['uid']
    res = {'statusCode': 200, "data": 'Pass', "info": ''}
    res['data'] = []
    logging.info(f'[{uid}]: Build the conn for MinIO')
    s3 = boto3.client('s3', endpoint_url=item['endpoint_url'], aws_access_key_id=item['access_key'], aws_secret_access_key=item['secret_key'])
    response = s3.list_objects(Bucket=item['bucket_name'])
    # obj > key / datetime / etag / size / storageClass / owner / id
    for obj in response.get('Contents', []):
        res['data'] += [obj['Key']]
    return res

@func_set_timeout(180)
def getObjFromMinIO(item):
    uid = item['uid']
    res = {'statusCode': 200, "data": 'Pass', "info": ''}
    res['data'] = []
    logging.info(f'[{uid}]: Build the conn for MinIO')
    s3 = boto3.client('s3', endpoint_url=item['endpoint_url'], aws_access_key_id=item['access_key'], aws_secret_access_key=item['secret_key'])
    csvData = s3.get_object(Bucket=item['bucket_name'], Key=item['object_key'])
    df = pd.read_csv(BytesIO(csvData['Body'].read()))
    jsonString = df.to_json(orient='records')
    res['data'] = json.loads(jsonString)
    return res

@func_set_timeout(180)
def downloadObjFromMinIO(item):
    uid = item['uid']
    res = {'statusCode': 200, "data": 'Pass', "info": ''}
    res['data'] = []
    logging.info(f'[{uid}]: Build the conn for MinIO')
    s3 = boto3.client('s3', endpoint_url=item['endpoint_url'], aws_access_key_id=item['access_key'], aws_secret_access_key=item['secret_key'])
    s3.download_file(item['bucket_name'], item['object_key'], item['download_path'])
    return res




if __name__ == '__main__':
    res = readConnMariadbSite('SIT')
    print(res)