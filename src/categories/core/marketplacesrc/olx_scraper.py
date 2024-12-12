import json
import requests
from config.config import API_KEY
from config.endpoints import olx_endpoint

def get_urls_from_user():
    """Prompts the user to input OLX URLs to scrape."""
    urls = []
    print("\nEnter OLX Brazil ad URLs to scrape (enter 'done' to finish):")
    while True:
        url = input("Enter URL: ")
        if url.lower() == 'done':
            break
        elif url:
            urls.append(url)
        else:
            print("Please enter a valid URL or 'done' to finish.")
    return urls

def scrape_olx_data(API_KEY, urls):
    """Scrapes the OLX Brazil data using the Bright Data API."""
    print(f"\nScraping data for OLX Brazil Ads...")

    payload = [{"url": url} for url in urls]

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    print(f"\nSending scraping request to OLX endpoint: {olx_endpoint}")
    try:
        response = requests.post(olx_endpoint, headers=headers, json=payload)
        
        if response.status_code == 200:
            print("Scraping completed successfully!")
            scraped_data = response.json()

            print("\nScraped Data:")
            for ad in scraped_data:
                print(f"\nAd URL: {ad['url']}")
                print(f"Subject: {ad['subject']}")
                print(f"Price: {ad['Currency']} {ad['priceValue']}")
                print(f"Location: {ad['locations'][0]['municipality']}, {ad['locations'][0]['neighbourhood']}")
                print(f"Description: {ad['body']}")
                print(f"Seller: {ad['Sellername']}")
                print(f"Tags: {', '.join(tag['label'] for tag in ad['tags'])}")
                print(f"Images: {', '.join(ad['images'])}")
                print(f"Category: {ad['categoryName']}")
                print(f"Publication Date: {ad['PublicationDate']}")
                print(f"Ad Reply: {ad['adReply']}")
                print(f"Friendly URL: {ad['friendlyUrl']}")
                print(f"Number of Images: {ad['NumberOfImages']}")
                print(f"Neighbourhood: {ad['locations'][0]['neighbourhood']}")
                print(f"Municipality: {ad['locations'][0]['municipality']}")
                print(f"Zipcode: {ad['locations'][0]['zipcode']}")
                print(f"Zone: {ad['locations'][0]['zone']}")
                print(f"Region: {ad['locations'][0]['region']}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

def olx_main():

    urls = get_urls_from_user()

    scrape_olx_data(API_KEY, urls)


