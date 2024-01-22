from src.main.python.log.logger import Logger as logger
logging = logger()
import pandas as pd
import mysql.connector
import json
import configparser
from func_timeout import func_set_timeout
from src.main.python.InfraAPI.InfraAPI import *

    
@func_set_timeout(180)
def mariadbSiteQuery(item):
    uid = item['uid']
    res = {'statusCode': 200, "data": 'Pass', "info": ''}
    connInfo = readConnMariadbSite(item['site'])
    dbConn = {}
    dbConn['host'] = connInfo['host']
    dbConn['user'] = connInfo['user']
    dbConn['password'] = connInfo['password']
    dbConn['database'] = item['database']
    dbConn['sql'] = item['sql']
    print(dbConn)
    res = API_getDataMariadbQuery(dbConn)
    return res

@func_set_timeout(180)
def mariadbSiteNonquery(item):
    uid = item['uid']
    res = {'statusCode': 200, "data": 'Pass', "info": ''}
    connInfo = readConnMariadbSite(item['site'])
    dbConn = {}
    dbConn['host'] = connInfo['host']
    dbConn['user'] = connInfo['user']
    dbConn['password'] = connInfo['password']
    dbConn['database'] = item['database']
    dbConn['sql'] = item['sql']
    res = API_getDataMariadbNonquery(dbConn)
    return res

@func_set_timeout(180)
def mariadbQuery(item):
    uid = item['uid']
    res = {'statusCode': 200, "data": 'Pass', "info": ''}
    db_config = {
    'host': item['host'],
    'user': item['user'],
    'password': item['password'],
    'database': item['database']
    }
    logging.info(f'[{uid}]: Build the conn for MariaDB')
    conn = mysql.connector.connect(**db_config)
    logging.info(f'[{uid}]: Connect with MariaDB')
    df = pd.read_sql(item['sql'], conn)
    conn.close()
    logging.info(f'[{uid}]: dataframe to json')
    jsonString = df.to_json(orient='records')
    res['data'] = json.loads(jsonString)
    return res

@func_set_timeout(180)
def mariadbNonquery(item):
    uid = item['uid']
    res = {'statusCode': 200, "data": 'Pass', "info": ''}
    db_config = {
    'host': item['host'],
    'user': item['user'],
    'password': item['password'],
    'database': item['database']
    }
    logging.info(f'[{uid}]: Build the conn for MariaDB')
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    logging.info(f'[{uid}]: Connect with MariaDB')
    cursor.execute(item['sql'])
    conn.commit()
    cursor.close()
    conn.close()
    return res

def readConnMariadbSite(site):
    config = configparser.ConfigParser()
    config.read('./src/main/python/config/db.ini')
    config = dict(config[site])
    return config

