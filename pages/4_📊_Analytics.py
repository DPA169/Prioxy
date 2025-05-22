import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils.functions.scoring import get_items, calculate_item_score
from utils.functions.risk import simulate_item_risk
from utils.functions.predict import predict_success
from utils.functions.theme import apply_theme

# Configure the page
st.set_page_config(
    page_title="Portfolio Prioritization App",
    page_icon="📊",
    layout="wide"
)

# Apply light/dark theme toggle
apply_theme()

st.title("📊 Item Risk & Success Analysis")

# Create tabs for different analyses
tab_risk, tab_success, tab_priority = st.tabs(["Risk", "Success", "Priority"])

# ------------------
# TAB 1: Risk Analysis (inputs inside)
# ------------------
with tab_risk:
    st.header("Risk Analysis")
    st.markdown(
        "Run Monte Carlo simulations to see how your item scores might vary under uncertainty."
    )

    col1, col2, col3, _ = st.columns(4)

    with col1:
        # Inputs inside the tab
        risk_vol = st.slider(
            label="Risk Volatility",
            min_value=0.0, max_value=1.0,
            value=st.session_state.get("risk_vol", 0.1),
            step=0.05,
            key="risk_vol",
            help="More volatility means wider swings around the base score."
        )
    
    with col2:
        n_sim = st.number_input(
            label="Number of Simulations",
            min_value=100, max_value=10000,
            value=st.session_state.get("n_sim", 1000), step=100,
            key="n_sim",
            help="More runs = smoother results but longer compute time."
        )
    
    with col3:
            seed = st.number_input(
            label="Random Seed",
            min_value=0, max_value=999999,
            value=st.session_state.get("seed", 123), key="seed",
            help="Use a fixed seed for reproducible simulations."
        )

    items = get_items()
    if not items:
        st.info("No items found. Please add items on the 'Item Prioritization' page.")
    else:
        # Prepare data frame
        df = pd.DataFrame(items)
        df['Base Score'] = df.apply(lambda r: calculate_item_score(r.to_dict()), axis=1)

        # Run simulations
        with st.spinner("Running Monte Carlo simulations..."):
            outcomes = simulate_item_risk(
                df['Base Score'].tolist(), risk_vol, n_sim, seed or None
            )

        df['Sim Mean'] = outcomes.mean(axis=1)
        df['Sim Std']  = outcomes.std(axis=1)

        # Summary chart
        st.subheader("Simulation Summary")
        fig_summary = px.bar(
            df, x='name', y='Sim Mean', error_y='Sim Std',
            labels={'name': 'Item', 'Sim Mean': 'Mean Score'},
            title="Mean and Std Dev of Simulated Scores"
        )
        st.plotly_chart(fig_summary, use_container_width=True)

        # Detailed mini charts
        st.subheader("Detailed Item View")
        for idx, row in df.iterrows():
            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown(f"**{row['name']}**")
                st.write(f"Base Score: {row['Base Score']:.2f}")
                st.write(f"Mean: {row['Sim Mean']:.2f}")
                st.write(f"Std Dev: {row['Sim Std']:.2f}")
            with col2:
                fig_mini = px.histogram(
                    outcomes[idx], nbins=20,
                    labels={'value': 'Score'},
                )
                fig_mini.update_layout(
                    margin=dict(l=0, r=0, t=0, b=0),
                    height=150,
                    xaxis_title=None,
                    yaxis_title=None
                )
                st.plotly_chart(fig_mini, use_container_width=True)
                st.write("\n")
                st.write("\n")

# ------------------
# TAB 2: Success Prediction (inputs inside)
# ------------------
with tab_success:
    st.header("Success Prediction")
    st.markdown(
        "Get a probability of success for each item, based on historical data if available, or fallback logic otherwise."
    )

    col1, col2, _, _ = st.columns(4)

    with col1:
        risk_vol_pred = st.slider(
            label="Risk Volatility for Prediction",
            min_value=0.0, max_value=1.0,
            value=st.session_state.get("risk_vol_pred", 0.1),
            step=0.05,
            key="risk_vol_pred",
            help="Affects fallback method when no model is found."
        )
    with col2:
        seed_pred = st.number_input(
            label="Random Seed (optional)",
            min_value=0, max_value=999999,
            value=st.session_state.get("seed_pred", 123), key="seed_pred",
            help="Use a fixed seed for reproducible predictions."
        )

    items = get_items()
    if not items:
        st.info("No items found. Please add items on the 'Item Prioritization' page.")
    else:
        df = pd.DataFrame(items)
        with st.spinner("Calculating success probabilities..."):
            df['Success Prob'] = predict_success(df, risk_vol_pred, seed_pred or None)
        df['Success %'] = (df['Success Prob'] * 100).round(2)

        st.subheader("Predicted Success Chances")
        st.table(
            df[['name', 'Success %']].rename(columns={'name': 'Item'})
        )

        fig2 = px.bar(
            df, x='name', y='Success %',
            title="Item Success Probability (%)",
            labels={'name': 'Item'}
        )
        st.plotly_chart(fig2, use_container_width=True)

# ------------------
# TAB 3: Priority Overview (inputs inside)
# ------------------
with tab_priority:
    st.header("Priority Overview")
    st.markdown(
        "Rank all items by combining their score and success chance into a single Priority metric."
    )

    col1, col2, col3, _ = st.columns(4)

    with col1:
        risk_vol_prio = st.slider(
            label="Risk Volatility for Priority",
            min_value=0.0, max_value=1.0,
            value=st.session_state.get("risk_vol_prio", 0.1),
            step=0.05,
            key="risk_vol_prio",
            help="Affects fallback prediction used in priority calculation."
        )
    
    with col2:
        seed_prio = st.number_input(
            label="Random Seed (optional)",
            min_value=0, max_value=999999,
            value=st.session_state.get("seed_prio", 123), key="seed_prio",
            help="Use a fixed seed for reproducible priority rankings."
        )

    items = get_items()
    if not items:
        st.info("No items found. Please add items on the 'Item Prioritization' page.")
    else:
        df = pd.DataFrame(items)
        df['Base Score'] = df.apply(lambda r: calculate_item_score(r.to_dict()), axis=1)
        with st.spinner("Calculating success probabilities for priority..."):
            df['Success Prob'] = predict_success(df, risk_vol_prio, seed_prio or None)

        df['Priority'] = (df['Base Score'] * df['Success Prob']).round(2)
        df['Success %'] = (df['Success Prob'] * 100).round(2)

        df_sorted = df.sort_values('Priority', ascending=False)
        st.subheader("Item Ranking")
        st.dataframe(
            df_sorted[['name', 'Base Score', 'Success %', 'Priority']]
            .rename(columns={'name': 'Item'})
        )

# Footer
st.divider()
st.caption("© 2025 David Peña. All rights reserved.")