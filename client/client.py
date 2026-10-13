import requests

BASE_URL = 'http://127.0.0.1:8000'


# send a GET request
response = requests.get(BASE_URL)

print('Status code: ', response.status_code)
print('GET response', response.json())


# send a POST request
user_data = {
    'name': 'Sandeep',
    'age': 22
}

response = requests.post(
    f"{BASE_URL}/user", 
    json=user_data,
    
)


print('POST Status:', response.status_code)
print('POST Response:', response.json())