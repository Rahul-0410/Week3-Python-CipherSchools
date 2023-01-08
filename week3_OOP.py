# class Person:
#     def __init__(self,first_name,last_name,age):
#         print('init method called')
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age

# p1=Person('Harshit','Vashistha',24)
# p2=Person('Rahul','Gupta',20)
# print(p1.first_name)
# print(p2.first_name)

# Excercise1
# class Laptop:
#     def __init__(self,brand,model_name,price):
#         self.brand=brand
#         self.model_name=model_name
#         self.price=price
#         self.model=brand+' '+model_name

# i1=Laptop('Dell','Vostro',70000)
# i2=Laptop('HP','Pavallion',65000)
# print(i1.brand)
# print(i1.model)

# OOP Instance Methods in Python
# class Person:
#     def __init__(self,first_name,last_name,age):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#     def above_age(self):
#         return self.age>18

# p1=Person('Ravi','Gupta',23)
# print(p1.full_name())
# print(p1.above_age())

# class Laptop:
#     def __init__(self,brand,model_name,price):
#         self.brand=brand
#         self.model_name=model_name
#         self.price=price
#         self.model=brand+' '+model_name
#     def apply_discount(self,num):
#         off_price=(num/100)*self.price
#         return self.price-off_price

# i1=Laptop('Dell','Vostro',70000)
# i2=Laptop('HP','Pavallion',65000)
# # print(i1.brand)
# # print(i1.model)
# print(i1.apply_discount(10))
# print(i1.apply_discount(20))

# class variable
# class Circle:
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def calc_circumfrance(self):
#         return 2*Circle.pi*self.radius

# c=Circle(4)
# print(c.calc_circumfrance())

# class Laptop:
#     discount_percent=10
#     def __init__(self,brand,model_name,price):
#         self.brand=brand
#         self.model_name=model_name
#         self.price=price
#         self.model=brand+' '+model_name
#     def apply_discount(self):
#         off_price=(self.discount_percent/100)*self.price
#         # off_price=(Laptop.discount_percent/100)*self.price
#         return self.price-off_price

# # Laptop.discount_percent=0
# i1=Laptop('Dell','Vostro',70000)
# i2=Laptop('HP','Pavallion',65000)
# i2.discount_percent=50
# print(i1.apply_discount())
# print(i2.apply_discount())
# print(i1.__dict__)

# Excercise 3
# class Person:
#     count_instance=0
#     def __init__(self,name,age):
#         Person.count_instance+=1
#         self.name=name
#         self.age=age
        
# p1=Person('Rahul',20)
# p1=Person('Raj',21)
# print(Person.count_instance)

# OOP Class Methods in Python
# class Person:
#     count_instance=0
#     def __init__(self,first_name,last_name,age):
#         Person.count_instance+=1
#         self.first_name=first_name
#         self.last_name=last_name
#         self.full_name=first_name+""+last_name
#         self.age=age
#     @classmethod
#     def from_string(cls,string):
#         first_name,last_name,age=string.split(',')
#         return cls(first_name,last_name,age)
#     @classmethod
#     def count_instances(cls):
#         return f"You have created {cls.count_instance} instances of {cls.__name__} class"
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#     def above_age(self):
#         return self.age>18
#     @staticmethod
#     def hello():
#         print('hello static method code')

# p1=Person('Ravi','Gupta',23)
# p2=Person('Rahul','Gupta',20)
# p3=Person.from_string('Raj, verma, 19')
# print(p3.full_name)

# Encapsulation, Abstraction, Naming Convention, Name Mangling in Python
# class Phone:
#     def __init__(self,brand,model_name,price):
#         self.brand=brand
#         self.model_name=model_name
#         # self._price=price
#         self.__price=price

#     def make_a_call(self,phone_number):
#         print(f"calling {phone_number}...")

#     def full_name(self):
#         return f"{self.brand} {self.model_name}"

#     def send_message(self):
#         pass

# _name convention of private name 
# __name__ dunder method 
# phone1=Phone('Nokia','1100',1000)
# # print(phone1._price)
# print(phone1._hone__price)
# print(phone1.__dict__)

# class Phone:
#     def __init__(self,brand,model_name,price):
#         self.brand=brand
#         self.model_name=model_name
#         self._price=max(price,0)
        # if price >0:
        #     self._price=price
        # else:
        #     self._price=0

        # self.complete_specification=f"{self.brand} {self.model_name} and price {self._price}"
#     def complete_specification(self):
#         return f"{self.brand} {self.model_name} and price {self._price}"
#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self,new_price):
#         self.price=max(new_price,0)


#     def make_a_call(self,phone_number):
#         print(f"calling {phone_number}...")

#     def full_name(self):
#         return f"{self.brand} {self.model_name}"

# phone1=Phone('Nokia','1100',1000)
# phone1._price=500
# print(phone1.brand)
# print(phone1.model_name)
# print(phone1.price)
# print(phone1.complete_specification())

# Inheritance 
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)

    
    def make_a_call(self,number):
        print(f"calling {number}...")

    def full_name(self,):
        return f"{self.brand} {self.model_name}"
class Smartphone(Phone):
     def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        # Phone.__init__(self,brand,model_name,price)
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera

     def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

# class Smartphone2(Phone):
#      def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
#         # Phone.__init__(self,brand,model_name,price)
#         super().__init__(brand,model_name,price)
#         self.ram=ram
#         self.internal_memory=internal_memory
#         self.rear_camera=rear_camera
#      def make_a_call(self,number):
#         print(f"calling {number}...")

class FlagshipPhone(Smartphone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera=front_camera
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price} and front camera= {self.front_camera}"


# phone=Phone('nokia','1100',1000)
smartphone=Smartphone('oneplus','5',30000,'6GB','64GB','20MP')
# print(smartphone.full_name())
# print(smartphone.rear_camera)
flagship1=FlagshipPhone('oneplus','9',30000,'6GB','64GB','20MP','16MP')
# print(flagship1.full_name())
# print(help(Smartphone))

# isinstance
# print(isinstance(flagship1,Smartphone))
# print(isinstance(smartphone,FlagshipPhone))

# issubclass
# print(issubclass(Smartphone,Phone))
# print(issubclass(FlagshipPhone,Smartphone))

#Multiple inheritance 
class A:
    def class_a_method(self):
        return 'I\'m just a class A method'
    def hello(self):
        return 'hello from class A'

isinstance_a=A()
# print(isinstance_a.class_a_method())

class B:
    def class_b_method(self):
        return 'I\'m just a class B method'
    def hello(self):
        return 'hello from class B'

class C(A,B):
    pass
isinstance_c=C()
# print(isinstance_c.class_a_method())
# print(isinstance_c.class_b_method())
# print(C.mro())
print(help(C))

