import streamlit as st 
from lib.utils import  *
from PIL import Image
img = Image.open("icon.png")
st.set_page_config(page_title='Stable-Cats-Generator',page_icon = img , layout="wide")

st.sidebar.image("icon.png")
st.info("""This is a simple Streamlit web application for generating white cat images using the 
        "Stable-Cats-Generator" model. The model is based on Stable Diffusion v2 and
        has been fine-tuned for generating white cat images from text prompts.""")
prompt = st.text_input("Enter your prompt :  ")
st.text("Press Enter to apply")
save_name = st.sidebar.text_input("Enter your image save name :")
st.sidebar.text("Press Enter to apply")
use_manual_seed = st.sidebar.selectbox("Do you want to use manual seed :" ,
                                [False , True])
if use_manual_seed == True : 
    seed_num = st.text_input("Pass Your random seed number :")
num_inference_steps = st.slider("Change your number of inference steps :" , min_value=1 , 
                                                                            max_value=50 , 
                                                                            step=1 , 
                                                                            value=3)
width = st.slider("You can Change the width :" , min_value=400 , max_value=512 , 
                                                                            step=1 , 
                                                                            value=512)
height = st.slider("You can Change the height :" , min_value=400 , max_value=512 , 
                                                                            step=1 , 
                                                                            value=512)

if st.button("start generate") : 
    with st.spinner("this process may take some time ..") : 
        run(save_name=save_name , 
            seed_num=seed_num , 
            manual_seed=use_manual_seed , 
            num_inference_steps= num_inference_steps,
            width=width , height=height)
        st.image(f"results/{save_name}.png")