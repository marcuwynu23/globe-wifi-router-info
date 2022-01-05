import requests as rq
import json

def getWifiData(url):
	return json.loads(rq.get(url).content)
