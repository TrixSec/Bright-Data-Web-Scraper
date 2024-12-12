import json
import requests
from config.config import API_KEY
from config.endpoints import yapo_chile_endpoint

def get_urls_from_user():
    """Prompts the user to input Yapo Chile listing URLs to scrape."""
    urls = []
    print("\nEnter Yapo Chile listing URLs to scrape (enter 'done' to finish):")
    while True:
        url = input("Enter URL: ")
        if url.lower() == 'done':
            break
        elif url:
            urls.append(url)
        else:
            print("Please enter a valid URL or 'done' to finish.")
    return urls

def scrape_yapo_chile_data(API_KEY, urls):
    """Scrapes Yapo Chile listing data using the Bright Data API."""
    print(f"\nScraping data for Yapo Chile listings...")

    payload = [{"url": url} for url in urls]

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    print(f"\nSending scraping request to Yapo Chile endpoint: {yapo_chile_endpoint}")
    try:
        response = requests.post(yapo_chile_endpoint, headers=headers, json=payload)
        
        if response.status_code == 200:
            print("Scraping completed successfully!")
            scraped_data = response.json()

            for listing in scraped_data:
                print("\nListing Title:", listing.get("title"))
                print("Description:", listing.get("description"))
                print("Price:", listing.get("price"), listing.get("currency"))
                print("City:", listing.get("city"))
                print("Region:", listing.get("region"))
                print("Date Created:", listing.get("date_creation"))
                print("Category:", listing.get("root_category_name"), ">", listing.get("parent_category_name"))
                print("Seller Name:", listing.get("seller_name"))
                print("Listing URL:", listing.get("url"))
                print("Images:")
                for image in listing.get("images", []):
                    print("  ", image)
                print("Main Phone:", listing.get("main_phone"))
                print("Estate Type:", listing.get("estate_type"))
                print("Total Square Meters:", listing.get("total_square"))
                print("Ad Type:", listing.get("ad_type"))
                print("Publisher Type:", listing.get("publisher_type"))
                print("-" * 50)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

def yapo_main():

    urls = get_urls_from_user()

    scrape_yapo_chile_data(API_KEY, urls)
