import streamlit as st
import pandas as pd
import numpy as np
import time

pr = st.button("Time is:")
if pr == True:
    st.write(time.time())

def fn():
     st.write(time.time())

st.button("Time" , on_click = fn)

#Download csv file
df = pd.DataFrame(
    np.random.randn(10 , 2) ,
    columns = ["col1" , "col2"]
)
data = df.to_csv().encode("utf-8")

st.download_button(
    label = "Download this" ,
    data = data ,
    file_name = "new_data_file.csv" ,
    mime = "text/csv"
)

#Download text file
text_contents = "This is some text"
st.download_button("Please download" , text_contents)

#Download image file
file = open("doggo.jpg" , "rb")
btn = st.download_button(
    label = "Download the image" ,
    data = file ,
    file_name = "the_dog_image.jpg" ,
    mime = "image/jpg"
)

#checkbox
ck = st.checkbox("I agree" , value = False)
if ck:
    st.write("Agreement reached")

#radio button
food = st.radio("What would like to eat?" ,
                ("Pizza" , "Burger" , "Chips"))
if food == "Pizza":
    st.write("You ordered Pizza")
elif food == "Burger":
    st.write("You ordered Burger")
elif food == "Chips":
    st.write("You ordered Chips")

#selectbox
option = st.selectbox("Where do you live?" ,
                      ("Moscow" , "New York" , "Istanbul"))
if option == "Moscow":
    st.write("You wrote Moscow")
elif option == "New York":
    st.write("You wrote New York")
elif option == "Istanbul":
    st.write("You wrote Istanbul")


