import requests
import csv
import os
from dotenv import load_dotenv

load_dotenv()
# EVENTBRITE_API_KEY = os.getenv("EVENTBRITE_API_KEY")
EVENTBRITE_API_KEY = "XBBRKVLOWIFNJ2DQEMYA"

def get_organization_id():
    headers = {"Authorization": f"Bearer {EVENTBRITE_API_KEY}"}
    response = requests.get("https://www.eventbriteapi.com/v3/users/me/organizations/", headers=headers)
    response.raise_for_status()
    orgs = response.json().get("organizations", [])
    if orgs:
        return orgs[0].get("id")  # just grab the first org
    return None

def get_organization_events(org_id):
    headers = {"Authorization": f"Bearer {EVENTBRITE_API_KEY}"}
    url = f"https://www.eventbriteapi.com/v3/organizations/{org_id}/events/"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        events = response.json().get("events", [])
        return [{
            "name": event.get("name", {}).get("text", "No name"),
            "start": event.get("start", {}).get("local", "N/A"),
            "end": event.get("end", {}).get("local", "N/A"),
            "url": event.get("url", "#")
        } for event in events]
    except requests.exceptions.HTTPError as err:
        print(f"Eventbrite API Error: {err}")
        print(f"Response content: {response.text}")
        return []

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

# Main run
try:
    org_id = get_organization_id()
    if org_id:
        print(f"Using organization ID: {org_id}")
        eventbrite_data = get_organization_events(org_id)
        if eventbrite_data:
            save_to_csv(eventbrite_data, "eventbrite_org_events.csv")
    else:
        print("No organization ID found for this user.")
except Exception as e:
    print(f"Unexpected error: {e}")
