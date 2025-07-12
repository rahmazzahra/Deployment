import streamlit as st
import numpy as np
import joblib

# Fungsi format harga


def format_price(price):
    if price >= 1_000_000_000:
        return f"{price / 1_000_000_000:.2f} miliar rupiah"
    else:
        return f"{price / 1_000_000:.2f} juta rupiah"


# Set page config
st.set_page_config(
    page_title="Prediksi Harga Rumah Cimanggis", page_icon="🏠")


def main():
    # Custom CSS styling dengan penyesuaian margin/padding
    st.markdown(
        """
        <style>
            :root {
                --primary-color: #2E7D32;
                --secondary-color: #81C784;
                --accent-color: #4CAF50;
                --background-color: #F5F5F5;
                --text-color: #333333;
            }

            .title {
                background: linear-gradient(120deg, var(--primary-color), var(--secondary-color));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-size: 42px;
                font-weight: 800;
                text-align: center;
                margin-bottom: 10px;
                padding: 20px 0;
            }

            .caption {
                font-size: 18px;
                text-align: center;
                color: var(--text-color);
                opacity: 0.8;
                margin-bottom: 30px;
            }

            .sidebar-header {
                font-size: 22px;
                color: var(--primary-color);
                font-weight: bold;
                text-align: center;
                padding: 15px 0;
                border-bottom: 2px solid var(--secondary-color);
                margin-bottom: 20px;
            }

            .sidebar-input {
                margin-bottom: 20px;
                background-color: white;
                padding: 15px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            }

            .container {
                background: white;
                padding: 20px 25px 25px 25px;
                border-radius: 15px;
                box-shadow: 0 8px 16px rgba(0,0,0,0.1);
                margin-top: 0 !important;
                margin-bottom: 25px;
                border: 1px solid rgba(0,0,0,0.05);
            }

            .metric {
                font-size: 28px;
                font-weight: bold;
                color: var(--primary-color);
                text-align: center;
                padding: 20px;
                background: var(--background-color);
                border-radius: 10px;
                margin: 15px 0;
                transition: transform 0.2s;
            }

            .metric:hover {
                transform: scale(1.02);
            }

            /* Custom button styling */
            .stButton>button {
                background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
                color: white;
                padding: 12px 24px;
                border-radius: 8px;
                border: none;
                cursor: pointer;
                font-size: 16px;
                font-weight: 600;
                width: 100%;
                transition: all 0.3s ease;
                text-transform: uppercase;
                letter-spacing: 1px;
                margin-top: 20px;
            }

            .stButton>button:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            }

            /* Custom number input styling */
            .stNumberInput>div>div>input {
                border-radius: 8px;
                border: 2px solid #e0e0e0;
                padding: 10px;
                transition: all 0.3s ease;
            }

            .stNumberInput>div>div>input:focus {
                border-color: var(--primary-color);
                box-shadow: 0 0 0 2px rgba(46, 125, 50, 0.2);
            }

            /* Responsive design adjustments */
            @media (max-width: 768px) {
                .title {
                    font-size: 32px;
                }
                .caption {
                    font-size: 16px;
                }
                .metric {
                    font-size: 24px;
                }
            }
        </style>
        """, unsafe_allow_html=True)

    # Judul dan caption
    st.markdown('<div class="title">🏡 Prediksi Harga Rumah Wilayah Cimanggis</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="caption">✨ By: Rahma Putri Azzahra | Powered by Random Forest 🌳</div>',
                unsafe_allow_html=True)

    st.markdown("""
        <div style='padding: 15px; background-color: #E8F5E9; border-radius: 10px; margin: 25px 0;'>
            <p style='margin: 0; color: #2E7D32; font-size: 16px;'>
                ℹ️ Isi detail rumah <strong>di sidebar kiri layar</strong>, kemudian klik tombol prediksi untuk mengetahui estimasi harga rumah Anda.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Sidebar input
    with st.sidebar:
        st.markdown('<div class="sidebar-header">📝 Detail Rumah</div>',
                    unsafe_allow_html=True)
        k_tidur = st.number_input("Jumlah Kamar Tidur", min_value=1, step=1,
                                  key="k_tidur", help="Masukkan jumlah kamar tidur rumah.")
        k_mandi = st.number_input("Jumlah Kamar Mandi", min_value=1, step=1,
                                  key="k_mandi", help="Masukkan jumlah kamar mandi rumah.")
        l_bangunan = st.number_input("Luas Bangunan (m²)", min_value=1.0, step=1.0,
                                     key="l_bangunan", help="Masukkan luas bangunan rumah (dalam meter persegi).")
        l_tanah = st.number_input("Luas Tanah (m²)", min_value=1.0, step=1.0,
                                  key="l_tanah", help="Masukkan luas tanah rumah (dalam meter persegi).")
        prediksi = st.button("🎯 Prediksi Harga Sekarang!", key="prediksi",
                             help="Klik untuk mendapatkan estimasi harga rumah.")

    # Proses prediksi dan output hasil
    if prediksi:
        # Load model dan scaler
        model = joblib.load("model/model.pkl")
        scaler = joblib.load("scaler/scaler.pkl")

        input_data = np.array([[k_tidur, k_mandi, l_bangunan, l_tanah]])
        input_scaled = scaler.transform(input_data)
        predicted_price = model.predict(input_scaled)[0]

        # Format hasil prediksi
        formatted_price = format_price(predicted_price)

        # Nilai akurasi model (hardcoded)
        r2_score_value = 0.96

        # Pesan sukses prediksi
        st.markdown("""
            <div style='padding: 10px 20px; background-color: #E8F5E9; border-radius: 10px; text-align: center; margin: 10px 0;'>
                <h3 style='color: #2E7D32; margin: 0;'>🎯 Prediksi Berhasil!</h3>
            </div>
        """, unsafe_allow_html=True)

        # Container hasil analisis properti tanpa spasi putih berlebih
        with st.container():
            st.markdown(
                "<div class='container' style='margin-top: 0;'>", unsafe_allow_html=True)
            st.markdown("""
                <h3 style='color: #2E7D32; text-align: center; margin: 5px 0 10px 0;'>
                    📊 Hasil Analisis Properti
                </h3>
            """, unsafe_allow_html=True)
            st.markdown(
                f"<div class='metric'>💰 Estimasi Harga: {formatted_price}</div>", unsafe_allow_html=True)
            st.markdown(
                f"<div class='metric'>📈 Akurasi Model: {r2_score_value:.2f}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        # Ringkasan input dengan style modern
        st.markdown("""
            <div style='margin: 20px 0 30px 0;'>
                <h3 style='color: #2E7D32; border-bottom: 2px solid #81C784; padding-bottom: 10px; margin-top: 0;'>
                    🔍 Ringkasan Input
                </h3>
            </div>
        """, unsafe_allow_html=True)

        summary_html = f"""
            <div style='background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <div style='display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;'>
                    <div style='padding: 10px; background: #F5F5F5; border-radius: 8px;'>
                        <strong>🛏️ Kamar Tidur:</strong> {k_tidur}
                    </div>
                    <div style='padding: 10px; background: #F5F5F5; border-radius: 8px;'>
                        <strong>🚿 Kamar Mandi:</strong> {k_mandi}
                    </div>
                    <div style='padding: 10px; background: #F5F5F5; border-radius: 8px;'>
                        <strong>🏠 Luas Bangunan:</strong> {l_bangunan} m²
                    </div>
                    <div style='padding: 10px; background: #F5F5F5; border-radius: 8px;'>
                        <strong>📏 Luas Tanah:</strong> {l_tanah} m²
                    </div>
                </div>
            </div>
        """
        st.markdown(summary_html, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
