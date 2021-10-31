import requests;

# GET request
url = 'http://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
print(response.json())

# POST request
jsonPayload = { 'album': 1, 'title': 'test', 'url': 'nothing.com', 'thumbnailUrl': 'nothing.com'}
response = requests.post(url, json=jsonPayload)
response.json()

# PUT request
url = 'http://jsonplaceholder.typicode.com/photos/100'
response = requests.put(url, json=jsonPayload)
response.json()

# DELETE request
response = requests.delete(url)

# authentication
url = 'https://api.github.com/user'
response = requests.get(url, auth=('djw-test', 'password1'))
response = requests.get(url, headers={'Authorization': 'KEY-from-github'})
response.json()

# Parsing data
my_json = response.json()
for key in my_json.keys():
 print (key)

my_json['id']

# Find duplicate URLs
url = 'http://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
json_data = response.json()
url_list = []
for photo in json_data:
    url_list.append(photo['url'])

print(len(url_list))
print(len(set(url_list)))