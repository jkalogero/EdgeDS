from pymongo import MongoClient
import pymongo
import random
import string
import pprint
from os import environ



#for developing
# storage_url= 'mongodb://127.0.01'
# port=27017

#needed when deployed at ICOM cloud (and also when we build the image)
# storage_url=environ.get("EMP_STORAGE_URI")

storage_url= 'mongodb://146.124.106.209'
port=32411

mydb_mongo='pi-edge'



def create_UserInfo(*args):
    """
    Create dummy data for the UserInfo model.
    """

    collection = "UserInfo"
    myclient = MongoClient(storage_url, port)
    db = myclient[mydb_mongo] # select database
    collection = db[collection] # select collection
    collection.drop() # drop all collection


    info = [
        (37.941761402332915, 23.873216229907975, 'device'), # Intracom - Telecom
        (37.94200677520598, 23.872508126793786, 'user'), # a few meters away
        (37.95095809436439, 23.86539490922638, 'user'), # even more
        (37.96290276838807, 23.907366111994733, 'device'), # Spata
        (38.005251783162436, 23.93792183425554, 'user'), # Pikermi
        (37.95572943048496, 23.757334084347566, 'user'), # Vironas
        (37.972781881574605, 23.72540507119863, 'device'), # Acropolis
        (37.99483592281826, 23.681459762778598, 'user'), # Aigaleo
        (37.938673019626336, 23.651419024600834, 'device'), # Piraeus
        (37.96114333604941, 23.50190197915611, 'user'), # Salamina
        (38.05311865470776, 24.322443284811484, 'user'), # Marmari
        (37.90644455577597, 22.90932695480973, 'device'), # Korinth
        (38.239419531695084, 21.7420296999025, 'user'), # Patras
        (37.46085090446012, 24.938364212181398, 'user'), # Syros
        (37.05424451887335, 25.163583917834085, 'device'), # Paros
        (36.59695096395881, 26.350107245175085, 'user'), # Astypalaia
        (36.468949726132784, 28.234262343684176, 'user'), # Rhodes
        (34.99304646707524, 32.93091714639594, 'device'), # Cyprus
        (41.83595710785188, 12.869883852649066, 'user'), # Rome
        (48.32626200988177, 11.353770502039712, 'user'), # Munich
        (52.65568494443906, 13.287363530906237, 'device'), # Berlin
        (39.627447089374996, 66.97578180583074, 'user'), # Samarqand
        (39.0637878574282, -9.067461300837797, 'user'), # Lisbon
        (57.78756365904864, 12.213054171006291, 'user'), # Gothenburg
        (60.01670983929293, 10.839763282880137, 'user') # Oslo

    ]

    l = []
    c = 0
    for i in range(5):
        for j in range(5):
            tmp = {}
            letters = string.ascii_lowercase
            tmp['accessPointId'] = 'AccessPoint' + str(i)
            tmp['user_type'] = info[c][2]
            tmp['address'] = 'sip%' + str(i)+'_'+str(j)
            tmp['location'] = {}
            tmp['location']['latitude'] = info[c][0]
            tmp['location']['longitude'] = info[c][1]
            tmp['resourceURL'] = ''.join(random.choice(letters) for i in range(5))
            tmp['timestamp'] = {}
            tmp['timestamp']['nanoSeconds'] = 945
            tmp['timestamp']['seconds'] = 5
            zone = str(random.randint(1,9))
            tmp['zoneId'] = 'zone' + "0"*(2-len(zone)) + zone # keep two digits
            l.append(tmp)
            c +=1
    collection.insert_many(l)



def checkColletion(collection: str = 'UserInfo'):
    myclient = pymongo.MongoClient(storage_url)
    db = myclient[mydb_mongo] # select database
    collection = db[collection] # select collection
    for el in collection.find():
        pprint.pprint(el)

def create_ZoneInfo(*args):
    """
    Create dummy data for the ZoneInfo model.
    """

    collection = "ZoneInfo"
    myclient = MongoClient(storage_url, port)
    db = myclient[mydb_mongo] # select database
    collection = db[collection] # select collection
    collection.drop() # drop all collection
    l = []
    for zone in range(1,9):
        tmp = {}
        letters = string.ascii_lowercase
        tmp['numberOfAccessPoints'] = random.randint(0,5)
        tmp['numberOfUnserviceableAccessPoints'] = random.randint(0,5)
        tmp['numberOfUsers'] = random.randint(0,5)
        tmp['resourceURL'] = ''.join(random.choice(letters) for i in range(5))
        tmp['zoneId'] = 'zone' + "0"*(2-len(str(zone))) + str(zone) # keep two digits
        l.append(tmp)
    collection.insert_many(l)

