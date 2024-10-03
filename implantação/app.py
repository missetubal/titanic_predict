import streamlit as st
import joblib
import numpy as np

model = joblib.load('gradient_boosting_model.pkl')

st.title("Previsão de Sobrevivência no Titanic")

pclass = st.selectbox('Classe', [1, 2, 3])
sex = st.selectbox('Sexo', ['male', 'female'])
age = st.slider('Idade', 0, 80, 25)
sibsp = st.number_input('Irmãos/Cônjuges a bordo', min_value=0, max_value=10, value=1)
parch = st.number_input('Pais/Filhos a bordo', min_value=0, max_value=10, value=0)
fare = st.slider('Tarifa paga', 0.0, 500.0, 50.0)

user_input = np.array([pclass, sex == 'male', age, sibsp, parch, fare]).reshape(1, -6)

if st.button('Prever'):
    prediction = model.predict(user_input)
    if prediction == 1:
        st.success('Sobreviveu!')
    else:
        st.error('Não sobreviveu.')
