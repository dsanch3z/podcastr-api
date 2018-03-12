import json
import requests
import xmltodict

def lambda_handler(event, context):
  # print('event: ', event)
  rss_url = get_rss_url(event)
  feed = requests.get(rss_url)
  parsed = xmltodict.parse(feed.text)
  rss_as_json = json.dumps(parsed)
  response = {
    'headers': headers(),
    'body': rss_as_json,
    'statusCode': 200
  }
  return response

def get_rss_url(event):
  query_params = event['queryStringParameters']
  print('queryStringParameters: ', query_params)
  rss_url = query_params['rss_url']
  return rss_url

def headers():
  return {
    'Access-Control-Allow-Origin' : '*', # Required for CORS support to work
  }

# with open('result.json', 'w') as f:
#     print(result, file=f)  # Python 3.x
