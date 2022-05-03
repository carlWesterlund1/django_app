import requests

id = 26 # id of article to change
endpoint="http://127.0.0.1:8000/api/update/{0}".format(id) 
data = {
    "title": "updated title",
    "body": "updated body",
    "slug": "new_version"
}

put_response = requests.put(endpoint, data)  

print({'data' : put_response.json()}) 