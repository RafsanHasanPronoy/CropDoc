"CropSage-BD: A Vision Transformer Enhanced Web Interface for Scalable Crop Disease Detection"

Overview 

CropSage-BD is a web-based application designed to empower farmers and agricultural professionals 
with AI-driven crop disease detection. Leveraging Vision Transformer (ViT) models, CropSage-BD
provides accurate and real-time identification of diseases affecting eight major crops: tomato, 
cauliflower, bell pepper, corn, wheat, rice, jute, and potato. The system offers a user-friendly 
interface for uploading crop images, selecting crop types, and receiving detailed analysis results, 
including disease identification, confidence scores, and treatment recommendations. 
The application is built using Flask for the backend, SQLite for data management, and TensorFlow 
for model inference. It supports scalable deployment and is designed to assist farmers in making 
data-driven decisions to improve crop health and yield. 


Objectives 


o Accurate Disease Detection: Utilize Convolutional Vision Transformer model trained on 
approximately 91000 of crop images to identify diseases with high confidence. 

o User-Friendly Interface: Provide an intuitive web interface for farmers to upload images 
and receive instant results. 

o Multi-Crop Support: Support eight major crops with a comprehensive disease database. 

o Scalable Architecture: Enable easy integration of additional crops and disease models. 

o Real-Time Analysis: Deliver results within seconds, including treatment 
recommendations. 


System Architecture 

CropSage-BD is structured as a Flask-based web application with the following components: 

1. Frontend (HTML/CSS/JavaScript) : 
 index.html: The homepage introducing CropSage-BD, highlighting its features and supported 
crops. 
 upload.html: The interface for selecting a crop type, uploading an image, and initiating AI 
analysis. 
 result.html: Displays the analysis results, including crop type, health status, confidence 
level, and disease description. 
 The frontend uses Tailwind CSS for responsive styling and includes interactive elements 
for file uploads and navigation.

2. Backend (Flask - app.py): 
 Flask Application: Handles routing, file uploads, and model inference. 
 Image Preprocessing: Uses PIL to resize images to 160x160 pixels and normalize pixel 
values for model input. 
 Model Inference: Loads pre-trained Vision Transformer models for each crop and predicts 
disease classes with confidence scores. 
 Database Integration: Queries a SQLite database to retrieve disease descriptions based 
on predictions. 
 File Management: Saves uploaded images to a designated folder (`static/uploads/`) with 
secure filenames.

4. Database (SQLite - init_db.py): - - 
A SQLite database (`cropdoc.db`) stores disease information for each crop, including disease 
names and treatment recommendations. 
The `init_db.py` script initializes the database with sample data for supported crops and 
diseases.

4. Machine Learning Models: - - 
Convolutional Vision Transformer models are stored in the `model/` directory, with one 
model per crop (e.g., `tomato_disease_cvt_model.h5`). 
Models are trained on crop-specific datasets and map to predefined disease classes (e.g., 
Tomato_Bacterial_spot, Tomato_healthy).


Features 

 AI-Powered Detection: Uses advanced Vision Transformer models for accurate disease 
identification. 

 Instant Results: Provides analysis results within seconds, including disease details and 
treatment suggestions. 

 Multi-Crop Support: Supports eight crops with a comprehensive disease database. 

 Responsive Design: Mobile-friendly interface built with Tailwind CSS. 

 Scalable Models: Modular model structure allows easy addition of new crops and diseases. 

 Database-Driven Descriptions: Retrieves detailed disease information from a SQLite 
database. 


Supported Crops and Diseases 

CropSage-BD supports the following crops and their associated diseases: 

Tomato: - Bacterial Spot, Late Blight, Target Spot, Healthy 

Cauliflower: - Bacterial Spot Rot, Black Rot, Downy Mildew, Disease-Free 

Bell Pepper: - Bacterial Spot, Healthy 

Corn: - Common Rust, Gray Leaf Spot, Leaf Blight, Healthy 

