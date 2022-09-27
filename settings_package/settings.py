class Settings:
    instance = None

    def __init__(self):
        self.image_size = (224, 224)

        self.dataset_directory = 'data/dataset'
        self.images_directory = 'data/images'
        self.allowed_image_extensions = ['jpg']

        self.authorization = False
        self.rest_endpoint_url = 'https://skuvision.edgesoft.ru:9060'

        self.extractor_url = 'https://tfhub.dev/tensorflow/efficientnet/lite0/feature-vector/2'

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = Settings()

        return cls.instance
