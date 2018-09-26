import sys
sys.path.append('../')

from parser_library import token

t = token()
t.get_address(1)
t.save_address('page-1', path='../address/')
