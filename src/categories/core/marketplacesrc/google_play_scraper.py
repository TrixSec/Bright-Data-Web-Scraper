import json
import requests
from config.config import API_KEY
from config.endpoints import google_play_endpoint

def get_urls_from_user():
    """Prompts the user to input Google Play Store app URLs to scrape."""
    urls = []
    print("\nEnter Google Play Store app URLs to scrape (enter 'done' to finish):")
    while True:
        url = input("Enter URL: ")
        if url.lower() == 'done':
            break
        elif url:
            urls.append(url)
        else:
            print("Please enter a valid URL or 'done' to finish.")
    return urls

def scrape_google_play_data(API_KEY, urls):
    """Scrapes the Google Play Store app data using the Bright Data API."""
    print(f"\nScraping data for Google Play Store apps...")

    payload = [{"url": url, "country": ""} for url in urls]

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    print(f"\nSending scraping request to Google Play Store endpoint: {google_play_endpoint}")
    try:
        response = requests.post(google_play_endpoint, headers=headers, json=payload)
        
        if response.status_code == 200:
            print("Scraping completed successfully!")
            scraped_data = response.json()

            if not scraped_data:
                print("No app data found.")
                return

            for app_data in scraped_data:
                print("\nApp Data:")

                print(f"URL: {app_data.get('url', 'N/A')}")
                print(f"Title: {app_data.get('title', 'N/A')}")
                print(f"Developer: {app_data.get('developer', 'N/A')}")
                print(f"App Category: {app_data.get('category', 'N/A')}")
                print(f"Installs: {app_data.get('installs', 'N/A')}")
                print(f"Version: {app_data.get('version', 'N/A')}")
                print(f"Size: {app_data.get('size', 'N/A')}")
                print(f"Content Rating: {app_data.get('content_rating', 'N/A')}")
                
                monetization_features = app_data.get('monetization_features', [])
                print(f"Monetization Features: {', '.join(monetization_features) if monetization_features else 'N/A'}")
                
                images = app_data.get('images', [])
                if images:
                    print(f"Images: {', '.join(images)}")
                else:
                    print("Images: N/A")
                
                about = app_data.get('about', {})
                if about:
                    print(f"About the App: {about.get('about_app', 'N/A')}")
                    print(f"Tags: {', '.join(about.get('tags', [])) if about.get('tags') else 'N/A'}")
                    print(f"Updated On: {about.get('updated_on', 'N/A')}")
                else:
                    print("About the App: N/A")

                data_safety = app_data.get('data_safety', {})
                if data_safety:
                    print(f"Data Privacy: {', '.join(data_safety.get('data_privacy', [])) if data_safety.get('data_privacy') else 'N/A'}")
                    print(f"Safety: {data_safety.get('safety', 'N/A')}")
                else:
                    print("Data Safety: N/A")
                
                print(f"Rating: {app_data.get('rating', 'N/A')}")
                print(f"Number of Reviews: {app_data.get('number_of_reviews', 'N/A')}")
                
                reviews = app_data.get('reviews', [])
                if reviews:
                    print(f"Reviews:")
                    for review in reviews:
                        reviewer_name = review.get('reviewer_name', 'Anonymous')
                        review_text = review.get('review', 'No text available')
                        review_rating = review.get('review_rating', 'N/A')
                        review_date = review.get('review_date', 'N/A')
                        
                        print(f"  Reviewer: {reviewer_name}")
                        print(f"  Rating: {review_rating}")
                        print(f"  Date: {review_date}")
                        print(f"  Review: {review_text}")
                        print("-" * 50)
                else:
                    print("No reviews available.")

                print("\n--- End of App Data ---")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

def gplay_main():
    urls = get_urls_from_user()
    scrape_google_play_data(API_KEY, urls)