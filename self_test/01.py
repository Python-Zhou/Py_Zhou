# test1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print('餐厅正在营业')

restaurant = Restaurant('lalala','kakaka')
print(restaurant.cuisine_type,restaurant.restaurant_name)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# test2
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name, self.last_name)

    def greet_user(self):
        print('welcome {0}'.format(self.first_name+self.last_name))

customer1 = User('Yu', 'Zhou')
customer1.describe_user()
customer1.greet_user()

