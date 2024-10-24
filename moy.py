import streamlit as st

# Fonction pour calculer la moyenne avec vérification des contraintes
def calculer_moyenne(nombres):
    try:
        # Vérifier si la liste est vide
        if len(nombres) == 0:
            st.error("La liste est vide, veuillez entrer au moins un nombre.")
            return None
        
        # Conversion en liste de float
        nombres = [float(x) for x in nombres]
        
        # Calcul de la moyenne
        somme = sum(nombres)
        moyenne = somme / len(nombres)
        
        return moyenne
    
    except ValueError:
        st.error("Veuillez entrer uniquement des nombres valides.")
        return None

# Titre de l'application
st.title("Application de Calcul de Moyenne")

# Input: l'utilisateur entre des nombres séparés par des virgules
nombres_str = st.text_input("Entrez une liste de nombres séparés par des virgules :", "")

# Bouton pour calculer la moyenne
if st.button("Calculer la moyenne"):
    # Séparer les nombres par des virgules et enlever les espaces
    nombres = [x.strip() for x in nombres_str.split(",") if x.strip()]
    
    # Calculer la moyenne
    moyenne = calculer_moyenne(nombres)
    
    # Affichage du résultat
    if moyenne is not None:
        st.success(f"La moyenne des nombres {nombres} est : {moyenne:.2f}")
