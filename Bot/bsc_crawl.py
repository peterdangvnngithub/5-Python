import requests
from bs4 import BeautifulSoup
import random
import time

# Define user agents
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
]

# Function to scrape data from page
def scrape_page(url):
    headers = {'User-Agent': random.choice(USER_AGENTS)}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', class_='table table-hover mb-0')
        if table:
            rows = table.find_all('tr')
            for row in rows:
                empty_token = row.find('img', src='/assets/bsc/images/svg/empty-token.svg?v=24.3.4.1')
                if empty_token:
                    text_muted = row.find('span', class_='text-muted')
                    if text_muted:
                        coin_name = text_muted.text.strip()
                        if not coin_exists(coin_name) and not coin_blacklisted(coin_name) and not coin_targeted(coin_name):
                            print(coin_name)
                            write_to_file(coin_name)
        else:
            print("Table not found on page:", url)
    else:
        print("Failed to fetch page:", url)

# Function to check if coin already exists in file
def coin_exists(coin_name):
    try:
        with open('coins.txt', 'r') as file:
            for line in file:
                if coin_name in line:
                    return True
        return False
    except FileNotFoundError:
        return False

# Function to check if coin is blacklisted
def coin_blacklisted(coin_name):
    try:
        with open('blacklist.txt', 'r') as file:
            for line in file:
                if coin_name in line:
                    return True
        return False
    except FileNotFoundError:
        return False

# Function to check if coin is targeted
def coin_targeted(coin_name):
    try:
        with open('target.txt', 'r') as file:
            for line in file:
                if coin_name in line:
                    return True
        return False
    except FileNotFoundError:
        return False

# Function to write coin name to file
def write_to_file(coin_name):
    try:
        with open('coins.txt', 'a') as file:
            file.write(coin_name + '\n')
    except Exception as e:
        print("Error writing to file:", e)

# Main function to scrape multiple pages
def scrape_pages():
    base_url = 'https://bscscan.com/tokentxns?p='
    for page_num in range(1, 201):
        print("Scraping page", page_num)
        url = base_url + str(page_num)
        scrape_page(url)
        time.sleep(1)  # Add a delay to avoid overwhelming the server

# Run the scraper
scrape_pages()