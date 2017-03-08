"""discovery.py is the build() function needed to create a service endpoint
for interacting with an API"""
"This application let's you query public ativities in the Google+ API HTTP Client Library "
import httplib2
import sys
from apiclient.discovery import build

API_KEY = 26b7fc1faccc9bccc4714f78ea9db6ac11e3015b
SERVICE = build(API, VERSION, developerKey=API_KEY)

TMPL = '''
    User: %s
    Date: %s
    Post: %s
'''

GPLUS = discovery.build('plus', 'v1', developerKey=API_KEY)

"Use search() method to query public activities"
items = GPLUS.activities().search(query='heaven').execute().get('items', [])
for data in items:
	post = ' '.join(data['title'].strip().split())
	if post:
		print(TMPL % (data['actor']['displayName'],
						data['published'], post))