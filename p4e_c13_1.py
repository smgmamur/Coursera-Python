import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input('Enter a URL: ')
if len(url) < 1:
    url = ' http://py4e-data.dr-chuck.net/comments_1558285.xml'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = (uh.read()).decode()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
sum = 0

for item in lst:
    sum = sum + int(item.find('count').text)
print(sum)

input("Press Enter to close this window")
