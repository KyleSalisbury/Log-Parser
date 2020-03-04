from urllib.request import urlretrieve
import re
from collections import Counter
import os
from datetime import datetime

Address = 'https://s3.amazonaws.com/tcmg476/http_access_log'

Local_copy = 'Log_copy.log'

local_file, headers = urlretrieve(Address, Local_copy) 

if os.path.exists(Local_copy):
    print("Local copy of log file detected...")
else:
    print("No log file found. Downloading from server...")
    local_file, headers = urlretrieve(Address, Local_copy) 
    
#////////
Local_copy = open('Log_copy.log')

lines = Local_copy.readlines()

checklist = ()

LogTotal = 0

Files = {}
FilesByMonth = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
}

failcount = 0
redirectcount = 0



jan = open('1.log', 'w')
feb = open('2.log', 'w')
mar = open('3.log', 'w')
apr = open('4.log', 'w')
may = open('5.log', 'w')
jun = open('6.log', 'w')
jul = open('7.log', 'w')
aug = open('8.log', 'w')
sep = open('9.log', 'w')
oct = open('10.log', 'w')
nov = open('11.log', 'w')
dec = open('12.log', 'w')


for line in lines:
    checklist = (line.split())
    #print(checklist)

    LogTotal = LogTotal+1 #Used to count the total number of requests

    #Used for tracking the usage of individual files
    if len(checklist) > 5:
        Filecheck = checklist[6]
        if Filecheck in Files:
            Files[Filecheck] += 1
        else:
            Files[Filecheck] = 1
    
   
    #Used for tracking error/redirection codes
    if len(checklist) > 8:
    codecheck = checklist[8]
    if codecheck[0] == "4":
        failcount += 1
    if codecheck[0] == "3":
        redirectcount += 1
    
    
    
counter = Counter(Files)    
MostPopFile = counter.most_common(1)
LeastPopFile = counter.most_common()[:-2:-1]

    
finalred = (redirectcount/LogTotal)*100
finalfail = (failcount/LogTotal)*100

print("The most popular file was", MostPopFile)
print("The least popular file was", LeastPopFile)
print("The total number of requests made was", LogTotal)
print("The percentage of requests that were redirected was", finalred, '%')
print("The percentage of requests that failed was", finalfail, "%" )    
