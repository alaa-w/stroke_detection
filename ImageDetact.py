import streamlit as st 
import io
import numpy as np 
from PIL import Image
from keras.models import load_model
# from tensorflow.keras.preprocessing import image

st.title('Stroke Detaction')


model=load_model('graduation project.h5')

img=st.file_uploader('Upload an Image',type=['jpg','jpeg'])


if img is not None:
    image=Image.open(img)
    st.image(image,'Uploaded Image',use_column_width=True)
    image=image.resize((224,224))
    image=image.convert('RGB')
    image=np.array(image)
    image=image/255
    image=image.reshape((1,image.shape[0],image.shape[1],image.shape[2]))
    pred=model.predict(image)
    pred_label=[1 if pred>=.50 else 0 for i in pred][0]
    classes = ['Normal', 'Stroke']
    class_map = {index: class_name for index, class_name in enumerate(classes)}
    st.write(f'Image Predication is : {class_map[pred_label]}')
