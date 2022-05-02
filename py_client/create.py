import requests


endpoint="http://127.0.0.1:8000/api/"
data =  {'title': ['api-article232'],
        'body': ['testing generic APIView'], 
        'slug': ['api-article'],'thumb': ['']}

get_response = requests.post(endpoint, data) 
print({'data' : get_response.json()})