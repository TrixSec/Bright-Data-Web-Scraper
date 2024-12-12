import requests
import json
from config.config import API_KEY 
from config.endpoints import toctoc_api_endpoint  

def get_url_from_user():
    """Prompts the user to input the URL for the property listing."""
    url = input("Enter the URL for the property listing: ")
    return url

def process_and_print_data(response_data):
    """Processes and formats the response data for better readability."""
    if isinstance(response_data, list):
        for property_listing in response_data:
            print("\n--- Property Information ---")
            print(f"Title: {property_listing.get('Titulo', 'N/A')}")
            print(f"Description: {property_listing.get('Descripcion', 'N/A')}")
            print(f"Price: {property_listing.get('Precio', 'N/A')} {property_listing.get('Currency', 'N/A')}")
            print(f"Location: {property_listing.get('Ubicacion', {}).get('lat', 'N/A')}, {property_listing.get('Ubicacion', {}).get('lng', 'N/A')}")
            print(f"Number of Rooms: {property_listing.get('Habitaciones', 'N/A')}")
            print(f"Bathrooms: {property_listing.get('Banos', 'N/A')}")
            print(f"Property Size: {property_listing.get('Dimension_propiedad', 'N/A')} m²")
            print(f"Seller: {property_listing.get('Seller', 'N/A')} ({property_listing.get('Tipo_de_vendedor', 'N/A')})")
            print(f"Phone: {property_listing.get('Phone1', 'N/A')}")
            print(f"Email: {property_listing.get('Email', 'N/A')}")
            print(f"Property Type: {property_listing.get('Type', 'N/A')}")
            print(f"Status: {property_listing.get('Nueva_usada', 'N/A')}")
            print(f"Region: {property_listing.get('Region', 'N/A')}")
            print(f"City: {property_listing.get('Comuna_Ciudad', 'N/A')}")
            print(f"URL: {property_listing.get('url', 'N/A')}")
            print(f"Seller ID: {property_listing.get('seller_id', 'N/A')}")
            
            print("\n--- Property Images ---")
            images = property_listing.get('Imagen', [])
            for img_url in images:
                print(f"- {img_url}")
            
            print("\n--- End of Property Information ---\n")
    else:
        print("No valid data to process.")

def send_request_to_api(url, API_KEY):
    """Sends a POST request to the Toctoc API with the given property URL."""
    payload = [{"url": url}]
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(toctoc_api_endpoint, headers=headers, json=payload)

        if response.status_code == 200:
            print("Request sent successfully!")
            response_data = response.json()
            process_and_print_data(response_data)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

def toctoc_main():
    url = get_url_from_user()

    if url:
        send_request_to_api(url, API_KEY)
    else:
        print("Invalid input. Exiting.")
