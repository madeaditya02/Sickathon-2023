import streamlit as st
import pandas as pd
import altair as alt

from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1exnxDgW94vPO3WXmKqLs5JL4Nl1ATcPo79xl_ZPSFXs/edit?usp=sharing"
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url)
indo = df[df['provinsi'] == 'INDONESIA'].reset_index()
indo = indo.drop(columns=['index','provinsi'])
indo.columns = ['Tahun', 'Rata-Rata Upah']
df = df[df['provinsi'] != 'INDONESIA']

st.header('Rata-Rata Upah Pekerja per Jam')

# Indonesia
st.subheader('Data Rata-Rata Upah Pekerja di Indonesia')
st.dataframe(indo.reset_index().drop(columns=['index']))

# Provinsi
form = {
    "Provinsi": None,
    "Tahun": None,
}

df.columns = ['Provinsi', 'Tahun', 'Rata-rata Upah']
st.subheader('Keseluruhan Data Setiap Provinsi')
col1, col2 = st.columns(2)
form['Provinsi'] = col1.selectbox('Pilih Provinsi', df["Provinsi"].unique(), key='prov', index=None, placeholder='Pilih Provinsi')
form['Tahun'] = col2.selectbox('Pilih Tahun', df["Tahun"].unique(), key='tahun', index=None, placeholder='Pilih Tahun')

new_df = df
if form['Provinsi']:
    new_df = new_df[new_df["Provinsi"] == form['Provinsi']]
if form['Tahun']:
    new_df = new_df[new_df["Tahun"] == form['Tahun']]

new_df.reset_index(drop=True, inplace=True)

st.dataframe(new_df)

st.subheader("Top 10 Provinsi dengan Rata-rata Upah Pekerja Tertinggi (per Tahun)")
tahun_tertinggi = st.selectbox('Pilih Tahun', df["Tahun"].unique(), key='tahun_tinggi', index=None, placeholder='Pilih Tahun')
if tahun_tertinggi:
    filtered = df[df['Tahun'] == tahun_tertinggi]
    top_10 = filtered.sort_values(by='Rata-rata Upah',ascending=False).head(10)
    top_chart = (
        alt.Chart(top_10).mark_bar().encode(
            x=alt.X('Provinsi', sort='-y'),
            y=alt.Y('Rata-rata Upah')
        )
    )
    st.altair_chart(top_chart, use_container_width=True)

st.subheader("Top 10 Provinsi dengan Rata-rata Upah Terendah (per Tahun)")
tahun_terendah = st.selectbox('Pilih Tahun', df["Tahun"].unique(), key='tahun_rendah', index=None, placeholder='Pilih Tahun')
if tahun_terendah:
    filtered = df[df['Tahun'] == tahun_terendah]
    top_10 = filtered.sort_values(by='Rata-rata Upah',ascending=True).head(10)
    faskes_chart = (
        alt.Chart(top_10).mark_bar().encode(
            x=alt.X('Provinsi', sort='y'),
            y=alt.Y('Rata-rata Upah')
        )
    )
    st.altair_chart(faskes_chart, use_container_width=True)