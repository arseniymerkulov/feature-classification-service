import cv2


from settings_package.settings import Settings


class Image:
    @staticmethod
    def load(path):
        settings = Settings.get_instance()

        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, settings.image_size)

        return image
