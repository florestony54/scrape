from bs4 import BeautifulSoup
import urllib.request as urllib



airpods = 'https://www.target.com/p/super-mario-bros-u-deluxe-nintendo-switch/-/A-54136573'

page = urllib.urlopen(airpods)
soup = BeautifulSoup(page, 'html.parser')

"""Target site shows product availability in green text, but also displays other
key identifiers with the same class... in_stock_check() checks the list
for "in stock"""
green_text = soup.find_all(attrs={'class': "h-text-greenDark"})



in_stock =  soup.find('div', attrs={'class': 'h-text-greenDark'})
out_of_stock = soup.find('div', attrs={'class': 'h-text-orangeDark'})
prod_name = soup.find('span', attrs={'data-test': 'product-title'})
prod_price = soup.find('span', attrs={'data-test': 'product-price'})


status = "N/A"
product = prod_name.text.strip()
price = prod_price.text.strip()
