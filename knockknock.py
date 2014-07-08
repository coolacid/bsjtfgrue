#!/usr/bin/python

from sys import exit
from operator import xor
import time

#now = time.strftime('%m%d%Y%H%M%S')

#now = "07082014100100"

def getaccess(mask, ditdah, salt, now):
  fn = []
  tn = []
  ditdah = ditdah.replace(" ", "")
  idx = -1
  ddidx = -1
  tidx = -1
  if(now[-2:] == "00" or now[-2:] == "30"):
    nstr = str(now) + str(salt)
  else:
    nstr = str(salt)

  for ltr in mask:
    idx += 1
    ddidx += 1
    tidx +=1
    if(ddidx >= len(ditdah)):
      ddidx = 0
    if(tidx >= len(nstr)):
      tidx = 0

    fn.append(chr(xor(xor(ord(ltr), ord(ditdah[ddidx:ddidx+1])), ord(nstr[tidx:tidx+1]))))

  fnstr = "".join(map(str, fn))
  return fnstr
  
def main():
  firsthacker = "Nevil Maskelyne"
  rats = ".-. .-- ..."
  year = "1903"

  print getaccess(firsthacker, rats, year)
  
if __name__ == "__main__":
  main()
