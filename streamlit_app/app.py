import streamlit as st
import requests
import re

def preprocessing_complition(chem_reaction: str) -> str:
    return re.findall('[A-Za-z0-9]+', chem_reaction)

st.title("Chem Reaction Helper")
col1, col2 = st.columns([1, 1])

with col1:
    complition_task = st.checkbox("Закончить реакцию")
with col2:
    coefficients_task = st.checkbox("Расставить коэффициенты")

left, middle, right = st.columns([20, 2, 20], vertical_alignment="bottom")
middle.write('**⮕**')
reagents = left.text_input('Реагенты')
products = right.text_input('Продукты')
coefficient = None

reaction = {
        'reagents': preprocessing_complition(reagents), 
        'products': preprocessing_complition(products),
        'coefficient': coefficient,
        }

api_url = 'http://backend:8000/predict'

if complition_task:
    products_result = requests.post(api_url, json={
        'task': 'complition', 
        'reagents': reagents
        })
    reaction.update({'products' : products_result})

if coefficients_task:
    coefficient_result = requests.post(api_url, json={
        'task': 'coefficient', 
        'reagents': reagents, 
        'products': products
        })
    reaction.update({'coefficient' : coefficient_result})

if reagents:
    st.write('Ответ')
    reagents_str = ' + '.join(
        [
            reaction['coefficient'][reag] + reag \
            if coefficient and coefficients_task else reag \
            for reag in reaction['reagents']
            ]
        )
    products_str = ' + '.join(
        [
            reaction['coefficient'][prod] + prod \
            if coefficient and coefficients_task else prod \
            for prod in reaction['products']
            ]
        )
    st.write(f'{reagents_str} = {products_str}'.replace('1', ''))