import pandas as pd
import requests
from bs4 import BeautifulSoup

all_data = pd.DataFrame(columns=["Product Name", "Product Price", "Product Rating"])

for i in range(1, 10):
    url = f"https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "lxml")

    product_name = []
    product_price = []
    product_rating = []

    for item in soup.find_all("div", class_="_75nlfW"):
        name_tag = item.find("div", class_="KzDlHZ")
        product_name.append(name_tag.text if name_tag else "N/A")

        price_tag = item.find("div", class_="Nx9bqj _4b5DiR")
        product_price.append(price_tag.text if price_tag else "N/A")

        rating_tag = item.find("div", class_="XQDdHH")
        product_rating.append(rating_tag.text if rating_tag else "N/A")

    page_data = pd.DataFrame({
        "Product Name": product_name,
        "Product Price": product_price,
        "Product Rating": product_rating
    })

    all_data = pd.concat([all_data, page_data], ignore_index=True)

all_data.to_csv('output.csv', index=False)
print("Data saved to output.csv")
