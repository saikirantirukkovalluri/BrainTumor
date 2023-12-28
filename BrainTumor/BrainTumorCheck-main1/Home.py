import streamlit as st
import streamlit.components.v1 as components

# Set page title
st.set_page_config(
    page_title="Brain Tumor Detection and Classification",
    initial_sidebar_state="expanded",
)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
components.html(
    """
    <style>
        #effect{
            margin:0px;
            padding:0px;
            font-family: "Source Sans Pro", sans-serif;
            font-size: max(8vw, 20px);
            font-weight: 700;
            top: 0px;
            right: 25%;
            position: fixed;
            background: -webkit-linear-gradient(0.25turn,blue,white);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 2rem;
        }
    </style>
    <p id="effect">Brain Tumor Check</p>
    """,
    height=69,
)



def page_layout():
   
    st.write("Brain Tumor Check is an app developed by Students Of SVEC that takes an image as input and predicts the type of tumor, using CNN and MRIs of the patients. This Web app uses advanced algorithms to diagnose various tumors and classify them into brain")
    st.write("Developed By SVEC")
    st.markdown("## Benefits:")
    st.write("- Fast and accurate diagnosis of diseases")
    st.write("- Non-invasive and painless diagnosis using MRI")
    st.write("- Accessible from anywhere, anytime")
    st.markdown("## Why to use our App?")
    st.write("- Our app combines multiple ML models into one app")
    st.write("- The app uses CNN on MRI imagery to diagnose diseases")
    st.write("- It uses advanced algorithms to provide fast and accurate diagnosis")
    st.markdown("## Uses:")
    st.write("- Hospitals and clinics can use our app to diagnose diseases more quickly")
    st.write("- Patients can use our app to get a quick and accurate diagnosis without the need for invasive procedures")

    
# Render page layout
page_layout()
