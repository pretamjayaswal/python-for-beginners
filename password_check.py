# password matcher

import re
pwd = "AAAsssggA45$nnnnnnnnnn"
# pwd = input("Password : ")

print(bool(re.search('[a-z]',pwd)))

error = ''

if not re.search('[a-z]',pwd):
    error = "cond 1 not matching"
if not re.search('[0-9]',pwd):
    error = "cond 2 not matching"
if not re.search('[A-Z]',pwd):
    error = "cond 3 not matching"
if not re.search('[$#@]',pwd):
    error = "cond 4 not matching"
if len(pwd) < 6:
    error = "cond 5 not matching, min len 6"
if len(pwd) >12:
    error = "cond 6 not matching, max len 12"

if error:
    print(f'Password {pwd} not Valid , reason: {error}')
else:
    print(f'Password {pwd} is OK')


