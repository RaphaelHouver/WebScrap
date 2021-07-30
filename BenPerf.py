import requests
from bs4 import BeautifulSoup
from requests.models import stream_decode_response_unicode


#Récupération de la page html
data = requests.get("https://www.leagueofgraphs.com/fr/summoner/euw/ace+champion#championsData-all-queues")

#Attribution du contenu de la page à Soup
soup = BeautifulSoup(data.text, "html.parser")

#Récupération de Victoires/Défaites dans une liste "Streak"
streak = []

for div in soup.find_all("div", {"class":"victoryDefeatText victory"}):
    print(div)
    
    """if int(div.text) > 0:
        streak.append("Victoire")
    else:
        streak.append("Défaite")"""

print(streak)
#Récupération du noms des joueurs de ses games pour voir s'il joue avec Guilleme
names_per_game = []



