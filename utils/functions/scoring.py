import streamlit as st
from typing import List, Dict, Any
from utils.functions.criteria import get_criteria

# Initialize items list in session state

def init_items():
    if "items" not in st.session_state:
        st.session_state["items"] = []


def add_item(item: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Add an item dict. Expects keys: 'name' and either nested 'scores' or flat criteria columns.
    """
    init_items()
    name = item.get("name", "").strip()
    # Extract scores dict
    if isinstance(item.get("scores"), dict):
        scores = item["scores"]
    else:
        scores = {k: v for k, v in item.items() if k != "name"}
    st.session_state["items"].append({"name": name, "scores": scores})
    return st.session_state["items"]


def calculate_item_score(item: Dict[str, Any]) -> float:
    """
    Compute weighted score: sum(score * weight) / total weight.
    """
    criteria = get_criteria()
    # Determine scores dict
    scores = item.get("scores") if isinstance(item.get("scores"), dict) else {k: v for k, v in item.items() if k != "name"}
    total_score = 0.0
    total_weight = 0.0
    for crit in criteria:
        w = crit["weight"]
        s = scores.get(crit["name"], 0)
        total_score += s * w
        total_weight += w
    return (total_score / total_weight) if total_weight else 0.0


def get_items() -> List[Dict[str, Any]]:
    init_items()
    return st.session_state["items"]


def remove_item(index: int) -> List[Dict[str, Any]]:
    init_items()
    try:
        st.session_state["items"].pop(index)
    except IndexError:
        st.error("Invalid item index.")
    return st.session_state["items"]