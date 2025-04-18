import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
st.header('Análisis de vehículos')
hist_button = st.checkbox('Construir histrograma')
dis_button = st.checkbox('Construir diagrama de dispersión')

if hist_button:
    st.write('Generando el histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

if dis_button:
    st.write('Generando el diagrama de dispesion')
    fig_dis = px.scatter(car_data, x='odometer', y="price")
    st.plotly_chart(fig_dis, use_container_width=True)

