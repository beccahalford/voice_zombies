import requests


base_url = 'http://localhost:8000'
url = base_url + '/zombies/api/map'
token = 'd1f327c3ebaff8747d77178e9c86ba49b4c54793'

response = requests.get(url, headers={
    'Content-type': 'application/json',
    'Authorization': 'Token {}'.format(token)
})

print(response.status_code)
print(response.json())