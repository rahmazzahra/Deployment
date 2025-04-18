import streamlit as st
import numpy as np
import joblib

# Fungsi format harga


def format_price(price):
    if price >= 1_000_000_000:
        return f"{price / 1_000_000_000:.2f} miliar rupiah"
    else:
        return f"{price / 1_000_000:.2f} juta rupiah"


def main():
    st.title("💰 Prediksi Harga Rumah Wilayah Cimanggis🏠")

    st.markdown(
        "Masukkan detail rumah pada **sidebar** di kiri layar, lalu klik tombol prediksi.")

    # Sidebar untuk input pengguna
    with st.sidebar:
        st.header("Masukkan Detail Rumah")
        k_tidur = st.number_input("Jumlah Kamar Tidur", min_value=1, step=1)
        k_mandi = st.number_input("Jumlah Kamar Mandi", min_value=1, step=1)
        l_bangunan = st.number_input(
            "Luas Bangunan (m²)", min_value=1.0, step=1.0)
        l_tanah = st.number_input("Luas Tanah (m²)", min_value=1.0, step=1.0)
        prediksi = st.button("🎯 Prediksi Harga")

    if prediksi:
        # Load model dan scaler
        model = joblib.load("model/model.pkl")
        scaler = joblib.load("scaler/scaler.pkl")

        input_data = np.array([[k_tidur, k_mandi, l_bangunan, l_tanah]])
        input_scaled = scaler.transform(input_data)
        predicted_price = model.predict(input_scaled)[0]

        # Format hasil prediksi
        formatted_price = format_price(predicted_price)
        st.success(f"Hasil prediksi harga rumah: **{formatted_price}**")

        # Menampilkan ulang input user
        st.markdown("### Detail Input")
        st.write(f"- Jumlah kamar tidur: {k_tidur}")
        st.write(f"- Jumlah kamar mandi: {k_mandi}")
        st.write(f"- Luas bangunan: {l_bangunan} m²")
        st.write(f"- Luas tanah: {l_tanah} m²")


if __name__ == '__main__':
    main()
