import json
import requests
from config.config import API_KEY
from config.endpoints import lawyer_url_endpoint
from config.endpoints import lawyer_keyword_endpoint
from termcolor import colored


def get_urls_from_user():
    """Prompts the user to input lawyer directory URLs to collect."""
    urls = []
    print("\nEnter lawyer directory URLs to collect (enter 'done' to finish):")
    while True:
        url = input("Enter URL: ")
        if url.lower() == 'done':
            break
        elif url:
            urls.append(url)
        else:
            print("Please enter a valid URL or 'done' to finish.")
    return urls


def get_keywords_from_user():
    """Prompts the user to input keywords to discover lawyers."""
    keywords = []
    print("\nEnter keywords to discover lawyers (enter 'done' to finish):")
    while True:
        keyword = input("Enter keyword: ")
        if keyword.lower() == 'done':
            break
        elif keyword:
            keywords.append(keyword)
        else:
            print("Please enter a valid keyword or 'done' to finish.")
    return keywords


def process_lawyer_data(data):
    """Processes the lawyer data to extract and display detailed information."""
    for lawyer in data:
        print(f"Lawyer Name: {lawyer.get('name', 'N/A')}")
        print(f"Type: {lawyer.get('type', 'N/A')}")
        print(f"Location: {lawyer.get('filial', 'N/A')}, {lawyer.get('location', 'N/A')}")
        print(f"Admission: {lawyer.get('admission', 'N/A')}")
        print(f"Law School Attended: {lawyer.get('law_school_attended', 'N/A')}")
        print(f"University Attended: {lawyer.get('university_attended', 'N/A')}")
        print(f"Year of First Admission: {lawyer.get('year_of_first_admission', 'N/A')}")
        print(f"Practice Areas: {', '.join(lawyer.get('areas_of_practice', ['N/A']))}")
        print(f"Profile Peer Review: {lawyer.get('profile_peer_review_count', 0)} reviews, {lawyer.get('profile_peer_review_star', 'N/A')} stars")
        print(f"Profile Awards: {', '.join(lawyer.get('profile_peer_review_awards', ['N/A']))}")
        print(f"Website: {lawyer.get('website', 'Not Available')}")
        print(f"Office Address: {lawyer.get('mailing_address', 'Not Available')}")
        print("------")

        if 'people' in lawyer:
            print("Peers:")
            for peer in lawyer['people']:
                print(f"  Peer Name: {peer.get('name', 'N/A')}")
                print(f"  Title: {peer.get('title', 'N/A')}")
                print(f"  Areas of Practice: {', '.join(peer.get('areas_of_practice', ['N/A']))}")
                print(f"  Peer Reviews: {peer.get('peer_reviews_count', 0)} reviews, {peer.get('peer_reviews', 'N/A')} stars")
                print(f"  Profile Link: {peer.get('link', 'N/A')}")
            print("------")


def collect_lawyers_by_url(API_KEY, urls):
    """Collects lawyer data by URLs using the Bright Data API."""
    print(f"\nCollecting data for lawyer directory URLs...")

    payload = [{"url": url} for url in urls]

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(lawyer_url_endpoint, headers=headers, json=payload)
        
        if response.status_code == 200:
            print("Collection completed successfully!")
            collected_data = response.json()

            if not collected_data:
                print("No lawyer data found.")
                return

            process_lawyer_data(collected_data)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")


def discover_lawyers_by_keyword(API_KEY, keywords):
    """Discovers lawyer data by keywords using the Bright Data API."""
    print(f"\nDiscovering lawyers by keywords...")

    payload = [{"keyword": keyword} for keyword in keywords]

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(lawyer_keyword_endpoint, headers=headers, json=payload, params={'type': 'discover_new', 'discover_by': 'keyword'})
        
        if response.status_code == 200:
            print("Discovery completed successfully!")
            discovered_data = response.json()

            if not discovered_data:
                print("No lawyer data found.")
                return

            process_lawyer_data(discovered_data)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

def print_bold_colored(message, color="green"):
    print(colored(message, color, attrs=["bold"]))

def martindale_main():

    print_bold_colored("\nSelect martindale.com Scraping Type:", "cyan")
    print_bold_colored("1.", "green"), print("Lawyer Information From Url")
    print_bold_colored("2.", "green"), print("Lawyer Information From Keyword")
    choice = int(input(colored("\nEnter your choice (1 or 2): ", "yellow")))

    if choice == "1":
        urls = get_urls_from_user()
        collect_lawyers_by_url(API_KEY, urls)
    elif choice == "2":
        keywords = get_keywords_from_user()
        discover_lawyers_by_keyword(API_KEY, keywords)
    else:
        print("Invalid choice. Please choose 1 or 2.")