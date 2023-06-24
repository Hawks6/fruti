import streamlit as st

st.title("Save food save life!:moon:")
st.header("**How hungry are you?**")
x = st.slider(1,5)  


st.write('we recommend you consume around', x * 200,"calories")
if(x==1):
    if st.button('Submit'):
        st.success("successfully submitted")
        st.caption('open [MENU](https://fruti-jym0qgj9ccs.streamlit.app/)')

if(x==2):
    if st.button('Submit'):
        st.success("successfully submitted")
        st.caption('open [MENU](https://fruti-3luk32bl952.streamlit.app/)')

if(x==3):
    if st.button('Submit'):
        st.success("successfully submitted")
        st.caption('open [MENU](https://fruti-rmbzzumxvep.streamlit.app/)')

if(x==4):
    if st.button('Submit'):
        st.success("successfully submitted")
        st.caption('open [MENU](https://fruti-6d9zuuf01bo.streamlit.app/)')

if(x==5):
    if st.button('Submit'):
        st.success("successfully submitted")
        st.caption('open [MENU](https://fruti-aqh0ud8om0l.streamlit.app/)')
