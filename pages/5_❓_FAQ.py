import streamlit as st
from utils.functions.theme import apply_theme

# Configure the page
st.set_page_config(
    page_title="Portfolio Prioritization App", 
    page_icon="🚀",
    layout="wide")

# Applies the theme
apply_theme()

st.title("📖 Frequently Asked Questions")
st.markdown(
    "Welcome! Click on any question to learn how the **Portfolio Prioritization App** works and get simple, clear explanations for all the key features."
)

with st.expander("❓ What does this app do?"):
    st.write(
        "This app helps you **decide what to focus on** by letting you:\n"
        "- **Define what matters** (criteria) for your projects or items.\n"
        "- **Score and rank** those items based on your custom criteria.\n"
        "- **See how shaky or solid** those scores are with risk checks.\n"
        "- **Get a smart guess** on each item’s chance to succeed, based on past data."
    )

with st.expander("❓ How do I get started?"):
    st.write(
        "1. Use the **sidebar** to go to **Criteria Setup** and list what matters most to you.\n"
        "2. Head to **Item Prioritization**, enter your items, and watch them get scored.\n"
        "3. Jump into **Analytics** to see risk details and success chances."
    )

with st.expander("❓ How do I choose and weight my criteria?"):
    st.write(
        "On the **Criteria Setup** page:\n"
        "- **Add** each factor you care about (like cost, impact, time).\n"
        "- **Set importance** by moving the slider: bigger slider = more important.\n"
        "- The app makes sure all sliders add up fairly behind the scenes."
    )

with st.expander("❓ What is Risk Volatility?"):
    st.write(
        "- **Risk Volatility** is how much uncertainty you want around a score.\n"
        "- Think of a **dartboard**: the farther your darts scatter, the higher the volatility.\n"
        "- **0** means all darts in the center (no risk). **1** means darts everywhere (high risk)."
    )

with st.expander("❓ What are Simulations?"):
    st.write(
        "- **Simulations** are like doing the same test over and over to see different results.\n"
        "- More simulations give you a smoother picture but take a bit longer.\n"
        "- Fewer simulations are quick but can look jumpy."
    )

with st.expander("❓ What is a Monte Carlo simulation?"):
    st.write(
        "It’s just a fancy name for running **many simulations** to show you:\n"
        "- **Best-case** (top of the results)\n"
        "- **Worst-case** (bottom of the results)\n"
        "- **Most likely** (middle of the results)\n"
        "All based on your chosen risk level."
    )

with st.expander("❓ How does the app guess success chances?"):
    st.write(
        "We look at how similar items did in the past and use that info to give each new item a **success score** (like a percentage)."
    )

with st.expander("❓ What do the success scores mean?"):
    st.write(
        "- A score near **100%** means a high chance of success.\n"
        "- A score near **0%** means low chance.\n"
        "- Use these numbers to compare items side by side."
    )

with st.expander("❓ Can I save or download my results?"):
    st.write(
        "Yes—just click the **Download CSV** button on the Portfolio or Analytics pages to get your data."
    )

with st.expander("❓ Can I change settings later?"):
    st.write(
        "Absolutely! Every slider and input can be adjusted at any time, and the app updates your results instantly."
    )

with st.expander("❓ Where can I get help or share feedback?"):
    st.write(
        "- **Email**: [mymail@mydomain.com](mailto:mymail@mydomain.com)\n"
        "- **GitHub**: [github.com/your-repo/issues](https://github.com/your-repo/issues)"
    )

# Footer
st.divider()
st.caption("© 2025 David Peña. All rights reserved.")