import urllib3 
import requests

my_google = requests.get("http://raynji.blogspot.co.ke/")

print (my_google.headers)
print (my_google.text[500:1000])
print(my_google.status_code)