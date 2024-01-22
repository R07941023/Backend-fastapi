from pydantic import BaseModel, Field
from typing import List

class mailSiteSenderFormat(BaseModel):
    site: str = Field(default='SIT')
    recevies: List[str] = Field(default=["a5822358@gmail.com"])
    Subject: str = Field(default='[Backend Info]')
    message: str = Field(default='detail')

class mailSenderFormat(BaseModel):
    account: str = Field(default='')
    password: str = Field(default='')
    recevies: List[str] = Field(default=["a5822358@gmail.com"])
    Subject: str = Field(default='[Backend Info]')
    message: str = Field(default='detail')

class connSQLSite(BaseModel):
    site: str = Field(default='SIT')
    database: str = Field(default='machine_learning')
    sql: str = Field(default='Select * from hyperparameter')

class connSQLInfra(BaseModel):
    host: str = Field(default='localhost')
    user: str = Field(default='root')
    password: str = Field(default='admin')
    database: str = Field(default='machine_learning')
    sql: str = Field(default='Select * from hyperparameter')

class GetUserID(BaseModel):
    name: str = Field(default='user123')


class GetDataMinIOObjKeys(BaseModel):
    endpoint_url: str = Field(default='http://127.0.0.1:9000')
    access_key: str = Field(default='yylui')
    secret_key: str = Field(default='passwd')
    bucket_name: str = Field(default='yylui')

class GetDataMinIOObj(BaseModel):
    endpoint_url: str = Field(default='http://127.0.0.1:9000')
    access_key: str = Field(default='yylui')
    secret_key: str = Field(default='passwd')
    bucket_name: str = Field(default='yylui')
    object_key: str = Field(default='test.txt')


class GetDataMinIOObjDownload(BaseModel):
    endpoint_url: str = Field(default='http://127.0.0.1:9000')
    access_key: str = Field(default='yylui')
    secret_key: str = Field(default='passwd')
    bucket_name: str = Field(default='yylui')
    object_key: str = Field(default='test.txt')
    download_path: str = Field(default='./test.txt')

class GetDataSiteMinIOObjKeys(BaseModel):
    site: str = Field(default='SIT')
    bucket_name: str = Field(default='yylui')

class GetDataSiteMinIOObj(BaseModel):
    site: str = Field(default='SIT')
    bucket_name: str = Field(default='yylui')
    object_key: str = Field(default='test.txt')

class tickerGetDataFormat(BaseModel):
    ticker: str = Field(default='2330.TW')
    start: str = Field(default='2023-12-11')
    end: str = Field(default='2023-12-12')
    interval: str = Field(default='1m')

