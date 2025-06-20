import streamlit as st

# Title and Header
st.title('Loan Calculator')
st.header("🏦 HDFC BANK OF INDIA")

# User Input Fields
name = st.text_input("Enter your name")
account_number = st.text_input("Enter your bank account number")
account_type = st.radio('Select your account type', options=['Saving', 'Student', 'Private', 'Joint'])
address = st.text_input("Enter your address")
amount = st.text_input('Enter loan amount required')
salary = st.number_input('Enter your monthly salary')
govt_emp = st.radio('Are you a government employee?', options=['Yes', 'No'])
credit_card = st.checkbox('Do you have a credit card?')
atm_card = st.checkbox('Do you have an ATM card?')
user_id = st.text_input("Enter your ID")
mobile = st.text_input("Enter your mobile phone number")
email = st.text_input("Enter your email address")
otp_option = st.radio("Choose OTP delivery method", options=['SMS', 'Email'])

# Sidebar loan options
st.sidebar.header('Schemes from Loan Dept')
st.sidebar.markdown('- 🎓 Education Loan')
st.sidebar.markdown('- 🏢 Business Loan')
st.sidebar.markdown('- 🌾 Farming Loan')
st.sidebar.markdown('- 🏠 Home Loan')

# Salary condition
if salary >= 50000:
    st.success("🎉 Congratulations! You're eligible based on your salary.")
    st.balloons()
else:
    st.warning("Sorry, you may not be eligible due to your current salary.")

# Govt employee check
if govt_emp == 'Yes':
    st.success("✅ Verified as a government employee.")
else:
    st.warning("❌ Not a government employee.")

# Simulated OTP confirmation
if mobile and otp_option == 'SMS':
    st.info(f"OTP will be sent to your mobile number: {mobile}")
elif email and otp_option == 'Email':
    st.info(f"OTP will be sent to your email: {email}")

# ✅ Final confirmation checkbox
confirm = st.checkbox("I confirm the above details are correct and want to submit")

# Show thank-you message after confirmation
if confirm and name and account_number and address and amount and user_id and (mobile or email):
    st.success("✅ Thank you for sharing your details. Please wait while we process your request!")

# Optional styling
st.markdown("""
<style>
    .big-font {
        font-size:300px !important;
    }
</style>
""", unsafe_allow_html=True)
