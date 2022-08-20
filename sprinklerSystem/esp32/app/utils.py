import ujson
import log

def getSsidAndPassword():
    try:
      sfile = open("secret.json", 'r')
      file_str = sfile.read()
      sfile.close()
      json_str = ujson.loads(file_str)
      ssid = json_str["ssid"]
      password = json_str["ssid_pwd"]
      del(file_str)
      del(sfile)
      return ssid, password
    except:
       log.info("File Not found")
       return None, None

def getMQTTServerIP():
    try:
      sfile = open("secret.json", 'r')
      file_str = sfile.read()
      sfile.close()
      json_str = ujson.loads(file_str)
      mqtt = json_str["mqtt_server"]
      del(file_str)
      del(sfile)
      return mqtt
    except:
       log.info("File Not found")
       return None

def connectToWifi():
    log.info('Connecting to WiFi')
    import network, time
    wlan = network.WLAN(network.STA_IF)
    count = 0
    wlan.active(True)
    if not wlan.isconnected():
        log.info('connecting to network...')
        ssid, password = getSsidAndPassword()
        if (ssid is None):
         log.info("SSID is not defined")
         return
        ret = wlan.connect(ssid, password)
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