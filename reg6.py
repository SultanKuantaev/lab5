import re

s = input()

def replace(s):
    return re.sub("[ ,.]", ":", s)
print(replace(s))