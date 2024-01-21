# Iris Inference Calculation Streamlit

Este proyecto muestra cómo crear tu propia app y ejecutarla con Streamlit para calcular la inferencia sobre tu dataset, en este caso, tratamos con un dataset de iris.

## Prerequisites
- An environment for working with Python.
- Internet connection.
- OpenAI account with access to the GPT and DALL-E 3 APIs.

## Script Execution
- Assuming Python and your environment are already installed, you will need to install openai:</br>
· !pip install openai==0.28</br>
· !pip install --upgrade openai</br>

- Import libraries:</br>
· import streamlit as st
· from pycaret.regression import load_model, predict_model 
· import pandas as pd 

- Assign your API key to a variable:</br>
· openai.api_key = "********" </br>
· Make sure to replace the asterisks with your API key.

- In case of an error with the Windows CLI, reset the kernel and re-execute the command:</br>
· !pip install openai==0.28

- In the script for making GPT queries, you can use "content": input(" "), to write queries in the input rather than in the code.

## Troubleshooting
- If you encounter any errors during execution, make sure all libraries are up to date and that your OpenAI API key is correctly set up in the API_openai.ipynb file.

