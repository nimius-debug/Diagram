import streamlit as st
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from io import BytesIO
import os

def generate_diagram():
    diagram_path = "temp_diagram.png"  # Define a path for the temporary file
    try:
        # Generate the diagram and save it to a temporary file
        with Diagram("Web Service", filename=diagram_path, show=False, outformat="png"):
            ELB("lb") >> EC2("web") >> RDS("userdb")
        
        # Initialize a BytesIO object and read the diagram into it
        buffer = BytesIO()
        with open(diagram_path, "rb") as f:
            buffer.write(f.read())
        buffer.seek(0)

        # Display the image from the BytesIO object
        st.image(buffer, caption='Web Service Architecture', format='PNG')
    finally:
        # Clean up by removing the temporary file after it's no longer needed
        if os.path.exists(diagram_path):
            os.remove(diagram_path)

if st.button('Generate Diagram'):
    generate_diagram()
