import requests


endpoint="http://127.0.0.1:8000/api/articles/16"

#get_response = requests.get(endpoint)
get_response = requests.delete(endpoint, ) # {'title': ['api-article'], 'body': ['article created with api-client'], 'slug': ['api-article'], 'thumb': ['']}

print({"data": get_response.json()})