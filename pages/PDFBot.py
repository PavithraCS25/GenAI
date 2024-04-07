import streamlit as st
from model import pdfmodel

st.set_page_config(page_title = 'Pavithra portfolio - PDFBot',page_icon="👩‍💻",)
st.header("Ask anything in the document")
pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit Button", type = 'pdf',accept_multiple_files=True)
if st.button("Submit"):
    with st.spinner("Processing..."):
        raw_text = pdfmodel.get_pdf_text(pdf_docs)
        text_chunks = pdfmodel.get_text_chunks(raw_text)
        print(text_chunks)
        pdfmodel.get_vector_store(text_chunks)
        st.success("Done")

user_question = st.text_input("Enter question below,")

if user_question:
    response = pdfmodel.user_input(user_question)
    st.write("Reply: ", response["output_text"])
