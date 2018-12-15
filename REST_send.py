import DeviceClient

KEY = 'wOsek8On/g+oy2a0houiZt225ozLM0DjYmjwqpNoF2Q='
HUB = 'IoT-Cloud-Hub'
DEVICE_NAME = 'Group04'

with open('temperature.txt', 'r') as f:
	string = f.readlines()
	cutstring = string[-2]
	cutstring += string[-1]
	cutstring = cutstring.strip() 
	b_cutstring = str.encode(cutstring)

device = DeviceClient.DeviceClient(HUB, DEVICE_NAME, KEY)

device.create_sas(600)

print( device.send(b_cutstring) )

#message = device.read_message()
#print(message['body'])

