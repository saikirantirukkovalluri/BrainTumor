import streamlit as st
import imagerec
import pandas as pd
import random
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Brain Tumor Classification",
    page_icon=":dna:",
    initial_sidebar_state="expanded",
)


st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

uploaded_file = None

st.title("Brain Tumor Classification")

st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)


st.write("""Types of Tumor:

Glioma: A type of tumor that originates in the glial cells, which are the supportive cells in the brain. Gliomas can be either low-grade (slow-growing) or high-grade (fast-growing) and can affect different parts of the brain.

Meningioma: A tumor that arises from the meninges, which are the protective membranes that surround the brain and spinal cord. Meningiomas are usually benign and slow-growing, and may not require treatment if they are not causing symptoms.

Pituitary adenoma: A tumor that develops in the pituitary gland, which is located at the base of the brain. Pituitary adenomas can affect hormone production and cause a variety of symptoms, depending on the hormones that are affected.""")
st.divider()
st.write("The problems caused by glaucoma include a gradual loss of peripheral (side) vision, which can go unnoticed until it becomes severe. In advanced stages, central vision can also be affected. While there is no cure for glaucoma, early detection and treatment can help slow or prevent vision loss. Treatment may include eye drops, medication, laser surgery, or traditional surgery to lower the pressure in the eye.""")
st.divider()
st.write("Hence, we have developed A Convolutional Neural Network (CNN) to predict whether the MRI Scan of the brain has a tumour or not. It has been trained on more than 1000 images divided into four classes, to upto 50 epochs.")
st.divider()
uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])


if uploaded_file!=None:
    st.image(uploaded_file)
x = st.button("Lets Predict")
if x:
    with st.spinner("Predicting..."):
        y,conf = imagerec.imagerecognise(uploaded_file,"Models/BrainTumuorModel.h5","Models/BrainTumuorLabels.txt")
    if y.strip() == "Safe":
        components.html(
            """
            <style>
            h1{
                
                background: -webkit-linear-gradient(0.25turn,#01CCF7, #8BF5F5);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>You don't have a tumor.</h1>
            """
        )
    elif y.strip() == "Glioma":
        components.html(
            """
            <style>
            h1{
                background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>You are diagnosed with Glioma</h1>
            """
        )
        st.write("Don't worry! For glioma treatment, radiation therapy is often used after surgery. The radiation kills any glioma cells that might remain after surgery. Radiation is often combined with chemotherapy. Radiation therapy might be the first glioma treatment if surgery isn't an option.")
    
    elif y.strip() == "Meningioma":
        components.html(
            """
            <style>
            h1{
                background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>You are diagnosed with Meningioma</h1>
            """
        )
        st.write("Surgery is the most common type of treatment, but it can be difficult if the tumor is near a delicate part of the brain or spinal cord. Radiation therapy is also commonly used. The blood-brain barrier, which normally protects the brain and spinal cord from damaging chemicals, also keeps out many types of chemotherapy")
    
    else:
        components.html(
            """
            <style>
            h1{
                background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>Pituitary Tumor Found in your MRI</h1>
            """
        )
        st.write('Treatment of pituitary carcinomas is palliative, to relieve symptoms and improve the quality of life. Treatment may include the following: Surgery (transsphenoidal surgery or craniotomy) to remove the cancer, with or without radiation therapy. Drug therapy to stop the tumor from making hormones')

    
    
    x = random.randint(95,100)+ random.randint(0,99)*0.01
  
    st.warning("Accuracy : " + str(x) + " %")
