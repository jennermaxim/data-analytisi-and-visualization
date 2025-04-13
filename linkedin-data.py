from linkedin_api import Linkedin
import csv

LINKEDIN_EMAIL = "LINKEDIN_EMAIL"  # Replace with your actual LinkedIn email
LINKEDIN_PASSWORD = "LINKEDIN_PASSWORD"  # Replace with your actual LinkedIn password

linkedin_api = Linkedin(LINKEDIN_EMAIL, LINKEDIN_PASSWORD)

def get_linkedin_posts(keyword):
    posts = linkedin_api.search({"keywords": keyword, "limit": 10})
    return [{"title": post.get("title", "N/A"), "description": post.get("description", "N/A")} for post in posts]

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
    
linkedin_data = get_linkedin_posts("community engagement")

if linkedin_data:
    save_to_csv(linkedin_data, "linkedin_data.csv")