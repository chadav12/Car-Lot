# Car lot program
from collections import namedtuple
# Separators horizontal and vertical
seperator = "-"*15
# Car Namedtuple being used
car1 = namedtuple("Car1", ["Make", "Model", "Price"])
Mazda = car1("Mazda", "sport", 10000)
car2 = namedtuple("Car2", ["Make", "Model", "Price"])
Chevy = car2("Chevrolet", "S10", 15000)
car3 = namedtuple("Car3", ["Make", "Model", "Price"])
Ford = car3("Ford", "Ranger", 18000)
car4 = namedtuple("Car4", ["Make", "Model", "Price"])
Ford_F150 = car4("Ford", "F-150", 25000)

# Print statements Make Model and Price...
print("John's Car Lot!")
print(seperator)
print(f"Make:  |{Mazda.Make:}\nModel: |{Mazda.Model:}\nPrice: |${Mazda.Price:,}")
print(seperator)
print(f"Make:  |{Chevy.Make:}\nModel: |{Chevy.Model:}\nPrice: |${Chevy.Price:,}")
print(seperator)
print(f"Make:  |{Ford.Make:}\nModel: |{Ford.Model:}\nPrice: |${Ford.Price:,}")
print(seperator)
print(f"Make:  |{Ford_F150.Make:}\nModel: |{Ford_F150.Model:}\nPrice: |${Ford_F150.Price:,}")
print(seperator)