from app import Food, db, Users

db.drop_all()
db.create_all()

testuser = Users(first_name='Grooty',last_name='Toot') # Extra: this section populates the table with an example entry
testuser1 = Users(first_name='John',last_name='Smith')
testuser_food = Food(food_name='Pizza',food_cost=10.99) # Extra: this section populates the table with an example entry
db.session.add(testuser)
db.session.add(testuser1)
db.session.add(testuser_food)
db.session.commit()