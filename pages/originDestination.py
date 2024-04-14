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
        base64.b64encode(open("images/car.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
with head:
    st.header("Origin Destination Analysis")

st.divider()
# Specify the path to your local PDF file
pdf_file_name = 'images/OD_analysispdf.pdf'
with fitz.open(pdf_file_name) as doc:
    # Convert the PDF page to a pixmap (an image)
    pix = doc[0].get_pixmap()
    # Convert the pixmap to an image format Streamlit can display (bytes)
    image_bytes = pix.tobytes("png")
    # Display the image in Streamlit
    with st.container(border=True):
        st.image(image_bytes,width=1090)