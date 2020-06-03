import urllib.request as ur
import xml.etree.ElementTree as et

url = input('Enter location: ')
# 'http://python-data.dr-chuck.net/comments_42.xml'


sum = 0

print('Retrieving', url)
xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree=et.fromstring(xml)
data=tree.findall('.//comment')
for i in data :
    sum=sum+int(i.find('count').text)
print(sum)
