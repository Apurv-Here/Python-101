# Python OOPS

"""
o/p:



"""

# CLASS

a = 2;
print(type(a));

# a is a variable but a is also an object of class int
# class ka naam should be in pascal case
# ThisIsPascalCase, thisIsCamelCase, this_is_snake_case


"""
o/p:

<class 'int'>

"""



# List is also class but why its object is like this?

L = [1, 2, 3];

# Because list is an built in class and it uses object literals



# Another way to create list and strings

Lt = list()
print(Lt)

print()

city = str()
print(city)
print(type(city))

"""
o/p:

[]


<class 'str'>

"""


# 


# Function Vs Methods : Methods are just functions inside class

# function
L = [1,2,3]
len(L)
# this len is a funtion
print(len(L))


L.append(5);
print(L)
# this append is a method


"""
o/p:

3
[1, 2, 3, 5]

"""




# Creating an ATM workflow

# In the atm class we have declared two variables pin and account balance. variables sirf self k under hi declare karna hai

class Atm:
    
    # Constructor
    def __init__(self):
        
        self.pin = ""
        self.balance = 0
        
        self.menu()
        
    
    def menu():
        pass





# Constructor ek special method hai jiske andar ka code automatically run hota hai jab aap class ka object banate ho

class ConstructorEg:
    
    def __init__(self):
        
        print("Print ho gya self wala constructor")
        
        
obj1 = ConstructorEg()

# obj1 k line execute hote hi constructor run ho gya jisme print statement tha

# Python me constructor ka naam hamesha __init__ hi hona chaiye


"""
o/p:

Print ho gya self wala constructor

"""






class Atm:
    
    # Constructor
    def __init__(self):
        
        self.pin = ""
        self.balance = 0
        
        self.menu()
        
        
        
    # jab bhi koi method banega to usse input me self dena hai (mandatory)
    
    def menu(self):
        
        # for input we will use triple inverted comma for multi line string
        
        user_input = input("""
                        Hello, how would you like to proceed?
                        1. Enter 1 to create pin.
                        2. Enter 2 to deposit.
                        3. Enter 3 to withdraw.
                        4. Enter 4 to check balance.
                        5. Enter 5 to exit.
        """)
    
        
        if user_input == "1":
            print("Create pin")
        elif user_input == "2":
            print("Withdraw")
        elif user_input == "3":
            print("Deposit")
        elif user_input == "4":
            print("Balance")
        else:
            print("Bye")


            
sbi = Atm()

"""
o/p:

                        Hello, how would you like to proceed?
                        1. Enter 1 to create pin.
                        2. Enter 2 to deposit.
                        3. Enter 3 to withdraw.
                        4. Enter 4 to check balance.
                        5. Enter 5 to exit.
         5
Bye

"""




class Atm:
    
    # Constructor
    def __init__(self):
        
        self.pin = ""
        self.balance = 0
        
        self.menu()
        
        
        
    # jab bhi koi method banega to usse input me self dena hai (mandatory)
    
    def menu(self):
        
        # for input we will use triple inverted comma for multi line string
        
        user_input = input("""
                        Hello, how would you like to proceed?
                        1. Enter 1 to create pin.
                        2. Enter 2 to deposit.
                        3. Enter 3 to withdraw.
                        4. Enter 4 to check balance.
                        5. Enter 5 to exit.
        """)
    
        
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Bye")
            
            
    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Print set successfully")
        
        
    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            self.balance = self.balance + amount
            print("Deposit successful")
        else:
            print("Invalid pin")
            
            
    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Withdrawal successful")
            else:
                print("Insufficient funds")
        else:
            print("Invalid pin")
            
            
    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")

            
sbi = Atm()
hdfc = Atm()

"""
o/p:

                        Hello, how would you like to proceed?
                        1. Enter 1 to create pin.
                        2. Enter 2 to deposit.
                        3. Enter 3 to withdraw.
                        4. Enter 4 to check balance.
                        5. Enter 5 to exit.
         2
Enter your pin:  1111
Invalid pin

"""






# What is instance variables?

# Wo variables jo constructor me hote hai aur unki value har alag object k hisaab se change hoti hai, Eg: pin aur balance atm waale example me.





# Encapsulation

# jaise java me access modifiers hote hai public or private waise hi python me same hote hai bas underscore se defined hote hai wo, directly java jaise public ya private nhi likh sakte


# Atm waale example me abhi pin aur balance open data hai, koi bhi naya object unhe dot ki help se directly dekh sakta hai aur change bhi kar sakta hai jo ki achi practice nhi hai. To is liye ham self.pin = "", aur self.balance = 0, se set karenegne taaki ye private ban jae. Ab inhe sirf class me hi access kiya jaa sakta hai, object directly access nhi kar sakta.


