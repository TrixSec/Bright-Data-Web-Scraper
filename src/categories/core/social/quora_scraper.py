import requests
import json
from config.config import API_KEY 
from config.endpoints import quora_api_endpoint  

def fetch_quora_posts(post_urls, API_KEY):
    
    data_payload = [{"url": post_url} for post_url in post_urls]
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(quora_api_endpoint, headers=headers, data=json.dumps(data_payload))
    
    if response.status_code == 200:
        posts_data = response.json()
        return process_quora_posts(posts_data)
    else:
        return f"Error: {response.status_code} - {response.text}"

def process_quora_posts(posts_data):
    post_details = []
    
    for post in posts_data:
        post_info = {
            "url": post.get("url"),
            "post_id": post.get("post_id"),
            "author_name": post.get("author_name"),
            "title": post.get("title"),
            "post_date": post.get("post_date"),
            "post_text": post.get("post_text"),
            "pictures_urls": post.get("pictures_urls", []),
            "videos_urls": post.get("videos_urls"),
            "external_urls": post.get("external_urls"),
            "upvotes": post.get("upvotes"),
            "shares": post.get("shares"),
            "views": post.get("views"),
            "author_content_views": post.get("author_content_views"),
            "author_active_spaces": post.get("author_active_spaces"),
            "author_joined_date": post.get("author_joined_date"),
            "author_about": post.get("author_about"),
            "author_education": post.get("author_education"),
            "header": post.get("header"),
            "top_comments": post.get("top_comments", [])
        }
        
        post_details.append(post_info)
    
    return post_details

def display_post_details(posts):
    if isinstance(posts, list):
        for idx, post in enumerate(posts, start=1):
            print(f"Post {idx} URL: {post['url']}")
            print(f"Post ID: {post['post_id']}")
            print(f"Author: {post['author_name']}")
            print(f"Title: {post['title']}")
            print(f"Post Date: {post['post_date']}")
            print(f"Post Text: {post['post_text']}")
            print(f"Upvotes: {post['upvotes']}")
            print(f"Shares: {post['shares']}")
            print(f"Views: {post['views']}")
            print(f"Author's Content Views: {post['author_content_views']}")
            print(f"Author Active Spaces: {post['author_active_spaces']}")
            print(f"Author Joined Date: {post['author_joined_date']}")
            print(f"Author About: {post['author_about']}")
            print(f"Author Education: {post['author_education']}")
            print(f"Header: {post['header']}")
            
            if post['pictures_urls']:
                print("Pictures URLs: ", ", ".join(post['pictures_urls']))
            if post['videos_urls']:
                print("Videos URLs: ", ", ".join(post['videos_urls']))
            if post['external_urls']:
                print("External URLs: ", ", ".join(post['external_urls']))

            if post['top_comments']:
                print("Top Comments:")
                for comment in post['top_comments']:
                    print(f"  Comment: {comment['comment']}")
                    print(f"  Commenter: {comment['commenter_name']}")
                    print(f"  Comment Date: {comment['comment_date']}")
                    for reply in comment['replys']:
                        print(f"    Reply: {reply['reply']}")
                        print(f"    Reply User: {reply['reply_user']}")
            print("-" * 50)
    else:
        print(posts)

def quora_main():
    post_urls = input("Enter the Quora post URLs (comma-separated): ").split(",")

    posts = fetch_quora_posts(post_urls, API_KEY)

    display_post_details(posts)

