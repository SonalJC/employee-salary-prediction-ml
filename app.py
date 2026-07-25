import streamlit as st
import numpy as np
import pandas as pd
import pickle

# load the model file.
with open('model (2).pkl','rb') as file:
    model=pickle.load(file)


# Title and header file.
st.title('💰 Employee Salary Prediction')
st.text('Predict whether an employees annual income is greater than $50K based on demographic and employment information.')
st.header('Enter the Employee Details')


# input columns
col1,col2=st.columns(2)

with col1:
    age=st.slider('Employee Age:',min_value=18,max_value=90,value=25)
    hours_per_week=st.slider('Working Hours per week:',min_value=20,max_value=250,value=30)
    workclass=st.selectbox('Work Class',['Private','Government','Other'])
    education=st.selectbox('Education:',['Graduation','School','PhD'])
    
with col2:

    marital_status=st.selectbox('Marital Status:',['Married','Single','Never-married'])
    occupation=st.selectbox('Occupation',['Prof-specialty','Other','craft-repair','Exec-managerial','Adm-clerical','Sales'])
    capital_gain=st.selectbox('Capital Gain',['Yes','No'])
    relationship=st.selectbox('Relationship',['Not-in-family','Husband','Own-child','Unmarried','Wife','Other-relative'])


feature_names=['age','workclass','education','marital_status','occupation','relationship','capital_gain','hours_per_week']

# Button Logic
if st.button("Salary Prediction"):
    user_inputs=[[age,workclass,education,marital_status,occupation,relationship,capital_gain,hours_per_week,]]
    
    # convert it itno dataframe
    user_df=pd.DataFrame(user_inputs,columns=feature_names)

    # model prediction
    model_predcition=model.predict(user_df)
    model_probability=model.predict_proba(user_df)


#
    # result
    st.subheader('Result')

    if model_predcition[0] == '>50K':
        st.success('High income greater than $50K/year')
        st.write(f"Model Confidence: {model_probability[0][1]*100:.2f}%")
    else:
        st.warning('Income is less than or equal to $50K/year')
        st.write(f"Model Confidence: {model_probability[0][0]*100:.2f}%")

