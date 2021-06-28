products = []

while True:
	name  = input('enter name of the product: ')
	if name == 'q' :
		break
	price = input('enter the price of the product: ')
	#products_attributes = []
	#products_attributes.append(name)
	#products_attributes.append(price)
	# same as above
	#products_attributes = [name, price]
	
	#products.append(products_attributes)
	# same as above
	products.append([name, price])

print(products)
print(products[0][0]) # first item of product with first item of the product_attributes