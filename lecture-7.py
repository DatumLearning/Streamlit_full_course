import streamlit as st
from PIL import Image
import cv2

img = Image.open("doggo.jpg")
img = cv2.imread("doggo.jpg")
st.image(
    img ,
    caption = "Image of a dog, bicycle and a truck" ,
    width = 800 ,
    channels = "BGR"
)

st.audio("audio_file.mp3" , start_time = 10)

st.video("dog_video.mp4")
