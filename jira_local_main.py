from jira_local_lib import *

#Setup document path, project name and server url
DOC_PATH = '/home/malchirichard/Desktop/cloud_ai/GPT-Demo/docs'
PROJECT = 'jira-openai-test'
SERVER_URL = "jira-openai-test.atlassian.net"

#main
responses = generate_response(DOC_PATH,SERVER_URL,PROJECT)
print(responses)
