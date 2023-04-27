import streamlit as st
from main import *
# Create a text input field for the string input
query = st.text_input("Enter your query:")

# Create a toggle button to select an option
option = st.radio("Select an option:", ("wo_data", "w_data"))

# Generate a response based on the selected option
if option == "wo_data":
    response = generate_response(query)
else:
    # Create a file upload component for the document upload
    document_upload = st.file_uploader("Upload a document:")
    if document_upload is None:
        response = "Please upload a document."
    else:
        doc_contents = document_upload.read()
        doc = document_upload.name
        with open(f"{doc}","wb") as f:
            f.write(doc_contents)
        response = generate_response(query,doc)

# Display the response in a box
st.info(response)