import requests
from bs4 import BeautifulSoup

url = 'https://assamtribune.com/'
print('Fetching Headlines. .')
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h2')

sl_no = 1

print('========== THE ASSAM TRIBUNE HEADLINES ===========')
for x in headlines:
    print(sl_no, ': ', x.text.strip())
    sl_no += 1

print('')
raw_input = input("Press enter to quit")
