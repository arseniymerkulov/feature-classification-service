import requests


if __name__ == '__main__':
    token = '.'
    url = 'http://127.0.0.1:5000'
    route = '/api/info'

    headers = {'Authorization': 'Bearer ' + token}

    req = requests.get(url + route,
                       headers=headers,
                       verify=True)
    
    print(req.text)
