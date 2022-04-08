import requests

# endpoint="https://httpbin.org/status/200/"
endpoint="http://localhost:8000/api/"

get_response=requests.get(endpoint,params={"message":1234},json={"query":"Hello!"})# HTTP request
# print(get_response.text)#raw response code(http)
print(get_response.json())
print(get_response.status_code)





