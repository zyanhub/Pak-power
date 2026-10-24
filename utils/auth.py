import hmac
import os

import streamlit as st


def get_admin_password():
    try:
        if "ADMIN_PASSWORD" in st.secrets:
            return st.secrets["ADMIN_PASSWORD"]
    except Exception:
        pass
    return os.environ.get("ADMIN_PASSWORD")


def check_password(entered):
    expected = get_admin_password()
    if not expected:
        return False
    return hmac.compare_digest(str(entered), str(expected))
