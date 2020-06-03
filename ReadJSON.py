import urllib.request
import json,ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
address = urllib.request.urlopen(url)
print("Retrieving ",url)
data = address.read().decode()
js = json.loads(data)
print("Retrieved ", len(data)," characters")
sum=0
j=0
for i in js["comments"]:
    sum+=(i['count'])
    j+=1
print("Count:",j)
print("Sum:",sum)
