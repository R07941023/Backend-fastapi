from pydantic import BaseModel, Field

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
    download_path: str = Field(default='./test.txt')

class tickerGetDataFormat(BaseModel):
    ticker: str = Field(default='2330.TW')
    start: str = Field(default='2023-12-11')
    end: str = Field(default='2023-12-12')
    interval: str = Field(default='1m')

