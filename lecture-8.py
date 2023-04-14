import streamlit as st

choice = st.sidebar.radio(
    label = "Choose the option" ,
    options = ("audio" , "video")
)
if choice == "audio":
    st.audio("audio_file.mp3")
    st.write("This is audio")
elif choice == "video":
    st.video("dog_video.mp4")
    st.write("this is video")

col1 , col2 = st.columns([1 , 3] , gap = "small")
col1.audio("audio_file.mp3")
col1.write("This is audio")
col2.video("dog_video.mp4")

tab1 , tab2 = st.tabs(["audio" , "video"])
tab1.audio("audio_file.mp3")
tab1.write("hi")
tab2.video("dog_video.mp4")

exp = st.expander("See pic")
exp.write("Video and image")
exp.image("doggo.jpg" , width = 400)

st.write("One")
st.write("Two")
st.write("Three")

cont = st.container()
cont.write("One")
st.write("Two")
cont.write("Three")
st.write("This is last")
cont.write("Last")







