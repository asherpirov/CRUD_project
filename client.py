import requests

new_data ={"shape_type": "square" ,"side": 101}

url = "http://127.0.0.1:8000/shapes/"

response = requests.post(url, json=new_data)
print(response.status_code)
print(response.text)





