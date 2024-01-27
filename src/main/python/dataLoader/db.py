from src.main.python.log.logger import Logger as logger
logging = logger()
import pandas as pd
import mysql.connector
import json
import configparser
from func_timeout import func_set_timeout
from src.main.python.InfraAPI.InfraAPI import *
from datetime import datetime


def tableToSql(tag, col, table, startTime, endTime):
    startTime = datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
    endTime = datetime.strptime(endTime, "%Y-%m-%d %H:%M:%S")
    sql = f"""Select Date, {col} from {table} where tag = '{tag}' AND Date BETWEEN '{startTime}' AND '{endTime}'"""
    return sql


@func_set_timeout(180)
def mariadbSiteTableQuery(item):
    res = {'statusCode': 200, "data": 'Pass', "info": ''}
    dbConn = {}
    dbConn['site'] = item['site']
    dbConn['database'] = item['database']
    dbConn['sql'] = tableToSql(item['tag'], item['column'], item['table'], item['startTime'], item['endTime'])
    print(dbConn)
    res = API_getDataSiteMariadbQuery(dbConn)
    return res

@func_set_timeout(180)
def mariadbSiteSqlQuery(item):
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
def mariadbSiteSqlNonquery(item):
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
def mariadbSqlQuery(item):
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
def mariadbSqlNonquery(item):
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

