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
