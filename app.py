import streamlit as st
import pandas as pd
import plotly.express as px

#ler dados
car_data = pd.read_csv('vehicles_us.csv') 

#titulo do app
st.header("Analise de dados de veiculos")

#caixa de selecao para histograma
build_histogram = st.checkbox('Mostrar histograma (odômetro)')

#caixa de selecao para grafico de dispersao
build_scatter =  st.checkbox('Mostrar grafico de dispersao (odômetro x Preco)')

#se o histograma for marcado
if build_histogram:
    st.write("Criando histograma para a coluna odômetro")
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

#se o grafico de dispersao for marcado
if build_scatter:
    st.write("Criando grafico de dispersao, odômetro x preco")
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)
    

