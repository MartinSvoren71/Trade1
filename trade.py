import requests
from bs4 import BeautifulSoup

# The URL of the page to be parsed
url = 'https://www.cboe.com/us/equities/market_statistics/book/PLTR/?mkt=edgx'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the <td> element with the required class and id
    orders_accepted = soup.find('td', {'class': 'book-viewer-orders', 'id': 'bkOrdersAccepted0'})
    # Check if the element was found and print the text
    if orders_accepted:
        print(orders_accepted.text.strip())
    else:
        print("The element with the required class and id was not found.")
else:
    print(f"Failed to retrieve the page, status code: {response.status_code}")
