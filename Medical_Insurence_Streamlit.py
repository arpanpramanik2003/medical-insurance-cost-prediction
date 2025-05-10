import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('insurance_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title and description
st.title("Insurance Charges Prediction")
st.write("""
This application predicts insurance charges based on the provided details of the user.
Fill in the details below to get the estimated charges.
""")

# Input fields for user details
age = st.number_input('Age', min_value=0, max_value=100, step=1, value=25)
sex = st.selectbox('Sex', options=['male', 'female'])
bmi = st.number_input('BMI', min_value=0.0, step=0.1, value=25.0)
children = st.number_input('Number of Children', min_value=0, max_value=10, step=1, value=0)
smoker = st.selectbox('Smoker', options=['yes', 'no'])
region = st.selectbox('Region', options=['southeast', 'southwest', 'northeast', 'northwest'])

# Button for prediction
if st.button('Predict Charges'):
    # Create input dataframe
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })

    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    st.success(f'Estimated Insurance Charges: ₹ {prediction[0]:.2f}')
