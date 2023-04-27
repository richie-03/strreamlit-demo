import os

openai.api_type = "azure"
openai.api_base = "https://gpt-demo1.openai.azure.com/"
openai.api_version = "2022-12-01"

with open("openai_key.txt", 'r') as file:
   api_key = file.read().replace('\n', '')
os.environ["OPENAI_API_KEY"] = api_key
os.environ["AZURE_OPENAI_API_KEY"] = api_key
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://gpt-demo1.openai.azure.com/"
os.environ["OPENAI_ENGINES"] = "GPT-35-Demo1"
os.environ["OPENAI_EMBEDDINGS_ENGINE_DOC"] = "text-embedding-ada"
os.environ["OPENAI_EMBEDDINGS_ENGINE_QUERY"] = "text-embedding-ada"
os.environ["OPENAI_API_BASE"] = "https://gpt-demo1.openai.azure.com"
os.environ["OPENAI_ENGINES"] = "GPT35-Demo1"
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
