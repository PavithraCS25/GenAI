import streamlit as st
import streamlit.components.v1 as components
import base64
import fitz

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
    st.header("Recognitions")
st.divider()
st.subheader('GroupM')
with st.container(border=True,height = 2500):
    images_on_page = ['appreciation/andy_linkedin.png','appreciation/joyce3.png','appreciation/tania.png','appreciation/amanda.png','appreciation/nithya.png','appreciation/zheng.png','appreciation/josh.png','appreciation/joyce2.png','appreciation/meena.png','appreciation/sid2.png','appreciation/sid.png','appreciation/flo.png','appreciation/andy2.png','appreciation/adam.png','appreciation/andy1.png','appreciation/joyce.png','appreciation/2023_EOY.png']
    st.image(images_on_page, use_column_width=True)
st.divider()
st.subheader('SGX')
with st.container(border=True):
    images_on_page = ['appreciation/keith.png']
    st.image(images_on_page, use_column_width=True)
st.divider()
st.subheader('Bosch')
with st.container(border=True,height=1300):
    images_on_page = ['appreciation/evelyn.png','appreciation/bosch_app.png']
    st.image(images_on_page, use_column_width=True)
st.divider()
st.subheader('Infosys')
with st.container(border=True,height=700):
    images_on_page = ['appreciation/Mayank.png','appreciation/Manoj.png']
    st.image(images_on_page, use_column_width=True)


