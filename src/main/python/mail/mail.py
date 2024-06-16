import smtplib, ssl
from email.mime.text import MIMEText
from func_timeout import func_set_timeout
import logging
from src.main.python.InfraAPI.InfraAPI import *

def readConnMailRelaySite(site):
    sql = f"""Select * from account where project = 'MailRelay' and site = '{site}'"""
    dbConn = {}
    dbConn['site'] = site
    dbConn['database'] = 'backend'
    dbConn['sql'] = sql        
    response = API_getDataSiteMariadbQuery(dbConn)
    logging.info(str(response))
    res = {}
    res['account'] = response['data'][0]['account']
    res['password'] = response['data'][0]['password']
    return res


@func_set_timeout(180)
def mailSiteSender(item):
    uid = item['uid']
    connInfo = readConnMailRelaySite(item['site'])
    connInfo['recevies'] = item['recevies']
    connInfo['Subject'] = item['Subject']
    connInfo['message'] = item['message']
    res = API_mailSenderSystem(connInfo)
    return res

@func_set_timeout(180)
def mailSender(item):
    res = {'statusCode': 200, "data": 'Pass', "info": ''}
    uid = item['uid']
    msg = MIMEText(item['message'], "html")
    msg["Subject"] = item['Subject']
    msg["To"] = ", ".join(item['recevies'])
    logging.info(f'[{uid}]: Build the conn for MailRelay')
    print('1')
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context())
    print('2', item)
    server.login(item['account'], item['password'])
    print('3')
    logging.info(f'[{uid}]: Send the message')
    server.send_message(msg)
    server.quit()
    return res



