import streamlit as st
import numpy as np
import pandas as pd
import json

#dataframe , table, metric, json
df = pd.DataFrame(
    np.random.randn(50 , 20) ,
    columns = ["cols" + str(i) for i in range(20)])
#st.dataframe(df , width = 200 , height = 1000)
#st.dataframe(np.random.randn(50 , 20))

#st.table(df)

#st.metric("TCS stock" , value = "3220.70" , delta = "19.10" , delta_color = "off")

f = open(r"D:\datum\aa_chatbot\simple_chatbot\prac\all_intents_js.json")
dt = json.load(f)
st.json(dt , expanded = False)
