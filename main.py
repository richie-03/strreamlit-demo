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

question = "What is physicians brain digital twin?"

llm = AzureOpenAI(deployment_name="text-davinci-003", model_name="text-davinci-003")
wo_data_response = llm(question)

loader = PyPDFLoader("cisco.pdf")
pages = loader.load_and_split()
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
vectorstore = FAISS.from_documents(pages, embeddings)

qa = ConversationalRetrievalChain.from_llm(AzureChatOpenAI(deployment_name="GPT35-Demo1", model_name="gpt-35-turbo", temperature=0), vectorstore.as_retriever())
w_data_response = qa({"question": question, "chat_history": ""})

