import streamlit as st
import pandas as pd
st.write("HALO MAS FEB")
df = pd.DataFrame(
    {'SKU': ['G2G-803', 'G2G-234', '-232', 'G2G-07', 'G2G-3103'],
     'QTY': [288, 96, 96, None, 288]})

print(df)
st.write(df)
st.header("Widget dasar")

nama = st.text_input("Nama")
region = st.selectbox("Region", ["Sulawesi 1", "Sulawesi 2"])
place = st.selectbox("Tempat", ["Makassar", "Parepare", "Palopo"])
produk = st.multiselect("Produk", ["Serum", "Sunscreen", "Cleanser"])
target = st.slider("Target pencapaian (%)", 0, 150, 100)
detail = st.checkbox("Tampilkan detail")
if st.button("Hitung"):
    st.success(f"{nama} - {region} - {place} - target {target}%")
if detail:
    st.write("Produk dipilih:", produk)

st.spinner("Loading data...")
st.balloons()
st.radio("Pilih warna tema", ["Merah", "Biru", "Hijau"])
st.warning("Perhatian! Data yang ditampilkan belum diverifikasi.")
st.color_picker("Pilih warna tema", "#00f900")