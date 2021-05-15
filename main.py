from data import Data
import streamlit as st

data = Data()

st.title("List of Integrals")
st.subheader("Source: https://en.wikipedia.org/wiki/Lists_of_integrals#Integrals_of_simple_functions")

option = st.selectbox("", data.options)

if option == data.options[0]:
    data.integrals_with_singularity()
elif option == data.options[1]:
    data.rational_functions()
elif option == data.options[2]:
    data.exponential_functions()
elif option == data.options[3]:
    data.logarithms()
elif option == data.options[4]:
    data.trig_functions()
elif option == data.options[5]:
    data.inverse_trig_functions()
elif option == data.options[6]:
    data.hyperbolic_functions()
elif option == data.options[7]:
    data.inverse_hyperbolic_functions()
elif option == data.options[8]:
    data.products_of_functions()
elif option == data.options[9]:
    data.absolute_value_functions()
