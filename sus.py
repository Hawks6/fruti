import streamlit as st
import Deta as deta
DETA_KEY = "d0kcaaayith_CVRFVkGkum8n8EUxpQYPXMJfbDdUPYUM"
deta = Deta(DETA_KEY)
db = deta.Base("hkth")

def form():
    st.write("**FORM**")
    with st.form(key = "information form"):
        name = st.text_input("Enter your **Name**")
        age = st.slider("Select your **Age** !",0,99)
        weight = st.number_input("Enter your **Weight** ! (kgs)",0,120)
        height = st.number_input("Enter your **Height** ! (cm)",0,400)
        choice = st.selectbox('Select your **Gender**',('Male','Female','Other'))
        submission = st.form_submit_button(label = "Submit")
        insert_data(name,age,weight,height,choice)
        if submission == True:
            insert_data(name,age,weight,height,choice)

    st.success("Successfully submitted")
    st.caption("  [continue](https://fruti-6i5fctpitnw.streamlit.app/) ")
def insert_data(name,age,weight,height,choice):
    return db.put({"key":name,"age":age, "wg":weight, "hg":height, "ch":choice})

def fetch_all():
    res = db.fetch()
    return res.items

def get_keys(name):
    return db.get(name)
fetch_all()
form()
