import sys
sys.path.append('./app')
import schedule_task
import utils
import gc
import lib.myntptime
#import webrepl
#webrepl.start()
gc.collect()
utils.connectToWifi()
lib.myntptime.init()
schedule_task.smain()
#sprinkler.init()