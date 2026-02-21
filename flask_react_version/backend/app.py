from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import numpy as np
import torch
import torchvision.transforms as T
from torchvision.models.segmentation import deeplabv3_resnet50
import base64
import io
import matplotlib.pyplot as plt

app = Flask(__name__)
CORS(app)

# Load model
model = deeplabv3_resnet50(weights='DeepLabV3_ResNet50_Weights.DEFAULT')
model.eval()

def preprocess(image):
    transform = T.Compose([
        T.Resize((520, 520)),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406],
                    std=[0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)

@app.route('/segment', methods=['POST'])
def segment():
    file = request.files['image']
    image = Image.open(file).convert('RGB')
    
    input_tensor = preprocess(image)
    with torch.no_grad():
        output = model(input_tensor)['out'][0]
    mask = output.argmax(0).byte().numpy()

    # Convert mask to image
    fig, ax = plt.subplots()
    ax.imshow(mask, cmap='tab20')
    ax.axis('off')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()

    return jsonify({'mask': encoded})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)