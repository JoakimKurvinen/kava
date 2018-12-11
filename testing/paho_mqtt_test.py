from paho.mqtt import client as mqtt

import ssl
import time


path_to_root_cert = "/home/pi/Azure/digicert.cer"

device_id = "Group05"

#sas_token = "HostName=IoT-Cloud-Hub.azure-devices.net;DeviceId=Group05;SharedAccessKey=vCEWoa85IyTKl8tg9ntQ8MrVRXnR+W3YlsvlZVCZvFo="

#sas_token = "SharedAccessKey=vCEWoa85IyTKl8tg9ntQ8MrVRXnR+W3YlsvlZVCZvFo="

sas_token = "vCEWoa85IyTKl8tg9ntQ8MrVRXnR+W3YlsvlZVCZvFo="
iot_hub_name = "IoT-Cloud-Hub"



def on_connect(client, userdata, flags, rc):
  print ("Device connected with result code: " + str(rc))

def on_disconnect(client, userdata, rc):
  print ("Device disconnected with result code: " + str(rc))

def on_publish(client, userdata, mid):
  print ("Device sent message")



client = mqtt.Client(client_id=device_id, protocol=mqtt.MQTTv311)



client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish



client.username_pw_set(username=iot_hub_name+".azure-devices.net/" + device_id, password=sas_token)



client.tls_set(ca_certs=path_to_root_cert, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1, ciphers=None)
client.tls_insecure_set(False)



client.connect(iot_hub_name+".azure-devices.net", port=8883)
time.sleep(4)
#Open file that contains data to send#
#file = open("temp_test.json")
#imagestring = file.read()
#barray = bytearray(imagestring)
#print barray	#for testing

#client.publish("Temperature", barray, qos=1, retain=False)	#Sends data
client.publish("devices/" + device_id + "/messages/events/", "{id=123}", qos=1)

time.sleep(4)
client.loop_forever()


