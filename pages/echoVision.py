# Importing necessary libraries
import streamlit as st
import base64
# Importing custom image model
from model import imagemodel
st.set_page_config(page_title = 'Pavithra Sainath Portfolio' ,page_icon="👩‍💻",layout="wide", initial_sidebar_state="expanded")

# Creating columns for image and header
img,head = st.columns([1,9])

# Displaying the image icon in the left column
with img:
    st.markdown(
    """<a>
    <img src="data:image/png;base64,{}" width="60">
    </a>""".format(
        base64.b64encode(open("images/image_icon.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)

# Displaying the header in the right column
with head:
    st.header("EchoVision - A multimodal bot")

# Adding a divider for separation
st.divider()
# Providing a file uploader for users to upload image files
image = st.file_uploader("Upload your image Files and Click on the Submit Button", type = ['png', 'jpg'],accept_multiple_files=True)

# Checking if the user clicked the "Submit" button
if st.button("Submit"):
    with st.spinner("Processing..."):
        # Processing the uploaded image files
        result_list = imagemodel.process_image(image)
        text_chunks = imagemodel.get_text_chunks(result_list)
        imagemodel.get_vector_store(text_chunks)
        # Displaying a success message after processing is complete
        st.success("Done")

# Providing a text input field for users to enter their questions
user_question = st.text_input("Enter question below,")

# Checking if the user has entered a question
if user_question:
    # Generating a response to the user's question using the custom image model
    response = imagemodel.user_input(user_question)
    # Displaying the response to the user
    st.write("Reply: ", response["output_text"])
