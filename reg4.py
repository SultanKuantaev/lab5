import re

s = input()
def matching(s):
    pattern = 'a.*?b$'
    if re.match(pattern,s):
        return "mathes"
    else:
        return "do not match"
print(matching(s))