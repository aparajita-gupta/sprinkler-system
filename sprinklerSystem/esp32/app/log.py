from time import localtime
import os
debug = True
filename = 'sprinkler.log'


def free(full=False):
  import gc
  gc.collect()
  F = gc.mem_free()
  A = gc.mem_alloc()
  T = F+A
  P = '{0:.2f}%'.format(F/T*100)
  if not full: return P
  else : return ('Total:{0} Free:{1} ({2})'.format(T,F,P))

def info(msg, console_only=False):
    if (debug == False):
        return
    if console_only:
        print(msg)
    else:
        try:
          if os.stat(filename)[6] > 200000:
            os.remove(filename)
        except:
            pass
        yr, mo, md, h, m, s, wd = localtime()[:7]
        fst = '{:02d}-{:02d}-{:02d}:{:02d}:{:02d}:{:02d} [INFO] '
        fst = fst.format(md, mo, yr, h, m, s)
        #print('{0} - {1}\n'.format(fst, msg))
        f = open(filename, 'a')

        f.write('{0} - {1}\n'.format(fst, msg))
        f.close()
