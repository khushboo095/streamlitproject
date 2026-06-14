# 🌸 Iris Flower Predictor

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/khushboo-kumari-207249303/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat&logo=streamlit)](https://share.streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)](https://python.org)

A machine learning web app built with **Streamlit** and **scikit-learn** that predicts the species of an Iris flower based on sepal and petal measurements — with a beautiful purple-gradient UI.

---

## 📸 Screenshot

![Iris Flower Predictor App](screenshot.png)



---

## 🚀 Live Demo

> [Click here to try the app](https://share.streamlit.io/your-username/streamlitproject/main/iris_app.py)

---



## 🌼 The 3 Iris Species (Class Labels)

| Class Index | Species    | Description                    |
|-------------|------------|--------------------------------|
| 0           | Setosa     | Small flower, easily separated |
| 1           | Versicolor | Medium, overlaps with others   |
| 2           | Virginica  | Largest petals                 |

These are the **class labels** — the 3 possible outputs the model can predict.

---

## 📐 Input Features

| Slider       | Min  | Max  | Default | What It Measures          |
|--------------|------|------|---------|---------------------------|
| Sepal Length | 4.3  | 7.9  | 5.4 cm  | Length of the outer leaf  |
| Sepal Width  | 2.0  | 4.4  | 3.4 cm  | Width of the outer leaf   |
| Petal Length | 1.0  | 6.9  | 1.3 cm  | Length of the inner petal |
| Petal Width  | 0.1  | 2.5  | 0.2 cm  | Width of the inner petal  |

---

## 🧠 Model Details

| Property         | Value                          |
|------------------|--------------------------------|
| Algorithm        | Random Forest Classifier       |
| Trees            | 100 (`n_estimators=100`)       |
| Random State     | 42                             |
| Dataset          | Iris (built into scikit-learn) |
| Training Samples | 150 rows                       |
| Output           | Class index 0, 1, or 2         |
