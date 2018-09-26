import sys
sys.path.append('../')

from parser_library import token

t = token()
address, name, code = t.save_all(1, 'page-1', add_path='../address', code_path='../src')