# Ham double underscore laga ki class k methods ko bhi hide kar sakte hai ya private bana sakte hai


# Now we will use getters and setters

class Atm:
    
    def __init__(self):
        
        # making the variables private
        self.__pin = "";
        self.__balance = 0;
        
    def get_pin(self):
        return self.__pin;
    
    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin;
            print("Pin changed");
        else:
            print("Not allowed");
        
        
if __name__ == "__main__":
    sbi = Atm();

# jab ham sbi = Atm() likhte hai tab sbi ek object nhi hai wo bas ek variable hai jisne reference value store kar rakhi hai jahan be Atm() craete ho rakha hai, to sbi ek reference variable hai





# Pass By Reference

class Customer:
    
    def __init__(self, name, gender):
        self.name = name;
        self.gender = gender
        
def greet(customer):
    if customer.gender == "Male":
        print("Hello, ", customer.name, " sir.");
    else:
        print("Hello, ", customer.name, " ma'am.");
        
        
        
        
cust = Customer("Nitish", "Male");

greet(cust);

"""
o/p:

Hello,  Nitish  sir.

"""




class Customer:
    
    def __init__(self, name):
        self.name = name;
        
def greet(customer):
    print(id(customer));
        
        
        
        
cust = Customer("Nitish");

print(id(cust));

greet(cust);

"""
o/p:

134550080700032
134550080700032

"""

# both the address value from print as well as greet function will be same

# It works like alias, a = 3, b = a, so a and b will have same value


class Customer:
    
    def __init__(self, name):
        self.name = name;
        
def greet(customer):
#     print(id(customer));
    customer.name = "Ankita";
    print("Greet function ka print: ", customer.name);
    
        
        
        
        
cust = Customer("Nitish");
print("Main fun ka print, changes k pehle: ", cust.name);

# print(id(cust));

greet(cust);

print("Main function ka print: ", cust.name);


"""
o/p:

Main fun ka print, changes k pehle:  Nitish
Greet function ka print:  Ankita
Main function ka print:  Ankita

"""


# Jab hamne object ko pass kara greet function me tab wo by reference pass hua 
# aur ham jab changes karenge object me to main object me saare changes hote chale jaenge, 
# kyunki main object aur greet object same name "Nitish" ko poin kar rhe the 
# to is liye jab change hoga kahin se bhi to Nitish ka naam change ho jaega.

# Ek aur cheez jab ham class ka id print karenge tab wo same hi rahega,

# Python me class ka objects are mutable, like list, dict and sets.



# We can loop an object also

class Customer:
    
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        
    def intro(self):
        print("I am", self.name, "and I am", self.age);
        
# main function

c1 = Customer("Nitish", 34);
c2 = Customer("Ankita", 45);
c3 = Customer("Neha", 3);

L = [c1, c2, c3];

for i in L:
    i.intro();


"""
o/p:

I am Nitish and I am 34
I am Ankita and I am 45
I am Neha and I am 3

"""




# STATIC

# Instance variable: Har object k liye value different hoti hai. Eg: pin ya balance customer ka.


#Static: Ye ek class variable hota hai, isme har object k liye static variable ki value same hoti hai. 
# Eg: IFSC code, it should be same for all customers for specific branch.


# Static variable hamesha constructor k bahar hota hai.


# Instance variables hamesha constructor k andar rehte hai.

# Instance variable ko access karne k liye self ka use hota hai but 
# static variable ko access karne k liye class ka naam use hota hai, see below example.

class Atm:
    
    # static variable
    counter = 1;
    
    def __init__(self):
        #instance variable
        self.__pin = "";
        self.__balance = 0;
        # Assigning serial no as 1, 2, 3 to cust
        self.sno = Atm.counter;
        Atm.counter = Atm.counter + 1;
        
        
c1 = Atm();
c2 = Atm();
c3 = Atm();

print(c1.sno);
print(c2.sno);
print(c3.sno);
print(Atm.counter);
# Since counter is 4 set, so if you access via c1, c2 or c3 
# it will be same
print(c1.counter);
print(c3.counter);


"""
o/p:

1
2
3
4
4
4

"""

# Now the problem is anyone can change the counter value directly 
# like change its value to string then the code will not work bcz 
# we have implemented addidtion of 1 to counter.


# To resolve this issue we will make counter private with the help of double underscore 
# and we can then change counter with the help of getters and setters.


