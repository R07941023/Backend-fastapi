import logging
import pandas as pd
import mysql.connector
import json
from func_timeout import func_set_timeout

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