def create_AccessPointInfo(*args):
    """
    Create dummy data for the AccessPointInfo model.
    """

    collection = "AccessPointInfo"
    myclient = MongoClient(storage_url, port)
    db = myclient[mydb_mongo] # select database
    collection = db[collection] # select collection
    collection.drop() # drop all collection

    types = [ 'Femto', 'LTE-femto', 'Smallcell', 'LTE-smallcell', 'Wifi', 'Pico', 'Micro', 'Macro', 'Wimax', 'Unknown']
    l = []
    for ap in range(5):
        tmp = {}
        tmp['accessPointId'] = 'AccessPoint' + str(ap)
        tmp['connectionType'] = types[ap]
        tmp['interestRealm'] = 'string'
        tmp['locationInfo'] = {}
        tmp['numberOfUsers'] = random.randint(0,5)
        tmp['operationStatus'] = 'Serviceable'
        tmp['resourceURL'] = 'Self referring URL'
        tmp['timezone'] = 'UTC'
        l.append(tmp)
    collection.insert_many(l)



def create_Services(*args):
    """
    Create dummy data for the ServiceInfo model.
    """

    collection = "ServiceInfo"
    myclient = MongoClient(storage_url, port)
    db = myclient[mydb_mongo] # select database
    collection = db[collection] # select collection
    collection.drop() # drop all collection
    l = []

  

    for _ in range(1):
        tmp = {}
        tmp['serInstanceId'] = 'service01'
        tmp['AppInstanceId'] = 'producer0'
        tmp['serName'] = 'ue_location_service'
        tmp['serCategory'] = {
            "href": "string",
            "id": "string",
            "name": "string",
            "version": "string"
        }
        tmp["version"] = "string"
        tmp["state"] = "ACTIVE"
        tmp["transportInfo"] = {
            "id": "string",
            "name": "string",
            "description": "string",
            "type": "REST_HTTP",
            "protocol": "string",
            "version": "string",
            "security": {
                "oAuth2Info": {
                    "grantTypes": [
                    "OAUTH2_AUTHORIZATION_CODE"
                    ],
                    "tokenEndpoint": "string"
                }
            },
            "implSpecificInfo": {}
        }
        tmp["serializer"] = "JSON",
        tmp["scopeOfLocality"] = "MEC_SYSTEM",
        tmp["consumedLocalOnly"] = True,
        tmp["isLocal"] = True,
        tmp["livenessInterval"] = 0,
        tmp["_links"] = {
            "self": {
                "href": "string"
            },
            "liveness": {
                "href": "string"
            }
        }
        l.append(tmp)
    collection.insert_many(l)


def createAppInstances(*args):
    collection = "AppInstanceInfo"
    myclient = MongoClient(storage_url, port)
    db = myclient[mydb_mongo] # select database
    collection = db[collection] # select collection
    collection.drop() # drop all collection
    l = []

    apps = {
        'consumer': ['http://127.0.0.1:5001/', [1,3,5], [2,4]], 
        'producer': ['http://127.0.0.1:5000/', [], []]
    }

    for app in apps:
        tmp = {}
        tmp['appInstanceId'] = app + '0'
        tmp['appName'] = app
        tmp['services'] = {}
        tmp['services']['available'] =[]
        tmp['services']['required'] = apps[app][1]
        tmp['services']['optional'] = apps[app][2]
        tmp['address'] = apps[app][0]
        l.append(tmp)
    collection.insert_many(l)

def dummyEmail(address):

    address_mapper = [
        'ikalogerop@intracom-telecom.com',
        'nikpsarom@intracom-telecom.com',
        'marmert@intracom-telecom.com',
        'dlaskaratos@intracom-telecom.com',
        'gsamaras@intracom-telecom.com'
    ]
    return address_mapper[int(address[-1])]

def create_EmailDB(*args):
    """
    Create dummy email addresses for each UE address.
    """
    # get addresses
    UE_collection = "UserInfo"
    myclient = MongoClient(storage_url, port)
    db = myclient[mydb_mongo] # select database
    UE_collection = db[UE_collection] # select collection

    addresses = [el['address'] for el in UE_collection.find()]
    
    # create email database
    collection = 'address_email'
    db = myclient['EmailAddresses'] # select database
    collection = db[collection] # select collection
    collection.drop() # drop all collection
    
    l = [{"ue":{'address': address, 'email': dummyEmail(address)}} for address in addresses]
    collection.insert_many(l)
    
    
# l = [(create_EmailDB,None)]
l = [(checkColletion, 'ZoneInfo')]
# l = [(create_UserInfo,None), (create_ZoneInfo,None), (create_Services,None), (create_EmailDB,None), (checkColletion, 'UserInfo'), (checkColletion, 'ServiceInfo')]

def main():
    [f(arg) for (f,arg) in l]




if __name__ == "__main__":
    main()