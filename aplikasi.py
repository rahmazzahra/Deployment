import streamlit as st
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# Path ke model dan scaler yang ada di folder model dan scaler
model_path = "model/model.pkl"
scaler_path = "scaler/scaler.pkl"

# Load model dan scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Streamlit UI
st.title("Prediksi Harga Rumah")
st.write("Masukkan data untuk memprediksi harga rumah.")

# Input fitur dari pengguna, pastikan step=1 agar hanya menerima integer
k_tidur = st.number_input("Jumlah Kamar Tidur", min_value=1, step=1)
k_mandi = st.number_input("Jumlah Kamar Mandi", min_value=1, step=1)
l_bangunan = st.number_input("Luas Bangunan (m2)", min_value=1.0, step=0.1)
l_tanah = st.number_input("Luas Tanah (m2)", min_value=1.0, step=0.1)

# Menambahkan tombol untuk memprediksi harga
if st.button('Prediksi Harga'):
    # Menyusun input menjadi array dan scaling
    input_data = np.array([[k_tidur, k_mandi, l_bangunan, l_tanah]])
    input_data_scaled = scaler.transform(input_data)

    # Prediksi harga rumah
    prediksi_harga = model.predict(input_data_scaled)

    # Menampilkan hasil prediksi
    st.write(f"Prediksi harga rumah: Rp {prediksi_harga[0]:,.2f}")
