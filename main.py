from app.wifi_info import getWifiData,printInfo
from app.App import Application


if __name__ == '__main__':
	url = 'http://192.168.254.254/goform/goform_get_cmd_process?isTest=false&cmd=system_status&_=1641388769779'
	data = getWifiData(url)
	app = Application()
	app.set_data(printInfo(data))
	app.run()
