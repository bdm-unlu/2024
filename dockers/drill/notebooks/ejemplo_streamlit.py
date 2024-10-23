import streamlit as st
import pandas as pd
import plotly.express as px
from pydrill.client import PyDrill
 
st.write("""
# Ejemplo con Streamlit*
""")
 
df = pd.read_csv('/data/encuesta_universitaria.csv', encoding = 'latin1', quotechar="'")
df_pie = df.groupby(['Medio_Transporte'])['Medio_Transporte'].count().reset_index(name='count')
fig = px.pie(df_pie, values='count', names='Medio_Transporte', title='Pie')

st.plotly_chart(fig)

drill = PyDrill(host='drill', port=8047)
query = "SELECT js.nombre, count(*) as cant FROM mysql.alumnos.alumnos ms JOIN dfs.`/data/paises.json` js ON CAST(js.id as int) = ms.id_nacionalidad JOIN postgres.public.carreras pg ON pg.id = ms.id_carrera GROUP BY js.nombre"
res = drill.query(query)
df_al = res.to_dataframe()

st.dataframe(df_al)

fig = px.pie(df_al, values='cant', names='nombre', title='Pie')

st.plotly_chart(fig)