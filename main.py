import requests
import functions as func
from bs4 import BeautifulSoup


# Step 1: Find the URL that you want to scrape.
page_1 = requests.get('http://example.com/')  # Step 1.1
soup_1 = BeautifulSoup(page_1.content, 'html.parser')  # Step 1.2

# Step 5: Run the code and extract the data.
csv_h1 = func.get_h1(soup_1)  # Step 5.1
#print(csv_h1)  # Step 5.2

# Step 6: Store the data in the required format.
path_csv_file_1 = "csv_files/data_1.csv"  # Step 6.1
func.save_data_to_csv(csv_h1, path_csv_file_1) 
