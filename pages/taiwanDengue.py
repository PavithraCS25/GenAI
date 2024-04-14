import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title = 'Pavithra Sainath Portfolio' ,page_icon="👩‍💻",layout="wide", initial_sidebar_state="expanded")
img,head = st.columns([1,15])
with img:
    st.markdown(
    """<a>
    <img src="data:image/png;base64,{}" width="60">
    </a>""".format(
        base64.b64encode(open("images/dengue.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
with head:
    st.header("Taiwan Dengue Analysis")
st.divider()
with st.container(border=True):
    iframe_src = "https://dengueepiviz.shinyapps.io/DengueEPIViz/"
    components.iframe(iframe_src,height=900,width=1090)
st.subheader('Report')
with st.container(border=True):
    st.markdown(
    """<a>
    <img src="data:image/png;base64,{}" width="1090">
    </a>""".format(
        base64.b64encode(open("images/dengue_analysis.jpg", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
