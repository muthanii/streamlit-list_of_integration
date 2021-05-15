import requests
from bs4 import BeautifulSoup
import streamlit as st

result = requests.get("https://en.wikipedia.org/wiki/Lists_of_integrals#Integrals_of_simple_functions")
src = result.content
soup = BeautifulSoup(src, "lxml")
imgs = soup.find_all("img")

latex = []

for i in imgs:
    latex.append(i.attrs["alt"])

del latex[101]
del latex[100]
del latex[99]
del latex[98]
del latex[0]

class Data:
    def __init__(self):
        self.tex_integrals_with_singularity = latex[0:2]
        self.tex_rational_functions = latex[2:8]
        self.tex_exponential_functions = latex[8:11]
        self.tex_logarithms = latex[11:13]
        self.tex_trig_functions = latex[13:31]
        self.tex_inverse_trig_functions = latex[31:37]
        self.tex_hyperbolic_functions = latex[37:43]
        self.tex_inverse_hyperbolic_functions = latex[43:49]
        self.tex_products_of_functions = latex[49:53]
        self.tex_absolute_value_functions = latex[53:65]
        self.options = ["Integrals with Singularity", 
                     "Rational Functions",
                     "Exponential Functions",
                     "Logarithms",
                     "Trigonometric Functions", 
                     "Inverse Trigonometric Functions",
                     "Hyperbolic Functions",
                     "Inverse Hyperbolic Functions",
                     "Products of Functions",
                     "Absolute Value of Functions"]

    def integrals_with_singularity(self):
        st.header("Integrals with Singularity")
        for i in self.tex_integrals_with_singularity:
            st.latex(i)

    def rational_functions(self):
        st.header("Rational Functions")
        for i in self.tex_rational_functions:
            st.latex(i)

    def exponential_functions(self):
        st.header("Exponential Functions")
        for i in self.tex_exponential_functions:
            st.latex(i)

    def logarithms(self):
        st.header("Logarithms")
        for i in self.tex_logarithms:
            st.latex(i)

    def trig_functions(self):
        st.header("Trigonometric Functions")
        for i in self.tex_trig_functions:
            st.latex(i)

    def inverse_trig_functions(self):
        st.header("Inverse Trigonometric Functions")
        for i in self.tex_inverse_trig_functions:
            st.latex(i)

    def hyperbolic_functions(self):
        st.header("Hyperbolic Functions")
        for i in self.tex_hyperbolic_functions:
            st.latex(i)

    def inverse_hyperbolic_functions(self):
        st.header("Inverse Hyperbolic Functions")
        for i in self.tex_inverse_hyperbolic_functions:
            st.latex(i)

    def products_of_functions(self):
        st.header("Product of Functions")
        for i in self.tex_products_of_functions:
            st.latex(i)

    def absolute_value_functions(self):
        st.header("Absolute Value of Functions")
        for i in self.tex_absolute_value_functions:
            st.latex(i)   
