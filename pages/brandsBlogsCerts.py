import streamlit as st
import streamlit.components.v1 as components
import base64
import fitz
from itertools import cycle

st.set_page_config(page_title = 'Pavithra Sainath Portfolio' ,page_icon="👩‍💻",layout="wide", initial_sidebar_state="expanded")
img,head = st.columns([1,9])
with img:
    st.markdown(
    """<a>
    <img src="data:image/png;base64,{}" width="90">
    </a>""".format(
        base64.b64encode(open("images/Pavithra.jpg", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
with head:
    st.header("Brands, Blogs, and Certifications")
st.divider()
st.subheader('Certifications')
with st.container(border=True):
    certImages = ['certifications/AWSCC.png','certifications/AWSDA.png','certifications/FLOT.png','certifications/GA.png']
    cols = cycle(st.columns(2)) # st.columns here since it is out of beta at the time I'm writing this
    for idx, certImage in enumerate(certImages):
        next(cols).image(certImage)
st.divider()
st.subheader('Brands worked')
with st.container(border=True):
    brandImages = ['brands/adidas.png','brands/dell.png','brands/sk2.png','brands/vw.png','brands/bosch.png','brands/sgx.png','brands/purple.jpg','brands/proctor.png','brands/uber.png','brands/zeiss.png','brands/apple.png','brands/ferrari.png']
    certImages = ['certifications/AWSCC.png','certifications/AWSDA.png','certifications/FLOT.png','certifications/GA.png']
    cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
    for idx, brandImage in enumerate(brandImages):
        next(cols).image(brandImage, width=250)
st.divider()
st.subheader('Blogs and links')
with st.container(border=True,height=100):
    medium,git = st.columns(2)
    with medium:
        st.markdown(
        """<a href="https://medium.com/@pavithrasainath7/mastering-file-access-in-sharepoint-with-oauth-2-0-a-comprehensive-guide-0a6b2d53736a/">
        <img src="data:image/png;base64,{}" width="300">
        </a>""".format(
            base64.b64encode(open("images/medium.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )
    with git:
        st.markdown(
        """<a href="https://github.com/PavithraCS25?tab=repositories/">
        <img src="data:image/png;base64,{}" width="200">
        </a>""".format(
            base64.b64encode(open("images/GitHub.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )

    
    



