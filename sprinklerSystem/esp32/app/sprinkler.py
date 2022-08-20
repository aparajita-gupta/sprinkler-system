import time

import log
#esp.osdebug(None)
import relay





async def init():
    log.info('pubsub is going to start  running...')
    relay.Relay()
    import pubsubtask
    await pubsubtask.initPubSub()


