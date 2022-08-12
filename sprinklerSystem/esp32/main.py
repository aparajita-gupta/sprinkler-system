import sys
sys.path.append('./app')
import schedule_task
#import sprinkler
import gc
#import webrepl
#webrepl.start()
gc.collect()

schedule_task.smain()
#sprinkler.init()