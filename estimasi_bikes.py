import pickle
import streamlit as st

model = pickle.load(open('estimasi_bikes.sav', 'rb'))

st.title('Estimasi Harga Motor di India')

kms_driven = st.number_input('Input Jarak Tempuh Motor')
age = st.number_input('Input Umur Motor')
power = st.number_input('Input Cc Motor')

prediksi = ''
if st.button('Estimasi Harga Motor'):
    prediksi = model.predict(
        [[kms_driven, age, power]]
    )
    st.write('Estimasi Harga Motor Dalam Rupee : ', prediksi)
    st.write('Estimasi Harga Motor Dalam IDR (Juta) : ', prediksi*16000)