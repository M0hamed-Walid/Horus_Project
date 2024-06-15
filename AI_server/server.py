from flask import Flask, jsonify, request
from PIL import Image
import os
import numpy as np
import base64
import tensorflow as tf
import json



classes=['Statue of Akhenaten',
        'Statue of Djoser',
        'Statue of Hatshepsut',
        'Statue of Horus',
        'Statue of Khafre',
        'Statue of Nevrtity',
        'Statue of Ramesses II',
        'Statue of Sphinx',
        'Statue of Tuhotmus III',
        'Statue of Tutankhamun']



app = Flask("app");
model = loaded_model = tf.keras.models.load_model('./AI_server/model.h5', compile=False)
@app.get("/predect")
def predectionPage():
    data = request.get_json()
    # error
    if 'image' not in data:
        return jsonify({'message': 'Image data not found'}), 400
    
    image_data = data['image']
    image_bytes = base64.b64decode(image_data)


    filename = 'image_to_predect'  
    file_path = os.path.join("./images", filename)
    with open(file_path, 'wb') as f:
        f.write(image_bytes)
    image = Image.open("./images/image_to_predect")


    # Preprocess the image
    img = image.resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    # Make predictions
    predictions = loaded_model.predict(img_array)
    class_labels = classes
    score = tf.nn.softmax(predictions[0])
    classification_score = np.max(score)
    

    res = {
        "name":class_labels[tf.argmax(score)],
        "score":str(classification_score),
    }

    return jsonify(res)

app.run(host="0.0.0.0",port=8080, debug=False)
