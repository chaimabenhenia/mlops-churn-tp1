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

TP4
Comment désigner officiellement le
modèle à utiliser ?

Avec l'alias champion : models:/churn-model@champion pointe vers la
version choisie, et on peut le déplacer en une ligne

Comment une application peut-elle
utiliser le modèle ?

Par une requête web à l'API : POST /predict avec un JSON, la réponse
contient la prédiction

Que se passe-t-il quand on change de
champion ?

On déplace l'alias et on redémarre l'API : le code de l'API et des
applications clientes ne change pas