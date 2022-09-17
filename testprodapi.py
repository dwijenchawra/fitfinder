from pyvisionproductsearch.ProductSearch import ProductSearch, ProductCategories

# Initialize ProductSearch with your credentials

ps = ProductSearch("neat-dynamo-362802", 'neat-dynamo-362802-b8eb099a1f3f.json', 'hello_wrdl123')

# Create a new product set
productSet = ps.createProductSet('my_test_set')

# Create a new product
product = ps.createProduct('my_fancy_shirt', ProductCategories.APPAREL)

# Add a reference image to a product
product.addReferenceImage('download.jpeg')

# List all reference images for a product
for img in product.listReferenceImages():
    print(img)

# Add a product to a product set
product.addProduct(product)

# List all products in a product set
for p in productSet.listProducts():
    print(p)

# Search for similar products by image
productSet.search(ProductCategories.APPAREL, file_path='download.jpeg')
