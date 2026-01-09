# collect.py
import csv
from datetime import datetime
from api_utils import get_parkings_voiture, get_parkings_velo
import time

def collect_data():
    date = datetime.now().isoformat()

    # Collecte voitures
    try:
        parkings_voiture = get_parkings_voiture()
        with open("parkings_voiture.csv", "a", newline="") as f:
            writer = csv.writer(f)
            for p in parkings_voiture:
                nom = p["name"]["value"]
                dispo = p["availableSpotNumber"]["value"]
                total = p["totalSpotNumber"]["value"]
                writer.writerow([date, nom, dispo, total])
        print(f"[{date}] Données voitures collectées avec succès.")
    except Exception as e:
        print(f"[{date}] Erreur collecte voitures :", e)

    # Collecte vélos
    try:
        parkings_velo = get_parkings_velo()
        with open("parkings_velo.csv", "a", newline="") as f:
            writer = csv.writer(f)
            for s in parkings_velo:
                nom = s["address"]["value"]["streetAddress"]
                dispo = s["availableBikeNumber"]["value"]
                total = s["totalSlotNumber"]["value"]
                writer.writerow([date, nom, dispo, total])
        print(f"[{date}] Données vélos collectées avec succès.")
    except Exception as e:
        print(f"[{date}] Erreur collecte vélos :", e)

if __name__ == "__main__":
    collect_data()
