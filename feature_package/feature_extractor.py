import tensorflow_hub as hub
import tensorflow as tf


from settings_package.settings import Settings


class FeatureExtractor:
    def __init__(self):
        settings = Settings.get_instance()
        self.model = hub.load(settings.extractor_url)

    def extract(self, image):
        model_input = tf.convert_to_tensor([image], dtype='float32')
        model_output = self.model.signatures['default'](model_input)
        features = model_output['default'].numpy()[0]
        return features
