import requests


if __name__ == '__main__':
    token = '.'
    url = 'http://127.0.0.1:5000'
    route = '/api/add/whale'

    headers = {'Authorization': 'Bearer ' + token}
    image = 'images/whale.jpg'

    req = requests.post(url + route,
                        files={'image': open(image, 'rb')},
                        headers=headers,
                        verify=True)
    
    print(req.text)
