"""
Nama        : Joshua Briantama Hanjaya
Email       : m244d4ky2998@bangkit.academy
ID Dicoding : joshua_briantama_h
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import seaborn as sns
from babel.numbers import format_currency
from matplotlib.ticker import FuncFormatter
sns.set(style='dark')

df_hour = pd.read_csv(r"./hour_data.csv")

df_hour['dteday'] = pd.to_datetime(df_hour["dteday"])
min_date = df_hour["dteday"].min()
max_date = df_hour["dteday"].max()



st.title("Bike Sharing dashboard :moyai:")

with st.sidebar:
    st.sidebar.title("Dataset Bike Share")

    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

    main_df = df_hour[(df_hour["dteday"] >= str(start_date)) & 
                (df_hour["dteday"] <= str(end_date))]

col1, col2 = st.columns(2)

with col1:
    total_rent = main_df['cnt'].sum()
    st.metric("Total rent", value=total_rent)

with col2:
    registered_user_rent = main_df['registered'].sum()
    st.metric("Registered user rent", value=registered_user_rent)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    main_df["dteday"],
    main_df["cnt"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)

st.subheader("waktu paling ramai menyewa sepeda")
 
fig, ax = plt.subplots(figsize=(35, 15))
 
sns.barplot(x="hr", y="cnt", data=main_df, color="orange", ax=ax)
ax.set_ylabel(None)
ax.set_xlabel("Number of Rent", fontsize=30)
ax.tick_params(axis='y', labelsize=35)
ax.tick_params(axis='x', labelsize=30)

st.pyplot(fig)

st.subheader("most temperatures for bicycle renters all time")
 
fig, ax = plt.subplots(figsize=(35, 15))

ax.hist(df_hour['temp']*41, bins=20, weights=df_hour['cnt'], color='orange', edgecolor='black')
ax.set_ylabel(None)
ax.set_xlabel("temperature", fontsize=30)
ax.tick_params(axis='y', labelsize=35)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)

st.subheader("perbandingan penyewaan pada working day dan tidak")

# Menghitung jumlah cnt untuk workingday = 0 dan workingday = 1
cnt_holiday_0 = main_df[main_df['workingday'] == 0]['cnt'].sum()
cnt_holiday_1 = main_df[main_df['workingday'] == 1]['cnt'].sum()

# Membuat data untuk pie chart
labels = ['workingday = 0', 'workingday = 1']
sizes = [cnt_holiday_0, cnt_holiday_1]
colors = ['lightblue', 'lightgreen']

# Membuat pie chart
fig, ax = plt.subplots(figsize=(35, 15))
wedges, _, _ = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 40})
ax.axis('equal')  # Menyamakan skala sumbu x dan y untuk membuat lingkaran

# Menambahkan legenda
ax.legend(wedges, labels, title='Working Day', loc='center right', fontsize=35)

# Menampilkan plot di Streamlit
st.pyplot(fig)

st.subheader("perbandingan penyewaan pada tahun 2011 dan 2012")
# Menghitung jumlah cnt untuk year 0 dan year 1
count_year_0 = df_hour[df_hour['yr'] == 0]['cnt'].sum()
count_year_1 = df_hour[df_hour['yr'] == 1]['cnt'].sum()

years = ['Year 2011', 'Year 2012']
counts = [count_year_0, count_year_1]

# Membuat plot
fig, ax = plt.subplots(figsize=(35, 15))

# Plot bar untuk year 0 dan year 1
ax.bar(years, counts, color=['lightblue', 'lightgreen'])

# Menambahkan judul dan label sumbu

ax.set_xlabel('Tahun', fontsize=35)
ax.set_ylabel('Jumlah Orang yang Bersepeda', fontsize=35)

# Mengatur ukuran font untuk label sumbu dan angka di sumbu
ax.tick_params(axis='x', labelsize=30)
ax.tick_params(axis='y', labelsize=30)
# Mengubah formatter sumbu y
def format_y(y, _):
    return f'{y:,.0f}'  # Mengubah format menjadi tanpa desimal dan dengan pemisah ribuan

ax.yaxis.set_major_formatter(FuncFormatter(format_y))

# Menampilkan plot di Streamlit
st.pyplot(fig)





st.subheader("perbandingan penyewaan pada pada cuaca")
st.markdown("""
    - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
    - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
    - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered
    - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
""")
# Menghitung jumlah cnt untuk year 0 dan year 1
count_weather_1 = df_hour[df_hour['weathersit'] == 1]['cnt'].sum()
count_weather_2 = df_hour[df_hour['weathersit'] == 2]['cnt'].sum()
count_weather_3 = df_hour[df_hour['weathersit'] == 2]['cnt'].sum()
count_weather_4 = df_hour[df_hour['weathersit'] == 2]['cnt'].sum()


weather = ['1', '2', '3', '4']
counts = [count_weather_1, count_weather_2, count_weather_3, count_weather_4]

# Membuat plot
fig, ax = plt.subplots(figsize=(35, 15))

# Plot bar untuk year 0 dan year 1
ax.bar(weather, counts, color=['yellow', 'lightblue', 'lightgrey', 'grey'])

# Menambahkan judul dan label sumbu

ax.set_xlabel('weather', fontsize=35)
ax.set_ylabel('Jumlah Orang yang Bersepeda', fontsize=35)

# Mengatur ukuran font untuk label sumbu dan angka di sumbu
ax.tick_params(axis='x', labelsize=30)
ax.tick_params(axis='y', labelsize=30)
# Mengubah formatter sumbu y
def format_y(y, _):
    return f'{y:,.0f}'  # Mengubah format menjadi tanpa desimal dan dengan pemisah ribuan

ax.yaxis.set_major_formatter(FuncFormatter(format_y))

# Menampilkan plot di Streamlit
st.pyplot(fig)
