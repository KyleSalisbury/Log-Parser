from urllib.request import urlretrieve
import re
from collections import Counter

Address = 'https://s3.amazonaws.com/tcmg476/http_access_log'

Local_copy = 'Log_copy.log'

local_file, headers = urlretrieve(Address, Local_copy) 


#////////
Local_copy = open('Log_copy.log')

lines = Local_copy.readlines()

checklist = ()

LogTotal = 0

Files = {}

failcount = 0
redirectcount = 0



jan = open('janlog.txt', 'w')
feb = open('feblog.txt', 'w')
mar = open('marlog.txt', 'w')
apr = open('aprlog.txt', 'w')
may = open('maylog.txt', 'w')
jun = open('junlog.txt', 'w')
jul = open('jullog.txt', 'w')
aug = open('auglog.txt', 'w')
sep = open('seplog.txt', 'w')
oct = open('octlog.txt', 'w')
nov = open('novlog.txt', 'w')
dec = open('declog.txt', 'w')
monthcheck = ''

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
    
    """
    #Used for tracking error/redirection codes
    if len(checklist) > 5:
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
