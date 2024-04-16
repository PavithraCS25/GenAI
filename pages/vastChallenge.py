# Import necessary libraries
import streamlit as st
import streamlit.components.v1 as components
import base64

'''
This file contains the frontend code for VAST Challenge analysis.
'''


# Set page configuration including title, icon, layout, and initial sidebar state
st.set_page_config(page_title = 'Pavithra Sainath Portfolio' ,page_icon="👩‍💻",layout="wide", initial_sidebar_state="expanded")
# Define column layout for image and header
img,head = st.columns([1,15])
# Display image
with img:
    st.markdown(
    """<a>
    <img src="data:image/png;base64,{}" width="60">
    </a>""".format(
        # Encode image to base64
        base64.b64encode(open("images/powerplant.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
# Display header
with head:
    st.header("VAST Challenge")
# Add divider
st.divider()
# Embed Tableau visualization using HTML component
with st.container(border=True):
    html_code = """
    # Define HTML code to embed Tableau visualization
    <div class='tableauPlaceholder' id='viz1712836590129' style='position: relative'><noscript><a href='#'><img alt='VAST_CHALLENGE_MC2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;CY&#47;CYGT563SP&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;CYGT563SP' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;CY&#47;CYGT563SP&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1712836590129');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    # Embed the HTML code using the HTML component
    components.html(html_code,height=900,width=1090)
