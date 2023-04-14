import streamlit as st
from datetime import time

option = st.multiselect(
    label = "Which places have you been?" ,
    options = ("Sydney" , "Tokyo" , "New Delhi" , "Paris" , "Cape Town") ,
    default = ("Sydney" , "Paris")
)
st.write(option)

num = st.slider(
    label = "Your age" ,
    min_value = 18 ,
    max_value = 120 ,
    value = 20 ,
    step = 1
)
st.write(num)

num = st.slider(
    label = "Your age" ,
    min_value = 18 ,
    max_value = 120 ,
    value = (40 , 60) ,
    step = 1
)
st.write(num)

##visit_timing = st.slider(
##    label = "Your appointment" ,
##    value = (time(11 , 30) , time(12 , 45))
##)
##st.write(visit_timing)

option = st.select_slider(
    label = "Select the best color" ,
    options = ("Violet" , "Indigo" , "Blue" , "Green" , "Yellow" , "Orange" , "Red")
)
st.write(option)

start_color , end_color = st.select_slider(
    label = "Select color range" ,
    options = ("Violet" , "Indigo" , "Blue" , "Green" , "Yellow" , "Orange" , "Red") ,
    value = ("Blue" , "Orange")
)
st.write("From" , start_color , "to" , end_color)

txt = st.text_input(
    label = "Please enter your email" ,
    max_chars = 20 ,
    placeholder = "Email here"
)
st.write(txt)

passw = st.text_input(
    label = "Enter your password" ,
    max_chars = 20 ,
    placeholder = "password here" ,
    type = "password"
)
st.write(passw)

num = st.number_input(
    label = "Enter your weight" ,
    min_value = 40 ,
    max_value = 120 ,
    value = 65 ,
    step = 1
)
st.write(num)















