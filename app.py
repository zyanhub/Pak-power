import streamlit as st
from utils.db import create_table, add_vote, get_results

# table create (first run)
create_table()

st.title("Pakistan Live Power 🇵🇰")

party = st.selectbox("Select Party", ["PTI", "PMLN", "PPP"])

if st.button("Vote"):
    add_vote(party)
    st.success("Vote Submitted!")

st.subheader("Live Results")

data = get_results()

for party, votes in data:
    st.write(f"{party}: {votes}")
