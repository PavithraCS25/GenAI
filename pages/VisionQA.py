import streamlit as st
from model import imagemodel

st.set_page_config(page_title = 'Pavithra portfolio - VisionQA',page_icon="👩‍💻",)
st.header("Ask anything on the image")
image = st.file_uploader("Upload your image Files and Click on the Submit Button", type = ['png', 'jpg'],accept_multiple_files=True)
if st.button("Submit"):
    with st.spinner("Processing..."):
        result_list = imagemodel.process_image(image)
        text_chunks = imagemodel.get_text_chunks(result_list)
        imagemodel.get_vector_store(text_chunks)
        st.success("Done")

user_question = st.text_input("Enter question below,")

if user_question:
    response = imagemodel.user_input(user_question)
    st.write("Reply: ", response["output_text"])
