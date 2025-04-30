# Customer Churn Prediction - Streamlit App

This project is a machine learning-based web application that predicts whether a customer is likely to churn (leave) or stay.
The model was trained using a dataset of customer behavior and deployed with **Streamlit** to allow interactive user input.

## 🚀 Features

- Predict customer churn using a trained K-Nearest Neighbors (KNN) model.
- Interactive web interface built with Streamlit.
- Input form for features like credit score, geography, age, etc.
- Real-time prediction with result feedback (churn or not).

## 🗂️ Project Structure

├── app.py 
├── Churn_Modelling.csv # Dataset used for training 
├── churn.ipynb # Jupyter notebook: training + model export 
├── knn_churn2.pkl # Trained KNN model 

## 🧠 Model

- Model: K-Nearest Neighbors (KNN)
- Input features:
  - Credit Score
  - Geography
  - Gender
  - Age
  - Tenure
  - Balance
  - Number of Products
  - Has Credit Card
  - Active Member
  - Estimated Salary
