from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['KaisenDT']  # Le nom de votre base de données
collection = db['toxianl']  # Le nom de votre collection

# Récupération et affichage de tous les documents de la collection
documents = collection.find()
for document in documents:
    print(document)