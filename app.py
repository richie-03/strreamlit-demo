#credentials.py
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

#main.py
import os
import openai
import langchain
from langchain.llms import AzureOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader

#from credentials import *
def generate_response(*args):
  if len(args) == 1:
    query = args[0]
    llm = AzureOpenAI(deployment_name="text-davinci-003", model_name="text-davinci-003")
    response = llm(query)
    return response 
  else:
    query = args[0]
    doc = args[1]
    loader = PyPDFLoader(doc)
    pages = loader.load_and_split()
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    #intialize vectorstore
    vectorstore = FAISS.from_documents([Document(page_content=" ")], embeddings)
    search_indices = []    
    for i, chunk in enumerate(pages):
      data = [Document(page_content=str(chunk))]
      var_name = f"search_index_{i}"
      locals()[var_name] = FAISS.from_documents(data, OpenAIEmbeddings(model="text-embedding-ada-002"))
      search_indices.append(locals()[var_name])
    for db in search_indices:
      vectorstore.merge_from(db)
    qa = ConversationalRetrievalChain.from_llm(AzureChatOpenAI(deployment_name="GPT35-Demo1", model_name="gpt-35-turbo", temperature=0), vectorstore.as_retriever())
    response = qa({"question": question, "chat_history": ""})
    return response

#app.py
import streamlit as st
#from main import *
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
