# Import necessary libraries
import streamlit as st
import streamlit.components.v1 as components
import base64
st.set_page_config(page_title = 'Pavithra Sainath Portfolio' ,page_icon="👩‍💻",layout="wide", initial_sidebar_state="expanded")
# Define column layout for image and header
img,head = st.columns([1,15])
# Display image
with img:
    st.markdown(
    """<a>
    <img src="data:image/png;base64,{}" width="60">
    </a>""".format(
        base64.b64encode(open("images/dengue.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
# Display header
with head:
    st.header("Taiwan Dengue Analysis")
# Add divider
st.divider()
# Embed Shiny web application using iframe
with st.container(border=True):
    iframe_src = "https://dengueepiviz.shinyapps.io/DengueEPIViz/"
    components.iframe(iframe_src,height=900,width=1000)
# Display report
st.subheader('Report')
with st.container(border=True):
    st.markdown(
    """<a>
    <img src="data:image/png;base64,{}" width="1090">
    </a>""".format(
        # Encode image to base64
        base64.b64encode(open("images/dengue_analysis.jpg", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
