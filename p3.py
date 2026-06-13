import pandas as pd
import streamlit as st
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.title("flower prediction app ")

st.sidebar.header("Give the Input of the flower")
data=datasets.load_iris()
print(data)
def flower():
    sepal_length=st.sidebar.slider("sepal_length",4.3, 7.9, 5.4)
    sepal_width=st.sidebar.slider("width",2.0, 4.4, 3.4)
    petal_length=st.sidebar.slider("petal_length",1.0, 6.9, 1.3)
    petal_width=st.sidebar.slider("petal_width",0.1, 2.5, 0.2)
    data={
         'sepal_length': sepal_length,
         'sepal_width': sepal_width,
         'petal_length': petal_length,
         'petal_width': petal_width}
    feature=pd.DataFrame(data,index=[0])
    return feature
df=flower()
st.subheader('User Input parameters')
st.write(df)

data=datasets.load_iris()
X=data.data
y=data.target

clf=RandomForestClassifier()
clf.fit(X,y)

pred=clf.predict(df)
pred_pro=clf.predict_proba(df)

st.subheader('class labels')
st.write(data.target_names)

st.subheader('prediction')
st.write(data.target_names[pred[0]])


st.subheader('Prediction Probability')
st.write(pred_pro)


st.subheader('Prediction')
st.write(pred)
print(pred)
