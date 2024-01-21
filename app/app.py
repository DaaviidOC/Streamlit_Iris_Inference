import streamlit as st
from pycaret.regression import load_model, predict_model 
import pandas as pd 

modelo = load_model("model")
st.title("Mi primera inferencia ;()")

sepal_length = st.number_input("sepal length (cm)")
sepal_width = st.number_input("sepal width (cm)")
petal_length = st.number_input("petal length (cm)")
petal_width = st.number_input("petal width (cm)")


if st.button("predecir"):
    input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns=["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"])
    prediction = predict_model(modelo, data = input_data)
    st.write(prediction)