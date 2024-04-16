# Import necessary libraries
import streamlit as st
 # Custom chat model module
from model import chatmodel
import base64
st.set_page_config(page_title = 'Pavithra Sainath Portfolio' ,page_icon="👩‍💻",layout="wide", initial_sidebar_state="expanded")
# Define column layout for image and header
img,head = st.columns([1,9])
# Display image
with img:
    st.markdown(
    """<a>
    <img src="data:image/png;base64,{}" width="60">
    </a>""".format(
        base64.b64encode(open("images/synapxe-logo.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
# Display header
with head:
    st.header("Synapxe MediGuide")
# Add divider
st.divider()
# Initialize session state variables if they don't exist
if 'memory' not in st.session_state:
    st.session_state.memory = chatmodel.demo_memory()


if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [] # Initialize chat history list

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])
# Get user input
input_text = st.chat_input("Ask your question here")
# If user input is provided
if input_text:
    with st.chat_message("user"):
        st.markdown(input_text)
    # Add user input to chat history
    st.session_state.chat_history.append({"role":"user","text":input_text})
    client = 'synapxe'
    # Get response from the chat model
    chat_response = chatmodel.demo_chain(input_txt = input_text,memory = st.session_state.memory,client = client)
    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(chat_response)
    # Add assistant response to chat history
    st.session_state.chat_history.append({"role":"assistant","text":chat_response})
