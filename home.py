import streamlit as st
import base64
import fitz

def display_pdf(file_path):
    # Open the PDF file
    with fitz.open(file_path) as doc:
        # Iterate through each page
        for page in doc:
            # Convert the PDF page to a pixmap (an image)
            pix = page.get_pixmap()
            # Convert the pixmap to an image format Streamlit can display (bytes)
            image_bytes = pix.tobytes("png")
            # Display the image in Streamlit
            st.image(image_bytes)

# Specify the path to your local PDF file
pdf_file_path = 'PavithraCS-Resume.pdf'
st.set_page_config(page_title = 'Pavithra portfolio - Home' ,page_icon="👩‍💻",)

st.header("Pavithra Coimbatore Sainath")
display_pdf(pdf_file_path)
st.divider()
st.text("Contact: +6583199786")
st.text("Email: pavithrasainath7@gmail.com")
st.markdown(
    """<a href="https://www.linkedin.com/in/pavithra-coimbatore-sainath25/">
    <img src="data:image/png;base64,{}" width="25">
    </a>""".format(
        base64.b64encode(open("linkedin.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
st.sidebar.success("select a page above")