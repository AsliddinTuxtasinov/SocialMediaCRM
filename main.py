import requests


access_token = 'YOUR_ACCESS_TOKEN'
api_base_url = 'https://graph.instagram.com/v18.0/'

username = input("Enter username you want to lookup: ")
print(f"The lookup username : {username}")

endpoint = f'{api_base_url}{username}?fields=id'
response = requests.get(endpoint, params={'access_token': access_token})
if response.status_code == 200:
    data = response.json()
    user_id = data.get('id')

    print(f'User ID for {username}: {user_id}')

    # Example endpoint for getting user profile information
    endpoint = f'{api_base_url}{user_id}?fields=id,username,followers_count'
    response = requests.get(endpoint, params={'access_token': access_token})
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print('Error:', response.status_code, response.json())

else:
    print('Error:', response.status_code, response.json())
