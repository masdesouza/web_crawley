# Zeep library which is more feature rich in making soap requests in python

from zeep import Client

wsdl = 'http://192.168.120.50/DynamicMenus/WS_DynamicMenu.asmx?wsdl'

client = Client(wsdl)

#result = client.service.GetURLMenuToModule(param1=arg1, param2=arg2)

result = client.service.GetURLMenuAll()

print(result)
