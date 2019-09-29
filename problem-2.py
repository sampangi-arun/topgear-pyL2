email='From abc.xyz@pqr.com Mon Dec 29 01:12:15 2016'

import re

results = re.search('([a-z]*.[a-z]*@([a-z]*.com)).*([0-9]{2}:[0-9]{2}:[0-9]{2})', email)
print(results.groups())