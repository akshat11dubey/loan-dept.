import streamlit as st
st.title('Loan calculator')
st.header("HDFC BANK OF INDIA")
st.text_input("Enter your name")
st.text_input("Enter your bank account number ")
p=st.radio('Enter your account type',option=['saving','student','private','joined'])
st.text_input("Enter your address")
st.text_input('Enter your amount')
y=st.number_input('Enter your salary')
if y>=50000:
    st.write('congratulations')
    st.balloons()
else:
     st.write('sorry sir')
z=st.radio('Are you govt. emp',options=['yes','no'])
if z>='yes':
    st.write('congratulations')
    st.balloons()
else:
     st.write('sorry sir')
st.checkbox('do you have a credit card')
st.sidebar.header('schemes from Loan dept')
st.checkbox('do you have a atm card')
st.sidebar.markdown('education loan')
st.sidebar.markdown('business loan')
st.sidebar.markdown('farming loan')
st.sidebar.markdown('home loan')
st.markdown("""
<style>
.big-font {
    font-size:300px !important;
}
</style>
""", unsafe_allow_html=True)

