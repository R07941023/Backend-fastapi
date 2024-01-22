import json
import requests

host = 'http://127.0.0.1:8001'

def API_mailSenderSystem(query):
    url = host + '/mail/sender'
    response = requests.post(url, json=query).content
    response = json.loads(response)
    return response

def API_getDataMinIOObjKeys(query):
    url = host + '/dataAccess/get/data/minIO/objKeys'
    response = requests.post(url, json=query).content
    response = json.loads(response)
    return response

def API_getDataMinIOObj(query):
    url = host + '/dataAccess/get/data/minIO/obj'
    response = requests.post(url, json=query).content
    response = json.loads(response)
    return response

def API_getDataSiteMariadbQuery(query):
    url = host + '/dataAccess/get/data/site/mariadb/query'
    response = requests.post(url, json=query).content
    response = json.loads(response)
    return response

def API_getDataSiteMariadbNonquery(query):
    url = host + '/dataAccess/get/data/site/mariadb/nonquery'
    response = requests.post(url, json=query).content
    response = json.loads(response)
    return response

def API_getDataMariadbQuery(query):
    url = host + '/dataAccess/get/data/mariadb/query'
    response = requests.post(url, json=query).content
    response = json.loads(response)
    return response

def API_getDataMariadbNonquery(query):
    url = host + '/dataAccess/get/data/mariadb/nonquery'
    response = requests.post(url, json=query).content
    response = json.loads(response)
    return response
