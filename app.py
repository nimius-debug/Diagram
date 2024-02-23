import streamlit as st
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from io import BytesIO

def generate_diagram():
    diagram_path = "temp_diagram.png"  # Temporary file
    with Diagram("Web Service", filename=diagram_path, show=False, outformat="png"):
        ELB("lb") >> EC2("web") >> RDS("userdb")
    
    # Read the diagram into a BytesIO buffer
    buffer = BytesIO()
    with open(diagram_path, "rb") as f:
        buffer.write(f.read())
    buffer.seek(0)

    # Display the image from the BytesIO buffer
    st.image(buffer, caption='Web Service Architecture', format='PNG')

if st.button('Generate Diagram'):
    generate_diagram()
