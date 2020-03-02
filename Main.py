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

datecheck = ''

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
