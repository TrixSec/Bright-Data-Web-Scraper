import json
import requests
from config.config import API_KEY
from config.endpoints import apple_endpoint

def get_urls_from_user():
    """Prompts the user to input URLs to scrape."""
    urls = []
    print("\nEnter Apple App URLs to scrape (enter 'done' to finish):")
    while True:
        url = input("Enter URL: ")
        if url.lower() == 'done':
            break
        elif url:
            urls.append(url)
        else:
            print("Please enter a valid URL or 'done' to finish.")
    return urls

def scrape_apple_data(API_KEY, urls):
    """Scrapes the Apple App Store data using the Bright Data API."""
    print(f"\nScraping data for Apple Apps...")

    payload = [{"url": url} for url in urls]

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    print(f"\nSending scraping request to Apple endpoint: {apple_endpoint}")
    try:
        response = requests.post(apple_endpoint, headers=headers, json=payload)
        
        if response.status_code == 200:
            print("Scraping completed successfully!")
            scraped_data = response.json()
            process_scraped_data(scraped_data)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_scraped_data(data):
    """Process and display the scraped Apple App data."""
    for app in data:
        print(f"\nApp Title: {app['title']}")
        print(f"App URL: {app['url']}")
        print(f"Developer: {app['developer']['developer_name']}")
        print(f"Developer URL: {app['developer']['developer_link']}")
        print(f"Top Charts: {', '.join(app['top_charts']) if app['top_charts'] else 'N/A'}")
        print(f"Monetization Features: {', '.join(app['monetization_features']) if app['monetization_features'] else 'N/A'}")
        print(f"Rating: {app['rating']} ({app['number_of_raters']} ratings)")
        
        print("App Image: ", app['image'])
        if app['screenshots']:
            print(f"Screenshots: {', '.join(app['screenshots'])}")

        print("\nRecent Changes/Updates:")
        for news in app['what_new']:
            print(f"- {news['news']} (Version {news['version_history']})")

        print("\nReviews:")
        for review in app['reviews']:
            print(f"Review by {review['reviewer_name']}: {review['review_title']} ({review['review_rating']} stars)")
            print(f"Review: {review['review']}")
            print(f"Date: {review['review_date']}")
            print("-" * 60)

def apple_main():
    urls = get_urls_from_user()

    scrape_apple_data(API_KEY, urls)