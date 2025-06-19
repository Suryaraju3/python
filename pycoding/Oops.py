#Oops concepts
# class
# object
# Inheritance
# Polymorphism
# Abstraction 
# Encapsulation

#class - It's blue print which consist of properties and functionalities or state and behaviours 
#object - instance of a class 
# class Peacoke():
#     def __init__(self,name):
#         self.name=name
#     def scream(self):
#         return f"{self.name} scram."
# pke=Peacoke("peacock")
# print(pke.scream())

# Inheritance
# Inheriting the state and behaviour from parents class to child class is known as inheritance.
# five types 
#1.single level inheritance
# class Onepuls_v1:
#     def battery_v1(self):
#         print("Mobile heat temperature notification not shown.. ")
# class Onepluls_v2(Onepuls_v1):
#     def battery_v2(self):
#         print("Now showing mobile temperature notifictaion")
# obj=Onepluls_v2()
# obj.battery_v1()
# obj.battery_v2()

#2.multilevel inheritance
#latest model release
# class Bmw_lv1:
#     def v1(self):
#         print("BMW 3 Series LWB:")
# class Bmw_lv2(Bmw_lv1):
#     def v2(self):
#         print("updated BMW X3")
# class Bmw_lv3(Bmw_lv2):
#     def v3(self):
#         print("BMW iX1 LWB")      
# bmw=Bmw_lv3()  
# bmw.v1()
# bmw.v2()
# bmw.v3()

# Hierarchical 
# class whatsapp:
#     def m_ai(self):
#         print("meta ai")
# class Install(whatsapp):
#     def install(self):
#         print("install")
# class Thread(whatsapp):
#     def thread(self):
#         print("thread")
# ins=Install()
# ins.install()
# ins.m_ai()
# thre=Thread()
# thre.thread()
# thre.m_ai()

# 4.multiple inheritance
# class Wapp_v1:
#     def chat(self):
#         print("Chatting")
# class Wapp_v2:
#     def contact(self):
#         print("Contact")
# class Wapp_v3:
#     def document(self):
#         print("Document")
# class Wapp_v4:
#     def camara(self):
#         print("Camara")
# class Wapp_v5:
#     def audio(self):
#         print("Audio")
#     def location(self):
#         print("Location")
# class Wapp_v6:
#     def quick_replay(self):
#         print("Quick Replay")
#     def poll (self):
#         print("Poll")
# class Wapp_v7(Wapp_v1,Wapp_v2,Wapp_v3,Wapp_v4,Wapp_v5,Wapp_v6):
#     def event(self):
#         print("Event")
# obj1=Wapp_v7()
# obj1.chat()
# obj1.contact()
# obj1.document()
# obj1.camara()
# obj1.audio()
# obj1.location() 
# obj1.quick_replay()
# obj1.poll()
# obj1.event()       

# 5.hybrid
# class Animal:
#     def sound(self):
#         print("sound")
# class Lion(Animal):
#     def hunting(self):
#         print("hunting")
# class Tiger(Animal):
#     def speed(self):
#         print("speed")
# class Liger(Lion,Tiger):
#     def strength(self):
#         print("strength")
# ob1=Lion()
# ob1.hunting()
# ob1.sound()
# obj2=Tiger()
# obj2.speed()
# obj2.sound()
# obj3=Liger()
# obj3.hunting()
# obj3.sound()
# obj3.speed()
# obj3.strength()


# Polymorphism
#Object storing different behaiours of different stages of its life cycle is known as polimorphism.
#1.inbuild function
# s="Hello world"
# a=[1,2,3,5]
# b={1:1,2:2,3:4}
# print(len(s)) #11 String
# print(len(s)) #11 List
# print(len(b)) #3  Dict
# print(len(100)) #TypeError: object of type 'int' has no len()

# 2.using operater

# print("hi"+"hello") #hihello
# l1=[1,2,4]
# l2=[11,22,33]
# print(l1+l2) #[1, 2, 4, 11, 22, 33]
# print(l1*5)  #[1, 2, 4, 1, 2, 4, 1, 2, 4, 1, 2, 4, 1, 2, 4]
# print(l1-l2) #TypeError: unsupported operand type(s) for -: 'list' and 'list'

#3. using class 
# class Student:
#     def pay_bill(self):
#         print("loan")
# class Employee:
#     def pay_bill(self):
#         print("create card")
# class Manager:
#     def pay_bill(self):
#         print("house loan")
# s=Student()
# s.pay_bill()
# e=Employee()
# e.pay_bill()
# m=Manager()
# m.pay_bill()

# Abstract

# Declearing all the required functionality in the abstract class and providing implimantation in the subclass is known as abstraction.
#we can't create object for the abstract class.
#To create a abstract class and abstract method we need to import ABC and abstract method from libery called abc.
#we need to inherit all the abstract methods into the subclass and override all the abstract method.

# from abc import ABC,abstractmethod
# class Bank(ABC):
    
#     @abstractmethod
#     def pin_number(self):
#         pass
#     @abstractmethod
#     def ifsc_no(self):
#         pass
#     @abstractmethod
#     def account_no(self):
#         pass
    
#     def verify(self): #concrete method
#         print("verify")
        

# class secure(Bank):
#     def pin_number(self):
#         print("pin number")
#     def account_no(self):
#         print("account number")
#     def ifsc_no(self):
#         print("ifsc number")
#     def verify(self):
#         return super().verify()
    
# ob=secure()
# ob.account_no()
# ob.pin_number()
# ob.ifsc_no()
# ob.verify
    
# Encapsulation
#Declearing all the public variables into private and restricking in the access from one class to another class to avoid the accidental modification.

#1.public access specifer
# ->Any variable which is declear without using underscore we call it as a public access specifier.
# class Demo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# d=Demo('alice',34)
# print(d.name)
# print(d.age)

#2.producted access specifier
#->Any variable which is declear by pre fixing "_" is known as product access specifier
#->We can access outside the class but accourding to the convention we should not access outside the class.

# class Demo:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
# d1=Demo("smith",23)
# print(d1._name)
# print(d1._age)
        
#3.Private access specifier
#->Any variable which is declear by prefixing "__" is known as PVA.

# class Demo:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
# d1=Demo("surya",23)
# print(d1.__name) #AttributeError: 'Demo' object has no attribute '__name'
# print(d1.__age)  #AttributeError: 'Demo' object has no attribute '__name'


    