Wheat: - Brown Rust, Yellow Rust, Healthy 

Rice: - Rice Blast, Tungro, Healthy 

Jute: - Cercospora Leaf Spot, Golden Mosaic, Healthy 

Potato: - Early Blight, Late Blight, Healthy 


Technical Requirements :

Python: 3.8 or higher 


Dependency: 
  - Flask: Web framework for routing and rendering templates 
  - TensorFlow: For loading and running Vision Transformer models 
  - Pillow (PIL): For image preprocessing 
  - NumPy: For array operations 
  - SQLite3: For database management 
  - Werkzeug: For secure file handling 
Frontend: 
  - Tailwind CSS (via CDN) 
  - HTML5, CSS3, JavaScript 
Storage: 
  - Directory for model files (`model/`) 
  - Directory for uploaded images (`static/uploads/`) 
  - SQLite database (`database/cropdoc.db`) 

 
 Setup Instructions 
 
1. Install Dependencies: 
     
   pip install flask tensorflow pillow numpy 
  
2. Initialize the Database: Run the `init_db.py` script to create and populate the SQLite database: 
  
   python init_db.py 
    
 
3. Prepare Model Files: - Ensure pre-trained Vision Transformer models are placed in the `model/` directory. -Verify that model paths in `app.py` (CROP_MODELS dictionary) match the actual file 
locations. 
4. Create Upload Directory: 
mkdir -p static/uploads 
5. Run the Application: Start the Flask server: 
python app.py 
The application will be accessible at `http://127.0.0.1:5000`.

Usage 
1. **Access the Homepage**: - Navigate to `http://127.0.0.1:5000` to view the CropSage-BD homepage. - Explore features and supported crops. 
2. **Upload an Image**: - Go to the `/upload` route. - Select a crop type from the dropdown (e.g., Tomato, Corn). - Upload a leaf image (JPG, PNG, or WebP, max 10MB). - Click "Start AI Analysis" to process the image. 
3. **View Results**: - The `/predict` route processes the image and displays results on `result.html`. - Results include: - Crop type - Health status (e.g., Tomato_Bacterial_spot, Healthy) - Confidence level (percentage) - Disease description and treatment recommendations - Options to analyze another image or return to the homepage. 
4. **Error Handling**: - Invalid file formats or crop selections redirect to the upload page with an error message. - Model or database errors are logged to the console and displayed to the user. 
Code Structure - **app.py**: Main Flask application handling routes, image processing, model inference, and 
database queries. - **init_db.py**: Script to initialize the SQLite database with crop and disease data. - **index.html**: Homepage template showcasing features and supported crops. - **upload.html**: Template for image upload and crop selection. - **result.html**: Template for displaying analysis results. - **static/uploads/**: Directory for storing uploaded images. - **model/**: Directory for storing pre-trained Vision Transformer models. - **database/cropdoc.db**: SQLite database for disease descriptions.

Future Enhancements 
- **Model Expansion**: Add support for additional crops and diseases. 
- **Real-Time Monitoring**: Integrate with IoT devices for continuous crop monitoring.
- **User Accounts**: Allow users to save analysis history and track crop health over time.
- **API Integration**: Provide an API for third-party applications to access CropSage-BD's
functionality.
- **Localization**: Support multiple languages for global accessibility.
- 
Limitations
 - **Model Dependency**: Requires pre-trained models for each crop, which must be updated 
regularly.
 - **Image Quality**: Analysis accuracy depends on image clarity and lighting conditions. - **File Size Limit**: Supports images up to 10MB, which may restrict high-resolution uploads.

Conclusion 

CropSage-BD represents a significant advancement in precision agriculture, combining Vision 
Transformer technology with a scalable web interface to deliver actionable crop health insights. 
Its modular design and robust feature set make it a valuable tool for farmers and agricultural 
professionals seeking to optimize crop yields and sustainability. 
