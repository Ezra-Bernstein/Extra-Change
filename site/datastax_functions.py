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
    data = '{ "username": "' + username + '", "password": "' + password + '", "funds": {}}'
    response = requests.post(BASE_URL + '/userData', headers=headers, data=data)

def getUserID(username):
    response = requests.get(BASE_URL +  '/userData?page-size=20&where={"username":{"$eq":"'+ username +'"}}', headers=headers)
    print(response.text)
    id = list(response.json()["data"].keys())[0]
    return id

def getUserData(id):
    response = requests.get(BASE_URL +  '/userData/' + id, headers=headers)
    print(BASE_URL +  '/userData/' + id)
    print(response.text)
    return response.json()["data"]

def checkUser(username, password):
    if userExists(username):
        print("exists")
        id = getUserID(username)
        print(id)
        userData = getUserData(id)
        print("get user data")
        usernameDB = userData["username"]
        passwordDB = userData["password"]
        if username == usernameDB and password == passwordDB:
            return True
        else:
            return False
    else:
        return False

def userExists(username):
    response = requests.get(BASE_URL +  '/userData?page-size=20&where={"username":{"$eq":"'+ username +'"}}', headers=headers)
    print(response.text)
    if len(response.json()["data"].keys()) > 0:
        return True
    else:
        return False

def createFund(fundName, fundDesc, fundGoal, fundCreator):
    data = '{"'+ fundName +'": {"fundName": "'+ fundName + '", "fundDesc": "'+ fundDesc + '", "fundGoal": "'+fundGoal+'", "fundAmount": "0"}}'
    id = getUserID(fundCreator)
    response = requests.patch(BASE_URL + '/userData/' + id + '/funds', headers=headers, data=data)
    return response

def addToFund(fundName, fundCreator, amount):
    id = getUserID(fundCreator)
    data = getUserData(id)["funds"]
    newAmount = str(int(data[fundName]["fundAmount"]) + amount)
    newData = '{"fundAmount": "' + newAmount + '"}'
    response = requests.patch(BASE_URL + '/userData/' + id + '/funds/' + fundName, headers=headers, data=newData)
    return response

def getFundsList():
    response = requests.get(BASE_URL +  '/userData?page-size=20&where={"username":{"$exists": true}}', headers=headers)
    
    returnList = []
    for user in response.json()["data"].keys():
        print(response.json()["data"][user]["funds"])
        creator = response.json()["data"][user]["username"]
        print("Creator: " + creator)
        for fund in response.json()["data"][user]["funds"].keys():
            name = response.json()["data"][user]["funds"][fund]["fundName"]
            print(name)
            returnList.append({"name": name, "creator": creator})

    returnDict = {"data": returnList}
    print(returnList)
    print(returnDict)
    return returnDict

def getFund(username, fundName):
    data = getUserData(getUserID(username))
    if fundName in data["funds"].keys():
        return data["funds"][fundName]
    else:
        return "that fund does not exists"

