🌸 Iris Flower Predictor

A machine learning web app built with Streamlit and scikit-learn that predicts the species of an Iris flower based on sepal and petal measurements — with a beautiful purple-gradient UI.


📸 What It Does


You move sliders → enter flower measurements
The app runs a Random Forest model
It predicts which of 3 Iris species it is
Shows prediction + probability bars instantly



🌼 The 3 Iris Species (Class Labels)

Class IndexSpeciesMeaning0SetosaSmall flower, easily separated1VersicolorMedium, overlaps with others2VirginicaLargest petals

These are called class labels — the 3 possible outputs the model can predict.

The model always picks one of these 3. It cannot predict anything outside them.


📐 Input Features (What You Enter)

SliderMinMaxDefaultWhat It MeasuresSepal Length4.37.95.4 cmLength of the outer leafSepal Width2.04.43.4 cmWidth of the outer leafPetal Length1.06.91.3 cmLength of the inner petalPetal Width0.12.50.2 cmWidth of the inner petal


🧠 Model Details

PropertyValueAlgorithmRandom Forest ClassifierTrees100 (n_estimators=100)Random State42 (for reproducibility)DatasetIris (built into scikit-learn)Training Samples150 rowsOutputClass index 0, 1, or 2

Project Structure
iris-flower-predictor/
│
├── iris_app.py          # Main app (loads style.css)
├── style.css            # All CSS styling
├── requirements.txt
└── README.md