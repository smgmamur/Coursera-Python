import json
import urllib.request, urllib.parse, urllib.error
import ssl

url = input('Enter a URL: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1558286.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)
data = (uh.read()).decode()
info = json.loads(data)

sum = 0
for item in info['comments']:
    sum = sum + int(item['count'])

print(sum)

input("Press Enter to close this window")
