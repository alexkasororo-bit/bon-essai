import streamlit as st

# Titre de l'application
st.title("Calcul du périmètre et de la surface d'un rectangle")

# Demander à l'utilisateur d'entrer la longueur et la largeur
longueur = st.number_input("Entrez la longueur du rectangle (en cm) :", min_value=0.1, step=0.1)
largeur = st.number_input("Entrez la largeur du rectangle (en cm) :", min_value=0.1, step=0.1)

# Calculs du périmètre et de la surface
perimetre = 2 * (longueur + largeur)
surface = longueur * largeur

# Afficher les résultats
st.write(f"Le périmètre du rectangle est : {perimetre:.2f} cm")
st.write(f"La surface du rectangle est : {surface:.2f} cm²")
