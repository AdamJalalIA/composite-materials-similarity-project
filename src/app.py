import streamlit as st
import pandas as pd
import numpy as np
import faiss
import matplotlib.pyplot as plt
import seaborn as sns

# configuration de la page
st.set_page_config(page_title="Exploration de matériaux composites", layout="wide")

#barre latérale
with st.sidebar:
    st.markdown("### Projet de stage - Adam Jalal")
    st.markdown("Recherche et visualisation de matériaux composites via FAISS et Streamlit.")
    st.markdown("---")

def load_data():
    df = pd.read_csv("data/processed/MHK_material_database_cleaned.csv")
    return df.dropna(subset=["Vf, %", "E, GPa (0.1-0.3%)", "Max. % Strain", "Thickness, mm", "Cycles", "Material"])

df = load_data()

# interface en deux onglets
tab_sim, tab_explore = st.tabs(["Recherche de similarité", "Exploration libre"])

# onglet 1 - recherche de similarité
with tab_sim:
    st.title("Recherche de matériaux similaires")

    st.subheader("Définir les propriétés du matériau de référence")
    col1, col2, col3 = st.columns(3)

    with col1:
        vf = st.slider("Taux de fibre Vf (%)", 20.0, 70.0, 50.0)
        thickness = st.slider("Épaisseur (mm)", 0.1, 10.0, 2.0)

    with col2:
        e = st.slider("Module E (GPa)", 10.0, 150.0, 60.0)
        cycles = st.number_input("Nombre de cycles", 1, 1_000_000, 1000)

    with col3:
        strain = st.slider("Déformation maximale (%)", 0.1, 5.0, 1.0)

    if st.button("Lancer la recherche"):
        # données vectorielles pour la recherche
        features = ["Vf, %", "E, GPa (0.1-0.3%)", "Max. % Strain", "Thickness, mm", "Cycles"]
        df_vect = df[features].astype("float32")
        X = df_vect.to_numpy()

        # initialisation et indexation FAISS
        index = faiss.IndexFlatL2(X.shape[1])
        index.add(X)

        # construction de la requête
        x_query = np.array([[vf, e, strain, thickness, cycles]], dtype="float32")
        distances, indices = index.search(x_query, k=5)

        # affichage des résultats
        st.success("Matériaux similaires trouvés :")
        df_results = df.iloc[indices[0]][["Material"] + features].copy()
        st.dataframe(df_results)

        # visualisation
        st.subheader("Positionnement des matériaux similaires")
        fig, ax = plt.subplots(figsize=(8, 6))

        scatter = ax.scatter(
            df_results["E, GPa (0.1-0.3%)"],
            df_results["Max. % Strain"],
            s=df_results["Thickness, mm"] * 50,
            c=df_results["Cycles"],
            cmap="viridis",
            alpha=0.7
        )

        for _, row in df_results.iterrows():
            ax.annotate(row["Material"], (row["E, GPa (0.1-0.3%)"], row["Max. % Strain"]),
                        fontsize=8, alpha=0.7)

        ax.set_xlabel("Module E (GPa)")
        ax.set_ylabel("Déformation max (%)")
        ax.set_title("Matériaux proches selon FAISS")
        plt.colorbar(scatter, label="Nombre de cycles")
        st.pyplot(fig)

# onglet 2 - exploration libre
with tab_explore:
    st.title("Exploration des matériaux composites")

    # filtres dynamiques
    with st.expander("Filtres personnalisés"):
        col1, col2 = st.columns(2)

        with col1:
            vf_range = st.slider("Vf (%)", 20.0, 70.0, (20.0, 70.0))
            e_range = st.slider("Module E (GPa)", 10.0, 150.0, (10.0, 150.0))

        with col2:
            strain_range = st.slider("Déformation max (%)", 0.1, 5.0, (0.1, 5.0))
            thickness_range = st.slider("Épaisseur (mm)", 0.1, 10.0, (0.1, 10.0))

    # application des filtres
    filtered = df[
        (df["Vf, %"].between(*vf_range)) &
        (df["E, GPa (0.1-0.3%)"].between(*e_range)) &
        (df["Max. % Strain"].between(*strain_range)) &
        (df["Thickness, mm"].between(*thickness_range))
    ]

    st.write(f"{len(filtered)} matériaux correspondent aux critères sélectionnés.")
    st.dataframe(filtered[["Material", "Vf, %", "E, GPa (0.1-0.3%)", "Max. % Strain", "Thickness, mm", "Cycles"]])

    # graphique d’exploration
    st.subheader("Résistance en fonction du taux de fibre")
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    ax2.scatter(
        filtered["Vf, %"],
        filtered["Max. Stress, MPa"],
        alpha=0.6,
        c=filtered["E, GPa (0.1-0.3%)"],
        cmap="plasma"
    )
    ax2.set_xlabel("Vf (%)")
    ax2.set_ylabel("Contrainte maximale (MPa)")
    ax2.set_title("Visualisation des performances mécaniques")
    st.pyplot(fig2)
