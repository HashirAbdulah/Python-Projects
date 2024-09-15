from bs4 import BeautifulSoup
import os
import pandas as pd

data = {'Title': [], 'Price': [], 'Discount': [], 'Link': []}

folder = r"C:\Users\M.Hashir Abdullah\Desktop\Python-Projects\WebScrapper\Data"

try:
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

       
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()

        soup = BeautifulSoup(html, "html.parser")

        t = soup.find("a", {"title": True})
        title = t["title"] if t else "No title found"
        link = t["href"] if t else "No link found"
        if link and link.startswith("//"):
            link = "https:" + link

        p = soup.find("span", class_="ooOxS")
        price = p.get_text(strip=True) if p else "No price found"

        # Extract the discount
        d = soup.find("span", class_="IcOsH")
        discount = d.get_text(strip=True) if d else "No discount found"

        print(f"Title: {title}, Price: {price}, Discount: {discount}, Link: {link}")

        data['Title'].append(title)
        data['Price'].append(price)
        data['Discount'].append(discount)
        data['Link'].append(link)

except Exception as e:
    print(e)

df = pd.DataFrame(data=data)

folder = r"C:\Users\M.Hashir Abdullah\Desktop\Python-Projects\WebScrapper"
output = os.path.join(folder, "Data.csv")
df.to_csv(output, index=False)