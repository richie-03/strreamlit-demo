import streamlit as st
from jira_local_lib import *

#Setup document path, project name and server url
DOC_PATH = '/home/malchirichard/Desktop/cloud_ai/GPT-Demo/docs'
SERVER_URL = "jira-openai-test.atlassian.net"

def jira_assistant():
    st.title("Jira Assistant")
    project = st.text_input("Enter Project Name")
    if project:
        responses = generate_response(DOC_PATH,SERVER_URL,project)
        for issue, response in responses.items():
            st.write(issue)
            st.info(response)

#main
jira_assistant()


#PROJECT = 'jira-openai-test'