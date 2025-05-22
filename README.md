# Prioxy: Portfolio Prioritization App

**Prioxy** is a Streamlit-based application that helps you:

* **Define custom evaluation criteria**
* **Score and rank** items/projects using weighted scoring (and AHP)
* **Analyze risk** with Monte Carlo simulations
* **Predict success** using a built-in heuristic or an ML model
* **Compare & prioritize** items with an integrated Priority metric

---

## 🚀 Features

* **Multi-page UI**: Navigate via the sidebar to:

  * **Portfolio**: View & export ranked items
  * **Criteria Setup**: Add, weight, import, and export criteria
  * **Item Prioritization**: Enter items manually or via CSV, calculate weighted scores
  * **Analytics**: Run risk simulations, view distributions, and get success probabilities
  * **FAQ**: Built-in help with collapsible explanations
* **Risk Simulations**: Monte Carlo engine with adjustable volatility, simulation count, and optional RNG seed
* **Smart Predictions**: Automatically uses `model.pkl` if present (ML pipeline), else falls back to a transparent sigmoid-based predictor
* **Theme Toggle**: Light & Dark mode switch, with CSS overrides for comfortable viewing
* **Persistence**: Widgets are backed by `st.session_state` so your settings stick across pages and reloads
* **Bulk Import/Export**: CSV upload/download for criteria and items
* **Caching**: Streamlit `@st.cache_data` and `@st.cache_resource` for fast repeated simulations and model loads

---

## ⚙️ Requirements

* Python 3.8+
* [Streamlit](https://streamlit.io/) (>=1.20)
* pandas, numpy, plotly
* scikit-learn, joblib (if using ML model)

Install dependencies via:

```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
Prioxy/
├── pages/                  
│   ├── 🏠_Home.py          
│   ├── 1_Portfolio.py
│   ├── 2_⚙️_Criteria_Setup.py
│   ├── 3_📝_Item_Prioritization.py
│   ├── 4_📊_Analytics.py
│   └── 5_❓_FAQ.py
├── utils/
│   └── functions/
│       ├── criteria.py     # CRUD for criteria in session_state
│       ├── scoring.py      # Add items, calculate weighted scores
│       ├── risk.py         # Monte Carlo simulation
│       ├── predict.py      # Smart predictor (ML or fallback)
│       └── theme.py        # Light/dark CSS toggle
├── data/                   # Placeholder
│   ├── sample_criteria.json
│   └── sample_projects.csv
├── .gitignore
├── requirements.txt
├── config/streamlit_config.toml  # Theme & server configs
└── model.pkl
```

---

## 💡 Usage Tips

* **Adjust volatility & sims** dynamically within each Analytics tab.
* **Use CSV uploads** to batch import criteria or items.
* **Toggle Dark mode** on the left sidebar for low-light environments.
* **FAQ page** has “for-dummies” answers and tooltips on all controls.

---

## 📃 License

This project is released under the **MIT License**. See [LICENSE](LICENSE) for details.

---