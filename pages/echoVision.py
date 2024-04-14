import streamlit as st
from model import imagemodel
import base64

st.set_page_config(page_title = 'Pavithra Sainath Portfolio' ,page_icon="👩‍💻",layout="wide", initial_sidebar_state="expanded")
img,head = st.columns([1,9])
with img:
    st.markdown(
    """<a>
    <img src="data:image/png;base64,{}" width="60">
    </a>""".format(
        base64.b64encode(open("images/image_icon.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
with head:
    st.header("EchoVision - A multimodal bot")
st.divider()
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