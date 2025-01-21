import requests
from bs4 import BeautifulSoup
import csv
import json

def web_scraper():
    print("\n The DataHarvester \n")
    base_url = input("Enter the URL of the website to scrape: ")
    if not base_url.startswith("http"):
        print(" Err: Please enter a valid URL starting with 'http' or 'https'.")
        return
    selector = input("Enter the CSS selector for the elements to scrape: ")
    pagination = input("Does the website have pagination? (y/n): ").lower()
    if pagination == "y":
        pagination_param = input("Enter the pagination parameter: ")
        all_data = handle_pagination(base_url, selector, pagination_param)
    else:
        all_data = scrape_single_page(base_url, selector)
    
    if not all_data:
        print("No data found to scrape.")
        return
    
    save_format = input("Save data as (CSV/JSON)? ").lower()
    if save_format == "csv":
        save_to_csv(all_data)
    elif save_format == "json":
        save_to_json(all_data)
    else:
        print("Invalid format. Data not saved.")

def scrape_single_page(url, selector):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.select(selector)
        if not elements:
            print(" No elements found using the provided selector.")
            return []
        return [element.get_text(strip=True) for element in elements]
    except requests.exceptions.RequestException as e:
        print(f" Network error: {e}")
        return []

def handle_pagination(base_url, selector, pagination_param):
    page_number = 1
    all_data = []
    while True:
        paginated_url = f"{base_url}?{pagination_param}={page_number}"
        print(f"Fetching page {page_number}...")
        try:
            response = requests.get(paginated_url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            elements = soup.select(selector)
            if not elements:
                print("No more data found. Stopping pagination.")
                break
            all_data.extend([element.get_text(strip=True) for element in elements])
            page_number += 1
        except requests.exceptions.RequestException as e:
            print(f" Error on page {page_number}: {e}")
            break
    return all_data

def save_to_csv(data):
    file_name = input("Enter the filename for the CSV file...: ")
    try:
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Scraped Data"])
            for item in data:
                writer.writerow([item])
        print(f"✅ Data successfully saved to {file_name}")
    except Exception as e:
        print(f" Error saving to CSV: {e}")

def save_to_json(data):
    file_name = input("Enter the filename for the JSON file (e.g., data.json): ")
    try:
        with open(file_name, mode='w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"✅ Data successfully saved to {file_name}")
    except Exception as e:
        print(f" Error saving to JSON: {e}")

if __name__ == "__main__":
    web_scraper()
