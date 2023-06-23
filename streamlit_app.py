import streamlit as st
st.title("Save food save life!:moon:")
st.header("**Hunger meter**")
x = st.slider('Hunger scale',0,10)  
st.write("Your hunger rating is",x, 'so you should consume around', x * 50,"calories")
if st.button('Submit'):
    st.write('your data has been submitted, open [MENU](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)')
