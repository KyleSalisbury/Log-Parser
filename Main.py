from urllib.request import urlretrieve

Address = 'https://s3.amazonaws.com/tcmg476/http_access_log'

Local_copy = 'Log_copy.log'

local_file, headers = urlretrieve(Address, Local_copy) 

#////////
Local_copy = open('Log_copy.log')

lines = Local_copy.readlines()

checklist = ()