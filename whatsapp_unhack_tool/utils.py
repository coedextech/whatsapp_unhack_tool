import requests

def send_request(url, params=None, data=None, headers=None):
    try:
        response = requests.get(url, params=params, data=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error sending request: {e}")
        return None