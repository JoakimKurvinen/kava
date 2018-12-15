from iothub_client import IoTHubClient, IoTHubTransportProvider, IoTHubMessage

import time



CONNECTION_STRING = "HostName=IoT-Cloud-Hub.azure-devices.net;DeviceId=Group04;SharedAccessKey=wOsek8On/g+oy2a0houiZt225ozLM0DjYmjwqpNoF2Q="


PROTOCOL = IoTHubTransportProvider.MQTT





def send_confirmation_callback(message, result, user_context):

    print("Confirmation received for message with result = %s" % (result))


def message_from_file():
	with open('temperature.txt', 'r'):
		string = f.readlines()
		cutstring = string[-2]
		cutstring += string[-1]
		cutstring = cutstring.strip()
		return cutstring



if __name__ == '__main__':

    client = IoTHubClient(CONNECTION_STRING, PROTOCOL)

    message = IoTHubMessage( message_from_file() )

    client.send_event_async(message, send_confirmation_callback, None)

    print("Message transmitted to IoT Hub")



    while True:

        time.sleep(1)
