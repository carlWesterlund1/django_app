import requests


endpoint="http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint)  

#post_response = requests.post(endpoint, {'title': ['api-article'], 'body': ['article created with api-client'], 'slug': ['api-article'], 'thumb': ['']})  

print({'data' : get_response.json()})