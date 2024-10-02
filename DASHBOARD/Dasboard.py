import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv("D:\Streamlit\day1.csv")

# Tambahkan judul aplikasi
st.title("Rozaq Leksono")

# Buat fitur pilihan menu
menu = st.selectbox("Pilih Tampilan", ["Tampilan per Tabel", "Tampilan per Musim", "Tampilan per Hari", "Tampilan per Bulan"])

# Tampilkan data berdasarkan pilihan menu
if menu == "Tampilan per Tabel":
    st.write(df)
elif menu == "Tampilan per Musim":
    musim_df = df.groupby("season")["count_cr"].sum().reset_index()
    fig, ax = plt.subplots()
    ax.pie(musim_df["count_cr"], labels=musim_df["season"], autopct='%1.1f%%')
    st.pyplot(fig)
elif menu == "Tampilan per Hari":
    hari_df = df.groupby("a_week")["count_cr"].sum().reset_index()
    fig, ax = plt.subplots()
    ax.pie(hari_df["count_cr"], labels=hari_df["a_week"], autopct='%1.1f%%')
    st.pyplot(fig)
elif menu == "Tampilan per Bulan":
    bulan_df = df.groupby("month")["count_cr"].sum().reset_index()
    fig, ax = plt.subplots()
    ax.pie(bulan_df["count_cr"], labels=bulan_df["month"], autopct='%1.1f%%')
    st.pyplot(fig)