class Atm:
    
    # static variable
    __counter = 1;
    
    def __init__(self):
        #instance variable
        self.__pin = "";
        self.__balance = 0;
        # Assigning serial no as 1, 2, 3 to cust
        self.sno = Atm.__counter;
        Atm.__counter = Atm.__counter + 1;
        
    
    # We do not need self because static variables or methods are accessesible by class name 
    # and self is used to pass the object 
    # and thus no object is used to use the static methods and variables so we do not need to pass the self value in argument
    
    @staticmethod
    def get_counter():
        return Atm.__counter;
    
    @staticmethod
    def set_counter(new_counter_val):
        if type(new_counter_val) == int:
            Atm.__counter = new_counter_val;
        else:
            print("Not Allowed");
        
        
        
# Main method

print(Atm.get_counter());
Atm.set_counter(5);
print(Atm.get_counter());



"""
o/p:

1
5

"""


# When we work in big projects there are multiple classes involved interlinking with each other.

# There are mainly two ways we can link classes, one is aggregation and other one is inheritance.

# Aggregation is called (has a relationship). Inheritance is called (is a relationship).


# Aggregation

class Address:
    
    def __init__(self, city, pincode, state):
        self.city = city;
        self.pincode = pincode;
        self.state = state;
        
     
    
add1 = Address("Noida", 200510, "UP");
cust = Customer("Nitish", "Male", add1);

print("This will print address object: ", cust.address);
print(cust.address.city);


"""
o/p:

This will print address object:  <__main__.Address object at 0x791f9ab26920>
Noida

"""


# Inheritance

class User:
    
    def login(self):
        print("Login");
        
    def register(self):
        print("Register");
        

# Inheritance
# Now student can access all data memebers and function on user as well
class Student(User):
    
    def enroll(self):
        print("Enroll");
        
    def review(self):
        print("Review");
        
        
stu1 = Student();

stu1.enroll();
stu1.rveiew();
stu1.login();
stu1.register();

# Student can access its methods as well as User method 
# bcz it has inherted those from User class
# Note: User class object cannot access other methods other than its own




# Inheriting Constructors

class Phone:
    
    def __init__(self, price, brand, camera):
        print("Inside phone constructor");
        self.price  = price;
        self.brand = brand;
        self.camera = camera;
        

class SmartPhone(Phone):
    pass;


# Main function

s = SmartPhone(20000, "Apple", 13);
print(s.brand);


"""
o/p:

Inside phone constructor
Apple

"""

class Phone:
    
    def __init__(self, price, brand, camera):
        print("Inside phone constructor");
        self.price  = price;
        self.brand = brand;
        self.camera = camera;
        

class SmartPhone(Phone):
    def __init__(self):
        print("Inside Smart phone constructor");
    


# Main function

s = SmartPhone();


"""
o/p:

Inside Smart phone constructor

"""



# Inheriting Private members

class Phone:
    
    def __init__(self, price, brand, camera):
        print("Inside phone constructor");
        self.price  = price;
        # Making brand a private member
        self.__brand = brand;
        self.camera = camera;
        

class SmartPhone(Phone):
    pass;


# Main function

s = SmartPhone(20000, "Apple", 13);
print(s.__brand)

# Earlier when brand was not private it could access that
# But when you make the brand private it is unable to access it


"""
o/p:

Inside phone constructor

"""


# Child class member cannot access hidden members of parent class



# Method Overriding -> Polymorphism

class Phone:
    
    def __init__(self, price, brand, camera):
        self.__price = price;
        self.brand = brand;
        self.camera = camera;
        
    def buy(self):
        print("Buying a phone");
        
class SmartPhone(Phone):
    
    def buy(self):
        print("Buying a smartphone");
        
s = SmartPhone(20000, "Apple", 13);

s.buy();

# note there are 2 buy functions
# one in Smartphone and one in phone
# Here smartphone one will run
# We have craeted the method with the same name in the child class
# This very thing is called method overridng



# Polymorphism has mainly 3 things, Method Overriding, Method Overloading, Operator Overloading


# Agar child k pass constructor nhi hai to parent ka constructor apne aap invoke ho jata hai.



# Agar child k paas apna constructor hai aur uska object bana child ka to child ka hi constructor run hota hai parent ka nhi


class parent:
    
    def __init__(self, num):
        self.__num = num;
        
    def get_num(self):
        return self.__num;
    
class Child(Parent):
    
    def __init__(self, val, num):
        self.__val = val;
        
    def get_val(self):
        return self.__val;
    

    
son = Child(100, 10);

print("Parent: Num : ", son.get_num());

# ye code error dega
# kyunki Child ka object bana aur uska constructor run hua bas
# Parent ka constructor run nhi hua
# Child k constructor me bas val ko set kara num ko nhi
# Aur print k line me ham get_num  function ko invoke kar rhe
# jisme parent ka num set hi nhi kara to kaise return karega wo num




# Super keyword


# super keyword sirf class k andar rehna chaiye, jaise ki main method me jaake super likhoge to kaam nhi karega


# super constructor me first statement hona chaiye


