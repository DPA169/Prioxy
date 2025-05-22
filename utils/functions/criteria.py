import streamlit as st
from typing import List, Dict

# Initialize criteria list in session state

def init_criteria():
    if "criteria" not in st.session_state:
        st.session_state["criteria"] = []


def add_criterion(criterion: Dict[str, float]) -> List[Dict[str, float]]:
    """
    Add a new criterion dict with 'name' and 'weight'.
    """
    init_criteria()
    st.session_state["criteria"].append(criterion)
    return st.session_state["criteria"]


def remove_criterion(name: str) -> List[Dict[str, float]]:
    """
    Remove a criterion by its name.
    """
    init_criteria()
    st.session_state["criteria"] = [c for c in st.session_state["criteria"] if c["name"] != name]
    return st.session_state["criteria"]


def get_criteria() -> List[Dict[str, float]]:
    """Retrieve the current list of criteria."""
    init_criteria()
    return st.session_state["criteria"]


def get_total_weight() -> float:
    return sum(c["weight"] for c in get_criteria())


def get_remaining_weight() -> float:
    return max(0.0, 1.0 - get_total_weight())