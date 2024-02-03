from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from flask_cors import cross_origin
# Importing deps for image prediction
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from caption import *
from captio_2 import *

app = Flask(__name__, static_folder='./build', static_url_path='/')
# CORS(app, resources={r"/*": {"origins": "http://localhost:8000"}})
CORS(app)

@app.route("/")
def home():
    return {"message": "Hello from backend"}


@app.route("/upload", methods=['POST'])
def upload():
    try:
        file = request.files['file']

        # Delete previous files in the folder
        folder_path = 'upload/'
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

        # Save the new file
        file.save(os.path.join(folder_path, file.filename))
        # file.save('upload/' + file.filename)
        # image_path = '../../backend/upload/' + file.filename
        # print(image_path)

        caption = predict_caption('upload/' + file.filename)
        print(caption)

        result_dic = {
            'image': "upload/" + file.filename,
            'description': caption
        }

        return jsonify({"caption": caption[0].title()})
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    app.run(port=8000, debug=True)


