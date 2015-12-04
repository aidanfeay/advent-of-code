import hashlib
import time

timer = time.time()
hashVal = ''
numVal = 0
while hashVal[:6] != "000000":
  numVal += 1
  hashVal = hashlib.md5('yzbqklnj' + str(numVal)).hexdigest()
print numVal, hashVal
print str(time.time() - timer) + "s"