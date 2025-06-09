import h5py
import json
import os

# Define model files (same as in app.py)
model_files = {
    "Tomato": "model/tomato_disease_cvt_model.h5",
    "Cauliflower": "model/cauli_disease_cvt_model.h5",
    "Pepper_bell": "model/pepper_disease_cvt_model.h5",
    "Corn": "model/corn_disease_cvt_model.h5",
    "Wheat": "model/wheat_disease_cvt_model.h5",
    "Rice": "model/rice_disease_cvt_model.h5",
    "Jute": "model/jute_disease_cvt_model.h5",
    "Potato": "model/potato_disease_cvt_model.h5"
}

def fix_model_config(input_path, output_path):
    try:
        with h5py.File(input_path, 'r') as f:
            model_config = f.attrs.get('model_config')
            if not model_config:
                print(f"No model_config found in {input_path}")
                return
            config = json.loads(model_config)
            modified = False
            for layer in config['config']['layers']:
                if layer['class_name'] == 'InputLayer' and 'batch_shape' in layer['config']:
                    layer['config']['batch_input_shape'] = layer['config'].pop('batch_shape')
                    modified = True
            if modified:
                with h5py.File(output_path, 'w') as f_new:
                    f_new.attrs['model_config'] = json.dumps(config)
                    f.copy('model_weights', f_new)
                    f_new.attrs['keras_version'] = f.attrs['keras_version']
                    f_new.attrs['backend'] = f.attrs['backend']
                print(f"Fixed model: {input_path} -> {output_path}")
            else:
                print(f"No changes needed for {input_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {str(e)}")

# Create a directory for fixed models
os.makedirs('model/fixed', exist_ok=True)

# Fix each model
for crop, model_path in model_files.items():
    output_path = f"model/fixed/{os.path.basename(model_path)}"
    fix_model_config(model_path, output_path)

print("All models processed.")