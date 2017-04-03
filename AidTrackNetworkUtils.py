import json
import urllib.request


BASE_URL = "http://api.aidtrack.donchev.net/index.php/api/"

def getItemJson(id):
    response = urllib.request.urlopen(BASE_URL + "v1/items/id/" + id)
    data = json.loads(response.read().decode('utf-8'))
    response.close()
    return data["item"]

def getProductJson(id):
    response = urllib.request.urlopen(BASE_URL + "v1/products/id/" + id)
    data = json.loads(response.read().decode('utf-8'))
    response.close()
    return data

def getShipmentJson(id):
    response = urllib.request.urlopen(BASE_URL + "v1/shipments/id/" + id)
    data = json.loads(response.read().decode('utf-8'))
    response.close()
    return data["shipment"][0]

def getCampaignJson(id):
    response = urllib.request.urlopen(BASE_URL + "v1/campaigns/id/" + id)
    data = json.loads(response.read().decode('utf-8'))
    response.close()
    return data["campaign"]
