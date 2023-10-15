from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

from keras.models import load_model
from keras.preprocessing import image
import numpy as np


def get_class_name(class_id):
    class_names = [
        "battery",
        "biological",
        "brown-glass",
        "cardboard",
        "clothes",
        "green-glass",
        "metal",
        "paper",
        "plastic",
        "shoes",
        "trash",
        "white-glass"
    ]
    if 0 <= class_id < len(class_names):
        return class_names[class_id]
    else:
        return "Invalid class ID"


def load_image(img_path, target_size=(150, 150)):
    img = image.image_utils.load_img(img_path, target_size=target_size)
    img_array = image.image_utils.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array


def predict_image(model_path, img_path):
    # Load the model
    model = load_model(model_path)
    # Load and preprocess the image
    img_array = load_image(img_path)
    # Make a prediction
    prediction = model.predict(img_array)
    # Get the class with the highest probability
    predicted_class = np.argmax(prediction)
    # Get the class name of the predicted class
    class_name = get_class_name(predicted_class)
    return class_name


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        model_path = 'modelsForWebsite/vgg16_transfer_learning_model.h5'
        prediction = predict_image(model_path, file_path)

        return render_template('display.html', filename=filename, prediction=prediction)
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
