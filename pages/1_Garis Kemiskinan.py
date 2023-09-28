import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/12kts_lLhFaxRyRXGNm6cYR8XmU8m-Z5VcioMUtLWQbU/edit?usp=sharing"
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url)

indo = df[df['provinsi'] == 'INDONESIA'].reset_index()
indo = indo.drop(columns=['index','provinsi'])
indo.columns = ['Jenis', 'Daerah', 'Tahun', 'Periode', 'Garis Kemiskinan']

df = df[df['provinsi'] != 'INDONESIA']

st.header('Garis Kemiskinan')

# Indonesia
form1 = {
    "Jenis": None,
    "Daerah": None,
    "Tahun": None,
    "Periode": None,
}
st.subheader('Data Garis Kemiskinan di Indonesia')
col1, col2 = st.columns(2)
form1['Jenis'] = col2.selectbox('Pilih Kategori', indo["Jenis"].unique(), key='category_indo', index=None, placeholder='Pilih Kategori')
form1['Daerah'] = col1.selectbox('Pilih Daerah', indo["Daerah"].unique(), key='daerah_indo', index=None, placeholder='Pilih Daerah')
form1['Tahun'] = col1.selectbox('Pilih Tahun', indo["Tahun"].unique(), key='tahun_indo', index=None, placeholder='Pilih Tahun')
form1['Periode'] = col2.selectbox('Pilih Periode', indo["Periode"].unique(), key='Periode_indo', index=None, placeholder='Pilih Periode')
if form1['Daerah']:
    indo = indo[indo["Daerah"] == form1['Daerah']]
if form1['Jenis']:
    indo = indo[indo["Jenis"] == form1['Jenis']]
if form1['Tahun']:
    indo = indo[indo["Tahun"] == form1['Tahun']]
if form1['Periode']:
    indo = indo[indo["Periode"] == form1['Periode']]
st.dataframe(indo.reset_index().drop(columns=['index']))


# Provinsi
form = {
    "Provinsi": None,
    "Jenis": None,
    "Daerah": None,
    "Tahun": None,
    "Periode": None,
}
new_df = df
new_df.columns = ['Provinsi','Jenis', 'Daerah', 'Tahun', 'Periode', 'Garis Kemiskinan']

st.subheader('Keseluruhan Data Setiap Provinsi')
col1, col2 = st.columns(2)
form['Provinsi'] = col1.selectbox('Pilih Provinsi', new_df["Provinsi"].unique(), key='prov', index=None, placeholder='Pilih Provinsi')
form['Jenis'] = col2.selectbox('Pilih Kategori', new_df["Jenis"].unique(), key='category', index=None, placeholder='Pilih Kategori')
form['Daerah'] = col1.selectbox('Pilih Daerah', new_df["Daerah"].unique(), key='daerah', index=None, placeholder='Pilih Daerah')
col2_1, col2_2 = col2.columns(2)
form['Tahun'] = col2_1.selectbox('Pilih Tahun', new_df["Tahun"].unique(), key='tahun', index=None, placeholder='Pilih Tahun')
form['Periode'] = col2_2.selectbox('Pilih Periode', new_df["Periode"].unique(), key='Periode', index=None, placeholder='Pilih Periode')

# st.write(new_df[new_df["Provinsi"] == ''])
# if not all(value is None for value in form.values()):
#     new_df = new_df[(new_df["Provinsi"] == form['Provinsi']) & (new_df["Daerah"] == form['Daerah'])]
if form['Provinsi']:
    new_df = new_df[new_df["Provinsi"] == form['Provinsi']]
if form['Daerah']:
    new_df = new_df[new_df["Daerah"] == form['Daerah']]
if form['Jenis']:
    new_df = new_df[new_df["Jenis"] == form['Jenis']]
if form['Tahun']:
    new_df = new_df[new_df["Tahun"] == form['Tahun']]
if form['Periode']:
    new_df = new_df[new_df["Periode"] == form['Periode']]

new_df.reset_index(drop=True, inplace=True)

st.dataframe(new_df)