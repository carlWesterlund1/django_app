import requests

id =  input("what is the id of article you want to delete?\n")# id of article to delete
try:
    id = int(id)
except:
    id = None
    print (f'{id} is not a valid id')
if id:
   endpoint="http://127.0.0.1:8000/api/delete/{0}".format(id) 
   response = requests.delete(endpoint)  
   print(response.status_code)