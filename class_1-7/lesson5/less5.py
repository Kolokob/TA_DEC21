from faker import Faker

data = Faker()
my_dict = {'name': data.name(), 'address': data.address()}
print(my_dict)


class Person:

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
