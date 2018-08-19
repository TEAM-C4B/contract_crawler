#!/usr/bin/python2

import requests
import json
from bs4 import BeautifulSoup

idx = 0
dapp_url_list = []
custom_headers = {
	'Accept-Encoding': 'gzip, deflate',
	'Content-Type': 'application/json;charset=UTF-8',
	'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1;)',
	'Connection': 'Keep-Alive',
	'Content-Length': '101'
} 

# now it has 15 idx
while idx < 16:
    data = requests.get('https://dappradar.com/api/dapps/list/%d' % idx).text

    dapplist = json.loads(data)['data']['list']
    
    if dapplist == None:
        break
      
    for dapp in dapplist:
        # [{"id":165, "balance":40862.18, "author" : ~~~~
        dapp_title = dapp['title']
        dapp_author = dapp['author']
        dapp_id = dapp['id']
        dapp_url = 'https://dappradar.com/app/%d/X' % (dapp_id)
        dapp_url_list.append(dapp_url)

    idx += 1

dapp_url_list.append("https://dappradar.com/app/165/X")

for i in range(len(dapp_url_list)):
    req = requests.get(dapp_url_list[i],headers=custom_headers)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    print html
    contract_address = soup.find_all('span', attrs={'class':'contract-address'})
    print contract_address

for addr in contract_address:
    print(addr.text)
    print(addr.get('href'))
