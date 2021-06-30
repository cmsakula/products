products = []

while True:
	name  = input('enter name of the product: ')
	if name == 'q' :
		break
	price = int(input('enter the price of the product: '))
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

#for p in products: 
#	print(p)
#	print('item ', p[0], 'price is ', p[1])

#'abc' + '123' = 'abc123'
#'acc' * 3 = 'abcabcabc'

with open('products.csv', 'w', encoding='utf-8') as f: # with is used to automatically close the file without explicitly close it
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
		