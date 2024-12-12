import requests
import json
from config.config import API_KEY
from config.endpoints import amazon_endpoint

def get_urls_from_user():
    """Prompts the user to input URLs to scrape."""
    urls = []
    print("\nEnter Amazon product URLs to scrape (enter 'done' to finish):")
    while True:
        url = input("Enter URL: ")
        if url.lower() == 'done':
            break
        elif url:
            urls.append(url)
        else:
            print("Please enter a valid URL or 'done' to finish.")
    return urls

def process_and_format_response(response_data):
    """Processes and formats the response for better readability."""
    for product in response_data['products']:
        print("\n--- Product Information ---")
        print(f"URL: {product['url']}")
        print(f"Title: {product['title']}")
        print(f"Rating: {product['rating']} (Based on {product['reviews_count']} reviews)")
        print(f"Price: {product['price']}")
        print(f"Original Price: {product['original_price'] if 'original_price' in product else 'N/A'}")
        print(f"Discount: {product['discount'] if 'discount' in product else 'N/A'}")
        print(f"Availability: {product['availability'] if 'availability' in product else 'Not Specified'}")
        print(f"Seller: {product['seller_name']}")
        print(f"Delivery: {product['delivery_price']}")
        
        print("\nProduct Details:")
        print(product['product_details'])

        print("\nProduct Variations:")
        for variation in product['variations']:
            print(f"- {variation['variation_name']}: {variation['variation_value']}")

        print("\nTags:")
        for tag in product['tags']:
            print(f"- {tag}")

        print("\nProduct Specifications:")
        for spec in product['product_specifications']:
            print(f"- {spec['specification_name']}: {spec['specification_value']}")

        print("\nProduct Images:")
        for image_url in product['images']:
            print(f"- {image_url}")
        
        print("\n--- End of Product Information ---\n")


def send_request_to_api(urls, API_KEY):
    """Sends a POST request to the Amazon API with the given URLs."""
    payload = [{"url": url} for url in urls]
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(amazon_endpoint, headers=headers, json=payload)

        if response.status_code == 200:
            print("Request sent successfully!")
            response_data = response.json()

            process_and_format_response(response_data)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

def amazon_main():
    """Main function to drive the flow."""
    urls = get_urls_from_user()

    if urls:
        send_request_to_api(urls, API_KEY)
    else:
        print("No URLs entered. Exiting.")
