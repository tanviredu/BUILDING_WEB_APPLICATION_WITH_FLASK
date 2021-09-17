import requests
url = "http://localhost:5000/api"
json_data = {
    "feature":[[3,142,80,15,0,32.4,0.2,63],[1,95,74,21,73,25.9,0.673,36],[2,127,46,21,335,34.4,0.176,22]]
}
r = requests.post(url,json=json_data)
print(r.json())