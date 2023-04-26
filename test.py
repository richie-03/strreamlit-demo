import streamlit as st

# Create a text input field for the string input
string_input = st.text_input("Enter a string input:")

# Create a toggle button to select an option
option_selected = st.radio("Select an option:", ("Option 1", "Option 2"))

# Generate a response based on the selected option
if option_selected == "Option 1":
    response = f"You selected {option_selected}. Your string input is: {string_input}."
else:
    # Create a file upload component for the document upload
    document_upload = st.file_uploader("Upload a document:")
    if document_upload is None:
        response = "Please upload a document."
    else:
        document_contents = document_upload.read()
        response = f"You selected {option_selected}. Your document contents are:\n\n{document_contents}"

# Display the response in a box
st.info(response)

