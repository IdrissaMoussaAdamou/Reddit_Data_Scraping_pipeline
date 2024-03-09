import praw
import pandas as pd
import datetime as dt

# Configuration de l'accès à Reddit
reddit = praw.Reddit(user_agent=True, 
                     client_id='st05beDxBFujTu7okNsGcA', 
                     client_secret='EJuUfQ6fvvXoliNYwatIqThgPhNtOw', 
                     username='CriticismHot3499', 
                     password='Kaizer741')

# Vérification de la connexion à l'API
try:
    reddit.user.me()
    print("Connecté à Reddit en tant que: {}".format(reddit.user.me()))
except Exception as e:
    print("Erreur lors de la connexion à Reddit: ", e)
    exit()

url = "https://www.reddit.com/r/football/comments/1b0e3h4/if_you_could_what_rules_would_you_change/"
submission = reddit.submission(url=url)

# Expander tous les commentaires
submission.comments.replace_more(limit=None)
comment_list = []

# Parcourir les commentaires et récupérer les informations
for comment in submission.comments.list():
    comment_data = {
        "author": comment.author.name if comment.author else "Deleted",
        "date": dt.datetime.fromtimestamp(comment.created),
        "text": comment.body
    }
    comment_list.append(comment_data)

# Créer un DataFrame à partir de la liste des commentaires
df_comments = pd.DataFrame(comment_list)

# Sauvegarder le DataFrame en fichier CSV
csv_file_path = "reddit_comments.csv"
df_comments.to_csv(csv_file_path, index=False)
print(f"Les commentaires ont été sauvegardés dans le fichier {csv_file_path}")
