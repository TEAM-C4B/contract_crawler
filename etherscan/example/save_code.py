import sys
sys.path.append('../')

from parser_library import token

t = token()
t.get_address(1)
t.get_code()
t.save_code(path='../src/')
