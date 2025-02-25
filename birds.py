import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('bothcountries_data_format_19feb2019_abundance_format.csv', encoding='latin-1')

# KPIs
st.title("Canopy tree preference by insectivorous birds on shade-coffee farms")
st.metric("Total Birds Observed", f"{df['num_birds'].sum()}")
st.metric("Total Observations", len(df))

df_treesp = df["treesp"].value_counts().to_frame()
df_treesp.reset_index(inplace=True)
df_treesp.columns = ["treesp", "count"]

df_birdsp = df["bird_sp"].value_counts().to_frame()
df_birdsp.reset_index(inplace=True)
df_birdsp.columns = ["bird_sp", "count"]

col1, col2 = st.columns((2))

with col1: # Chart
  st.subheader("Tree Species")
  fig = px.bar(df_treesp, x = "treesp", y = "count", text = [f"{x}" for x in df_treesp["treesp"]],
                 template = "seaborn")
  st.plotly_chart(fig,use_container_width=True, height = 200)

with col2: #Chart
  st.subheader("Bird Species")
  fig = px.bar(df_birdsp, x = "bird_sp", y = "count", text = [f"{x}" for x in df_birdsp["bird_sp"]],
                 template = "seaborn")
  st.plotly_chart(fig,use_container_width=True, height = 200)

# Create a multiselect for Country in the sidebar
country = st.sidebar.multiselect("Select Country", df["Country"].unique())

# Filter the DataFrame based on the Country selection
if country:
    filtered_df = df[df["Country"].isin(country)]
else:
    filtered_df = df.copy()

# Display the filtered DataFrame
st.write("Filtered DataFrame", filtered_df)
