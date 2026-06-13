import pandas as pd
import streamlit as st
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
 
st.set_page_config(page_title="Iris Flower Predictor", page_icon="🌸", layout="wide")
 
st.markdown("""
    <style>
        /* ── Global font & background ── */
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
        }
 
        /* ── Main page background ── */
        .stApp {
            background: linear-gradient(135deg, #f0f4ff 0%, #faf0fb 100%);
        }
 
        /* ── Title styling ── */
        h1 {
            color: #4a2d82;
            font-size: 2.4rem !important;
            font-weight: 700 !important;
            letter-spacing: -0.5px;
            margin-bottom: 0.2rem !important;
        }
 
        /* ── Sidebar ── */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #2d1b69 0%, #4a2d82 100%);
            border-right: none;
        }
        [data-testid="stSidebar"] * {
            color: #e8dff8 !important;
        }
        [data-testid="stSidebar"] .stSlider > label {
            font-weight: 600;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #c8b8f0 !important;
        }
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            color: #ffffff !important;
        }
 
        /* ── Slider accent color ── */
        [data-testid="stSlider"] [data-testid="stThumbValue"] {
            background-color: #7c4dff;
            color: white;
            border-radius: 6px;
            padding: 2px 6px;
            font-size: 0.8rem;
        }
 
        /* ── Metric / dataframe cards ── */
        [data-testid="stMetric"] {
            background: white;
            border-radius: 12px;
            padding: 1rem 1.25rem;
            box-shadow: 0 2px 12px rgba(74, 45, 130, 0.08);
            border: 1px solid #e8dff8;
        }
        [data-testid="stMetricLabel"] {
            color: #8b7bb5 !important;
            font-size: 0.78rem !important;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }
        [data-testid="stMetricValue"] {
            color: #4a2d82 !important;
            font-weight: 700 !important;
        }
 
        /* ── Subheaders ── */
        h2, h3 {
            color: #4a2d82 !important;
            font-weight: 600 !important;
            margin-top: 1.5rem !important;
        }
 
        /* ── DataFrames ── */
        [data-testid="stDataFrame"] > div {
            border-radius: 10px;
            overflow: hidden;
            border: 1px solid #e8dff8;
            box-shadow: 0 2px 10px rgba(74, 45, 130, 0.06);
        }
 
        /* ── Prediction badge ── */
        .prediction-badge {
            display: inline-block;
            background: linear-gradient(135deg, #7c4dff, #e040fb);
            color: white;
            font-size: 1.5rem;
            font-weight: 700;
            padding: 0.6rem 1.8rem;
            border-radius: 50px;
            margin: 0.5rem 0 1rem;
            letter-spacing: 0.03em;
            box-shadow: 0 4px 15px rgba(124, 77, 255, 0.35);
        }
 
        /* ── Info box ── */
        .info-box {
            background: white;
            border-left: 4px solid #7c4dff;
            border-radius: 0 10px 10px 0;
            padding: 1rem 1.25rem;
            margin: 0.75rem 0;
            box-shadow: 0 2px 8px rgba(74, 45, 130, 0.07);
            color: #3a2060;
        }
        .info-box p { margin: 0; font-size: 0.95rem; }
 
        /* ── Probability table ── */
        .prob-row {
            display: flex;
            align-items: center;
            gap: 12px;
            margin: 0.5rem 0;
        }
        .prob-label {
            width: 120px;
            font-size: 0.88rem;
            color: #4a2d82;
            font-weight: 600;
        }
        .prob-bar-wrap {
            flex: 1;
            background: #ede8f8;
            border-radius: 20px;
            height: 14px;
            overflow: hidden;
        }
        .prob-bar {
            height: 100%;
            border-radius: 20px;
            background: linear-gradient(90deg, #7c4dff, #e040fb);
            transition: width 0.4s ease;
        }
        .prob-value {
            width: 48px;
            font-size: 0.85rem;
            color: #7c4dff;
            font-weight: 700;
            text-align: right;
        }
 
        /* ── Divider ── */
        hr {
            border: none;
            border-top: 1px solid #e8dff8;
            margin: 1.5rem 0;
        }
 
        /* ── Footer ── */
        .footer {
            text-align: center;
            color: #a898cc;
            font-size: 0.78rem;
            margin-top: 3rem;
            padding-top: 1rem;
            border-top: 1px solid #e8dff8;
        }
    </style>
""", unsafe_allow_html=True)
 
 
# ── Sidebar inputs ──────────────────────────────────────────────────────────
st.sidebar.markdown("## 🌸 Flower Inputs")
st.sidebar.markdown("Adjust the measurements below:")
 
def get_user_input():
    sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.3, 7.9, 5.4)
    sepal_width  = st.sidebar.slider("Sepal Width (cm)",  2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider("Petal Length (cm)", 1.0, 6.9, 1.3)
    petal_width  = st.sidebar.slider("Petal Width (cm)",  0.1, 2.5, 0.2)
    return pd.DataFrame({
        "sepal_length": [sepal_length],
        "sepal_width":  [sepal_width],
        "petal_length": [petal_length],
        "petal_width":  [petal_width],
    })
 
df = get_user_input()
 
 
# ── Train model ─────────────────────────────────────────────────────────────
iris = datasets.load_iris()
clf  = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(iris.data, iris.target)
 
pred     = clf.predict(df)
pred_pro = clf.predict_proba(df)[0]
species  = iris.target_names
 
 
# ── Main content ─────────────────────────────────────────────────────────────
st.title("🌸 Iris Flower Predictor")
st.markdown(
    "<div class='info-box'><p>Enter the flower's sepal and petal measurements "
    "in the sidebar. The Random Forest model will predict the species instantly.</p></div>",
    unsafe_allow_html=True,
)
 
st.markdown("---")
 
# Input parameters
st.subheader("📐 Your Input Parameters")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Sepal Length", f"{df['sepal_length'][0]:.1f} cm")
col2.metric("Sepal Width",  f"{df['sepal_width'][0]:.1f} cm")
col3.metric("Petal Length", f"{df['petal_length'][0]:.1f} cm")
col4.metric("Petal Width",  f"{df['petal_width'][0]:.1f} cm")
 
st.markdown("---")
 
# Prediction
st.subheader("🔮 Predicted Species")
st.markdown(
    f"<div class='prediction-badge'>{species[pred[0]].capitalize()}</div>",
    unsafe_allow_html=True,
)
 
st.markdown("---")
 
# Probability bars
st.subheader("📊 Prediction Probabilities")
for i, (sp, prob) in enumerate(zip(species, pred_pro)):
    pct = prob * 100
    st.markdown(f"""
        <div class="prob-row">
            <div class="prob-label">{sp.capitalize()}</div>
            <div class="prob-bar-wrap">
                <div class="prob-bar" style="width:{pct:.1f}%"></div>
            </div>
            <div class="prob-value">{pct:.1f}%</div>
        </div>
    """, unsafe_allow_html=True)
 
st.markdown("---")
 
# Class labels
st.subheader("🏷️ All Class Labels")
st.dataframe(
    pd.DataFrame({"Class Index": [0, 1, 2], "Species": list(species)}),
    use_container_width=True,
    hide_index=True,
)
 
st.markdown(
    "<div class='footer'>Iris Flower Predictor · Powered by scikit-learn RandomForestClassifier</div>",
    unsafe_allow_html=True,
)
 