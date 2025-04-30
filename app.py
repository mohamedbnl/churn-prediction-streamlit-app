import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load('knn_churn2.pkl')

# Title
st.title('Churn Prediction App')

# Input fields
st.header('Enter customer features:')

feature1 = st.number_input('Credit Score', step=10)
feature2 = st.selectbox('Geography', ['France', 'Spain', 'Germany'])
feature3 = st.radio('Gender', ['Male', 'Female'])
feature4 = st.number_input('Age', min_value=18, max_value=100, step=1, value=18)
feature5 = st.number_input('Tenure', max_value=10, min_value=0, step=1, value=0)
feature6 = st.number_input('Balance', step=100)     
feature7 = st.number_input('Num of Products', max_value=4, min_value=0, step=1, value=1)
feature8 = st.radio('Has Card', ['Yes', 'No'])
feature9 = st.radio('Is Active Member', ['Yes', 'No'])

feature10 = st.number_input('Estimated Salary', step=1000.00)

# Convert categorical features to numerical
if feature2 == 'France':
    feature2 = 0
elif feature2 == 'Spain':
    feature2 = 1
else:
    feature2 = 2

feature3 = 0 if feature3 == 'Female' else 1

feature8 = 1 if feature8 == 'Yes' else 0
feature9 = 1 if feature9 == 'Yes' else 0


# Prediction button
if st.button('Predict'):
    features = np.array([[feature1, feature2, feature3, feature4, feature5,
                          feature6, feature7, feature8, feature9, feature10]])
    prediction = model.predict(features)
    if prediction[0]:
        st.success(f"The client will not churn")
    else:
        st.error(f"The client will churn")