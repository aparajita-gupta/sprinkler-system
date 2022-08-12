import uasyncio as asyncio
from lib.sched import schedule
import log
import sprinkler
import ujson
import relay


async def sprinklerZone1(off=10):
    zone1 = relay.Relay()
    log.info('sprinklerZone1 start')
    zone1.setRelay1(0)
    await asyncio.sleep(off)
    zone1.setRelay1()
    log.info('sprinklerZone1 stop')

async def sprinklerZone2(off=10):
    zone2 = relay.Relay()
    log.info('sprinklerZone2 start')
    zone2.setRelay2(0)
    await asyncio.sleep(off)
    zone2.setRelay2()
    log.info('sprinklerZone2 stop')

async def sprinklerZone3(off=10):
    zone3 = relay.Relay()
    log.info('sprinklerZone3 start')
    zone3.setRelay3(0)
    await asyncio.sleep(off)
    zone3.setRelay3()
    log.info('sprinklerZone3 stop')

async def sprinklerZone4(off=10):
    sprinkler = relay.Relay()
    log.info('sprinklerZone4 start')
    sprinkler.setRelay4(0)
    await asyncio.sleep(off)
    sprinkler.setRelay4()
    log.info('sprinklerZone4 stop')

async def main():
    asyncio.create_task(sprinkler.init())
    sfile = open("./app/schedule.json", 'r')
    file_str = sfile.read()
    #log.info("main1 - {}".format(log.free()))
    sfile.close()
    json_str = ujson.loads(file_str)
    del(file_str)

    zone1Off = json_str["zone1"]['off']['mins'][0] - json_str["zone1"]['on']['mins'][0]
    asyncio.create_task(schedule(sprinklerZone1, zone1Off * 60,
                        wday=json_str["zone1"]['on']['wday'],
                        hrs=json_str["zone1"]['on']['hours'],
                        mins=json_str["zone1"]['on']['mins']))
    del(zone1Off)

    zone2Off = json_str["zone2"]['off']['mins'][0] - json_str["zone2"]['on']['mins'][0]
    asyncio.create_task(schedule(sprinklerZone2, zone2Off * 60,
                        wday=json_str["zone2"]['on']['wday'],
                        hrs=json_str["zone2"]['on']['hours'],
                        mins=json_str["zone2"]['on']['mins']))
    del(zone2Off)


    zone3Off = json_str["zone3"]['off']['mins'][0] - json_str["zone3"]['on']['mins'][0]
    asyncio.create_task(schedule(sprinklerZone3, zone3Off * 60,
                        wday=json_str["zone3"]['on']['wday'],
                        hrs=json_str["zone3"]['on']['hours'],
                        mins=json_str["zone3"]['on']['mins']))
    del(zone3Off)
    #log.info("task zone 3- {}".format(log.free()))

    zone4Off = json_str["zone4"]['off']['mins'][0] - json_str["zone4"]['on']['mins'][0]
    asyncio.create_task(schedule(sprinklerZone4, zone4Off * 60,
                        wday=json_str["zone4"]['on']['wday'],
                        hrs=json_str["zone4"]['on']['hours'],
                        mins=json_str["zone4"]['on']['mins']))
    del(zone4Off)

    #log.info("task zone 4- {}".format(log.free()))
    #asyncio.create_task(schedule(zone1, 'every 2 mins', hrs=None, mins=range(0, 60, 2)))
    # Launch a coroutine
    #asyncio.create_task(schedule(zone2, 'every 3 mins', hrs=None, mins=range(0, 60, 3)))
     #asyncio.create_task(schedule(foo, 'one shot', hrs=None, mins=range(0, 60, 2), times=1))
    #await asyncio.sleep(900)  # Quit after 15 minutes

    while 1:
       log.info('Every 1 minute')
       await asyncio.sleep(60)  # Running forever

def smain():
    try:

        asyncio.run(main())
        log.info('sprinkler is initialized')

    finally:
        _ = asyncio.new_event_loop()

