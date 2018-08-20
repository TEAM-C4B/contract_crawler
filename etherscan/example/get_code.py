import sys
sys.path.append('../')

from etherscan_parser import token

t = token()
t.get_address(1)
name, code = t.get_code()

print name
print code