class Phone:
    
    def __init__(self, price, brand, camera):
        self.__price = price;
        self.brand = brand;
        self.camera = camera;
        print("Inside Phone constructor")
        
    def buy(self):
        print("Buying a Phone");
    
    
class SmartPhone(Phone):
    
    def buy(self):
        print("Buying a smartphone");
        super().buy();
            
            
# Main method

s = SmartPhone(20000, "Apple", 13);

s.buy();


"""
o/p:

Inside Phone constructor
Buying a smartphone
Buying a Phone

"""


# Super example with constructor

class Phone:
    
    def __init__(self, price, brand, camera):
        print("Inside Phone constructor");        
        self.__price = price;
        self.brand = brand;
        self.camera = camera;
        
class SmartPhone(Phone):
    
    def __init__(self, price, brand, camera, os, ram):
        print("pehle Samrtphone constructor ka print")
        super().__init__(price, brand, camera);
        self.os = os;
        self.ram = ram;
        print("Inside smartphone constructor");
        
        
s = SmartPhone(20000, "Samsung", 12, "Android", 2);

print(s.os);

print(s.brand);


"""
o/p:

pehle Samrtphone constructor ka print
Inside Phone constructor
Inside smartphone constructor
Android
Samsung

"""


# Types of Inheritance

# Single level, multi level, heirarchical, multiple (not in java) & hybrid (combination of above 4)


# Multi level inheritance Example

class Product:
    
    def review(self):
        print("Product customer review");
        
class Phone(Product):
    
    def __init__(self, price, brand, camera):
        print("Inside phone constructor");
        self.__price = price;
        self.brand = brand;
        self.camera = camera;
        
    def buy(self):
        print("Buying a phone");
        
class SmartPhone(Phone):
    pass

# Main Function

s = SmartPhone(20000, "Apple", 13);
p = Phone(1000, "Samsung", 1);

s.buy();
s.review();
p.review();


"""
o/p:

Inside phone constructor
Inside phone constructor
Buying a phone
Product customer review
Product customer review

"""


# Heirarchical inheritance Example

class Phone:
    
    def __init__(self, price, brand, camera):
        print("Inside phone constructor");
        self.__price = price;
        self.brand = brand;
        self.camera = camera;
        
    def buy(self):
        print("Buying a phone");
        
    def return_phone(self):
        print("Returning a phone");
        
class SmartPhone(Phone):
    pass;

class FeaturePhone(Phone):
    pass;

SmartPhone(1000, "Apple", "13px").buy();



"""
o/p:

Inside phone constructor
Buying a phone

"""


# Multiple Inheritance

class Phone:
    
    def __init__(self, price, brand, camera):
        print("Inside phone constructor");
        self.__price = price;
        self.brand = brand;
        self.camera = camera;
        
    def buy(self):
        print("Buying a phone");
        
class Product:
    
    def review(self):
        print("Customer review");
        
class SmartPhone(Phone, Product):
    pass;


# Main function

s = SmartPhone(2000, "Apple", 13);

# SInce SamrtPhone doesn't have a constructor so Phone constructor will be invoked
# Why phone constructor is invoked?
# Bcz it is written first, If phone did not had a constructor then it will jump to invoke Product constructor
# It follows the order of whatever is written first



"""
o/p:

Inside phone constructor

"""


# There could be a situation of conflict in multiple inheritance


class Phone:
    
    def __init__(self, price, brand, camera):
        print("Inside phone constructor");
        self.__price = price;
        self.brand = brand;
        self.camera = camera;
        
    def buy(self):
        print("Phone buy method");
        
class Product:
    
    def buy(self):
        print("Product buy method");
        
class SmartPhone(Product, Phone):
    pass;


# Main function

s = SmartPhone(2000, "Apple", 13);

s.buy();

# Now buy is in both Phone and Product which buy should run?
# Product buy will run bcz Product is written first in SamrtPhone argument



"""
o/p:

Inside phone constructor
Product buy method

"""


# Polymorphism: 1. Method Overriding, 2. Method Overloading, 3. Operator Overloading

class geometry:
    
    # Circle area method
    def area(self, radius):
        return 3.14 * radius * radius;
    
    # Rectangle area method
    def area(self, l, b):
        return l*b;
    
obj = geometry();

obj.area(4);

# This will throw error
# This is fine in java but you cannot have same method name with different arguments in pyhton
# Only rectangle area method will work bcz it has done method overriding of circle area



# Method overloading does not work in python

# Trick

class Geometry:
    
    def area(self, a, b = 0):
        
        if b == 0:
            print("Circle", 3.14 * a * a);
        else:
            print("Rect", a * b);
            
obj = Geometry();
obj.area(4);
obj.area(4, 5);


"""
o/p:

Circle 50.24
Rect 20

"""

