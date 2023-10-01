import streamlit as st
import pandas as pd

from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1DmkjLqP4D9p1JwB3msg3JUFJ2_GI6LH09ip8dEJ1Uh4/edit?usp=sharing"
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url)

indo = df[df['provinsi'] == 'INDONESIA'].reset_index()
indo = indo.drop(columns=['index','provinsi'])
indo.columns = ['Daerah', 'Jenis', 'Tahun', 'Rata-Rata Pengeluaran']

df = df[df['provinsi'] != 'INDONESIA']

st.header('Rata-Rata Pengeluaran per Kapita')

# Indonesia
form1 = {
    "Jenis": None,
    "Daerah": None,
    "Tahun": None,
    "Periode": None,
}
st.subheader('Rata-Rata Pengeluaran per Kapita di Indonesia')
col1, col2 = st.columns(2)
form1['Jenis'] = col2.selectbox('Pilih Kategori', indo["Jenis"].unique(), key='category_indo', index=None, placeholder='Pilih Kategori')
form1['Daerah'] = col1.selectbox('Pilih Daerah', indo["Daerah"].unique(), key='daerah_indo', index=None, placeholder='Pilih Daerah')
form1['Tahun'] = col1.selectbox('Pilih Tahun', indo["Tahun"].unique(), key='tahun_indo', index=None, placeholder='Pilih Tahun')
if form1['Daerah']:
    indo = indo[indo["Daerah"] == form1['Daerah']]
if form1['Jenis']:
    indo = indo[indo["Jenis"] == form1['Jenis']]
if form1['Tahun']:
    indo = indo[indo["Tahun"] == form1['Tahun']]
if form1['Periode']:
    indo = indo[indo["Periode"] == form1['Periode']]
st.dataframe(indo.reset_index().drop(columns=['index']))

form = {
    "Provinsi": None,
    "Jenis": None,
    "Daerah": None,
    "Tahun": None,
}
df.columns = ['Provinsi','Daerah', 'Jenis', 'Tahun', 'Pengeluaran']

st.subheader('Keseluruhan Data Setiap Provinsi')
col1, col2 = st.columns(2)
form['Provinsi'] = col1.selectbox('Pilih Provinsi', df["Provinsi"].unique(), key='prov', index=None, placeholder='Pilih Provinsi')
form['Jenis'] = col2.selectbox('Pilih Kategori', df["Jenis"].unique(), key='category', index=None, placeholder='Pilih Kategori')
form['Daerah'] = col1.selectbox('Pilih Daerah', df["Daerah"].unique(), key='daerah', index=None, placeholder='Pilih Daerah')
form['Tahun'] = col2.selectbox('Pilih Tahun', df["Tahun"].unique(), key='tahun', index=None, placeholder='Pilih Tahun')

if form['Provinsi']:
    df = df[df["Provinsi"] == form['Provinsi']]
if form['Daerah']:
    df = df[df["Daerah"] == form['Daerah']]
if form['Jenis']:
    df = df[df["Jenis"] == form['Jenis']]
if form['Tahun']:
    df = df[df["Tahun"] == form['Tahun']]

df.reset_index(drop=True, inplace=True)


st.dataframe(df)