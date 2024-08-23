import streamlit as st

st.header('Factorial')
st.write('Welcome to my page')
num = st.number_input('enter a number',value=0)
btn = st.button('calculate')
if btn:
    result=1
    for i in range(1,num+1):
        result = result*i
    st.subheader(result)

  