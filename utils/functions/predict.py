import os
import streamlit as st
import joblib
import pandas as pd
import numpy as np
from utils.functions.scoring import calculate_item_score

@st.cache_resource
def load_model(path: str = 'model.pkl'):
    """
    Load the trained ML pipeline once per session (if it exists).
    """
    return joblib.load(path)

@st.cache_data(show_spinner=False)
def predict_success(df_items: pd.DataFrame,
                    risk_volatility: float = 0.1,
                    seed: int | None = None) -> pd.Series:
    """
    Smart predictor: use ML model if model.pkl exists, else fallback to manual sigmoid.
    """
    model_path = 'model.pkl'
    if os.path.exists(model_path):
        model = load_model(model_path)
        # Ensure DataFrame has required features
        X = df_items[model.feature_names_in_]
        probs = model.predict_proba(X)[:, 1]
        return pd.Series(probs, index=df_items.index)

    # Fallback: manual sigmoid on weighted score
    def manual_prob(row):
        base = calculate_item_score(row.to_dict())
        adj  = base / (1 + risk_volatility)
        return 1 / (1 + np.exp(-(adj - 5)))

    return df_items.apply(manual_prob, axis=1)  # type: ignore