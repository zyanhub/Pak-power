import streamlit as st
from utils.auth import get_admin_password, check_password
from utils.db import reset_data, get_results

st.title("Admin Panel 🔐")

password = st.text_input("Enter Password", type="password")

if not get_admin_password():
    st.error("Admin password set nahi hai.")
elif check_password(password):
    st.success("Access Granted")

    if st.button("Reset All Data"):
        reset_data()
        st.warning("All data deleted!")

    st.subheader("Current Data")
    data = get_results()

    for party, votes in data:
        st.write(f"{party}: {votes}")

else:
    st.error("Wrong Password")
