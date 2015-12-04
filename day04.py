import hashlib
import re

hashVal = hashlib.md5('')
numVal = 0
pattern = re.compile('^0{5}')
while not pattern.match(hashVal.hexdigest()):
  numVal += 1
  hashVal = hashlib.md5('yzbqklnj' + str(numVal))
print numVal, hashVal.hexdigest()