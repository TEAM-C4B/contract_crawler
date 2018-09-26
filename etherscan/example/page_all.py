import sys
sys.path.append('../')

from parser_library import token

t = token()

for i in range(1, 14):
	filename = 'page-' + str(i)
	t.save_all(i, filename, add_path='../address', code_path='../src')
