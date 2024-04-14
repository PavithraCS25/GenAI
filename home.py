import streamlit as st
import base64
import fitz
from model import pdfmodel
import os
from st_pages import Page, show_pages, add_page_title,Section
st.set_page_config(page_title = 'Pavithra Sainath Portfolio' ,page_icon="👩‍💻",layout="wide", initial_sidebar_state="expanded")
# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be

header = st.container()
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)


name,link = header.columns(2)
with name:
    st.header(':blue[Pavithra Coimbatore Sainath]', divider='rainbow')
with link:
    st.markdown(
    """<a href="https://www.linkedin.com/in/pavithra-coimbatore-sainath25/">
    <img src="data:image/png;base64,{}" width="60">
    </a>""".format(
        base64.b64encode(open("images/linkedin-blue-logo-icon.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)

contact, email = header.columns(2)
with contact:
    st.write("Contact: +6583199786")
with email:
    st.write("Email: pavithrasainath7@gmail.com")
    
### Custom CSS for the sticky header
st.markdown(
    """
<style>
    div[data-testid="stVerticalBlock"] div:has(div.fixed-header) {
        position: sticky;
        top: 2.875rem;
        background-color: black;
        z-index: 999;
    }
    .fixed-header {
        border-bottom: 1px solid black;
    }
</style>
    """,
    unsafe_allow_html=True
)


show_pages(
    [
        Page("home.py", "About Me",icon=":woman:"),
        Page("pages/accoladeAtlas.py", "Recognitions"),
        Page("pages/brandsBlogsCerts.py", "Artefacts"),
        Section(name="Generative AI work", icon=":robot_face:"),
        Page("pages/docuGenius.py","PDF Bot"),
        Page("pages/echoVision.py","Multimodal Bot"),
        Page("pages/insureBuddy.py","FWD Bot"),
        Page("pages/mediGuide.py","Health Bot"),
        Section(name="Data Analytics", icon=":bar_chart:"),
        Page("pages/taiwanDengue.py","TW Dengue Outbreak"),
        Page("pages/sgPopulationStudy.py","SG Population Study"),
        Page("pages/vastChallenge.py","Radioactive Leak Analysis"),
        Page("pages/originDestination.py","Origin Desination Analysis"),
    ]
)

# Specify the path to your local PDF file
pdf_file_name = 'sample_data/PavithraCS-Resume.pdf'
def display_pdf(file_path):
    # Open the PDF file
    with fitz.open(file_path) as doc:
        # Convert the PDF page to a pixmap (an image)
        pix = doc[0].get_pixmap()
        # Convert the pixmap to an image format Streamlit can display (bytes)
        image_bytes = pix.tobytes("png")
        col3,col4 = st.columns([40,40])
        with col3:
            # Display the image in Streamlit
            with st.container(border=True):
                st.image(image_bytes)
        with col4:
            with st.container(border=True):
                sample_question = st.radio(
                    "Here are few sample questions.",
                    ["Summarize the profile","List her Gen AI and ML experience", "What are her technical skills?"])
                
                user_question = st.text_input('Ask about me here...',key='resume')
                if not user_question:
                    if sample_question == 'Summarize the profile':
                        resume_question = sample_question
                    elif sample_question == 'List her Gen AI and ML experience':
                        resume_question = sample_question
                    elif sample_question == 'What are her technical skills?':
                        resume_question = sample_question
                else:
                    resume_question = user_question
                if resume_question:
                    response = pdfmodel.user_input(resume_question)
                    st.write(response["output_text"])
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 100px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

    
raw_text = pdfmodel.get_pdf_text([pdf_file_name])
text_chunks = pdfmodel.get_text_chunks(raw_text)
pdfmodel.get_vector_store(text_chunks)
display_pdf(pdf_file_name)
