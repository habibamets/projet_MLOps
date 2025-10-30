# Iris classifier - MLOps mini-projet

Ce projet consiste à **prédire l'espèce d'une fleur Iris** (`setosa`, `versicolor`, `virginica`) à partir de **4 caractéristiques numériques** : longueur et largeur du sépal et du pétal.  
Le modèle utilisé est une **régression logistique** entraînée sur le dataset Iris de scikit-learn.

## Etapes clés de la méthodologie

1. **Chargement du dataset Iris** depuis sklearn.datasets
2. **Split train/test** pour evaluer les performances. 
3. **Creation d'un pipleine et recherche d'hyperparametres** : StandardSacler + LogisticRegression pour ensuite faire un GridSearchCV. 
4. **Evaluation du modele**
5. **Sauvegarde du modele entraîné** (`iris_classifier.pkl`) et des métadonnées (`model_metadata.json`). 
6. **Développement d’une API FastAPI** pour exposer un endpoint `/predict` pour faire des predictions. 
7. **Creation d'un test manuel avec pytest** pour vérifier que l’API fonctionne correctement.
8. **Conteneurisation avec Docker** pour faciliter le déploiement, en creant un fichier requirements.txt. 

## Pour lancer l'application localement

### Avec Docker
```bash
# construire l'image 
docker build -t iris-api .
#lancer le conteneur 
docker run -p 8000:8000 iris-api

```
L’API sera accessible sur : http://127.0.0.1:8000 et une documentation interactive Swagger UI : http://127.0.0.1:8000/docs


## Utilisation de l'API 

### Avec Sawgger UI 

Clique sur /predict → Try it out → remplis les valeurs des 4 features → Execute
L'endpoint /predict renvoie une réponse JSON avec la classe prédite et les métadonnées.
 
### Avec curl

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  - d '{"sepal_length":4.4,"sepal_width":3.0,"petal_length":1.3,"petal_width":0.2}' \
```


## Choix techniques 
Création d’un fichier metadata.json pour stocker les informations importantes du modèle (nom, date d’entraînement, hyperparamètres, accuracy, noms des classes). Ce fichier va permettre une meilleure explicabilité et tracabilité des predictions.  
Implémentation d’un endpoint GET / sert à vérifier rapidement si l’API est en ligne.
Gestion des exceptions dans le code pour identifier rapidement les problèmes.
Tests unitaires avec pytest pour s’assurer que l’API fonctionne correctement.


##  Difficultés rencontrées / points à approfondir
- J'ai rencontré des difficultés avec la syntaxe de curl. Elle est diffère entre Windows PowerShell et  Linux, ce qui a provoqué des erreurs lors des tests de l’API.
- Les options avancées de Docker comme `--no-cache-dir` ou la réduction de la taille de l’image nécessitent encore de la pratique.
