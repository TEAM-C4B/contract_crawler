import bs4
import json
import requests

class token:
	def __init__(self):
		self.api_url = 'https://api.etherscan.io/api?module=contract&action=getsourcecode&address='
		self.token_url = 'https://etherscan.io/tokens?p='
		
		self.address_list = []
		self.name_list = []
		self.code_list = []

	
	def get_address(self, page):
		if page < 0:
			print '[-] Not found !'
			return -1
		
		self.address_list = []		

		url = self.token_url + str(page)
		
		r = requests.get(url)
		html = r.text.encode('utf-8')
		
		soup = bs4.BeautifulSoup(html, 'html.parser')
		parse = soup.find('table', {'class':'table'}).find_all('h5', {'style':'margin-bottom:4px'})
		
		for p in parse:
			info = p.find('a')
		
			address = info['href']
			address = address.split('/')[2]
			
			self.address_list.append(address)
		
		return self.address_list	
		

	def save_address(self, filename, path='address'):
		if self.address_list == []:
			print '[-] Have not data !'
			return -1
		
		filename = path + '/' + filename
		f = open(filename, 'w')

		for address in self.address_list:
			f.write(address + '\n')
		
		f.close()

		print '[+] Success saving !'
		
		return 0

	def get_code_with_address(self, address):
		url = self.api_url + address
		
		r = requests.get(url)
		data = r.text.encode('utf-8')
		
		info = json.loads(data)['result']
		name = info[0]['ContractName'].encode('utf-8')
		code = info[0]['SourceCode'].encode('utf-8')
		
		if code == '':
			print '[-] Not found code !'
	
		return name, code


	def get_code(self):
		if self.address_list == []:
			print '[-] Have not data !'
			return -1
			
		self.name_list = []
		self.code_list = []
	
		for address in self.address_list:
			name, code = self.get_code_with_address(address)

			self.name_list.append(name)
			self.code_list.append(code)

		return self.name_list, self.code_list
		

	def save_code(self, path='src'):
		if self.address_list == []:
			print '[-] Have not data !'
			return -1

		if self.code_list == []:
			print '[-] Have not data !'
			return -1
		
		
		for i in range(0, len(self.code_list)):
			if self.code_list[i] != '':
				filename = path + '/' + self.name_list[i] + '_' + self.address_list[i] + '.sol'
				f = open(filename, 'w')
				f.write(self.code_list[i])
				f.close()

		print '[+] Success saving !'

		return 0

	
	def save_all(self, page, filename, add_path='address', code_path='src'):
		address = self.get_address(page)
		self.save_address(filename, path=add_path)
		name, code = self.get_code()
		self.save_code(path=code_path)

		return address, name, code
