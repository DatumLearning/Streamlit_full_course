import streamlit as st

#initialize ss
st.session_state
if "key" not in st.session_state:
    st.session_state["key"] = 1
st.session_state

#change ss value
st.session_state
if "key" in st.session_state:
    st.session_state["key"] = 2
st.session_state

#delete one ss
st.session_state
if "key" in st.session_state:
    del st.session_state["key"]
st.session_state

st.session_state["k1"] = 10
st.session_state["k2"] = 20

#delete bulk ss
st.session_state
for k in st.session_state.keys():
    del st.session_state[k]
st.session_state


#input widget key as ss

st.session_state
st.text_input("Name" , key = "name")
st.session_state

#callback

def form_callback():
    st.write(st.session_state["my_slider"])
    st.write(st.session_state["my_checkbox"])

with st.form(key = "my_form"):
    slider_input = st.slider("My slider" , 0 , 15 , 5 , key = "my_slider")
    checkbox_input = st.checkbox("Yes or No" , key = "my_checkbox")
    submit_button = st.form_submit_button("Submit" , on_click = form_callback)
    










