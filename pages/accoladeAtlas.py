# Importing necessary libraries
import streamlit as st
import streamlit.components.v1 as components
import base64
import fitz
st.set_page_config(page_title = 'Pavithra Sainath Portfolio' ,page_icon="👩‍💻",layout="wide", initial_sidebar_state="expanded")

# Creating columns for image and header
img,head = st.columns([1,9])

# Displaying the image in the left column
with img:
    st.markdown(
    """<a>
    <img src="data:image/png;base64,{}" width="90">
    </a>""".format(
        base64.b64encode(open("images/Pavithra.jpg", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)

# Displaying the header in the right column
with head:
    st.header("Recognitions")

# Adding a divider for separation
st.divider()
# Displaying recognitions from GroupM
st.subheader('GroupM')
# Creating a container to display images with a scrollable view
with st.container(border=True,height = 2500):
    # List of image paths
    images_on_page = ['appreciation/andy_linkedin.png','appreciation/joyce3.png','appreciation/tania.png','appreciation/amanda.png','appreciation/nithya.png','appreciation/zheng.png','appreciation/josh.png','appreciation/joyce2.png','appreciation/meena.png','appreciation/sid2.png','appreciation/sid.png','appreciation/flo.png','appreciation/andy2.png','appreciation/adam.png','appreciation/andy1.png','appreciation/joyce.png','appreciation/2023_EOY.png']
    # Displaying images
    st.image(images_on_page, use_column_width=True)
# Adding a divider for separation
st.divider()
# Displaying recognitions from SGX
st.subheader('SGX')
# Creating a container to display images with a scrollable view
with st.container(border=True):
    # List of image paths
    images_on_page = ['appreciation/keith.png']
    # Displaying images
    st.image(images_on_page, use_column_width=True)

# Adding a divider for separation
st.divider()
# Displaying recognitions from Bosch
st.subheader('Bosch')
# Creating a container to display images with a scrollable view
with st.container(border=True,height=1300):
    # List of image paths
    images_on_page = ['appreciation/evelyn.png','appreciation/bosch_app.png']
    # Displaying images
    st.image(images_on_page, use_column_width=True)

# Adding a divider for separation
st.divider()
# Displaying recognitions from Infosys
st.subheader('Infosys')
# Creating a container to display images with a scrollable view
with st.container(border=True,height=700):
    # List of image paths
    images_on_page = ['appreciation/Mayank.png','appreciation/Manoj.png']
    # Displaying images
    st.image(images_on_page, use_column_width=True)


