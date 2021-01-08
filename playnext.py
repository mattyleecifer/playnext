import os
import csv
from os import listdir
from os.path import isfile, join

try:
    with open('eplist.csv', newline='') as f:
        reader = csv.reader(f)
        eplist = list(reader)

    eplist = [i for i in eplist[0]]
    if ".py" in eplist[0] or ".txt" in eplist[0] or ".csv" in eplist[0]:
        eplist.pop(0)
    else:
        pass
    os.system('"' + eplist[0] + '"')
    eplist.pop(0)
    with open('eplist.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(eplist)
except:
    mypath = os.getcwd()
    eplist = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    with open('eplist.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(eplist)
