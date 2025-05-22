import streamlit as st
from utils.functions.theme import apply_theme

# Configure the page
st.set_page_config(
    page_title="Portfolio Prioritization App", 
    page_icon="🚀",
    layout="wide")

# Applies the theme
apply_theme()

st.title("🚀 Prioxy")
st.subheader("Turn data into decisions: prioritize with confidence")

st.markdown(
    """
    Welcome to **Prioxy: A Portfolio Prioritization App**, your one-stop solution to:
    
    - 🎯 **Define & Refine Criteria**: Create custom evaluation metrics and weight them to match your goals.
    - 📈 **Score & Rank Items**: Employ weighted scoring and the Analytic Hierarchy Process (AHP) for transparent, defensible rankings.
    - ⚖️ **Analyze Risk**: Explore uncertainties with Real Options Analysis and Monte Carlo simulations—see best-, worst-, and most-likely outcomes.
    - 🤖 **Leverage AI Insights**: Harness machine learning for forward-looking predictions and data-driven recommendations.
    
    
    Ready to take control of your portfolio? Use the sidebar to dive into each module and start prioritizing smarter!
    """,
    unsafe_allow_html=True
)

st.divider()
st.markdown("### 🔍 Navigation Quick Start")
st.markdown(
    "1. **Portfolio**: Browse and filter your full list of items.\n"
    "2. **Criteria Setup**: Build, adjust, and weight your evaluation factors.\n"
    "3. **Item Prioritization**: Score and compare items in real time.\n"
    "4. **Analytics**: Dive into risk simulations, predictions, and final priority breakdowns.\n"
    "5. **FAQ**: Find answers to common questions and learn more about this app."
)

# Footer
st.divider()
st.caption("© 2025 David Peña. All rights reserved.")