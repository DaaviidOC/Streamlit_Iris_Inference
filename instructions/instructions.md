# Iris Inference Calculation with Streamlit

This project demonstrates how to create and run your own app using Streamlit to calculate inferences on your dataset, specifically focusing on an iris dataset.

## Prerequisites
- A Python-compatible working environment.
- Internet connection.

## Script Execution
- Assuming Python and your environment are already installed, you will need to install pycaret:</br>
· !pip install pycaret</br>

- Import the required libraries:</br>
· import streamlit as st</br>
· from pycaret.regression import load_model, predict_model </br>
· import pandas as pd</br>
· from sklearn.datasets import load_iris</br>

- Execute the code blocks step-by-step in the streamlit_iris.ipynb file.</br>

- Open the console and navigate to the directory where your app.py is located. Then, execute it:</br>
![Captura](https://github.com/DaaviidOC/Streamlit_Iris_Inference/blob/main/Files/Captura.PNG)</br>

- If successful, you should see a message like the one in the following image, providing a URL. (If it doesn't open automatically, click on the URL):</br>
![Captura](https://github.com/DaaviidOC/Streamlit_Iris_Inference/blob/main/Files/Captura2.PNG)</br>

- Once inside, you can input your data and perform inferential calculations:</br>
![Captura](https://github.com/DaaviidOC/Streamlit_Iris_Inference/blob/main/Files/Captura4.PNG)</br>

- When you click "Predict," if everything is functioning correctly, the following message should appear in your console:</br>
  ![Captura](https://github.com/DaaviidOC/Streamlit_Iris_Inference/blob/main/Files/Captura3.PNG)</br>
  
## Troubleshooting
- If you encounter any errors during execution, ensure that all libraries are up to date and that you have replaced the names of the model .pkl and the dataset with your own.

