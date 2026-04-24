import streamlit as st
import pickle

# ── Encoding dictionaries (must match notebook) ────────────────────────────────
d1 = {
    'Dell':0,'Lenovo':1,'HP':2,'Asus':3,'Acer':4,
    'MSI':5,'Toshiba':6,'Apple':7,'Samsung':8,'Microsoft':9,
    'Razer':10,'Xiaomi':11,'Huawei':12,'Google':13,'LG':14,
    'Fujitsu':15,'Mediacom':16,'Vero':17,'Chuwi':18
}
d2 = {
    'Core i3':0,'Core i5':1,'Core i7':2,'Core i9':3,
    'Ryzen 3':4,'Ryzen 5':5,'Ryzen 7':6,'Ryzen 9':7,
    'Core M':8,'Celeron':9,'Pentium':10,'Atom':11,
    'A-Series':12,'E-Series':13,'Other':14
}
d3 = {'HDD':0,'SSD':1,'SSD+HDD':2,'Hybrid':3,'Flash':4,'Other':5}
d4 = {'Windows':0,'macOS':1,'Linux':2,'Chrome OS':3,'Other':4}

# ── Load model ─────────────────────────────────────────────────────────────────
final_model = pickle.load(open('laptop_model.pkl', 'rb'))

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title='Laptop Price Predictor', page_icon='💻')

# ── UI ─────────────────────────────────────────────────────────────────────────
st.title('💻 Laptop Price Predictor')
st.write('Select the laptop specifications to get an estimated price in Euros.')

st.divider()

col1, col2 = st.columns(2)

with col1:
    brand        = st.selectbox('Brand',        list(d1.keys()))
    processor    = st.selectbox('Processor',    list(d2.keys()))
    ram          = st.selectbox('RAM (GB)',      [4, 8, 16, 32, 64])

with col2:
    storage      = st.selectbox('Storage (GB)', [32, 64, 128, 256, 512, 1000, 2000])
    storage_type = st.selectbox('Storage Type', list(d3.keys()))
    os           = st.selectbox('Operating System', list(d4.keys()))

st.divider()

if st.button('🔍 Predict Price', use_container_width=True):
    test = [[
        d1[brand],
        d2[processor],
        ram,
        storage,
        d3[storage_type],
        d4[os]
    ]]
    predicted_price = int(final_model.predict(test)[0])
    st.success(f'### Estimated Price: €{predicted_price:,}')
    st.caption('Prediction based on KNN model trained on laptop price dataset.')
