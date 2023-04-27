import os
import openai

openai.api_type = "azure"
openai.api_base = "https://gpt-demo1.openai.azure.com/"
openai.api_version = "2022-12-01"

# with open("openapi_key.txt", 'r') as file:
#    api_key = file.read().replace('\n', '')
api_key = "d6420559b1154f5d82f8364ec4c77b55"
os.environ["OPENAI_API_KEY"] = api_key
os.environ["AZURE_OPENAI_API_KEY"] = api_key
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://gpt-demo1.openai.azure.com/"
os.environ["OPENAI_ENGINES"] = "GPT-35-Demo1"
os.environ["OPENAI_EMBEDDINGS_ENGINE_DOC"] = "text-embedding-ada"
os.environ["OPENAI_EMBEDDINGS_ENGINE_QUERY"] = "text-embedding-ada"
os.environ["OPENAI_API_BASE"] = "https://gpt-demo1.openai.azure.com"
os.environ["OPENAI_ENGINES"] = "GPT35-Demo1"
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"


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
