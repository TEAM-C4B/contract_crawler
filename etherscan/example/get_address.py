import sys
sys.path.append('../')

from etherscan_parser import token

t = token()

address_list = t.get_address(1)
print address_list
