import requests
import json
from config.config import API_KEY
from config.endpoints import booking_api_endpoint

def get_input():
    url = "https://www.booking.com" 
    location = input("Enter the location (e.g., 'Tel Aviv'): ")
    check_in = input("Enter the check-in date (e.g., '2025-02-01T00:00:00.000Z'): ")
    check_out = input("Enter the check-out date (e.g., '2025-02-10T00:00:00.000Z'): ")
    adults = int(input("Enter the number of adults: "))
    rooms = int(input("Enter the number of rooms: "))
    
    return {
        "url": url,
        "location": location,
        "check_in": check_in,
        "check_out": check_out,
        "adults": adults,
        "rooms": rooms
    }

def send_request(data):
    headers = {
        "Authorization": f"Bearer {API_KEY}", 
        "Content-Type": "application/json"
    }
    payload = [data]
    
    response = requests.post(booking_api_endpoint, headers=headers, data=json.dumps(payload))
    return response.json()

def process_response(response):
    for item in response:
        print(f"Title: {item['title']}")
        print(f"Location: {item['location']}")
        print(f"Check-in: {item['check_in']}")
        print(f"Check-out: {item['check_out']}")
        print(f"Price: {item['currency']} {item['final_price']}")
        print(f"Review Score: {item['review_score']}")
        print(f"Review Count: {item['review_count']}")
        print(f"Image: {item['image']}")
        print(f"Address: {item['address']}")
        print(f"City: {item['city']}")
        print(f"Full Location: {item['full_location']['display_location']}")
        print("-" * 50)

def booking_main():
    user_input = get_input()
    
    response = send_request(user_input)
    
    if response:
        process_response(response)
    else:
        print("No data received or an error occurred.")


