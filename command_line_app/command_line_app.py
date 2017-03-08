"""discovery.py is the build() function needed to create a service endpoint
for interacting with an API"""
"This application let's you query public ativities in the Google+ API HTTP Client Library "
from apiclient.discovery import build

"""Template for the results that comeback. Set parameters to be displayed"""
TMPL = '''
	User: %s 
	Date: %s
	Post: %s
'''

API_KEY = 26b7fc1faccc9bccc4714f78ea9db6ac11e3015b #copied from credentials page where a project was created via goodle dev account
SERVICE = build(API, VERSION, developerKey=API_KEY)

GPLUS = discovery.build('plus', 'v1', developerKey=API_KEY)
 
"Use search() method to query public activities"
items = GPLUS.activities().search(query='love').execute().get('items', [])
for data in items:
	post = ' '.join(data['title'].strip().split())
	if post:
		print(TMPL % (data['actor']['displayName'],
						data['published'], post))