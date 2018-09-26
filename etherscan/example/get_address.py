import sys
sys.path.append('../')

from parser_library import token

t = token()

address_list = t.get_address(1)
print address_list
