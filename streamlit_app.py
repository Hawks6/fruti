import streamlit as st

st.title("Save food save life!:moon:")
st.header("**Hunger meter**")
x = st.slider('Hunger scale',0,5)  


st.write('we recommend you consume around', x * 200,"calories")
if(x=200):
    if st.button('Submit'):
        st.success("successfully submitted")
        st.caption('open [MENU]()')

if(x=400):
    if st.button('Submit'):
        st.success("successfully submitted")
        st.caption('open [MENU]()')

if(x=600):
    if st.button('Submit'):
        st.success("successfully submitted")
        st.caption('open [MENU]()')

if(x=800):
    if st.button('Submit'):
        st.success("successfully submitted")
        st.caption('open [MENU]()')

if(x=1000):
    if st.button('Submit'):
        st.success("successfully submitted")
        st.caption('open [MENU]()')
