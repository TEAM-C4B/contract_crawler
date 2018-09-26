import sys
sys.path.append('../')

from parser_library import token

t = token()
t.get_address(1)
name, code = t.get_code()

print name
print code
