import streamlit as st
from PIL import Image
image=Image.open(r'C:\Users\daksh\Downloads\bank.jpeg')
st.image(image,caption='WELCOME TO VVT BANK')
st.title('Loan calculator')
st.header("VVT BANK OF INDIA")
st.text_input("Enter your name")
st.text_input("Enter your bank account number ")
st.text_input("Enter your account type")
st.text_input("Enter your address")
st.text_input('Enter your amount')
y=st.number_input('Enter your salary')
if y>=50000:
    st.write('congratulations')
    st.balloons()
else:
     st.write('sorry sir')
z=st.radio('Are you govt. emp',options=['yes','no'])
st.checkbox('do you have a credit card')
st.sidebar.header('schemes from Loan dept')
st.checkbox('do you have a atm card')
st.sidebar.markdown(["1~education loan"])
st.sidebar.markdown(["2~business loan"])
st.sidebar.markdown(["3~farming loan"])
st.sidebar.markdown(['4~home loan'])
st.markdown("""
<style>
.big-font {
    font-size:300px !important;
}
</style>
""", unsafe_allow_html=True)

