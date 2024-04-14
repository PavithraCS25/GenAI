# Importing the necessary Streamlit library
import streamlit as st
# Importing the custom PDF model module
from model import pdfmodel

'''
This is the frontend code for the PDF Bot page
'''

# Setting up Streamlit page configuration
st.set_page_config(page_title = 'Pavithra portfolio - PDFBot',page_icon="👩‍💻",)
# Displaying a header to prompt users to ask questions about the document
st.header("Ask anything in the document")

# Providing a file uploader for users to upload PDF files
pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit Button", type = 'pdf',accept_multiple_files=True)

# Checking if the user clicked the "Submit" button
if st.button("Submit"):
    # Displaying a spinner while processing the PDF files
    with st.spinner("Processing..."):
        # Extracting raw text from the uploaded PDF files using the custom PDF model
        raw_text = pdfmodel.get_pdf_text(pdf_docs)
        # Splitting the raw text into chunks for vectorization
        text_chunks = pdfmodel.get_text_chunks(raw_text)
        # Creating and saving a vector store from the text chunks using the custom PDF model
        pdfmodel.get_vector_store(text_chunks)
        # Displaying a success message after processing is complete
        st.success("Done")

# Providing a text input field for users to enter their questions
user_question = st.text_input("Enter question below,")

# Checking if the user has entered a question
if user_question:
    # Generating a response to the user's question using the custom PDF model
    response = pdfmodel.user_input(user_question)
    # Displaying the response to the user
    st.write("Reply: ", response["output_text"])
