import pandas as pd
import streamlit as st
from utils.auth import get_admin_password, check_password
from utils.db import create_table, add_vote, get_results, reset_data

# ---------------- INITIAL SETUP ----------------
st.set_page_config(page_title="Pakistan Live Power", layout="centered")

# Create DB table
create_table()

# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["User Panel", "Admin Panel"])

# ---------------- USER PANEL ----------------
if page == "User Panel":
    st.title("Pakistan Live Power 🇵🇰")

    st.markdown("### Vote for your party")
    
     party = st.selectbox("Select Party", ["MQM", "PMLN", "PPP", "JUI-F", "PTI", "JI", "TLP"])

    if st.session_state.get("voted"):
        st.info("Aap is session mein vote de chuke hain ✅")
    elif st.button("Submit Vote"):
        add_vote(party)
        st.session_state["voted"] = True
        st.success(f"Vote submitted for {party} ✅")

    st.divider()

    st.subheader("📊 Live Results")

    data = get_results()

    if data:
        total = sum(v for _, v in data)
        df = pd.DataFrame(data, columns=["Party", "Votes"]).set_index("Party")
        st.bar_chart(df)
        for name, votes in data:
            st.write(f"👉 {name}: {votes} votes ({votes / total * 100:.1f}%)")
        st.caption(f"Total votes: {total}")
    else:
        st.info("No votes yet")

# ---------------- ADMIN PANEL ----------------
elif page == "Admin Panel":
    st.title("Admin Dashboard 🔐")

    password = st.text_input("Enter Admin Password", type="password")

    if not get_admin_password():
        st.error("Admin password set nahi hai.")
    elif password:
        if check_password(password):
            st.success("Access Granted ✅")

            st.divider()

            # Reset Button
            if st.button("⚠️ Reset All Data"):
                reset_data()
                st.warning("All voting data has been deleted!")

            st.divider()

            st.subheader("📊 Current Voting Data")

            data = get_results()

            if data:
                for party, votes in data:
                    st.write(f"👉 {party}: {votes} votes")
            else:
                st.info("No data available")

        else:
            st.error("❌ Wrong Password")
