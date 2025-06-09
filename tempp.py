from flask import Flask, request, render_template, redirect, url_for
import os
import numpy as np
from PIL import Image
import tensorflow as tf
import sqlite3
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'PNG' ,'JPG', 'JPEG'}

# Crop and model mapping
CROP_MODELS = {
    "Tomato": "model/tomato_disease_cvt_model.h5",
    "Cauliflower": "model/cauli_disease_cvt_model.h5",
    "Pepper_bell": "model/pepper_disease_cvt_model.h5",
    "Corn": "model/corn_disease_cvt_model.h5",
    "Wheat": "model/wheat_disease_cvt_model.h5",
    "Rice": "model/rice_disease_cvt_model.h5",
    "Jute": "model/jute_disease_cvt_model.h5",
    "Potato": "model/potato_disease_cvt_model.h5"
}

CROP_CLASSES = {
    "Tomato": [
        "Tomato_Bacterial_spot",
        "Tomato_Late_blight",
        "Tomato__Target_Spot",
        "Tomato_healthy"
    ],
    "Cauliflower": [
        "Bacterial_spot_rot",
        "Black_Rot",
        "Disease_Free",
        "Downy_Mildew"
    ],
    "Pepper_bell": [
        "Pepper__bell___Bacterial_spot",
        "Pepper__bell___healthy"
    ],
    "Corn": [
        "Corn___Common_Rust",
        "Corn___Gray_Leaf_Spot",
        "Corn___Healthy",
        "Corn___Leaf_Blight"
    ],
    "Wheat": [
        "Wheat___Brown_Rust",
        "Wheat___Healthy",
        "Wheat___Yellow_Rust"
    ],
    "Rice": [
        "Healthy_leaf_Rice",
        "Rice_Blast",
        "Tungro"
    ],
    "Jute": [
        "Cescospora_Leaf_Spot",
        "Golden_Mosaic",
        "Healthy_Leaf"
    ],
    "Potato": [
        "Potato___Early_Blight",
        "Potato___Healthy",
        "Potato___Late_Blight"
    ]
}

# Load models (load on-demand to save memory)
def load_model(crop):
    return tf.keras.models.load_model(CROP_MODELS[crop])

# Check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Preprocess image (match training: 160x160, normalize to [0,1])
def preprocess_image(image):
    img = image.resize((160, 160))  # Match model input size
    img_array = np.array(img) / 255.0  # Normalize to [0,1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Get disease description from database
def get_disease_description(crop, disease_name):
    conn = sqlite3.connect('database/cropdoc.db')
    cursor = conn.cursor()
    cursor.execute("SELECT description FROM diseases WHERE crop = ? AND disease_name = ?", (crop, disease_name))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "No description available."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html', crops=CROP_CLASSES.keys())

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files or 'crop' not in request.form:
        return redirect(url_for('upload'))
    
    crop = request.form.get('crop')
    if crop not in CROP_CLASSES:
        return redirect(url_for('upload'))
    
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Load and preprocess image
        image = Image.open(file_path).convert('RGB')
        img_array = preprocess_image(image)
        
        # Load model and predict
        model = load_model(crop)
        predictions = model.predict(img_array)
        predicted_class_idx = np.argmax(predictions[0])
        predicted_class = CROP_CLASSES[crop][predicted_class_idx]
        confidence = float(predictions[0][predicted_class_idx]) * 100
        
        # Get description
        description = get_disease_description(crop, predicted_class)
        
        return render_template('result.html', 
                             crop=crop,
                             image_path=file_path,
                             prediction=predicted_class,
                             confidence=confidence,
                             description=description)
    
    return redirect(url_for('upload'))

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)