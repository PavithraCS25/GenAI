# Importing necessary libraries
import streamlit as st
# Importing custom package for PDF model
from model import pdfmodel
import os
import base64
st.set_page_config(page_title = 'Pavithra Sainath Portfolio' ,page_icon="👩‍💻",layout="wide", initial_sidebar_state="expanded")
# Creating columns for image and header
img,head = st.columns([1,9])

# Displaying the image in the left column
with img:
    st.markdown(
    """<a>
    <img src="data:image/png;base64,{}" width="60">
    </a>""".format(
        # Encoding and embedding the PDF file icon image
        base64.b64encode(open("images/PDF_file_icon.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)

# Displaying the header in the right column
with head:
    st.header("DocuGenius")
# Adding a divider for separation
st.divider()
# Providing a file uploader for users to upload PDF files
pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit Button", type = 'pdf',accept_multiple_files=True)

# Checking if the user clicked the "Submit" button
if st.button("Submit"):
    with st.spinner("Processing..."):
        # Processing the uploaded PDF files
        raw_text = pdfmodel.get_pdf_text(pdf_docs)
        text_chunks = pdfmodel.get_text_chunks(raw_text)
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
