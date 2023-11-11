import streamlit as st

st.title("Kuliah Praktikum Analisa Big Data Ekonomi")
st.write("# Sri Yani K")
st.write("## Dosen FEB Universitas Trisakti")
st.write("### Jakarta Barat")

#kinerja
st.metric("Kinerja", 40, -1)
st.metric("Response Time", 30, 20)

#membuat pilihan
pilih1 = st.checkbox('Ya')
pilih2 = st.checkbox('Tidak')

st.write(pilih1)
st.write(pilih2)

makanan = st.radio('Makanan kesukaan', ['Bakso', 'Sate', 'Mie Ayam'])

st.write(makanan)

minuman = st.selectbox('Pilih minuman yang dipesan', ['es teh','jus', 'kopi'])

st.write(minuman)

bayar = st.multiselect('Bayar pakai:',['Tunai','OVo', 'GoPay'])
st.write(bayar)