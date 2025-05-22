import streamlit as st

# Theme switcher utility
def apply_theme():
    """
    Adds a light/dark mode toggle in the sidebar and injects CSS for dark mode.
    """
    # Use a dedicated key for the radio so Streamlit stores the mode string
    mode = st.sidebar.radio(
        label="Display Theme", 
        options=["Light 🌞", "Dark 🌙"],
        index=0,
        key="theme_mode",
        help="Switch between light and dark modes."
    )
    if mode == "Dark 🌙":
        dark_css = """
        <style>
        .stApp, .reportview-container { background-color: #0A1116 !important; color: #E0E0E0 !important; }
        .sidebar .sidebar-content { background-color: #1E1E1E !important; }
        .stButton>button, .stDownloadButton>button { background-color: #333333 !important; color: #E0E0E0 !important; }
        .stDataFrame table { background-color: #1E1E1E !important; }
        .js-plotly-plot .plotly .main-svg { background-color: #0A1116 !important; }
        </style>
        """
        st.markdown(dark_css, unsafe_allow_html=True)
