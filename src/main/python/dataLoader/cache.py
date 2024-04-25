import redis
import pandas as pd

def test():
    cacheServer = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
    cacheServer.set('123', '456')
    res = cacheServer.mget(['123', '123'])
    print(res)


if __name__ == '__main__':
    res = test()