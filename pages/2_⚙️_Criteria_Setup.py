import streamlit as st
import pandas as pd
from utils.functions.criteria import get_criteria, add_criterion, remove_criterion
from utils.functions.theme import apply_theme

# Configure the page
st.set_page_config(
    page_title="Portfolio Prioritization App",
    page_icon="⚙️",
    layout="wide"
)

# Apply light/dark theme toggle
apply_theme()

st.title("⚙️ Criteria Setup")
st.markdown("Define and weight the factors you'll use to score your items.")

st.divider()

# --- Bulk Import: Criteria CSV ---
uploaded_criteria = st.file_uploader(
    label="Upload criteria CSV",
    type=["csv"],
    help="CSV file must have columns: 'name' and 'weight'.",
    key="crit_upload"
)
if uploaded_criteria is not None:
    df_crit = pd.read_csv(uploaded_criteria)
    count = 0
    for _, row in df_crit.iterrows():
        name = str(row.get('name', '')).strip()
        weight = float(row.get('weight', 0.0))
        if name:
            add_criterion({'name': name, 'weight': weight})
            count += 1
    st.success(f"Imported {count} criteria from CSV.")

st.divider()

# --- Manual Add / Edit ---
st.subheader("Add a New Criterion")
with st.form("crit_form", clear_on_submit=True):
    col1, col2 = st.columns([2,1])
    with col1:
        new_name = st.text_input(
            label="Criterion Name",
            key="new_crit_name"
        )
    with col2:
        new_weight = st.slider(
            label="Weight",
            min_value=0.0, max_value=1.0,
            value=st.session_state.get("new_weight", 0.1),
            step=0.05,
            key="new_weight",
            help="Set how important this criterion is. All weights will be normalized."
        )
    submitted = st.form_submit_button("Add Criterion")
    if submitted:
        if new_name:
            add_criterion({'name': new_name, 'weight': new_weight})
            st.success(f"Added criterion '{new_name}'.")
        else:
            st.error("Please enter a criterion name.")

st.divider()

# --- List & Remove ---
criteria = get_criteria()
if criteria:
    st.subheader("Current Criteria")
    for crit in criteria:
        col1, col2 = st.columns([4,1])
        col1.write(f"**{crit['name']}** — weight: {crit['weight']:.2f}")
        if col2.button(
            label="Remove",
            key=f"rm_{crit['name']}"
        ):
            remove_criterion(crit['name'])
            st.experimental_rerun()

# --- Export Criteria as CSV ---
if criteria:
    df_export = pd.DataFrame(criteria)
    csv_data = df_export.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download criteria as CSV",
        data=csv_data,
        file_name="criteria_export.csv",
        mime="text/csv",
        help="Download current list of criteria and weights."
    )

# Footer
st.divider()
st.caption("© 2025 David Peña. All rights reserved.")