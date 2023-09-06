import streamlit as st
import requests
from PIL import Image

image_path = 'src\streamlit_app\images\image.jpg'
image = Image.open(image_path)





# Set API Endpoint
URL = 'https://radiant-lowlands-86946.herokuapp.com/predict'


# Create a function to make prediction
def make_prediction(pg: float, bwr1: float, bp : float, bwr2: float, bwr3: float, bmi: float, bwr4: float, age: int, insurance: bool):

    parameters={
        'plasma_glucose':pg,
        'blood_work_result_1':bwr1,
        'blood_pressure':bp,
        'blood_work_result_2':bwr2,
        'blood_work_result_3':bwr3,
        'body_mass_index':bmi,
        'blood_work_result_4':bwr4,
        'age':int(age),
        'insurance':bool(insurance)}
    response = requests.post(URL, params=parameters)
    response_text =  response.json()
    sepsis_status = response_text['results'][0]['0']['output']['Predicted Label']
    return sepsis_status


# set page configuration
st.set_page_config(
    page_title='Sepsis Prediction',
    page_icon="🤖",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This is a Health App. Call it the Covid Vaccine Sepsis Analyzer!"
    }
)  


# create a sidebar and contents
st.sidebar.markdown("""
## Demo App

This app return sepsis status base on the input parameters
""")

st.markdown('''
    <h1 style="color: green; text-align:center">The Sepsis Prediction App</h1>
    ''', unsafe_allow_html=True)

# insert an image
st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


# Create app interface
container = st.container()
container.write("Inputs to predict Sepsis")
with container:
    col1, col2, col3 = st.columns(3)
    
    age = col1.number_input(label='Age')
    pg = col2.number_input(label='Blood Glucose')
    bp = col3.number_input(label='Blood Pressure')
    with st.expander(label='Blood Parameter', expanded=True, ):
        bwr1 = col1.number_input(label='Blood Work Result-1')
        bwr2 = col2.number_input(label='Blood Work Result-2')
        bwr3 = col1.number_input(label='Blood Work Result-3')
        bwr4 = col2.number_input(label='Blood Work Result-4')
    ins = col3.selectbox(label='Insurance', options=[True, False])
    bmi = col3.number_input(label='Body Mass Index')
    button = st.button(label='Predict', type='primary', use_container_width=True)
    

if button:
    response = make_prediction(pg, bwr1, bp, bwr2, bwr3, bmi, bwr4, age, ins)
    st.write(response)














