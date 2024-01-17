import boto3
import logging
import pandas as pd
from func_timeout import func_set_timeout
from io import BytesIO
import json

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