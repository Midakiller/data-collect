# collect.py
import csv
import os  # Nécessaire pour vérifier si le fichier existe
from datetime import datetime, timezone, timedelta
from api_utils import get_parkings_voiture, get_parkings_velo

def collect_data():
    tz_gmt1 = timezone(timedelta(hours=1))
    date = datetime.now(tz_gmt1).strftime('%Y-%m-%d %H:%M:%S')
    # --- Collecte VOITURES ---
    csv_voiture = "parkings_voiture.csv"
    try:
        parkings_voiture = get_parkings_voiture()
        
        # On vérifie si le fichier existe déjà pour savoir s'il faut mettre les titres
        file_exists = os.path.isfile(csv_voiture)
        
        with open(csv_voiture, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            
            # Si le fichier est nouveau, on écrit l'en-tête
            if not file_exists:
                writer.writerow(["Date", "Nom", "Disponibles", "Total"])
            
            for p in parkings_voiture:
                nom = p["name"]["value"]
                dispo = p["availableSpotNumber"]["value"]
                total = p["totalSpotNumber"]["value"]
                writer.writerow([date, nom, dispo, total])
                
        print(f"[{date}] Données voitures sauvegardées.")
    except Exception as e:
        print(f"[{date}] Erreur collecte voitures :", e)

    # --- Collecte VÉLOS ---
    csv_velo = "parkings_velo.csv"
    try:
        parkings_velo = get_parkings_velo()
        
        # On vérifie si le fichier existe déjà
        file_exists = os.path.isfile(csv_velo)
        
        with open(csv_velo, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            
            # Si le fichier est nouveau, on écrit l'en-tête
            if not file_exists:
                writer.writerow(["Date", "Adresse", "Vélos Dispo", "Places Total"])
            
            for s in parkings_velo:
                # Attention : vérifiez bien la structure de votre JSON ici
                nom = s["address"]["value"]["streetAddress"]
                dispo = s["availableBikeNumber"]["value"]
                total = s["totalSlotNumber"]["value"]
                writer.writerow([date, nom, dispo, total])
                
        print(f"[{date}] Données vélos sauvegardées.")
    except Exception as e:
        print(f"[{date}] Erreur collecte vélos :", e)

if __name__ == "__main__":
    collect_data()
