# Importing necessary libraries
import streamlit as st
import streamlit.components.v1 as components
import base64
import fitz
from itertools import cycle

'''
This file contains code to display the Artefacts of the brands, blogs and certifications that i have
'''

# Setting Streamlit page configuration
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
    st.header("Brands, Blogs, and Certifications")
# Adding a divider for separation
st.divider()
st.subheader('Certifications')
# Displaying certifications
with st.container(border=True):
    # List of certification images
    certImages = ['certifications/AWSCC.png','certifications/AWSDA.png','certifications/FLOT.png','certifications/GA.png']
    # Using itertools.cycle to cycle through columns
    cols = cycle(st.columns(2))
    # Displaying certification images
    for idx, certImage in enumerate(certImages):
        next(cols).image(certImage)
# Adding a divider for separation
st.divider()
# Displaying brands worked
st.subheader('Brands worked')
with st.container(border=True):
    # List of brand images
    brandImages = ['brands/adidas.png','brands/dell.png','brands/sk2.png','brands/vw.png','brands/bosch.png','brands/sgx.png','brands/purple.jpg','brands/proctor.png','brands/uber.png','brands/zeiss.png','brands/apple.png','brands/ferrari.png']
    # Using itertools.cycle to cycle through columns
    cols = cycle(st.columns(4)) 
    # Displaying brand images
    for idx, brandImage in enumerate(brandImages):
        next(cols).image(brandImage, width=250)
# Adding a divider for separation
st.divider()
# Displaying blogs and links
st.subheader('Blogs and links')
with st.container(border=True,height=100):
    # Creating columns for Medium and GitHub images
    medium,git = st.columns(2)
    # Displaying Medium image with a link
    with medium:
        st.markdown(
        """<a href="https://medium.com/@pavithrasainath7/mastering-file-access-in-sharepoint-with-oauth-2-0-a-comprehensive-guide-0a6b2d53736a/">
        <img src="data:image/png;base64,{}" width="300">
        </a>""".format(
            # Encoding and embedding the Medium image
            base64.b64encode(open("images/medium.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )
    # Displaying GitHub image with a link
    with git:
        st.markdown(
        """<a href="https://github.com/PavithraCS25?tab=repositories/">
        <img src="data:image/png;base64,{}" width="200">
        </a>""".format(
            # Encoding and embedding the GitHub image
            base64.b64encode(open("images/GitHub.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )

    
    



