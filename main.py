from app.wifi_info import getWifiData

def printInfo(data):
	for item in data.items():
			key,value = item
			print(f'{key}: {value}')

if __name__ == '__main__':
	url = 'http://192.168.254.254/goform/goform_get_cmd_process?isTest=false&cmd=system_status&_=1641388769779'
	data = getWifiData(url)
	printInfo(data)
