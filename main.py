import requests
from bs4 import BeautifulSoup
domain  = input("Enter you domain: ")
URL = 'https://whois.phurix.co.uk/'+domain
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')


def test():
    result = soup.text
    result = result.split("Creation Date", 1)[1]
    result = result.split("Registrar Registration Expiration Date", 1)[0]

    print("The " + domain + " was created on" + result)


test()
