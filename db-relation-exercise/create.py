from app import db, Orders, Products, Orders_Products

db.drop_all()
db.create_all()

order1 = Orders(name ='first')
order2 = Orders(name ='second')
product1 = Products(name='Halo', price=15.99)
product2 = Products(name='COD', price=10.99)
product3 = Products(name='FIFA', price=5.99)
product4 = Products(name='GTA', price=25.99)

order_prod1= Orders_Products(orderbr=order1, productsbr=product1)
order_prod2= Orders_Products(orderbr=order1, productsbr=product2)
order_prod3= Orders_Products(orderbr=order2, productsbr=product3)
order_prod4= Orders_Products(orderbr=order2, productsbr=product4)


db.session.add(order1)
db.session.add(order2)
db.session.add(product1)
db.session.add(product2)
db.session.add(product3)
db.session.add(product4)
db.session.add(order_prod1)
db.session.add(order_prod2)
db.session.add(order_prod3)
db.session.add(order_prod4)
db.session.commit()

print(order1.name)
print(product1.name)
print(product1.price)
print(order_prod1.order_id)
print(order_prod2.order_id)
print(order_prod2.product_id)
print(order_prod3.order_id)
print(order_prod4.product_id)

print(order_prod1.orderbr.name)
print(order_prod3.orderbr.name)

# print(f"Cities in the UK are: {uk.cities[0].name}, {uk.cities[1].name}")
# print(f"London's country is: {ldn.country.name}")
# print(f"Manchester's country is: {ldn.country.name}")