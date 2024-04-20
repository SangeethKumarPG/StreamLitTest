import streamlit as st
import pickle

st.header("Predict weight from height")

st.write('Demo of linear regression')

with st.form("height_input_fom", clear_on_submit=True):
    height = st.number_input(label="Enter Height in inches",
    min_value=35.0,
    max_value=130.0,
    step=1.0)
    submitted = st.form_submit_button("Submit")


print(height)

if submitted:
    pickle_model = pickle.load(open("model.pkl",'rb'))
    weight = pickle_model.predict([[height]])
    st.write(f"The predicted weight is : {weight[0]:.2f} pounds")