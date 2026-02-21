import torch
import torchvision.transforms as T
from torchvision.models.segmentation import deeplabv3_resnet50
from PIL import Image
import numpy as np

# Load pre-trained DeepLabV3 model
def load_model():
    model = deeplabv3_resnet50(weights='DeepLabV3_ResNet50_Weights.DEFAULT')
    model.eval()
    return model

# Preprocess image
def preprocess(image):
    transform = T.Compose([
        T.Resize((520, 520)),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406],
                    std=[0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)

# Run segmentation
def segment_image(model, image):
    input_tensor = preprocess(image)
    with torch.no_grad():
        output = model(input_tensor)['out'][0]
    mask = output.argmax(0).byte().numpy()
    return mask

