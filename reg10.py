import re
s = input()
def camel_to_snake(s):
        
        changed = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', changed).lower()

print(camel_to_snake(s))