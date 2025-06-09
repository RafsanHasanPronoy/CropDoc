import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database/cropdoc.db')
cursor = conn.cursor()

# Create diseases table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS diseases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        crop TEXT NOT NULL,
        disease_name TEXT NOT NULL,
        description TEXT NOT NULL
    )
''')

# Sample data (replace with accurate descriptions)
sample_data = [
    ("Tomato", "Tomato_Bacterial_spot", "Caused by Xanthomonas species, characterized by dark, water-soaked spots on leaves. Treatment: Use copper-based bactericides."),
    ("Tomato", "Tomato_Late_blight", "Caused by Phytophthora infestans, leading to dark lesions and leaf decay. Treatment: Apply fungicides and remove infected plants."),
    ("Tomato", "Tomato__Target_Spot", "Caused by Corynespora cassiicola, showing concentric rings on leaves. Treatment: Use fungicides and improve air circulation."),
    ("Tomato", "Tomato_healthy", "The leaf is healthy with no signs of disease."),
    ("Cauliflower", "Bacterial_spot_rot", "Bacterial infection causing dark spots and rot. Treatment: Apply bactericides and ensure proper drainage."),
    ("Cauliflower", "Black_Rot", "Caused by Xanthomonas campestris, leading to blackening of leaf veins. Treatment: Use resistant varieties and remove infected plants."),
    ("Cauliflower", "Disease_Free", "The leaf is healthy with no signs of disease."),
    ("Cauliflower", "Downy_Mildew", "Caused by Peronospora parasitica, showing yellow patches and white mold. Treatment: Apply fungicides and reduce humidity."),
    ("Pepper_bell", "Pepper__bell___Bacterial_spot", "Caused by Xanthomonas, showing water-soaked spots. Treatment: Use copper sprays and remove debris."),
    ("Pepper_bell", "Pepper__bell___healthy", "The leaf is healthy with no signs of disease."),
    ("Corn", "Corn___Common_Rust", "Caused by Puccinia sorghi, showing orange pustules. Treatment: Use resistant varieties and fungicides."),
    ("Corn", "Corn___Gray_Leaf_Spot", "Caused by Cercospora zeae-maydis, showing grayish lesions. Treatment: Apply fungicides and rotate crops."),
    ("Corn", "Corn___Healthy", "The leaf is healthy with no signs of disease."),
    ("Corn", "Corn___Leaf_Blight", "Caused by Exserohilum turcicum, leading to large lesions. Treatment: Use resistant hybrids and fungicides."),
    ("Wheat", "Wheat___Brown_Rust", "Caused by Puccinia recondita, showing brown pustules. Treatment: Apply fungicides and use resistant varieties."),
    ("Wheat", "Wheat___Healthy", "The leaf is healthy with no signs of disease."),
    ("Wheat", "Wheat___Yellow_Rust", "Caused by Puccinia striiformis, showing yellow stripes. Treatment: Use fungicides and resistant cultivars."),
    ("Rice", "Healthy_leaf_Rice", "The leaf is healthy with no signs of disease."),
    ("Rice", "Rice_Blast", "Caused by Magnaporthe oryzae, leading to lesions and yield loss. Treatment: Apply fungicides and use resistant varieties."),
    ("Rice", "Tungro", "Viral disease causing stunting and yellowing. Treatment: Use resistant varieties and control leafhoppers."),
    ("Jute", "Cescospora_Leaf_Spot", "Caused by Cercospora, showing brown spots. Treatment: Apply fungicides and remove infected leaves."),
    ("Jute", "Golden_Mosaic", "Viral disease causing yellowing and mosaic patterns. Treatment: Control whiteflies and remove infected plants."),
    ("Jute", "Healthy_Leaf", "The leaf is healthy with no signs of disease."),
    ("Potato", "Potato___Early_Blight", "Caused by Alternaria solani, showing concentric rings. Treatment: Apply fungicides and rotate crops."),
    ("Potato", "Potato___Healthy", "The leaf is healthy with no signs of disease."),
    ("Potato", "Potato___Late_Blight", "Caused by Phytophthora infestans, leading to dark lesions. Treatment: Use fungicides and remove infected plants.")
]

cursor.executemany('INSERT OR REPLACE INTO diseases (crop, disease_name, description) VALUES (?, ?, ?)', sample_data)

# Commit and close
conn.commit()
conn.close()

print("Database initialized successfully.")