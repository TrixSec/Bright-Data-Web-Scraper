import requests
import json
from config.config import API_KEY
from config.endpoints import wiki_api_endpoint

def send_request(keyword):
    url = f'https://en.wikipedia.org/wiki/{keyword}'

    payload = json.dumps([{"url": url}])

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }


    response = requests.post(wiki_api_endpoint, headers=headers, data=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}

def process_response(response_data):
    if 'error' in response_data:
        print("Error:", response_data['error'])
        return

    for item in response_data:
        print(f"URL: {item['url']}")
        print(f"Title: {item['title']}")
        print("Table of Contents:")
        for toc in item.get('table_of_contents', []):
            print(f"- {toc}")
        print("Raw Text:\n", item.get('raw_text', 'No raw text available'))
        print("\nReferences:")
        for ref in item.get('references', []):
            print(f"- {ref['reference']}")

def wiki_main():
    keyword = input("Enter a keyword for Wikipedia search: ").strip().replace(" ", "_")
    response_data = send_request(keyword)
    process_response(response_data)