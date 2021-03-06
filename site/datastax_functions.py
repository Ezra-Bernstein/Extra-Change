import os
import requests
from dotenv import load_dotenv

load_dotenv()

ASTRA_DB_APPLICATION_TOKEN = os.getenv('ASTRA_DB_APPLICATION_TOKEN')
ASTRA_DB_ID = os.getenv('ASTRA_DB_ID')
ASTRA_DB_REGION = os.getenv('ASTRA_DB_REGION')
ASTRA_DB_KEYSPACE = os.getenv('ASTRA_DB_KEYSPACE')


headers = {
    'X-Cassandra-Token': f"{ASTRA_DB_APPLICATION_TOKEN}",
    'Content-Type': 'application/json',
}

BASE_URL = "https://" + ASTRA_DB_ID + "-" + ASTRA_DB_REGION + ".apps.astra.datastax.com/api/rest/v2/namespaces/" + ASTRA_DB_KEYSPACE + "/collections"

def createUser(username, password):
    data = '{ "username": "user1", "password": "mypassword",  "funds": "{}"}'
    response = requests.post(BASE_URL + '/userData', headers=headers, data=data)

def getUserID(username):
    response = requests.get(BASE_URL +  '/userData?page-size=20&where\"username\"$eq\"'+ username +'+\"', headers=headers)
    print(response.text)
    id = response.json()["data"].keys()[0]
    return id

def getUserData(id):
    response = requests.get(BASE_URL +  '/userData/' + id)
    print(response.text)
    return response["data"]

def checkUser(username, password):
    if userExists(username):
        id = getUserID(username)
        userData = getUserData(id)
        usernameDB = userData["username"]
        passwordDB = userData["password"]
        if username == usernameDB and password == passwordDB:
            return True
        else:
            return False
    else:
        return False

def userExists(username):
    response = requests.get(BASE_URL +  '/userData?page-size=20&where\"username\"$eq\"'+ username +'+\"', headers=headers)
    print(response.text)
    if len(response.json()["data"].keys()) > 0:
        return True
    else:
        return False

def createFund(fundName, fundDesc, fundGoal, fundCreator):
    data = '{ "username": "user1", "password": "mypassword",  "funds": "{}"}'
    response = requests.patch(BASE_URL + '/userData/')
    return True



