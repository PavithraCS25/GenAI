import streamlit as st
from model import pdfmodel
import os
import base64

st.set_page_config(page_title = 'Pavithra Sainath Portfolio' ,page_icon="👩‍💻",layout="wide", initial_sidebar_state="expanded")
img,head = st.columns([1,9])
with img:
    st.markdown(
    """<a>
    <img src="data:image/png;base64,{}" width="60">
    </a>""".format(
        base64.b64encode(open("images/PDF_file_icon.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
with head:
    st.header("DocuGenius")
st.divider()
pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit Button", type = 'pdf',accept_multiple_files=True)
if st.button("Submit"):
    with st.spinner("Processing..."):
        raw_text = pdfmodel.get_pdf_text(pdf_docs)
        text_chunks = pdfmodel.get_text_chunks(raw_text)
        pdfmodel.get_vector_store(text_chunks)
        st.success("Done")
user_question = st.text_input("Enter question below,")

if user_question:
    response = pdfmodel.user_input(user_question)
    st.write("Reply: ", response["output_text"])