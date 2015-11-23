# import json
import requests


prefix = 'https://api.github.com/search/repositories?q='
suffix = '&sort=stars&order=desc&page='

lang     = raw_input('Language (java, cpp, python,...): ')
stars    = raw_input('Min. number of stars: ')
projects = input('Number of projects: ')
outFile  = raw_input('Output file: ')
 
lang  = '+language:' + lang 
stars = 'stars:%3E'  + stars

uri   = prefix + stars + lang + suffix


print 'searching the github API'
print 'query string:', uri

response = requests.get(uri + '1')
data = response.json()

items = data['items']

pagination = 0

f = open(outFile, 'w')

for item in items:
#  line = item["name"] + ";" + item["size"] + ";" + item["watchers"] + ";" + item["forks"] + ";" + item["git_url"] + ";" + item["description"] 
#  print(line)
  pagination += 1 

pages = 1 + (projects // pagination)

for i in range(1, pages):
  print uri + str(i + 1)
  response = requests.get(uri + str(i + 1))
  data = response.json()
  if(data.has_key('items')): 
      items = items + data['items']
  else: 
      print data
      break 

count = 0   
for item in items: 
  if(count < projects and item != None):
      line   = item.get("name", "-") + ","
      line  += str(item.get("size", "-")) + "," 
      line  += str(item.get("watchers", "-")) + "," 
      line  += str(item.get("forks", "-")) + "," 
      line  += item.get("git_url", "-") + "," 
      line  += item.get("description", "-")    
      count += 1
      f.write(line.encode('utf8') + '\n')
  elif(count >= projects):  
    break

f.close()
print 'Number of projects: ', count

