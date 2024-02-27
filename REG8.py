import re

s = input()

def replace2(s):
    return re.findall('[A-Z][^A-Z]*', s)
print(replace2(s))