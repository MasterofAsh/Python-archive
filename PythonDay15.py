# Python Exercise 2

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestampH = int(time.strftime('%H'))
timestampM = int(time.strftime('%M'))
timestampS = int(time.strftime('%S'))
print(timestampH, timestampM, timestampS)

if(timestampH < 10):
    print("Good morning sir")
elif(timestampH > 10 and timestampH < 18):
    print("Good afternoon sir")
else:
    print("Good evening sir.")