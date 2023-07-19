import streamlit as st

st.title('Hello PEDD')
my_slider = st.slider('slider', 0, 100)
st.write(my_slider)


col1, col2, col3 = st.columns([1,1,1])
with col2:
    st.write('center')

with st.button('click me'):
    st.ballons()

