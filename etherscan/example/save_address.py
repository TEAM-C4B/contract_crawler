import sys
sys.path.append('../')

from etherscan_parser import token

t = token()
t.get_address(1)
t.save_address('page-1', path='../address/')
