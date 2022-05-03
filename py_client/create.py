import requests


endpoint="http://127.0.0.1:8000/api/"
data =  {'title': ['api-article55'],
        'body': ['testing generic APIView'], 
        'slug': ['api-article'],'thumb': ['']}

post_response = requests.post(endpoint, data) 
print({'data' : post_response.json()})