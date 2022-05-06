import requests


endpoint="http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint)  

#post_response = requests.post(endpoint, {'title': ['api-article'], 'body': ['article created with api-client'], 'slug': ['api-article'], 'thumb': ['']})  



print({'data' : get_response.json()})
"""article_dict = {}
for x in get_response.json(): article_dict[x['title']]=x # creates python dictionary with titles of articles as keys
print(article_dict)"""