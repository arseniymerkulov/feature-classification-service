import numpy as np
import glob
import json
import os


from settings_package.settings import Settings


class FeatureDataset:
    class NumpyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            return json.JSONEncoder.default(self, obj)

    def __init__(self):
        settings = Settings.get_instance()
        self.dataset_directory = settings.dataset_directory

        self.features = []
        self.labels = []

    @staticmethod
    def get_norm(features):
        return np.sum(features*features)

    @staticmethod
    def features_from_json(features_json):
        return np.array(json.loads(features_json))

    @staticmethod
    def features_to_json(features):
        return json.dumps(features, cls=FeatureDataset.NumpyEncoder)

    def add(self, features, label):
        self.features.append(features)
        self.labels.append(label)
        self.save(len(self.features) - 1)

    def save(self, i):
        dir_path = f'{self.dataset_directory}/{self.labels[i]}'

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        category = glob.glob(f'{dir_path}/*.json')
        file_path = f'{dir_path}/{self.labels[i]}_{len(category)}.json'

        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                features_json = FeatureDataset.features_to_json(self.features[i])
                file.write(features_json)

    def load(self):
        for label in os.listdir(self.dataset_directory):
            category = glob.glob(f'{self.dataset_directory}/{label}/*.json')

            for path in category:
                with open(path, 'r') as file:
                    self.features.append(FeatureDataset.features_from_json(file.read()))
                    self.labels.append(label)

    def classify(self, features):
        assert len(self.features) > 0, 'dataset is empty'
        assert features.shape == self.features[0].shape, 'features have wrong shape'

        diff = [FeatureDataset.get_norm(dataset_features - features) for dataset_features in self.features]
        diff_with_labels = zip(diff, self.labels)
        diff_with_labels = sorted(diff_with_labels, key=lambda tup: tup[0])

        return diff_with_labels[0][1]

    def describe(self):
        return f'categories: {self.labels}, length {len(self.labels)}'
