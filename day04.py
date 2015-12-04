import hashlib
import re
import time

timer = time.time()
hashVal = hashlib.md5('')
numVal = 0
pattern = re.compile('^0{6}')
while not pattern.match(hashVal.hexdigest()):
  numVal += 1
  hashVal = hashlib.md5('yzbqklnj' + str(numVal))
print numVal, hashVal.hexdigest()
print time.time() - timer

# this is slow as sin