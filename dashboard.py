import streamlit as st
from PIL import Image

st.title("Dashboard")
col1,col2 = st.columns(2)
gambar = Image.open("E:/Data Science IDCamp/fig.png")
gambar1 = Image.open("E:/Data Science IDCamp/fig1.png")

with col1:
    st.header("Jumlah sewa harian disaat hari kerja dan hari libur")
    st.image(gambar)
    
with col2:
    st.header("Jumlah sewa setiap musim")
    st.image(gambar1)
