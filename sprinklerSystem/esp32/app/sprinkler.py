import time

import log
import ujson


#esp.osdebug(None)
import relay




def do_connect():
    try:
      sfile = open("secret.json", 'r')
      file_str = sfile.read()
      sfile.close()
      json_str = ujson.loads(file_str)
      ssid = json_str["ssid"]
      password = json_str["ssid_pwd"]
      del(file_str)
      del(sfile)
    except:
       log.info("File Not found")
    log.info('Connecting to WiFi')
    import network
    wlan = network.WLAN(network.STA_IF)
    count = 0
    wlan.active(True)
    if not wlan.isconnected():
        log.info('connecting to network...')
        ret = wlan.connect(ssid, password)
        log.info ("ret: {}".format(ret))
        while not wlan.isconnected():
           log.info(log.free())
           time.sleep(2)
           #await asyncio.sleep(2)
           if(count > 30):
              count = count + 1
              break
           pass
    log.info('connected to network.')
    del(wlan)


async def init():
    log.info('pubsub is going to start  running...')
    relay.Relay()
    do_connect()
    import pubsubtask
    await pubsubtask.initPubSub()


