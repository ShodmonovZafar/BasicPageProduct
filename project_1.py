import requests
from bs4 import BeautifulSoup
 
page = requests.get('https://www.imdb.com/chart/top/')  # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser')  # Parsing content using beautifulsoup
 
links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
first10 = links[:10] # Keep only the first 10 anchors
for anchor in first10:
    print(anchor.text) # Display the innerText of each anchor

def get_product(data: str) -> str:
    """
    Get the product name from the data string.
    Args:
        data (str): The HTML string.

    Returns:
        str: The product name in CSV format.
    """
    # list of products
    products = ['Product Name, Product Price, Product Description']

    soup = BeautifulSoup(markup=data, features='html.parser')
    # get div tags
    product_tags = soup.find_all('div', class_='product')
    for div in product_tags:
        # get product name
        product_name = div.h3.text
        # get price
        price = div.find('p', class_='price').text
        # get description
        description = div.find('p', class_='description').text

        products.append(','.join([product_name, price, description]))
    
    # convert to str
    products_str = '\n'.join(products)
    return products_str

def save_product(product:str) -> None:
    """Save the product name to the CSV file.

    Args:
        product (str): The product name in CSV format.
    """
    with open('products.csv', 'w') as f:
        f.write(product)

# Open the file and read the HTML string
# with open('html/product1.html', 'r') as f:
#     data = f.read()

# Get the product name in CSV format
product_csv=get_product(soup.prettify()) 
# Save the product name to the CSV file
save_product(product_csv) 
