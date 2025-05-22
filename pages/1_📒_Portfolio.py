import streamlit as st
import pandas as pd
from utils.functions.scoring import get_items, calculate_item_score
from utils.functions.predict import predict_success
from utils.functions.theme import apply_theme

# Configure the page
st.set_page_config(
    page_title="Portfolio Prioritization App",
    page_icon="🚀",
    layout="wide"
)

# Apply light/dark theme toggle
apply_theme()

st.title("📒 Portfolio Overview")
st.markdown("Browse and rank all your items by combining their score and predicted success into a single Priority metric.")

st.divider()

col1,_=st.columns([1,2])
with col1:
    # Risk volatility slider
    st.write("#### Risk Volatility")
    risk_vol_prio = st.slider(
        "Risk Volatility for Priority Calculation",
        min_value=0.0,
        max_value=1.0,
        value=st.session_state.get("risk_vol_prio", 0.1),
        step=0.05,
        key="risk_vol_prio",
        help=(
            "Controls uncertainty in the success prediction fallback. "
            "0 = No uncertainty; 1 = High uncertainty; e.g., 0.1 = ±10% swings."
        )
    )

st.write("\n")
st.write("\n")

# Fetch items
items = get_items()
if not items:
    st.info("No items found. Please add items on the 'Item Prioritization' page.")
else:
    # Build DataFrame of items
    df = pd.DataFrame(items)
    # Calculate base scores
    df['Base Score'] = df.apply(lambda row: calculate_item_score(row.to_dict()), axis=1)

    # Predict success probabilities (uses ML model if available, else fallback)
    with st.spinner("Calculating success probabilities..."):
        df['Success Prob'] = predict_success(df, risk_vol_prio)
    df['Success %'] = (df['Success Prob'] * 100).round(2)

    # Compute final priority metric
    df['Priority'] = (df['Base Score'] * df['Success Prob']).round(2)

    # Sort and display
    df_sorted = df.sort_values('Priority', ascending=False)
    st.subheader("Priority Ranking")
    st.dataframe(
        df_sorted[
            ['name', 'Base Score', 'Success %', 'Priority']
        ].rename(
            columns={
                'name': 'Item',
            }
        )
    )

# Footer
st.divider()
st.caption("© 2025 David Peña. All rights reserved.")