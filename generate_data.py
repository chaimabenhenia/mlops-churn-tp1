import pandas as pd  # pandas : pour construire et manipuler notre tableau de données
import numpy as np   # numpy : pour générer des valeurs numériques aléatoires

# Graine aléatoire : point de départ fixe du générateur,
# pour que les mêmes données soient recréées à chaque exécution (reproductibilité).
np.random.seed(42)

n = 500  # nombre de clients fictifs à générer

# Chaque colonne ci-dessous est une FEATURE (donnée d'entrée du futur modèle).
data = pd.DataFrame({
    "age": np.random.randint(18, 70, n),          # âge entre 18 et 69 ans
    "salaire": np.random.randint(1200, 8000, n),  # salaire mensuel simulé
    "abonnement": np.random.choice(["Basique", "Standard", "Premium"], n),  # type d'offre
    "anciennete": np.random.randint(0, 15, n),    # ancienneté en années
    "consommation": np.random.randint(0, 100, n), # score d'usage du service, sur 100
})

# TARGET (colonne à prédire) : churn.
# Règle simplifiée : client peu actif (consommation < 30) ET récent (ancienneté < 2 ans)
# = « à risque de départ ».
data["churn"] = (
    (data["consommation"] < 30) &
    (data["anciennete"] < 2)
).astype(int)  # True/False converti en 1/0

# Sauvegarde dans un fichier CSV (pas encore versionné à ce stade).
data.to_csv("churn_data.csv", index=False)

# Contrôles visuels
print(data.head())
print(f"Taux de churn : {data['churn'].mean():.1%}")