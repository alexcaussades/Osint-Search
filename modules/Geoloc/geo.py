import requests
import webbrowser

import json

# Function to get address from latitude and longitude using OpenStreetMap's Nominatim API
class Geoloc:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def get_address(self):
        return MapsGeoloc(self.longitude, self.latitude)

    def open_in_google_maps(self):
        return GoogleGeoloc(self.longitude, self.latitude)
    
    def to_json(self):
        return json.dumps({
            'longitude': self.longitude,
            'latitude': self.latitude
        })
    
    

def MapsGeoloc(longitude, latitude):
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}&addressdetails=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    if 'error' in data:
        return "Address not found"

    address = data.get('address', {})
    road = address.get('road', '')
    suburb = address.get('suburb', '')
    city = address.get('city', '') or address.get('town', '') or address.get('village', '')
    state = address.get('state', '')
    country = address.get('country', '')

    formatted_address = ', '.join(filter(None, [road, suburb, city, state, country]))
    return formatted_address

def GoogleGeoloc(latitude, longitude):
    url = f"https://www.google.com/maps/@{latitude},{longitude},18z"
    response = requests.get(url)
    webbrowser.open(url)
    return "Google Maps opened in web browser."


# rechercher une adresse à partir du nom de la rue, de la ville, du pays
def address_to_coordinates(address):
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={address}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if not data:
        return "Coordinates not found"

    latitude = data[0]['lat']
    longitude = data[0]['lon']

    GoogleGeoloc(latitude, longitude)
