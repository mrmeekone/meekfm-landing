
import streamlit as st

st.set_page_config(page_title="Meek FM", page_icon="📊", layout="centered")

# Logo
st.image("meekfm_logo.png", use_column_width=True)

# Tagline
st.markdown("<h2 style='text-align: center;'>AI finance & strategic execution</h2>", unsafe_allow_html=True)

# About section
st.markdown("""
### About Meek FM
We build scalable, AI-native platforms that turn data into power, profit, and precision.  
Our mission is to architect the future of finance through intelligence and execution.
""")

# Call to action
st.markdown("### 🚀 Join the Waitlist")
st.markdown("[Click here to contact us](mailto:contact@meekfm.com)")

# Footer
st.markdown("---")
st.markdown("© 2025 Meek FM. All rights reserved.")
