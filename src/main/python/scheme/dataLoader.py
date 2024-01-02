from pydantic import BaseModel, Field

class GetUserID(BaseModel):
    name: str = Field(default='user123')

class tickerGetDataFormat(BaseModel):
    ticker: str = Field(default='2330.TW')
    start: str = Field(default='2023-12-11')
    end: str = Field(default='2023-12-12')
    interval: str = Field(default='1m')