import streamlit as st
header_left, header_mid, header_right = st.columns([1,3,1],gap = 'large')

with header_mid:
    st.title('   Manna  ')
    st.title('Client Dashboard')
    st.caption('Here are Some NGOs in your location you could consider :')

st.divider()

with st.sidebar:
    st.title('What Amounts of Surplus Food are we looking at?')
    st.divider()
    st.text_input(label="Surplus Food 1")
    st.number_input(label="Weight in kg", step=1, min_value=0, key="a")
    st.text_input(label="Surplus Food 2")
    st.number_input(label="Weight in kg", step=1, min_value=0, key="b")
    st.text_input(label="Surplus Food 3")
    st.number_input(label="Weight in kg", step=1, min_value=0, key="c")
    st.text_input(label="Surplus Food 4")
    st.number_input(label="Weight in kg", step=1, min_value=0, key="d")
    if st.button('Submit'):
        st.success('NGOs Around You have been Informed!')



col1, col2, col3 = st.columns(3)
with col1:
    st.header("NGO 1")
    st.image("https://global-uploads.webflow.com/5e157548d6f7910beea4e2d6/6332e9e8b024d89bf989b17b_NGO-logo-templates.png", width=150)

with col2:
    st.header("NGO 2")
    st.image("https://global-uploads.webflow.com/5e157548d6f7910beea4e2d6/6332e9e74c2759515541a737_NGO-logo-p-500.png", width=150)

with col3:
    st.header("NGO 3")
    st.image("https://d1csarkz8obe9u.cloudfront.net/posterpreviews/ngo-organisation-logo-design-template-c7743343fbd04ee5b4bc57047cd28da6_screen.jpg?ts=1656406216", width=150)

col4, col5, col6 = st.columns(3)

with col4:
    st.header("NGO 4")
    st.image("https://d1csarkz8obe9u.cloudfront.net/posterpreviews/ngo-organisation-logo-design-template-c7743343fbd04ee5b4bc57047cd28da6_screen.jpg?ts=1656406216", width=150)

with col5:
    st.header("NGO 5")
    st.image("https://d3jmn01ri1fzgl.cloudfront.net/photoadking/webp_thumbnail/60ba0d8bd4895_json_image_1622805899.webp", width=150)

with col6:
    st.header("NGO 6")
    st.image("https://global-uploads.webflow.com/5e157548d6f7910beea4e2d6/6332e9e8b024d89bf989b17b_NGO-logo-templates.png", width=150)



    

    
