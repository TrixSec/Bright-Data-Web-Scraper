import requests
import json
from config.config import API_KEY
from config.endpoints import google_news_endpoint

def get_country_and_keyword_from_user():
    """Prompts the user to input the country and keyword for news search."""
    country = input("Enter the country (e.g., 'US', 'FR', 'GB'): ")
    keyword = input("Enter the keyword (e.g., 'Joe Biden', 'Politics news', 'Premier league'): ")
    return country, keyword

def process_and_print_data(response_data):
    """Processes and formats the response data for better readability."""
    if isinstance(response_data, list):
        for article in response_data:
            print("\n--- Article Information ---")
            print(f"URL: {article.get('url', 'N/A')}")
            print(f"Title: {article.get('title', 'N/A')}")
            print(f"Publisher: {article.get('publisher', 'N/A')}")
            print(f"Date: {article.get('date', 'N/A')}")
            print(f"Category: {article.get('category', 'N/A')}")
            print(f"Keyword: {article.get('keyword', 'N/A')}")
            print(f"Country: {article.get('country', 'N/A')}")
            print(f"Image URL: {article.get('image', 'N/A')}")
            print("\n--- End of Article Information ---\n")
    else:
        print("No valid data to process.")

def send_request_to_api(country, keyword, API_KEY):
    """Sends a POST request to the Bright Data API with the given country, keyword, and URL."""
    payload = [{
        "url": "https://news.google.com/",
        "keyword": keyword,
        "country": country,
        "language": ""
    }]
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(google_news_endpoint, headers=headers, json=payload)

        if response.status_code == 200:
            print("Request sent successfully!")
            response_data = response.json()

            process_and_print_data(response_data)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

def google_news_main():

    country, keyword = get_country_and_keyword_from_user()

    if country and keyword:
        send_request_to_api(country, keyword, API_KEY)
    else:
        print("Invalid input. Exiting.")
