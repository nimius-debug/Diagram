import streamlit as st
from PIL import Image

# Assuming 'diagram.py' saves the diagram as 'Web_Service.png' in the current directory.
image_path = 'Web_Service.png'

def generate_diagram():
    # This will execute your diagram script and generate the image.
    # Make sure 'diagram.py' is in the same directory as this script, or adjust the path accordingly.
    import diagram  # This executes the diagram script.
    st.title('My Web Service Architecture')
    image = Image.open(image_path)
    st.image(image, caption='Web Service Architecture')
st.button('Generate Diagram', on_click=generate_diagram)  # Generate the diagram when the button is clicked.
  # Generate the diagram when the app runs.


