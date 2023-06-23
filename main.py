import streamlit as st
header_left, header_mid, header_right = st.columns([1,3,1],gap = 'large')

with header_mid:
    st.title('Hello!')
    st.subheader('Choose the Service you would like to Avail :')
    st.caption('Are You a [Customer]() or a [Business](https://fruti-0ggql26iuzi.streamlit.app/)?')

st.divider()

