# JEDHA-Projet-2-Kayak

L'équipe marketing de Kayak souhaite développer une application qui aide les utilisateurs à planifier leur prochaine destination de vacances. Cette application utilisera des données en temps réel sur les conditions météorologiques et la disponibilité des hôtels dans divers endroits. En analysant ces variables, l'application fournira des recommandations personnalisées pour les meilleures destinations et hôtels à tout moment.

## Objectifs 🎯
☁️ Utiliser des données météorologiques de différentes ville à partir d'une API.
🏨 Récupérer les données enrichies des hôtels sur le site de booking.
📂 Livrer des résultats incluant des données enrichies dans un DataLake, une intégration avec une base de données, et des cartes interactives présentant les meilleures destinations et hôtels.

## Fonctionnalités ⚙️
- **Analyse Météorologique**: Le script analysera les conditions météorologiques actuelles dans différentes destinations pour suggérer des endroits avec des climats favorables.
- **Disponibilité des Hôtels**: Les données d'hôtels en temps réel seront utilisées pour recommander des hébergements en fonction des préférences, du nombre et de la disponibilité des utilisateurs.
- **Personnalisation**: Les utilisateurs auront la possibilité de personnaliser leurs critères de recherche, tels que le climat préféré, le budget et les dates de voyage, pour des recommandations plus précises.

## Livrables 📬
1. **Données Enrichies**: Un fichier .csv contenant des informations enrichies sur la météo et les hôtels pour chaque ville française sera stocké dans un bucket S3.
2. **Base de Données SQL**: Les données nettoyées du bucket S3 seront intégrées dans une base de données SQL (AWS RDS) pour un accès et une récupération faciles.
3. **Cartes Interactives**: Deux cartes interactives seront créées en utilisant Plotly ou des bibliothèques similaires :
   - **Top 5 des Destinations**: Affichage des cinq meilleures destinations recommandées en fonction des préférences des utilisateurs et de l'analyse des données.
   - **Top 20 des Hôtels**: Présentation des vingt meilleurs hôtels de la région en fonction de la disponibilité, des évaluations des utilisateurs et d'autres facteurs pertinents.

## Structure
```
JEDHA-Projet-2-Kayak/ 
│ 
├── .gitignore 
├── API_city_weather.ipynb 
├── API_key.txt 
├── config.py 
├── config.yaml 
├── DataLake_ETL.ipynb 
├── main.ipynb 
├── main_scrap.py 
├── planning_projet.xlsx 
├── README.md 
├── .git/ 
│   ├── (Git-related files and directories) 
│ 
├── DataLake_DataWarehouse_screen/ 
│   ├── (Image files) 
│ 
├── datas/ 
│   ├── city.csv 
│   ├── Data_Enriched_Weather_Hotel_French_Cities.csv 
│   └── hotel_saved.json 
│ 
├── hotel_crawler/ 
│   ├── (Scrapy project for hotel crawling) 
│ 
└── url_crawler/ 
    ├── (Scrapy project for URL crawling) 
```


### Guide d'Utilisation 

**Prérequis:**
- Python doit être installé sur votre système.
- Assurez-vous d'avoir une connexion Internet.

**Étapes:**

1. **Configuration de l'Environnement:**
   - Exécutez `pip install -r requirements.txt` pour installer les bibliothèques nécessaires.

2. **Clés d'API:**
   - Obtenez les clés d'API pour l'accès aux données météorologiques et aux données de villes.
     - [Données météorologiques](https://api.openweathermap.org)
     - [Données de villes](https://nominatim.openstreetmap.org)

3. **Exécution des Scripts:**
   - Utilisez `API_city_weather.ipynb` pour accéder aux données météorologiques.
   - Lancez `main_scrap.py` pour le web scraping des données sur les URL et les hôtels.
   - Utilisez `main.ipynb` pour accéder aux résultats des deux scripts précédents.

4. **ETL:**
   - Utilisez `DataLake_ETL.ipynb` pour effectuer les opérations d'Extraction, Transformation et Chargement.

5. **Gestion des Données:**
   - Les données sont stockées dans le dossier `datas/`.
   - Utilisez `config.py` pour définir des chemins relatifs plus robustes pour la gestion des données.



## Resultats
<div style="text-align: left;">
  <img src="Result_screen/TOP5.png" style="width:400px; margin-right:30px;" />
  <img src="Result_screen/Hotels.png" style="width:400px;" />
  <img src="Result_screen/City_hotels.png" style="width:400px;" />
  <img src="Result_screen/bayonne.png" style="width:400px;" />
  <img src="Result_screen/hover.png" style="width:400px;" />
</div>


## Aller plus loin

Le projet peut être rendu plus configurable en termes de :
- Type de voyage : nombre de jours de voyage, nombre de personnes, destinations spécifiques choisie par l'utilisateur.
- Préférences météorologiques : préférence pour la pluie, température minimale/maximale, vent fort.
- Préférences d'hébergement : nombre de chambres, note minimale dans une catégorie, équipements spécifiques.
