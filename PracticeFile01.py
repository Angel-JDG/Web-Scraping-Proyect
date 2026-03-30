# This file is for testing web scraping and file handling in 
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

page_response = requests.get(url, headers=headers)
print(page_response.status_code)

soup = BeautifulSoup(page_response.text, "html.parser")
tables = soup.find_all("table", class_ = ["wikitable", "sortable"])

table1 = tables[0] # Get the first table
table2 = tables[1] # Get the second table

table_select = input("Which table do you want to extract data from? (1 or 2): ")

# Obtain the data from the selected table
while True:

    if table_select == "1":
        column_data = table1.find_all("tr")
        for row in column_data:
            cells = row.find_all("td")
            individual_data = [cell.text.strip() for cell in cells]
            print(individual_data)
        break
    elif table_select == "2":
        column_data = table2.find_all("tr")
        for row in column_data:
            cells = row.find_all("td")
            individual_data = [cell.text.strip() for cell in cells]
            print(individual_data)
        break
    else:
        print("Invalid input. Please enter '1' or '2'.")