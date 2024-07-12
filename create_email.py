import requests

payload = {
    'requestor': 'test',
    'version': '1.0',
}

response = requests.post('http://api.nodemailer.com/user', json=payload)
if response.status_code == 200:
    account =  response.json()
    print(account)
else:
    raise Exception(f'Could not create Ethereal account: {response.text}')


'''
{'status': 'success', 'user': 'hthw6mmwctsswjt5@ethereal.email', 'pass': '8r469B1EAGQQhrGVTQ', 'smtp': {'host': 'smtp.ethereal.email', 'port': 587, 'secure': False}, 'imap': {'host': 'imap.ethereal.email', 'port': 993, 'secure': True}, 'pop3': {'host': 'pop3.ethereal.email', 'port': 995, 'secure': True}, 'web': 'https://ethereal.email', 'mxEnabled': False}
'''
