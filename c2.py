class Cat:
    # constructor
    def __init__(self, name, age, breed):
        # syntax for instance_variable
        # self.<attribute> = <parameter>
        self.name = name
        self.age = age
        self.breed = breed

Cat1 = Cat('Soni', 3, 'Persian')
Cat2 = Cat('Mia', 2, 'Siamese')
Cat3 = Cat('Molly', 4, 'Egyptian Mau')

print(Cat1.name, Cat1.age, Cat1.breed)
print(Cat2.name, Cat2.age, Cat2.breed)
print(Cat3.name, Cat3.age, Cat3.breed)

        