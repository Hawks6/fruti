import streamlit as st
st.title("MENU:")
# f=open('data.txt','r')
# x= f.readline()
# st.title(x)
col1, col2, col3 = st.columns(3, gap= "large")
with col1:
   st.header("Freach Fries")
   st.image("https://www.awesomecuisine.com/wp-content/uploads/2009/05/french-fries.jpg",width=200)
   st.number_input(label="Quantity", step=1, min_value=0, key="a")
   if st.button('Add', key="j"):
      st.success('Pres Tips')

with col2:
   st.header("Omlette")
   st.image("https://www.mygorgeousrecipes.com/wp-content/uploads/2018/02/Worlds-Best-Vegetarian-Omelette-Quick-and-Easy.jpg",width=200)
   st.number_input(label="Quantity", step=1, min_value=0, key="b")
   if st.button('Add', key="k" ):
      st.success('Pres Tips')

with col3:
   st.header("Chicken Shawarma")
   st.image("https://www.licious.in/blog/wp-content/uploads/2020/12/Chicken-Shawarma-750x750.jpg",width=200)
   st.number_input(label="Quantity", step=1, min_value=0, key="c")
   if st.button('Add', key="l"):
      st.success('Pres Tips')

col4, col5, col6 = st.columns(3,gap= "large")

with col4:
   st.header("Chicken kebab")
   st.image("https://www.thetakeiteasychef.com/wp-content/uploads/2016/12/unpaid-review-easterns-kebab-masala.1024x1024-3.png",width=200)
   st.number_input(label="Quantity", step=1, min_value=0, key="d")
   if st.button('Add', key="m"):
      st.success('Pres Tips')

with col5:
   st.header("Chicken Burger Meal")
   st.image("https://s7d1.scene7.com/is/image/mcdonalds/chickenburgermeal:1-3-product-tile-desktop?wid=765&hei=472&dpr=off",width=200)
   st.number_input(label="Quantity", step=1, min_value=0, key="e")
   if st.button('Add', key="n"):
      st.success('Pres Tips')

with col6:
   st.header("pepperoni pizza")
   st.image("https://www.simplyrecipes.com/thmb/I4razizFmeF8ua2jwuD0Pq4XpP8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__simply_recipes__uploads__2019__09__easy-pepperoni-pizza-lead-4-82c60893fcad4ade906a8a9f59b8da9d.jpg",width=200)
   st.number_input(label="Quantity", step=1, min_value=0, key="f")
   if st.button('Add', key="o"):
      st.success('Pres Tips')

col7, col8, col9 = st.columns(3,gap= "large")

with col7:
   st.header("Mac n Cheese")
   st.image("https://www.allrecipes.com/thmb/X94tJBe-nYseXIbMXo03pVXWnRA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/238691-Simple-Macaroni-And-Cheese-mfs_008-7a50b284b67140919a0984093cb4611b.jpg",width=200)
   st.number_input(label="Quantity", step=1, min_value=0, key="g")
   if st.button('Add', key="p"):
      st.success('Pres Tips')

with col8:
   st.header("Chole Bhature")
   st.image("https://media.vogue.in/wp-content/uploads/2020/08/chole-bhature-recipe.jpg",width=200)
   st.number_input(label="Quantity", step=1, min_value=0, key="h")
   if st.button('Add', key="q"):
      st.success('Pres Tips')

with col9:
   st.header("Behrouz Biryani")
   st.image("https://img.etimg.com/thumb/msid-70476197,width-1200,height-900,imgsize-696197,overlay-etrise/photo.jpg",width=200)
   st.number_input(label="Quantity", step=1, min_value=0, key="i")
   if st.button('Add', key="r"):
      st.success('Pres Tips')
