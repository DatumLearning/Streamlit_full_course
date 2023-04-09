import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10 , 2) , columns = ["prices" , "diff"])
#line chart
#st.line_chart(df , y = ["diff"])

#st.area_chart(df , y = ["prices"])

#st.bar_chart(df)

#matplotlib scatter
#fig , ax = plt.subplots()
#ax.scatter(np.arange(10) , np.arange(10) ** 2)
#ax.hist(np.random.randn(100) , bins = 10)
#st.pyplot(fig)

places = pd.DataFrame({
        "lat" : [19.07 , 28.64] ,
        "lon" : [72.87 , 77.21]
    })
st.map(places)

