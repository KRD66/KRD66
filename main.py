print("hello world")
print("50+50")
print("hello, world")
if 5 > 2:
 print("five is greater than two!")
 x = 5
 y = "hello, world!"
 print(x)
 print(y)
 #This is a comment .
 print("Hello, World")
 #print("hello, world")
 print("cheers, mate!")


x = 5
x = "farouq"
print(x) 
x =str(3)
y = int(3)
z = float(3)
v = chr(3)
p = bool(3)

print(x)
print(y)
print(z)

x = 8
y = "3&"
print(type(x))
print(type(y))

x,y,z ="orange","banana","cherry"
print(x)
print(y)
print(z)

cars = ["toyota", "sienna", "mercedes"]
x,y,z = cars
print(x)
print(y)
print(z)
x = "awesome"

x = 5
print(type(x))

x = {"name" : "john", "age" : 36}





x = 7
y = 2.3
z = 1j
 
print(type(x))
print(type(y))
print(type(z))

#convert from int to float:
a = float(32)

#convert from float to int:
b = int(56.5)


print(a)
print(b)

print(type(a))
print(type(b))


import random
print(random.randrange(1, 50))


print("hello")


print("it's alright")
a = "hello"
print(a)

a = 5
print(a)

for x  in "1 2 3 4 5 6 7":
    print(x)
    
    a = "Loba, Tobi!"
    print(len(a))
    
    txt = "the best things in life are free"
    if "free" in txt:
        print("yes, 'free' is available")
        
        txt = "farouq is a backend developer"
        print("programmer" not in txt) 
        
        
        A = 5
        B = 6
        if A > B:
            print("yes")
        if B > A: 
            print("no")
            
            
            b = "Hailey, Arnold"
            print(b[2:2])
            
            a = "HELLO, WORLD!"
            print(a.lower())
            
            a = "Hello, World!"
            print(a.replace("Hell", "for"))
            
            a = "Hello, World"
            print(a.split(","))
            
            
            
            a = "loba"
            b = "Tobi"
            c = a + " " + b
            print(c)
            
            
            age = 19
            txt = f"My name is Hailey, I am {age}"
            print(txt)
            
            
            score = float(57)
            txt = f"your exam score is {score}"
            print(txt)
            
            price = 87
            txt = f"The price tag on the shirt is {price:.2f} dollars"
            print(txt)
            
txt = "we are the so called \"Gen z\" from 1990 ."
print(txt) 
print(10 >9)
print(10 == 9)
print(10 < 9)

a = 205
b = 75

if b > a:
    print("b is greater than a")
else:
    print("a is greather than b")
    
    x = 5
    print(x > 3 and x <10)
    
    x = 15
    y = 17
    print(x + y)
    
    thislist = ["farouq", "korede", "alexander", "arnold"]
    print(thislist)
    
    thislist = ["apple", "banana", "cherry"] 
    print(len(thislist))
    
    thislist = ["farouq", "taiwo", "korede","alexander", "arnold"]
    print(thislist[:4])
    
    thislist = ["banana","cherry"]
    if "apple" not in thislist:
        print("no,apple no dey here")
    else :
     print("yes,apple dey here")
     
thislist = ["apple", "banana","cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple","banana","cherry"]
thislist.append("pineapple")
print(thislist)

thislist = ["apple", "banana",]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist = ["apple","banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist = ["apple","banana","coconut"]
del thislist[1]
print(thislist)
thislist = ["apple", "banana", "cherry"]
for  x in thislist:
    print(x)
    fruits = ["apple", "coconut", "cherry"]
for farouq in fruits:
  if farouq == "banana":
    break
else:
   print(farouq)

for x in range(2, 100, 4) :
  print(x)
  
else:
    print("Finished!")
    
    flavor = ["red", "tropical", "cola"]
    fruits = ["orange", "pineapple", "apple"]
    
    for x in flavor:
      for y in fruits:
          print(x,y)
          
          
def my_function():
    print("Hello, this is a function")
my_function()
        
def my_function(fname):
    print(fname + " Raji")
my_function("farouq")
my_function("fawaz")
my_function("fareedah")

def my_function(fname, lname):
    print(fname + " " + lname)
my_function("farouq", "raji")
my_function("fawaz", "raji")
my_function("fareedah","raji")

def my_function(food):
 for x in food:
     print(x)
     
fruits = ["apple" , "banana" , "cherry" ]

my_function(fruits)

def my_function(x) :
  return 50 * x
print(my_function(3))
print(my_function(10))
print(my_function(25))

def myfunction(a, b, /, *, c, d):
  print(a + b + c + d)
my_function("5 = 7, b = 6, c = 7, d = 8")

    
def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
tri_recursion(6)

cars = ["toyota", "ford", "ferrari"]
cars [1] = "lamborghini"
print(cars)
   
cars = ["toyota", "ford", "ferrari"] 
for x in cars :
    print(x)    
    
class MyClass :
  x = 5
print(MyClass)

class Myclass:
    x = 5
    
p1 = Myclass()
print(p1.x)   
 

  
     






     
      