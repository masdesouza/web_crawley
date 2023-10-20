# One popular library is suds-py3, which provides a lightweight SOAP client for Python. 

from suds.client import Client

url = "http://192.168.120.50/DynamicMenus/WS_DynamicMenu.asmx?wsdl"

client = Client(url)

#result = client.service.GetURLMenuToModule(param1, param2)
result = client.service.GetURLMenuAll()

print(result)