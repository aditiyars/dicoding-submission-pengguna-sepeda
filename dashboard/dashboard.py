import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data():
    weather_data = pd.read_csv('weather_data.csv')
    day_data = pd.read_csv('day_data.csv')
    return weather_data, day_data

weather_df, day_df = load_data()

st.title('Submission Dicoding')
st.write('Aditiya Ramadhan Saputra')
tab1, tab2, tab3 = st.tabs(["Preview Data", "Pengaruh Cuaca", "Pengaruh Hari Libur"])

with tab1:
    st.subheader("Dataframe Cuaca")
    st.write(weather_df)
    st.subheader("Dataframe Hari Libur")
    st.write(day_df)

with tab2:
    st.subheader("Pengaruh cuaca, suhu, dan kelembapan terhadap jumlah rata-rata pengguna sepeda terdaftar (registered) dan tidak terdaftar (casual)")
    tab21, tab22, tab23 = st.tabs(["Cuaca", "Suhu", "Kelembapan"])
    with tab21:
        # pengaruh weathersit
        st.subheader('Visualisasi Pengaruh cuaca (weathersit)')
        fig, ax = plt.subplots()
        
        ax.bar(weather_df['weathersit_'],weather_df['registered_mean'], color='orange', label='Registered')
        ax.bar(weather_df['weathersit_'],weather_df['casual_mean'], color='blue', label='Casual')

        ax.set_xlabel('Kondisi Weathersit')
        ax.set_ylabel('Total Rata-rata Pengguna Sepeda')
        ax.set_title('Pengaruh Cuaca(weathersit) Terhadap Rata-rata Pengguna Sepeda')
        ax.set_xticks([1,2,3], ['1', '2', '3'])
        ax.legend()
        st.pyplot(fig)
        
        st.markdown("---")
        st.write("1 = Cuaca cerah atau sebagian berawan (Clear, Few clouds, Partly cloudy)")
        st.write("2 = Kabut dengan awan sedang hingga tebal (Mist + Cloudy, Mist + Broken clouds)")
        st.write("3 = Hujan ringan, salju ringan, atau badai petir dengan awan tersebar (Light Snow, Light Rain + Thunderstorm + Scattered clouds).")
    
    with tab22:
        #pengaruh temp
        st.subheader('Visualisasi Pengaruh suhu (temp)')
        fig, ax = plt.subplots()
        
        ax.bar(weather_df['temp_'],weather_df['registered_mean'], color='orange', label='Registered')
        ax.bar(weather_df['temp_'],weather_df['casual_mean'], color='blue', label='Casual')

        ax.set_xlabel('Kondisi suhu (temp)')
        ax.set_ylabel('Total Rata-rata Pengguna Sepeda')
        ax.set_title('Pengaruh suhu (temp) Terhadap Rata-rata Pengguna Sepeda')
        ax.legend()
        st.pyplot(fig)
        
        st.markdown("---")
        st.write("Berdasarkan rentang data yang ada berkisar antara 0 (dingin) - 1 (panas) namun untuk membuat grafik terlihat lebih baik matplotlib secara default menambahkan margin pada sumbu x")
    
    with tab23:
        #pengaruh hum
        st.subheader("Visualisasi pengaruh kelembapan (hum)")
        fig, ax = plt.subplots()
        
        ax.bar(weather_df['hum_'],weather_df['registered_mean'], color='orange', label='Registered')
        ax.bar(weather_df['hum_'],weather_df['casual_mean'], color='blue', label='Casual')

        ax.set_xlabel('Kondisi kelembapan (hum)')
        ax.set_ylabel('Total Rata-rata Pengguna Sepeda')
        ax.set_title('Pengaruh kelembapan (hum) Terhadap Rata-rata Pengguna Sepeda')
        ax.legend()
        st.pyplot(fig)
        
        st.markdown("---")
        st.write("Berdasarkan rentang data yang ada berkisar antara 0 (kering) - 1 (sangat lembap) namun untuk membuat grafik terlihat lebih baik matplotlib secara default menambahkan margin pada sumbu x")
        
        
with tab3 : 
    st.subheader('Visualisasi pengaruh hari kerja dan hari libur')
    fig, ax = plt.subplots()
    ax.bar(day_df['holiday_'], day_df['cnt_mean'])
    ax.set_xlabel('Hari Libur (0 = tidak, 1 = Ya)')
    ax.set_ylabel('Rata-rata pengguna sepeda')
    ax.set_title('Pengaruh Hari Libur terhadap pengguna sepeda')
    ax.grid(axis='y')
    ax.set_xticks([0,1], ['0', '1'])
    st.pyplot(fig)
    