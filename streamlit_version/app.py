import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from model import load_model, segment_image

# Page config
st.set_page_config(page_title="Image Segmentation App", layout="wide")
st.title("Image Segmentation Web App")
st.write("Upload an image to get semantic segmentation using DeepLabV3")

# Load model (only once)
@st.cache_resource
def get_model():
    return load_model()

model = get_model()

# Image upload
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Segmented Output")
        with st.spinner("Segmenting... please wait"):
            mask = segment_image(model, image)
            fig, ax = plt.subplots()
            ax.imshow(mask, cmap="tab20")
            ax.axis("off")
            st.pyplot(fig)

    st.success("Segmentation Complete!")