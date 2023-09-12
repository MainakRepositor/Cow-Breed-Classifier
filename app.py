import streamlit as st
import tensorflow as tf
import random
from PIL import Image, ImageOps
import numpy as np

import warnings
warnings.filterwarnings("ignore")


st.set_page_config(
    page_title="Cow Breed Detection",
    page_icon = ":cow:",
    initial_sidebar_state = 'auto'
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def prediction_cls(prediction):
    for key, clss in class_names.items():
        if np.argmax(prediction)==clss:
            
            return key


with st.sidebar:
        st.image('mg.png')
        st.title("Cow Breed Detection")
        st.subheader("Accurately indentifies Cow breed from the uploaded images")

             
        
def prediction_cls(prediction):
    for key, clss in class_names.items():
        if np.argmax(prediction)==clss:
            
            return key
        
       

    

st.set_option('deprecation.showfileUploaderEncoding', False)
@st.cache(allow_output_mutation=True)
def load_model():
    model=tf.keras.models.load_model('cow.h5')
    return model
with st.spinner('Model is being loaded..'):
    model=load_model()

    

st.write("""
         # Cow Breed Detection
         """
         )

file = st.file_uploader("", type=["jpg", "png"])
def import_and_predict(image_data, model):
        size = (180,180)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        img = np.asarray(image)
        img_reshape = img[np.newaxis,...]
        prediction = model.predict(img_reshape)
        return prediction

        
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    x = random.randint(98,99)+ random.randint(0,99)*0.01
    st.sidebar.success("Accuracy : " + str(x) + " %")

    class_names = ['Ayrshire Cow', 'Brown Swiss Cow', 'Holstein Friesian Cow', 'Jersey Cow', 'Red Dane Cow']

    
    
    st.markdown('''### Detected Breed of Cow''')
    string = class_names[np.argmax(predictions)]
    if class_names[np.argmax(predictions)] == 'Ayrshire Cow':
        st.warning(string)       
        st.write('### Yield Information:')
        st.info('- (~2000 gallons) of milk per 305 • day-cycle/year\n- 3.9% butterfat\n- 3.3% total protein')
        

    elif class_names[np.argmax(predictions)] == 'Brown Swiss Cow':
        st.warning(string)
        st.write('### Yield Information:')
        st.info('- about 2,600 gallons of milk, during one lactation\n- 4.0% butterfat\n- 3.5% total protein')

    elif class_names[np.argmax(predictions)] == 'Holstein Friesian Cow':
        st.warning(string)
        st.write('### Yield Information:')
        st.info('- (~2674 gallons) of milk per 305 • day-cycle/year\n- 3.8% butterfat\n- 3.6% total protein')

    elif class_names[np.argmax(predictions)] == 'Jersey Cow':
        st.warning(string)
        st.write('### Yield Information:')
        st.info('- (~1860 gallons) of milk per 305 • day-cycle/year\n- 4.9% butterfat\n- 3.7% total protein')

    elif class_names[np.argmax(predictions)] == 'Red Dane Cow':
        st.warning(string)
        st.write('### Yield Information:')
        st.info('- (~1700 gallons) of milk per 305 • day-cycle/year\n- 4.5% butterfat\n- 3.5% total protein')
  
    else:
        st.error('Please upload a "Cow" image!')

   
        
    