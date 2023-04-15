import streamlit as st
import numpy as np
import pandas as pd
import torch
import time
from full_model import Net

#loading cache_resource
#else cache_data

@st.cache_resource
def load_model():
    st.write("load time" , time.time())
    model = Net()
    checkpoints = torch.load(r"D:\datum\streamlit\final_mnist_model.pth")
    model.load_state_dict(checkpoints["model_state"])
    return model

@st.cache_data
def inference(data):
    st.write("inference time" , time.time())
    return model(torch.Tensor(data))

model = load_model()
#inp = np.random.randn(1 , 1 , 28 , 28)
inp = np.zeros((1 , 1 , 28 , 28))
out = inference(inp)
st.write(out)
