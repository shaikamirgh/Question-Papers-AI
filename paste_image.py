import streamlit as st
from streamlit_paste_button import paste_image_button as pbutton
from PIL import Image


paste_result = pbutton(
    label="📋 Paste an image",
    errors="raise",
)

if paste_result.image_data is not None:
    st.write('Pasted image:')
    st.image(paste_result.image_data)
    paste_result.image_data.save('pasted_image.png')  
    
    print(paste_result.image_data)
