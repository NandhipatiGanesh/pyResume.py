import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Digital Marketing Resume",
    page_icon="👋",
)

#hide unwanted text
st.set_option('deprecation.showfileUploaderEncoding', False)
    
#opening the image
image = Image.open ('./Images/New Passport profile photo.png')

#displaying the image on streamlit app
st.image (image, caption='')
