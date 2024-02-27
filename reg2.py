import re

s = input()
def matching(s):
    pattern = '^ab{2,3}$'
    if re.match(pattern,s):
        return "mathes"
    else:
        return "do not match"
print(matching(s))