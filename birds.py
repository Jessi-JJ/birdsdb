import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('bothcountries_data_format_19feb2019_abundance_format.csv', encoding='latin-1')

# KPIs
st.title("Canopy tree preference by insectivorous birds on shade-coffee farms")
st.metric("Total Birds Observed", f"{df['num_birds'].sum():,.2f}")
st.metric("Total Orders", len(df))

df_treesp = df["treesp"].value_counts().to_frame()
df_treesp.reset_index(inplace=True)
df_treesp.columns = ["treesp", "count"]

col1, col2 = st.columns((2))

with col1: # Chart
  st.subheader("Tree Species")
  fig = px.bar(df_treesp, x = "treesp", y = "count", text = [f"{x}" for x in df["treesp"]],
                 template = "seaborn")
  st.plotly_chart(fig,use_container_width=True, height = 200)

st.sidebar.header("Choose your filter: ")
# Create for Country
country = st.sidebar.multiselect("Pick a Country", df["country"].unique())
if not country:
    df2 = df.copy()
else:
    df2 = df[df["country"].isin(country)]

# Data Table
st.subheader("Birds Data")
st.dataframe(df)
