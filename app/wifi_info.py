import requests as rq
import json

def getWifiData(url):
	return json.loads(rq.get(url).content)



#return str of data
def printInfo(data):
	info = ""
	for item in data.items():
			key,value = item
			info += f' {key}: {value}\n'
	return info