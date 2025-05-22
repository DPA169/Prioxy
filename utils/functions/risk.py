import numpy as np
import streamlit as st

@st.cache_data(show_spinner=False)
def simulate_item_risk(base_scores, risk_volatility, n_simulations, seed=None):
    """
    Monte Carlo simulation: returns array shape (len(base_scores), n_simulations).
    """
    rng = np.random.default_rng(seed)
    stds = risk_volatility * np.array(base_scores)
    return rng.normal(
        loc=np.array(base_scores)[:, None],
        scale=stds[:, None],
        size=(len(base_scores), n_simulations)
    )
