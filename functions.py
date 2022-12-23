from bs4 import BeautifulSoup

# Step 4: Write the code.
def get_h1(soup):
    csv = ['H1,']
    tags = soup.find_all('h1')

    for i in tags:
        column_0 = i.text
        csv.append(','.join([column_0]))
    
    # convert to str
    csv_str = '\n'.join(csv)
    return csv_str

def save_data_to_csv(data, path_csv_file):
    with open(path_csv_file, 'w') as f:
        f.write(data)

def get_product(data):
    
    products = ['Product Name, Product Price, Product Description']
    soup = BeautifulSoup(markup=data, features='html.parser')
    product_tags = soup.find_all('div', class_='product')

    for div in product_tags:
        product_name = div.h3.text
        price = div.find('p', class_='price').text
        description = div.find('p', class_='description').text
        products.append(','.join([product_name, price, description]))
    
    # convert to str
    products_str = '\n'.join(products)
    return products_str