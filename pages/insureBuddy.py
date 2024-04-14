import streamlit as st
from model import chatmodel
import base64

st.set_page_config(page_title = 'Pavithra Sainath Portfolio' ,page_icon="👩‍💻",layout="wide", initial_sidebar_state="expanded")
img,head = st.columns([1,9])
with img:
    st.markdown(
    """<a>
    <img src="data:image/png;base64,{}" width="60">
    </a>""".format(
        base64.b64encode(open("images/FWDLife.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
with head:
    st.header("FWD InsureBuddy")
st.divider()

if 'memory' not in st.session_state:
    st.session_state.memory = chatmodel.demo_memory()


if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
    
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

input_text = st.chat_input("Ask your question here")
if input_text:
    with st.chat_message("user"):
        st.markdown(input_text)

    st.session_state.chat_history.append({"role":"user","text":input_text})
    client = 'fwd'
    chat_response = chatmodel.demo_chain(input_txt = input_text,memory = st.session_state.memory,client=client)

    with st.chat_message("assistant"):
        st.markdown(chat_response)

    st.session_state.chat_history.append({"role":"assistant","text":chat_response})
