from mqttclient import MQTTClient
import ubinascii
import machine
import log
import relay
import time

topics = [ b'sprinkler/zone1',
           b'sprinkler/zone2',
           b'sprinkler/zone3',
           b'sprinkler/zone4',
           b'sprinkler/status',
           b'reset',
           b'update',
           b'mode',
           b'schedule']
mqtt_server = '98.51.182.241'
#mqtt_server = '192.168.40.231'
client_id = ubinascii.hexlify(machine.unique_id())
r = relay.Relay()

def restart_and_reconnect():
    print('Failed toconnect to MQTT broker, Reconnecting...')
    time.sleep(10)
    machine.reset()

def initPubSub():
    try:
        client = connect_and_subscribe()
    except OSError as e:
        restart_and_reconnect()
    while True:
        try:
            client.check_msg()
            time.sleep (0.5)
            r.setBoardLed1(1)
            time.sleep(0.5)
            r.setBoardLed1(0)
        except OSError as e:
            restart_and_reconnect()

def sub_cb(topic, msg):
    print((topic, msg))
    log.info('ESP received on message {}'.format(msg))

    if topic == b'sprinkler/zone1' and msg == b'on':
        r.setRelay1(0)
        # create a class for pin to off and on
    elif topic == b'sprinkler/zone1' and msg == b'off':
        r.setRelay1(1)
        # create a class for pin to off and on
    elif topic == b'sprinkler/zone2' and msg == b'on':
        r.setRelay2(0)
        # create a class for pin to off and on
    elif topic == b'sprinkler/zone2' and msg == b'off':
        r.setRelay2(1)
        # create a class for pin to off and on
    elif topic == b'sprinkler/zone3' and msg == b'on':
        r.setRelay3(0)
        # create a class for pin to off and on
    elif topic == b'sprinkler/zone3' and msg == b'off':
        r.setRelay3(1)
        # create a class for pin to off and on
    elif topic == b'sprinkler/zone4' and msg == b'on':
        r.setRelay4(0)
        # create a class for pin to off and on
    elif topic == b'sprinkler/zone4' and msg == b'off':
        r.setRelay4(1)
        # create a class for pin to off and on
    elif topic == b'reset':
        machine.reset()
        #reboot esp
    elif topic == b'update':
        log.info('ESP received uodate')
        #update code OTA
        from lib.ota_updater import OTAUpdater
        otaUpdater = OTAUpdater('https://github.com/aparajita-gupta/sprinkler-system', github_src_dir='sprinklerSystem', main_dir='esp8266')
        otaUpdater.install_update_if_available()
        del(otaUpdater)
    elif topic == b'schedule':
        log.info('ESP received schedule')
    elif topic == b'getStatus':
        log.info('ESP received schedule')
        client.publish(b'setStatus', '')
    else:
        log.info('ESP couldn not understand message')


def connect_and_subscribe():
    global client_id, mqtt_server, client
    print('Connecting server: {}'.format(mqtt_server))
    client = MQTTClient(client_id, mqtt_server)
    client.set_callback(sub_cb)
    client.connect()
    for topic_sub in topics:
        client.subscribe(topic_sub)
        print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
    return client