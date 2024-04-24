import joblib
import streamlit as st 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import pickle
from PIL import Image
import plotly.express as px
import os
import json
# Load the trained model
os.chdir(r"C:\Users\islam\OneDrive\Desktop\Work File\Machine Learning\Supervised ML_Classfication\Loan Prediction _Classification")
model = pickle.load(open("model.pkl", "rb"))


def run():
    img1 = Image.open('OIP.jpg')
    img1 = img1.resize((600,200))
    st.image(img1,use_column_width=False)

    st.title("Bank Loan Prediction")

    account_no = st.text_input('Account number')
    fn = st.text_input('Full Name')

    gen_display = ('Female', 'Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender", gen_options, format_func=lambda x: gen_display[x])

    mar_display = ('No', 'Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    dep_display = ('No', 'One', 'Two', 'More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dependents", dep_options, format_func=lambda x: dep_display[x])

    edu_display = ('Not Graduate', 'Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education", edu_options, format_func=lambda x: edu_display[x])

    emp_display = ('Job', 'Business')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status", emp_options, format_func=lambda x: emp_display[x])

    prop_display = ('Rural', 'Semi-Urban', 'Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area", prop_options, format_func=lambda x: prop_display[x])

    cred_display = ('Between 300 to 500', 'Above 500')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit Score", cred_options, format_func=lambda x: cred_display[x])

    mon_income = st.number_input("Applicant's Monthly Income($)", value=0)
    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)", value=0)
    loan_amt = st.number_input("Loan Amount", value=0)

    dur_display = ['2 Month', '6 Month', '8 Month', '1 Year', '16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration", dur_options, format_func=lambda x: dur_display[x])

    if st.button("Submit"):
        duration_mapping = {0: 60, 1: 180, 2: 240, 3: 360, 4: 480}
        duration = duration_mapping.get(dur, 0)

        features = np.array([[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]])

        prediction = model.predict(np.array(features).reshape(-1, len(features)))
        if prediction[0] == 0:
            st.error(f"Hello {fn}, Account number {account_no}: You will not get the loan from the bank.")
        else:
            st.success(f"Hello {fn}, Account number {account_no}: Congratulations! You will get the loan from the bank.")

if __name__ == "__main__":
    run()



