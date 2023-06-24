import streamlit as st
from deta import Deta
st.title("Save food save life!:moon:")
st.header("**Hunger meter**")
x = st.slider('Hunger scale',0,10)  
deta = Deta(st.secrets["d0e7kgqnw4j_diMQAoXmbyn4iWV7fF1cQRVrXvZDwypq"])
db = deta.Base("example-db")

st.write("Your hunger rating is",x, 'so you should consume around', x * 50,"calories")
if st.button('Submit'):
    if submitted:
        db.put({"value" : x})
    st.success("successfully submitted")
    st.caption('open [MENU](https://fruti-nca5gzi9h2j.streamlit.app/)')
db_content = db.fetch().items
st.write(db_content)
