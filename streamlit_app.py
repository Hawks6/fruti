import streamlit as st

st.title("Save food save life!:moon:")
st.header("**Hunger meter**")
x = st.slider('Hunger scale',0,5)  


st.write('we recommend you consume around', x * 200,"calories")
if(x==0):
    if st.button('Submit'):
        st.success("successfully submitted")
        st.caption('open [MENU]()')

if(x==2):
    if st.button('Submit'):
        st.success("successfully submitted")
        st.caption('open [MENU]()')

if(x==4):
    if st.button('Submit'):
        st.success("successfully submitted")
        st.caption('open [MENU]()')

if(x==6):
    if st.button('Submit'):
        st.success("successfully submitted")
        st.caption('open [MENU]()')

if(x==8):
    if st.button('Submit'):
        st.success("successfully submitted")
        st.caption('open [MENU]()')
