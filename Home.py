import streamlit as st
import pandas as pd
import altair as alt
import webbrowser
# from streamlit_gsheets import GSheetsConnection

# url = "https://docs.google.com/spreadsheets/d/1NY2_jqkJkP0F6sOYSaiPFAeCM7Ghqo15o5lnlW6Ay4M/edit?usp=sharing"

# conn = st.experimental_connection("gsheets", type=GSheetsConnection)

# data = conn.read(spreadsheet=url)
# st.dataframe(data)

st.title('Data Kesejahteraan Pekerja Indonesia')
st.write('Website ini menampilkan data yang berkaitan dengan kesejahteraan pekerja di Indonesia. Data-data yang dihadirkan terdapat 4 data, yaitu :')
st.markdown('''
    - **Garis Kemiskinan** dengan disagresi Provinsi, Tahun, Periode Survei, Jenis Pengeluaran, dan Daerah Tempat Tinggal
    - **Rata-Rata Pengeluaran Per Kapita** dengan disagresi Provinsi, Tahun, Periode Survei, Jenis Pengeluaran, dan Daerah Tempat Tinggal
    - **Upah Minimum Provinsi (UMP)** dengan disagresi Provinsi dan Tahun
    - **Rata-Rata Upah Pekerja Per Jam** dengan disagresi Provinsi dan Tahun \n
    Untuk melihat setiap data, anda bisa mengarah ke setiap halaman pada sidebar \n \n
    Data ini didapat via [kaggle.com](https://www.kaggle.com/datasets/rezkyyayang/pekerja-sejahtera) oleh [Rezky Yayang Yakhamid](https://www.kaggle.com/rezkyyayang)
''')