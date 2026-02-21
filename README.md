
# Image Segmentation Web App

This project demonstrates semantic image segmentation using DeepLabV3, implemented both as a Streamlit prototype and as a Flask + React production-style application.


## Technologies
- Python, PyTorch, DeepLabV3
- Streamlit (Version 1)
- Flask + React.js (Version 2)
- Docker

## Version 1 — Streamlit
cd streamlit_version
pip install -r requirements.txt
streamlit run app.py

## Version 2 — Flask + React
### Backend
cd flask_react_version/backend
pip install -r requirements.txt
python app.py

### Frontend
cd flask_react_version/frontend
npm install
npm start

## Docker
docker-compose up

## Usage
1. Open http://localhost:8501 (Streamlit)
2. Or http://localhost:3000 (React)
3. Upload image
4. Click Segment Image
5. View results

## Model
Pre-trained DeepLabV3 ResNet50 on COCO dataset.

# Image-Segmentation-Web-App
Semantic Image Segmentation Web App using DeepLabV3, Flask, React and Streamlit with Docker deployment
