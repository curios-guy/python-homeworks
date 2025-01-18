class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def can_talk(self):
        print("Somehow this person can talk, intereesting...")
        

    def __str__(self):
        return f"{self.name} is great person, he is {self.age} years old"
         

    

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def sing(self):
        print("HeeeHaaaa!!!")
        
    
    def __str__(self):
        return super().__str__()

student1 = Student("Alish", 12, "STEM")
print(str(student1))
student1.can_talk()
student1.sing()


class NewList(list):
    def __init__(self, *args):
        for item in args:
            if not isinstance(item, (int, float)):
                raise ValueError
        super().__init__(args)

    def sum(self):
        return sum(item for item in self)
    
    def append(self, object):
        return super().append(object)

class MyDict(dict):
    def inverter(self, is_inversted = False):
        if is_inversted:
            for keys, values in self.items():
                self[values] = keys

        else: return MyDict({ values:keys for keys, values in self.items()})

my_dict = MyDict(a=1, b=2, c=3)
print(my_dict)

a = my_dict.inverter()
print(a)


class PrimePerson():
    def __init__(self, name, age):
        if not isinstance(name, str) or name == "":
            raise ValueError(f"Name can't be {name}")
        else: 
            self.name = name
            print("Changed!!!")

        if not isinstance(age, int) or age < 0:
            raise ValueError(f"Age can't be {age}")
        else: self.age = age

    def get_name(self):
        return self.name

    def set_name(self, value):
        if not isinstance(value, str) or value == "":
            raise ValueError(f"Name can't be {value}")
        else: self.name = value

    def get_age(self):
        return self.age

    def set_age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"Age can't be {value}")
        else: self.age = value

class AverageList(list):

    @property
    def average(self):
        return sum(self) / len(self)

avg1 = AverageList([1,3,5,2])
avg1.average

person1 = PrimePerson("salom", 12)
print(person1.get_age())
print(person1.set_name("salom"))
