import requests
import json
from config.config import API_KEY
from config.endpoints import insta_post_endpoint, insta_comment_endpoint, insta_reel_endpoint

def fetch_instagram_comments(post_urls, API_KEY):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = json.dumps([{"url": post_url} for post_url in post_urls])
    
    response = requests.post(insta_comment_endpoint, headers=headers, data=data)
    
    if response.status_code == 200:
        comments_data = response.json()
        for comment in comments_data:
            print(f"Post URL: {comment['url']}")
            print(f"User: {comment['comment_user']}")
            print(f"Comment: {comment['comment']}")
            print(f"Likes: {comment['likes_number']}")
            print(f"Replies: {comment['replies_number']}")
            for reply in comment['replies']:
                print(f"  Reply: {reply['reply']}")
                print(f"  Reply User: {reply['reply_user']}")
            print("-" * 50)
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Function to fetch Instagram posts
def fetch_instagram_posts(post_urls, API_KEY):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = json.dumps([{"url": post_url} for post_url in post_urls])
    
    response = requests.post(insta_post_endpoint, headers=headers, data=data)
    
    if response.status_code == 200:
        posts_data = response.json()
        for post in posts_data:
            print(f"Post URL: {post['url']}")
            print(f"Description: {post['description']}")
            print(f"Hashtags: {', '.join(post['hashtags'])}")
            print(f"Likes: {post['likes']}")
            print(f"Comments: {post['num_comments']}")
            print(f"Date Posted: {post['date_posted']}")
            print(f"Location: {', '.join(post['location'])}")
            print(f"Video Views: {post['video_view_count']}")
            print(f"Post Content: {post['post_content'][0]['url']}")
            print("-" * 50)
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Function to collect Instagram Reels
def collect_instagram_reels(profile_url, num_of_posts, API_KEY):
    
    data_payload = [
        {
            "url": profile_url,
            "num_of_posts": num_of_posts
        }
    ]
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(insta_reel_endpoint, headers=headers, data=json.dumps(data_payload))
    
    if response.status_code == 200:
        reels_data = response.json()
        return process_reels_data(reels_data)
    else:
        return f"Error: {response.status_code} - {response.text}"

def process_reels_data(reels_data):
    reel_details = []
    
    for reel in reels_data:
        reel_info = {
            "url": reel.get("url"),
            "user_posted": reel.get("user_posted"),
            "description": reel.get("description"),
            "hashtags": reel.get("hashtags", []),
            "num_comments": reel.get("num_comments"),
            "date_posted": reel.get("date_posted"),
            "likes": reel.get("likes"),
            "views": reel.get("views"),
            "video_play_count": reel.get("video_play_count"),
            "top_comments": reel.get("top_comments", []),
            "post_id": reel.get("post_id"),
            "thumbnail": reel.get("thumbnail"),
            "shortcode": reel.get("shortcode"),
            "video_url": reel.get("video_url"),
            "audio_url": reel.get("audio_url")
        }
        
        reel_details.append(reel_info)
    
    return reel_details

def insta_main():
    print("Choose an option:")
    print("1. Fetch Instagram Comments from Post URL")
    print("2. Fetch Instagram Post Details (Collect Post URL)")
    print("3. Collect Instagram Reels from Profile URL")
    
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == "1":
        post_urls = input("Enter the Instagram post URLs (comma-separated): ").split(",")
        fetch_instagram_comments(post_urls, API_KEY)
    
    elif choice == "2":
        post_urls = input("Enter the Instagram post URLs (comma-separated): ").split(",")
        fetch_instagram_posts(post_urls, API_KEY)
    
    elif choice == "3":
        profile_url = input("Enter the Instagram profile URL: ")
        num_of_posts = int(input("Enter the number of posts to collect: "))
        reels = collect_instagram_reels(profile_url, num_of_posts, API_KEY)
        
        if isinstance(reels, list):
            for idx, reel in enumerate(reels, start=1):
                print(f"Reel {idx} URL: {reel['url']}")
                print(f"User Posted: {reel['user_posted']}")
                print(f"Description: {reel['description']}")
                print(f"Likes: {reel['likes']}")
                print(f"Views: {reel['views']}")
                print(f"Video Play Count: {reel['video_play_count']}")
                print(f"Comments: {reel['num_comments']}")
                print(f"Video URL: {reel['video_url']}")
                print("-" * 50)
        else:
            print(reels)
    
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
