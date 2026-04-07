import time
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

with open('scrape_setting.json', 'r', encoding='utf-8') as jfile:
    settings = json.load(jfile)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
url = settings["url"]
headers = settings["headers"]
driver.get(url)
html = driver.page_source
choice = input("Do you want to scrape the website or just watch it is which type of website? (scrape/watch): ").lower()

def scrape_website(): #scrape the website
    try:
        if choice == "watch":
            print("Website content preview:",html[:500])

        elif choice == "scrape":
            print("Scraping the website...")
            for page in range(settings["start_page"], settings["end_page"] + 1):
                if page < 1:
                    driver.get(url)
                else:
                    driver.get(url + f'{page}')
                html = driver.page_source
                time.sleep(2)  # Simulate scraping delay
                soup = BeautifulSoup(html, 'html.parser')
                things = soup.find_all(settings["tag"],{'class':settings["class"]})
                for thing in things:
                    print(thing[settings["sub_tag"]])

        else: 
            print("Invalid choice. Please enter 'scrape' or 'watch'.")

        print("****************************")
        print("Scraping completed.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
        scrape_website()