import requests

BASE_URL = "https://portail-api-data.montpellier3m.fr"

def get_parkings_voiture():
    """
    Récupère les données temps réel des parkings voiture
    """
    response = requests.get(f"{BASE_URL}/offstreetparking")
    response.raise_for_status()
    return response.json()

def get_parkings_velo():
    """
    Récupère les données temps réel des stations vélo
    """
    response = requests.get(f"{BASE_URL}/bikestation")
    response.raise_for_status()
    return response.json()
