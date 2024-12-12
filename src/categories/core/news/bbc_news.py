import requests
import json
from config.config import API_KEY
from config.endpoints import bbc_news_endpoint

def get_keyword_from_user():
    """Prompts the user to input the keyword for news search."""
    keyword = input("Enter the keyword (e.g., 'cats', 'Cars', 'Elections'): ")
    return keyword

def process_and_print_data(response_data):
    """Processes and formats the response data for better readability."""
    if isinstance(response_data, list):
        for article in response_data:
            print("\n--- Article Information ---")
            print(f"ID: {article.get('id', 'N/A')}")
            print(f"URL: {article.get('url', 'N/A')}")
            print(f"Author: {article.get('author', 'N/A')}")
            print(f"Headline: {article.get('headline', 'N/A')}")
            print(f"Publication Date: {article.get('publication_date', 'N/A')}")
            print(f"Keyword: {article.get('keyword', 'N/A')}")
            print("Topics: " + ", ".join(article.get('topics', [])))
            print(f"Content: {article.get('content', 'N/A')}")
            
            print("\n--- Related Articles ---")
            related_articles = article.get('related_articles', [])
            for related_article in related_articles:
                print(f"- {related_article.get('article_title', 'N/A')}: {related_article.get('article_url', 'N/A')}")
                
            print("\n--- Images ---")
            images = article.get('images', [])
            for image in images:
                print(f"- {image.get('image_description', 'N/A')}: {image.get('image_url', 'N/A')}")
            print("\n--- End of Article Information ---\n")
    else:
        print("No valid data to process.")

def send_request_to_api(keyword, API_KEY):
    """Sends a POST request to the Bright Data API with the given keyword."""
    payload = [{"keyword": keyword}]
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Bright Data API endpoint

    try:
        # Sending POST request
        response = requests.post(bbc_news_endpoint, headers=headers, json=payload)

        if response.status_code == 200:
            print("Request sent successfully!")
            response_data = response.json()

            process_and_print_data(response_data)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

def bbc_main():

    keyword = get_keyword_from_user()

    if keyword:
        send_request_to_api(keyword, API_KEY)
    else:
        print("Invalid input. Exiting.")
