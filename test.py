import re

string = u"2 men 3 dogs"

x = re.findall('\d',string)

print(x)
print(string)