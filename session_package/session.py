import requests
import glob
import os


from feature_package.image import Image
from feature_package.feature_dataset import FeatureDataset
from feature_package.feature_extractor import FeatureExtractor
from settings_package.settings import Settings


class Session:
    def __init__(self):
        settings = Settings.get_instance()

        self.extractor = FeatureExtractor()
        self.dataset = FeatureDataset()
        self.dataset.load()

        self.allowed_image_extensions = settings.allowed_image_extensions
        self.images_directory = settings.images_directory

        self.authorization = settings.authorization
        self.rest_endpoint_url = settings.rest_endpoint_url

    def check_token(self, token):
        headers = {'Authorization': token}

        return requests.get(
            self.rest_endpoint_url + '/api/check',
            headers=headers,
            verify=True
        ).ok

    def check_image_extension(self, filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in self.allowed_image_extensions

    def clear_images(self):
        for extension in self.allowed_image_extensions:
            images = glob.glob(f'{self.images_directory}/*.{extension}')

            for image in images:
                os.remove(image)

    def add(self, image_path, label):
        image = Image.load(image_path)
        features = self.extractor.extract(image)
        self.dataset.add(features, label)

    def describe_dataset(self):
        return self.dataset.describe()

    def classify(self, features_json):
        features = FeatureDataset.features_from_json(features_json)

        try:
            label = self.dataset.classify(features)
            return label, True, ''

        except Exception as e:
            print(f'in session.classify: {e}')
            return '', False, str(e)
