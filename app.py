from flask import Flask, request
from werkzeug.utils import secure_filename


from session_package.session import Session


session = Session()
app = Flask(__name__)


@app.route('/')
def index():
    return {'message': 'feature classification service'}


@app.route('/api/info', methods=['GET'])
def info():
    return {'message': session.describe_dataset()}


@app.route('/api/add/<label>', methods=['POST'])
def add(label):
    if session.authorization and not session.check_token(request.headers['Authorization']):
        return {'error': 'unauthorized'}

    session.clear_images()

    if 'image' not in request.files:
        return {'error': 'no image part'}

    image = request.files['image']

    if image.filename == '':
        return {'error': 'image filename is empty'}

    if image and session.check_image_extension(image.filename):
        filename = secure_filename(image.filename)
        image_path = f'{session.images_directory}/{filename}'

        image.save(image_path)
        session.add(image_path, label)

        return {'message': 'image features added to dataset'}
    else:
        return {'error': 'invalid image extension'}


@app.route('/api/classify', methods=['POST'])
def classify():
    if session.authorization and not session.check_token(request.headers['Authorization']):
        return {'error': 'unauthorized'}

    features_json = request.get_json(force=True)
    label, success, err = session.classify(features_json)
    return {'message': label} if success else {'error': err}
