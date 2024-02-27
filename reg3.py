import re

s = input()
def matching(s):
    pattern = '^[a-z]+_[a-z]+$'
    if re.match(pattern,s):
        return "mathes"
    else:
        return "do not match"
print(matching(s))