import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "tbmw9x",
        "typeId": "NodeMCU",
        "deviceId":"12345"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

latitude = [16.426449,16.431841]
longitude = [80.9989193,80.9498083]

while True:
    for i in range(0, len(latitude)):
        temp=random.randint(-20,125)
        hum=random.randint(0,100)
        lat=latitude[i] 
        lon=longitude[i]
        airfreshness=random.randint(0,100)
        if airfreshness < 50:
            print("Alert air freshness is low")
        myData={'temperature':temp, 'humidity':hum, 'longitude':lon,'latitude':lat}
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Successfully: %s", myData)
        client.commandCallback = myCommandCallback
        time.sleep(2)
client.disconnect()
