Question du TP1
Quel est le meilleur des 3 modèles ? Peux-tu le
prouver ?
Oui — git log montre les 3 commits distincts, chacun avec son
message explicite

Peux-tu redonner exactement le modèle de l'Essai
1 ?
Oui — git checkout <commit> -- churn_model.ipynb

Un camarade peut-il reproduire ton travail sur une autre machine ?
Oui — git clone donne une copie identique du code et des données

TP3
Quel est le meilleur modèle ? Peux-tu le
prouver ?

Oui — l'interface (ou search_runs) trie les runs par f1 ; le résultat
est daté et conservé

Peux-tu redonner exactement le modèle de
l'Essai 1 ?

Oui — mlflow.sklearn.load_model("runs:/<id>/model") recharge le
modèle d'un run précis

Un camarade peut-il reproduire ton travail sur
une autre machine ?

En partie — le code (Git), les paramètres et les versions de
bibliothèques (requirements.txt du run) sont connus ; reste le
problème de l'environnement identique : Docker (TP5-6)