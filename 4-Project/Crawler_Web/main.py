import requests
from bs4 import BeautifulSoup
import sys
# Setting the console's default character code to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# URL of web crawler
url = 'https://dantri.com.vn/'

# Send a GET request to load the website with SSL verification turned off
response= requests.get(url)

# Check request success or unsuccessful
if response.status_code == 200:
    # Get content HTML website
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all('h2')
    for title in titles:
        print(title.text)
else:
    print('Request unsuccessful')