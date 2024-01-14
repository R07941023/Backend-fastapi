import boto3
import logging
from func_timeout import func_set_timeout

# # 替换为你的 MinIO 信息
# minio_endpoint = 'http://127.0.0.1:9000'
# access_key = 'yylui'
# secret_key = 'applezxcv1234567890-'
# bucket_name = 'yylui'
# object_key = 'test.txt'

# # 创建 S3 客户端


# # 列出存储桶中的所有对象


# # 下载文件
# download_path = 'D:/Users/yenying/Downloads/test.txt'
# # s3.download_file(bucket_name, object_key, download_path)

# print(f'文件已下载到 {download_path}')


@func_set_timeout(1800)
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

@func_set_timeout(1800)
def downloadObjFromMinIO(item):
    uid = item['uid']
    res = {'statusCode': 200, "data": 'Pass', "info": ''}
    res['data'] = []
    logging.info(f'[{uid}]: Build the conn for MinIO')
    s3 = boto3.client('s3', endpoint_url=item['endpoint_url'], aws_access_key_id=item['access_key'], aws_secret_access_key=item['secret_key'])
    s3.download_file(item['bucket_name'], item['object_key'], item['download_path'])
    return res