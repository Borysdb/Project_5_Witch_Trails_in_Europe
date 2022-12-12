import streamlit as st
import pandas as pd
import numpy as np


value = st.slider('val') # this is a widget

st.write(value, 'squared is', value * value)


st.title("Welcome to Streamlit!")

st.write("Our first DataFrame")

st.write(
  pd.DataFrame({
      'A': [1, 2, 3, 4],
      'B': [5, 6, 7, 8]
    })
)


st.title("Welcome to Streamlit!")


selectbox = st.sidebar.selectbox(
    "Select yes or no",
    ["Yes", "No"]
)
st.write(f"You selected {selectbox}")


checkbox_one = st.checkbox("Yes")
checkbox_two = st.checkbox("No")

if checkbox_one==True and checkbox_two==False :
    value = "Yes"
elif checkbox_two==True and checkbox_one==False :
    value = "No"
elif checkbox_one==True and checkbox_two==True:
    value="Clarify your choice"
else:
    value = "No value selected"

st.write(f"You selected: {value}")


st.write("Line Chart in Streamlit")
# 10 * 2 dimensional data
chart_data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=[f"Col{i+1}" for i in range(2)]
)

st.line_chart(chart_data)

