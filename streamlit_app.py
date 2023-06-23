import streamlit as st
st.title("Save food save life!:moon:")
st.header("**Hunger meter**")
x = st.slider('Hunger scale',0,10)  
file = open('data.txt',"w")
wt = repr(x)
file.write(wt)
file.close()
st.write("Your hunger rating is",x, 'so you should consume around', x * 50,"calories")
if st.button('Submit'):
    st.success("successfully submitted")
    st.caption('open [MENU](https://fruti-nca5gzi9h2j.streamlit.app/)')
