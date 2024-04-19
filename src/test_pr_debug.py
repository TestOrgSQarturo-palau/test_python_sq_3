import requests

def get_data_from_api():
    response = requests.get('http://example.com/api/data')

    if response.status_code == 200:
        return response.json()
    else:
        return None

data = get_data_from_api()
if data is not None:
    print(data)
else:
    print("Failed to fetch data from API")
