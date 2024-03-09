from fastapi import FastAPI, HTTPException
from detoxify import Detoxify
import pandas as pd
from pymongo import MongoClient
import os

app = FastAPI()

# Configuration de la connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['KaisenDT']  # Remplacez 'KaisenDT' par le nom de votre choix
collection = db['toxianl']  # Remplacez 'toxianl' par le nom de votre choix

# Nom du fichier CSV à chercher dans le répertoire courant
NOM_FICHIER_CSV = "reddit_comments.csv"  # Remplacez par le nom réel de votre fichier CSV

@app.post("/process_csv/")
async def process_csv():
    # Chemin complet vers le fichier CSV dans le répertoire courant
    file_path = os.path.join(os.getcwd(), NOM_FICHIER_CSV)
    
    # Vérifier si le fichier existe
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Fichier CSV non trouvé")

    # Lire le fichier CSV
    try:
        data = pd.read_csv(file_path, nrows=15)
        # Nettoyage des données (selon les besoins) cependant, nos données sont déjà dans un forme utilisable pour la suite 
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur de lecture du CSV: {e}")

    # Analyse de toxicité et sauvegarde dans MongoDB
    results = []
    for _, row in data.iterrows():
        scores = Detoxify('original').predict(row['text'])
        result = {
            "text": row['text'],
            "toxicity_scores": {k: float(v) for k, v in scores.items()}  # Conversion en flottants Python
        }
        results.append(result)
        collection.insert_one(result)  

    return {"message": "Données traitées et enregistrées avec succès", "nombre_de_commentaires": len(results)}
