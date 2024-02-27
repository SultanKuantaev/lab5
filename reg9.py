import re

s = input()

def replace2(s):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", s)
print(replace2(s))