import pandas as pd
import seaborn as sns
#How to run strimlit app in Anaconda prompt
import streamlit as st
st.write("Hi! Vous êtes sur la page web de Jacques de Lavernette")

st.title("Welcome to the wine paradise ! We will study the wine in this website")
st. subheader("That's very intresting")
a = st.text_input("what's your name ?")
st.write("What's up ",a,"?")
#age
age = st.slider("What's your age ?", 0, 125, 25)
st.write(f"Vous avez {age} ans.")
import numpy as np

# Choix dans une liste deroulante (dans la sidebar)
graph_type = st.sidebar.selectbox("lil choose your type of graphic ? :", ["Ligne", "Barres", "Aucun"])

st.write(f"Vous avez choisi le type de graphique : {graph_type}")
#3 UPLOAD CSV FILE
uploaded_file = st.file_uploader("Téléchargez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.write("Voici un aperçu de votre fichier :")
    st.dataframe(df.head())


#4 Affichage du graphique en fonction du type choisi
    if graph_type == "Ligne":
        st.line_chart(df)
    elif graph_type == "Barres":
        st.bar_chart(df)
    else:
        st.write("Aucun graphique selectionné.")



# Checkbox
if st.checkbox("show the correlation"):
    #To plot the heatmap of correlations:
    print(sns.heatmap(df.corr(), cmap="YlGnBu", annot= True ))
