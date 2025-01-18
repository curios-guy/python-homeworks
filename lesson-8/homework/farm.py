
# type verifiers
def str_verifier(string):
    if not isinstance(string, str) or string == "":
            return True
    else: return False

def num_verifier(number):
    if not isinstance(number, int) or number < 0 or number == 0:
            return True
    else: return False

def float_verifier(float_num):
    if not isinstance(float_num, (int, float)) or float_num == 0 or float_num < 0:
        return True
    else: return False

def bool_verifier(bool_val):
    if not isinstance(bool_val, bool):
        return True
    else: return False
# main class
class Animal():
    def __init__(self, name, age, weight):
        if num_verifier(age):
            raise ValueError(f"age can't be {age}")
        else: 
            self.age = age

        if str_verifier(name):
            raise ValueError(f"name can't be {name}")
        else: self.name = name

        if float_verifier(weight):
            raise ValueError(f"weight can't be {weight}")
        else: self.weight = weight

    def __str__(self):
        return f"{self.name}  is {self.age} year(s) old and weights {self.weight}"
    
# sub-classes
class Cow(Animal):
    def __init__(self, name, age, weight, food):
        super().__init__(name, age, weight)
        if str_verifier(food):
            raise ValueError(f"food can't be {food}")
        else:
            self.food = food
        
    def eating(self):
        return f"Cow {self.name} loves eating {self.food}"
    
class Chicken(Animal):
    def __init__(self, name, age, weight, food):
        super().__init__(name, age, weight)
        if str_verifier(food):
            raise ValueError(f"food can't be {food}")
        else:
            self.food = food

    def eating_or_walking(self):
        if self.age > 2:
            return f"{self.name} is running for {self.food}"
        else: return f"{self.name} is too young and learning how to walk"

class Dog(Animal):
    def __init__(self, name, age, weight, on_guard = True):
        super().__init__(name, age, weight)
        if bool_verifier(on_guard):
            raise ValueError(f"bool can't be {on_guard}")
        else: 
            self.on_guard = on_guard

    def guarding(self):
        if self.on_guard and self.name == "Tuzik": return f"{self.name} is a good boy heehow! Rest in peace buddy"
        elif self.on_guard: return f"{self.name} is a good boy"
        else: return f"{self.name} is asleep"


class LilDog(Dog):
    def __init__(self, name, age, weight, on_guard=True, cute = True):
        super().__init__(name, age, weight, on_guard)
        if bool_verifier(cute):
            raise ValueError(f"bool can't be {cute}")
        else: 
            self.cute = cute

    def __str__(self):
        return f"{super().__str__()} and is so cute"

# doggy = Dog("Tuzik", 17, 12)
# doggy1= Dog("Apchalka", 2, 15)
# print(doggy.guarding())
# print(doggy)

# cow = Cow("Masha", 5, 120, "weed") #yea weed
# print(cow.eating())

# chicky = Chicken("Joja", 2, 12, "don")
# print(chicky.eating_or_walking())

# lildoggy = LilDog("Apachi", 2, 12)
# print(lildoggy)