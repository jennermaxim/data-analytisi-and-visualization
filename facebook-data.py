from facebook_scraper import get_posts
import csv

def get_facebook_posts(keyword, pages=5):
    posts = []
    for post in get_posts(keyword, pages=pages):
        posts.append({
            "text": post["text"],
            "likes": post["likes"],
            "comments": post["comments"],
            "shares": post["shares"]
        })
    return posts

facebook_data = get_facebook_posts("community engagement")

def save_to_csv(data, filename):
    if not data:
        print(f"No data to save for {filename}")
        return
    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")

if facebook_data:
    save_to_csv(facebook_data, "facebook_data.csv")