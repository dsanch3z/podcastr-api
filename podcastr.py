import json
import requests
import xmltodict

def lambda_handler(event, context):
  print(event)
  url = event.url
  feed = requests.get(url)
  parsed = xmltodict.parse(feed.text)
  result = json.dumps(parsed)
  return result

# with open('result.json', 'w') as f:
#     print(result, file=f)  # Python 3.x
