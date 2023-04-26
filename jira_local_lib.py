#get jira tickets and search solution from local doc
import os

from JiraReader import *
from credentials import *

from llama_index import GPTSimpleVectorIndex, download_loader
from langchain import OpenAI
from gpt_index.response.utils import get_response_text

#load local document and index to gpt
def load_doc(doc_path):
	SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
	loader = SimpleDirectoryReader(doc_path, recursive=True, exclude_hidden=True)
	documents = loader.load_data()
	index = GPTSimpleVectorIndex.from_documents(documents)
	return index

#Fetch tickets from jira
def generate_response(doc_path,server_url,project):
	index = load_doc(doc_path)
	response_list = []
	response_dict = {}
	reader = JiraReader(email=email, api_token=api_token, server_url=server_url)
	issues = reader.load_data(query=f'project = {project}')
	#get responses as text and store in list
	for i in issues:
		response = index.query(i)
		text = get_response_text(response.response)
		text = text.replace('\n', '')
		response_list.append(text)
	for i in range(len(issues)):
		response_dict[issues[i]] = response_list[i]
	return response_dict

