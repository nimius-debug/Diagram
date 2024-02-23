from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from io import BytesIO
import streamlit as st
from PIL import Image

def generate_diagram():
    # Define the diagram and save it to a BytesIO object
    with Diagram("Web Service", show=False, outformat="png"):
        ELB("lb") >> EC2("web") >> RDS("userdb")
    
    # Instead of saving the diagram to a file, save it to a BytesIO object
    bytes_io = BytesIO()
    bytes_io.seek(0)
    
    # Load the image from BytesIO object into PIL Image
    image = Image.open("Web_Service.png")
    
    # Display the image in Streamlit
    st.image(image, caption='Web Service Architecture')

# Streamlit button to generate and display the diagram
if st.button('Generate Diagram'):
    generate_diagram()