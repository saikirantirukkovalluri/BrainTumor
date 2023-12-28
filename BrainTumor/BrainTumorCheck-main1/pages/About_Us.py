import streamlit as st
import streamlit.components.v1 as components


# Set page title
st.set_page_config(
    page_title="Brain Tumor Detector | We are...",
    page_icon=":brain:",
    initial_sidebar_state="expanded",
)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
img{border-radius: 10px;}
</style> """, unsafe_allow_html=True)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)



st.markdown("## Brain Tumor Detector & classifier")
st.write("Introducing our Brain Tumor Detector & classifier app, a cutting-edge solution harnessing advanced artificial intelligence. This innovative application utilizes machine learning algorithms to analyze medical imaging, swiftly identifying potential brain tumors with high accuracy. Empowering healthcare professionals, our app facilitates early detection, enhancing treatment outcomes and saving lives.")


