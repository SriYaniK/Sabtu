import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Visualisasi data Diamond")
st.write("by Yani")

df.pd.read_csv('data/diamonds.csv', sep=',')

st.write(df.head())

st.write("Histogram harga diamonds")
plot = px.histogram(
    df,
    x = 'price',
    title = 'histogram harga diamonds'
)

plot.update_layout(
    xaxis_title = 'Harga'
    yaxis_title = 'Jumlah'
)

st.plotly_chart(plot)

st.write("histogram color")
plot_color = px.histogram(
    df,
    x = 'color',
    title = 'histogram warna diamonds'
)

plot_color.update_layout(
    df,
    xaxis_title = 'warna',
    yaxis_titel = jumlah'

st.plotly_chart(plot_color)

st.write('Lone chart dimensi x, y, dan z')
plot_dimensi = px.line


    
    
    


ig.show()