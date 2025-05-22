import streamlit as st
import pandas as pd
from utils.functions.scoring import get_items, add_item, remove_item, get_criteria, calculate_item_score
from utils.functions.theme import apply_theme

# Configure the page
st.set_page_config(
    page_title="Portfolio Prioritization App",
    page_icon="📝",
    layout="wide"
)

# Apply light/dark theme toggle
apply_theme()

st.title("📝 Item Prioritization")
st.markdown("Evaluate your items using weighted scoring based on your defined criteria.")

# --- Bulk Import: Items CSV ---
uploaded_items = st.file_uploader(
    label="Upload items CSV",
    type=["csv"],
    help="CSV must include a 'name' column and one column per criterion.",
    key="items_upload"
)
if uploaded_items is not None:
    df_csv = pd.read_csv(uploaded_items)
    imported = 0
    for _, row in df_csv.iterrows():
        item = row.to_dict()
        name = item.get('name', '').strip()
        if name:
            add_item(item)
            imported += 1
    st.success(f"Imported {imported} items from CSV.")

# --- Manual Add ---
criteria = get_criteria()
if not criteria:
    st.info("Please add evaluation criteria first on the 'Criteria Setup' page.")
else:
    st.subheader("Add a New Item")
    with st.form("item_form", clear_on_submit=True):
        item_name = st.text_input(
            label="Item Name",
            key="new_item_name"
        )
        scores = {}
        for crit in criteria:
            key_slider = f"score_{crit['name']}"
            scores[crit['name']] = st.slider(
                label=f"Score for {crit['name']}",
                min_value=0, max_value=10,
                value=5,
                key=key_slider
            )
        submitted = st.form_submit_button("Add Item")
        if submitted:
            if item_name:
                add_item({'name': item_name, **scores})
                st.success(f"Added item '{item_name}'.")
            else:
                st.error("Please enter an item name.")

    # --- List & Remove ---
    items = get_items()
    if items:
        st.subheader("Current Items & Weighted Scores")
        df_items = pd.DataFrame(items)
        df_items['Weighted Score'] = df_items.apply(
            lambda r: calculate_item_score(r.to_dict()), axis=1
        )
        for idx, row in df_items.iterrows():
            col1, col2 = st.columns([3,1])
            with col1:
                st.write(f"**{row['name']}** — Score: {row['Weighted Score']:.2f}")
            with col2:
                if st.button("Remove", key=f"remove_{idx}"):
                    remove_item(idx)
                    st.experimental_rerun()

        # --- Export Items as CSV ---
        export_df = df_items.drop(columns=['Weighted Score'])
        csv_bytes = export_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download items as CSV",
            data=csv_bytes,
            file_name="items_export.csv",
            mime="text/csv",
            help="Download your current items and their entered values."
        )
    else:
        st.info("No items added yet. Use the form above or upload a CSV file.")

# Footer
st.divider()
st.caption("© 2025 David Peña. All rights reserved.")