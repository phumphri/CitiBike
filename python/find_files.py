from os import walk
import os
import post_trips
mypath = os.path.join('C:\\', 'citibike')
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
i = 0
for filename in filenames:
    csvpath = os.path.join(mypath, filename)
    # print(csvpath)
    post_trips.run(csvpath)
    i += 1
    if i > 0:
        pass

