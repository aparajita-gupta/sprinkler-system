import time
from lib.mqttclient import MQTTClient
import ubinascii
import machine

#esp.osdebug(None)
import relay
# Replease the ssid text with the network name for your local Wifi connection
# replace the password text with the WiFi password
# replace the mqtt_server text with the mqtt server IP or url
# replace the topic_sub with the topic you want to subscribe to
# replace the topic_pub with the topic you want to publish to


print('Start connecting...')
ssid = '<ssid>'
password = '<pwd>'
mqtt_server = '192.168.40.231' # Replace with the IP or URI of the MQTT server you use
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'sprinkler' # This is the topic you want to subscribe to
last_message = 0
message_interval = 5
counter = 0

print ("Connecting from {}".format(client_id))
#wlan.scan()

bssid1 = b'\xe2\xb4\xf7\x89\x8f\x02'
bssid2 = b'\x8e\x73\x29\xea\x58\xde'

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    count = 0
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
       # sc = wlan.scan()
        """ for sc1 in sc:
            for sc2 in sc1:
                s1 = str(ubinascii.hexlify(str(sc2), ":"))
                print(s1) """
       # print("Scanned.... {}".format(sc))
        ret = wlan.connect(ssid, password)
        print ("ret: {}".format(ret))
        while not wlan.isconnected():
           print("Failed.... {}".format(count))
           print (wlan.status())
           count = count + 1
           time.sleep(2)
           if count >90:
             exit(0)
           pass
    print(' wlan Connection successful')
    print('network config:', wlan.ifconfig())

    mac = wlan.config('mac')      # get the interface's MAC address

    print("mac config: {}".format(mac))

def init():
    relay.Relay()
    do_connect()
    import pubsubtask
    pubsubtask.initPubSub()


