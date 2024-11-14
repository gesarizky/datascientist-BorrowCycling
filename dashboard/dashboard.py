import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Load Clean data
main_df = pd.read_csv("main_data.csv")

# Title
st.title("Dashboard Penyewaan Sepeda")

# Sidebar
st.sidebar.header("Filter")
selected_year = st.sidebar.selectbox("Pilih Tahun", options=main_df['yr'].unique())
selected_season = st.sidebar.multiselect("Pilih Musim", options=main_df['season'].unique(), default=main_df['season'].unique())

# Filter data
filtered_data = main_df[(main_df['yr'] == selected_year) & (main_df['season'].isin(selected_season))]

# Display data
st.write(f"Menampilkan data untuk tahun {selected_year} dan musim {', '.join(selected_season)}")
st.dataframe(filtered_data.head())

# Visualisasi rata-rata penyewaan sepeda per musim
season_rentals = filtered_data.groupby('season')['cnt'].sum()

st.subheader("Rata-rata Penyewaan Sepeda per Musim")
fig, ax = plt.subplots()
season_rentals.plot(kind='bar', color=['springgreen', 'gold', 'orange', 'lightskyblue'], ax=ax)
ax.set_title('Rata-rata Penyewaan Sepeda per Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-rata Penyewaan')
st.pyplot(fig)

# Visualisasi penyewaan sepeda pada hari kerja vs hari libur
workingday_rentals = filtered_data.groupby('workingday')['cnt'].sum()

st.subheader("Rata-rata Penyewaan Sepeda pada Hari Kerja vs Hari Libur")
fig, ax = plt.subplots()
workingday_rentals.plot(kind='bar', color=['lightcoral', 'lightseagreen'], ax=ax)
ax.set_title('Rata-rata Penyewaan Sepeda pada Hari Kerja vs Hari Libur')
ax.set_xlabel('Working Day')
ax.set_ylabel('Rata-rata Penyewaan')
ax.set_xticklabels(['Libur', 'Hari Kerja'], rotation=0)
ax.ticklabel_format(style='plain',axis='y')
st.pyplot(fig)