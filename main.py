import streamlit as st
header_left, header_mid, header_right = st.columns([1,3,1],gap = 'large')

with header_mid:
    st.title('Hello!')
    st.header('Choose the Service you would like to Avail :')
    st.subheader('Are You a [Customer](https://fruti-tlso26160en.streamlit.app/) or a [Business](https://fruti-0ggql26iuzi.streamlit.app/)?')

st.divider()

