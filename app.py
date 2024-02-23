import streamlit as st
import base64
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
import tempfile
import os

def generate_diagram():
    # Use a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        diagram_path = tmpfile.name

    # Generate the diagram
    with Diagram("Web Service", filename=diagram_path, show=False, outformat="png"):
        ELB("lb") >> EC2("web") >> RDS("userdb")

    # Encode the diagram in Base64
    with open(diagram_path, "rb") as img_file:
        base64_img = base64.b64encode(img_file.read()).decode('utf-8')

    # Display the Base64-encoded image using HTML in Streamlit
    html_str = f"<img src='data:image/png;base64,{base64_img}' />"
    st.markdown(html_str, unsafe_allow_html=True)

    # Clean up the temporary file
    os.remove(diagram_path)

if st.button('Generate Diagram'):
    generate_diagram()
