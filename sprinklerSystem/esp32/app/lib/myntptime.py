# Adapted from official ntptime by Peter Hinch July 2022
# The main aim is portability:
# Detects host device's epoch and returns time relative to that.
# Basic approach to local time: add offset in hours relative to UTC.
# Timeouts return a time of 0. These happen: caller should check for this.
# Replace socket timeout with select.poll as per docs:
# http://docs.micropython.org/en/latest/library/socket.html#socket.socket.settimeout

import socket
import struct
import select
from time import gmtime
import log

# (date(2000, 1, 1) - date(1900, 1, 1)).days * 24*60*60
# (date(1970, 1, 1) - date(1900, 1, 1)).days * 24*60*60
NTP_DELTA = 3155673600 if gmtime(0)[0] == 2000 else 2208988800

# The NTP host can be configured at runtime by doing: ntptime.host = 'myhost.org'
host = "pool.ntp.org"

def mytime(hrs_offset=0):  # Local time offset in hrs relative to UTC
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    poller = select.poll()
    poller.register(s, select.POLLIN)
    s.sendto(NTP_QUERY, addr)
    if poller.poll(1000):  # time in milliseconds
        msg = s.recv(48)
        print(msg)
        s.close()
        val = struct.unpack("!I", msg[40:44])[0]
        return val - NTP_DELTA + hrs_offset * 3600
    s.close()  # Timeout occurred
    log.info("NTP - timeout occured")
    return 0
# There's currently no timezone support in MicroPython, and the RTC is set in UTC time.
def settime():
    t = mytime(-7)
    import machine
    import utime
    tm = utime.gmtime(t)
    machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))

def init():
    import time
    log.info("Current time (before setting): " + str(time.localtime()))
    settime()
    log.info("Current time (after setting): " + str(time.localtime()))
