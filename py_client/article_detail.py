import requests

id = 29 # id of article to change
endpoint="http://127.0.0.1:8000/api/details/{0}".format(id) 

get_response = requests.get(endpoint)  

#delete_response = requests.delete(endpoint) 

#put_response = requests.put(endpoint, {'title': ['api-article'], 'body': ['article created with api-client'], 'slug': ['api-article'], 'thumb': ['']})  

print({'data' : get_response.json()}) # change get_response if using other variable