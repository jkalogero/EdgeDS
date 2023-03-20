import json
import string
from tokenize import String
from unicodedata import name

import yaml
import pymongo
from bson import json_util
from typing import List
from os import environ

#for developing
storage_url= 'mongodb://127.0.0.1'

#needed when deployed at ICOM cloud (and also when we build the image)
#storage_url=environ.get("EMP_STORAGE_URI")


port=27017
mydb_mongo='pi-edge'

def get_subs_area_circle():

    collection = "subscriptions"
    myclient = pymongo.MongoClient(storage_url, port)
    db = myclient[mydb_mongo]
    collection = db[collection]



def getResourceList(collection: str, **kwargs):

    myclient = pymongo.MongoClient(storage_url)
    db = myclient[mydb_mongo] # select database
    col = db[collection] # select collection
    params = {k:{"$in":v} for k,v in kwargs.items() if v is not None}
    userinfo = [_ for _ in col.find(params)]
    return userinfo

def getResource(collection: str, **kwargs):

    myclient = pymongo.MongoClient(storage_url)
    db = myclient[mydb_mongo] # select database
    col = db[collection] # select collection
    params = {k:{"$eq":v} for k,v in kwargs.items() if v is not None}
    userinfo = col.find_one(params)
    return userinfo



def getServices(collection: str ='ServiceInfo', params: dict = {}):
    """
    Query parameters must follow the below format:
    {
        "multiple": {
            "param1": <List>,
            "param2": <List>
        },
        "single": {
            "param3": <value>,
            "param4": <value>
        }
    }
    """

    myclient = pymongo.MongoClient(storage_url)
    db = myclient[mydb_mongo] # select database
    col = db[collection] # select collection

    operator = {
        'multiple': '$in',
        'single': '$eq'
    }

    _params = {k:{operator[key]:v} for key in params for k,v in params[key].items() if v is not None}
    serviceinfo = [_ for _ in col.find(_params)]

    return serviceinfo


def postService(collection: str ='ServiceInfo', params: dict = {}):
    
    myclient = pymongo.MongoClient(storage_url)
    db = myclient[mydb_mongo] # select database
    col = db[collection] # select collection
    inserted_id = col.insert_one(params).inserted_id
    result = col.find_one({"_id": inserted_id})

    return result

def getService(collection: str ='ServiceInfo', params: dict = {}):
    
    myclient = pymongo.MongoClient(storage_url)
    db = myclient[mydb_mongo] # select database
    col = db[collection] # select collection

    serviceinfo = col.find_one(params)
    return serviceinfo


def deleteService(collection: str ='ServiceInfo', params: dict = {}):

    myclient = pymongo.MongoClient(storage_url)
    db = myclient[mydb_mongo] # select database
    col = db[collection] # select collection

    return col.delete_one(params)

def getRelevantApps(collection: str = 'AppInstanceInfo', service_category_id: int = None):
    """
    Query AppInstanceInfo collection 
    """
    myclient = pymongo.MongoClient(storage_url)
    db = myclient[mydb_mongo] # select database
    col = db[collection] # select collection
    
    serviceinfo = col.find({"$or": [{"services.required":{"$in":[int(service_category_id)]}}, {"services.optional":{"$in":[int(service_category_id)]}}]})
    app_addresses = [el['address'] for el in serviceinfo]
    return app_addresses

