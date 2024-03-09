# Reddit_Data_Scraping_pipeline
Reddit Data Scraping pipeline and post toxicity classification

## Détails du projet: 

- Tout d'abord, on a créer un premier script qui scrappe les données (Commentaires sur un Post) sur Reddit puis nous retourne les données dans un fichier csv:
    * Vous trouverez le code source dans scraper2.py.
    * Pour exécuter ce script vous devrez créer une application développeur sur Reddit pour obtenir les clés d'accès de Reddit.
- Puis on a creer une api avec FastAPI que vous trouverez dans main.py qui se charge de :
    * Récupérer les données scrapper
    * Importer le modèle de classification de toxicité "detoxify" (https://github.com/unitaryai/detoxify).
    * Passer ces donner au modèle et récupérer un tableau avec le niveau de toxicité de chaque commentaire.
    * Enregistrer ces données sur MongoDB.
-  Enfin, un script pour tester l'enregistrement des résultats finaux sur MangoDB dans le fichier verifiingest.py
-  Dans requirements.txt il y a les différentes dépendances.
