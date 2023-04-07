import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#st.text("This is a text.")

#st.write("This is **just** a **_test_**")
df = pd.read_csv(r"D:\datum\streamlit\some_data.csv")
dc = {"a" : 10 , "b" : 20 , "c" : 30}
fig , ax = plt.subplots()
ax.scatter(np.arange(5) , np.arange(5) ** 2)

##st.title("This is the title")
##st.header("Header")
##st.subheader("Subs")

code = '''def func():
    print(np.arange(10))'''
st.code(code , language = "python")
