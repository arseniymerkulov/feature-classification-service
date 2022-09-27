import requests


from feature_package.feature_dataset import FeatureDataset
from feature_package.feature_extractor import FeatureExtractor
from feature_package.image import Image


if __name__ == '__main__':
    token = '.'
    url = 'http://127.0.0.1:5000'
    route = '/api/classify'

    headers = {'Authorization': 'Bearer ' + token}
    image = 'images/goldfish-check.jpg'
    features = FeatureExtractor().extract(Image.load(image))
    features_json = FeatureDataset.features_to_json(features)

    req = requests.post(url + route,
                        headers=headers,
                        verify=True,
                        json=features_json)
    
    print(req.text)
