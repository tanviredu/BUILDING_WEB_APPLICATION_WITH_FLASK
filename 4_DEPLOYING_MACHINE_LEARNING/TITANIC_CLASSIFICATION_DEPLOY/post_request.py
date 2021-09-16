
## if you dont want to use POSTMAN
## consider this is a client side program 
## that communicate with the server
import requests
url = "http://localhost:5000/api"
json_data = {
    "feture":[[3,1,22.0,1,0,7.25,2],[1,0,38.0,1,0,71.2833,0],[3,0,26.0,0,0,7.925,2],[1,0,35.0,1,0,53.1,2]]
}
r = requests.post(url,json=json_data)
print(r.json())
