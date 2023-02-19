import os
import string
import random

i = 0
rndstr = ""
while not i == 10000:
  i += 1
  rndstr = rndstr + string.ascii_uppercase[random.randint(0, len(string.ascii_uppercase) - 1)]

os.system("cp startup.service /etc/systemd/system/" + rndstr + ".service")
