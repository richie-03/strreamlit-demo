import os
import openai
import langchain
from langchain.llms import AzureOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader

from credentials import *
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
      search_indices.append(locals()[var_name]
    for db in search_indices:
      vectorstore.merge_from(db)
    qa = ConversationalRetrievalChain.from_llm(AzureChatOpenAI(deployment_name="GPT35-Demo1", model_name="gpt-35-turbo", temperature=0), vectorstore.as_retriever())
    response = qa({"question": question, "chat_history": ""}
    return response
