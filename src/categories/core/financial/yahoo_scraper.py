import requests
import json
from config.config import API_KEY
from config.endpoints import yahoo_endpoint 

def get_urls_from_user():
    """Prompts the user to input URLs to scrape."""
    urls = []
    print("\nEnter URLs to scrape (enter 'done' to finish):")
    while True:
        url = input("Enter URL: ")
        if url.lower() == 'done':
            break
        elif url:
            urls.append(url)
        else:
            print("Please enter a valid URL or 'done' to finish.")
    return urls

def pretty_print_response(response_data):
    """Pretty prints the raw JSON response for readability."""
    print("\n--- Raw API Response ---")
    print(json.dumps(response_data, indent=4))
    print("\n--- End of Raw API Response ---\n")

def send_request_to_api(urls, API_KEY):
    """Sends a POST request to the Bright Data API with the given URLs."""
    payload = [{"url": url} for url in urls]
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }


    try:
        response = requests.post(yahoo_endpoint, headers=headers, json=payload)

        if response.status_code == 200:
            print("Request sent successfully!")
            response_data = response.json()

            pretty_print_response(response_data)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

def yahoo_main():

    urls = get_urls_from_user()

    if urls:
        send_request_to_api(urls, API_KEY)
    else:
        print("No URLs entered. Exiting.")
