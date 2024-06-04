from func_timeout import func_set_timeout
import yfinance as yf
import json


def dfToJson(df):
    datas = df.to_json(orient='records')
    res = json.loads(datas)
    return res


@func_set_timeout(10000)
def tickerGetData(item):
    '''
    ticker: '2330.TW'
    start/end: '2023-12-11'
    interval: '1m'
    '''
    res = {'statusCode': 200, "data": 'Pass', "info": ''}
    ticker, start, end, interval = item['ticker'], item['start'], item['end'], item['interval']
    yfTicker = yf.Ticker(ticker)
    df = yfTicker.history(start=start, end=end, interval=interval)
    df = df.reset_index()
    res['data'] = dfToJson(df)
    return res