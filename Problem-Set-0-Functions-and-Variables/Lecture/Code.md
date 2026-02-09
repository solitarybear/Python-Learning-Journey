# 1 
>hello.py
print  ("What's your name? ") #asking some question for some input
input ()                      #input is a function that helps to get input from the user  
print ("Namaste, I'm SolitaryBear")

# 2 
when we read the documentation for the inoput function we can see that it takes an argument itself 
so we don't need to write print and input seperately 

>hello.py
input ("What's your name? ")  
print ("Namaste, I'm SolitaryBear")

* well it takes input but didn't use any how our input 

# 3 
>hello.py
input ("What's your name? ")  
print ("Namaste, SolitaryBear")


* we literally written my name inside the string 
so we need some way now  of actually getting back what the user's input is and doing something with it ultimately 

# 4 levarage features of some functions that can have return values 
now to do that we need one more feature of programming that is variable 

>hello.py
name = input ("What's your name? ")  
print ("Namaste, name")


* error 
it will print Namaste , name
not the input we took 


* = sign is called assignment operator 
so the equal sign copies from the right to the left whatever the return value of the function on the right is 

# 5 now we are not putting in the double quotes 
>hello.py
name = input ("What's your name? ")  
print ("Namaste,")
print (name) 


# Questions and Answers 
>Is the function Input work for any type of information or only for the words?
So According to its documentation , input is going to what is called a string , that is a sequence of text with which to promp the user 

>how can we comment in Python 
using the symbol #
or 
writing something btw """ up and """ down then everything btw them will be seen as comment or ignored by the compiler 



# 6 improving code 5
>hello.py
name = input ("What's your name? ")  
print ("Namaste," + name)

* getting both the words on same line 
still there is a asthetic mistake that is we got result in with there is no space btw Namaste, and the name 

# 7 improving code 6 
>hello.py 
#this approach uses one argument technically even it look like little curious 
name = input ("What's your name? ")  
print ("Namaste, " + name) #here this '+' means concatenation to join the thing on the left  and thing on the right  


>this ("Namaste, " + name)
becomes the english phrase ("Namaste, SolitaryBear") 
and then what pass to the function tecnically something like this 
print(SolitaryBear)
but its doing it all dynamically 





* so we added that space
now there you may have noticed why we have a space after ? in the input is also for asthetics - just to write a our name a space after the argument the input holds 

# 8th another way to do code 6 
>hello.py 
#this approach uses a function print with two argument 
name = input ("What's your name? ")  
print ("Namaste, ", name)

* using comma sign i.e. ,    
so this comma is outside the "" and btw two seperate argument 


>so we got two space btw the Namaste, and name 
that is becoz 

as comma is used and we can use it to pass multiple argument  to print 
>it automarically inserts a space for you

it was not relevent earlier boz we are the print a big  argument to bring all at once, becoz of + operator 
this time we are passing in two because of comma 
so if we don't need that extra space 

* correct 
>hello.py 
name = input(What's Your name? ")
print ("Namaste," , name )


# One of the best thing you can do is going through documentation 
>print(*objects, sep=' ' , end="\n" , file = none , flash= "False" )

>hello.py
#Ask user for their name 
name = input("What's your name? ")

#Say Namaste to user
print ("Namaste, " , end= "") #we change end from default (\n ) to nothing so after printing there nothing will be at the end so not gone to the next line  
print (name) #but here as we didn't change anything so at end then it will move to the next line after executing this line of code


* output 
Namaste, user_name

# overriding the sep behaviour inside the print function
>hello.py
name = input("What's your name? ")

print ("Namaste," , name ,sep ="???") 



# printing double quaotes itself 
>hello.py
print ("hello, "friend"")

* error -- syntax error 



* by using single quotes 
>hello.py 
print ('hello, "friend"')

* no error




* alternate way -- using back slash --- \
>hello.py
print("hello, \"friend\"")

* no error

# now relatively new feature of python -- the most frequently done way to solve this problem --- quotation printing 
>python.py
name = input("What's your name? ")

print ("Namaste, {name}" ) 


* error -- still it prints 
{name} --- not user name

we have to some how tell python that this is special string

* this is what we called a format string or f string 
that tells python actually format stuff in the string in a special way
the symbol we use is f
that is clue to python this is a special string , let me format this in special way for you


>python.py
name = input("What's your name? ")

print (f"Namaste, {name}" ) 

# str
strings themselvess comes with the lot of build in functionality 
We can manipulate the user input to do morethan just join it with something else like hello, we can actually clean it up or reformat it in a way that hopefully looks  a little better for us

we aren't perfect in typying do basic misstakes staring many spaces and capitalising word etc 

>hello.py
name = input("What's your name? ")

#remove white space from str
name = name.strip() #strip is a method (otherwise we can call it as function)

print(f"Namaste, {name}")

# capitalised user input 
>hello.py
name = input("What's your name? ")

#remove white space from str
name = name.strip() 

#Capitalize user's input
name = name.capitalize()

print(f"Namaste, {name}")


> still capitalizing is not really capitalizing at all --- only one word is capitalize a first letter

# title function --- for capitalizing each first letter of the word


>hello.py
name = input("What's your name? ")

name = name.strip() 

name = name.title()

print(f"Namaste, {name}")





# using strip and title in a single cofe
>hello.py
name = input("What's your name? ")

#remove white space from str
name = name.strip().title() #strip is a method (otherwise we can call it as function)


print(f"Namaste, {name}")



# we can also use strip and title inthe first line let see
>hello.py
name = input("What's your name? ").strip().title()


print(f"Namaste, {name}")


>
Now I've capitalized things and cleaned things up. But what about my code? I've got like eight lines of code now, four of which

are comments, four of which are actual code. Do I really need this much? Well, not necessarily. Watch what I can also do in Python. Let me not bother capitalizing the user's name separately. Let me say this-- and capitalize user's name. I can chain these functions together. I can add Title to the end of this. And now what's happening?

Well again, with a line of code like this, you first focus on what's to the right of the equal sign, then we'll get to the left of the equal sign. 

# spliting the name in the first name and the last name
>hello.py
#Ask user for their name
name = input("What's your name? ").strip().title()


#Split user's name in first name and last name 
first, last = name.split(" ")


print(f"Namaste, {first}")  


# making own calculator 
>calculator.py
x = 1 
y = 2 

z = x + y 

print(z)

# modification
>calculator.py
x = input("What's x? ") 
y = input("What's y? ")

z = x + y 

print(z)


* error or bug 
if we put the value x = 1 and value y = 2 then 
answer we got is 12 

because  that + is also used for catnation for the strings 
so just put them together assuming or taking the values x and y as string 



# changing the data type from one type to another(we can do such things sometimes)
>calculator.py
x = input("What's x? ") 
y = input("What's y? ")

z = int(x) + int(y)  #changing to x to integer version of x 


print(z)


>this code works (miracle !!!! miraclee!!!!)

* so it turns out that INT is not only a type of data  in python, its also a function and it is a function that if you pass in an input, like a string, so long is that string looks like a number like 1 or 2 
it will convert it to actuall number, that you can mathematics on instead

# alternative way
>calculator.py
x = int(input("What's x? ")) #int is function here
y = int(input("What's y? ")) #return value of inner function becomes argument to other (outer) function


print(x + y)



# alternative way 
we don't really want x and y we could so something like below
>calculator.py
print(int(input("What's x? ")) + int(input("What's y? ")))


now some one says wow we really made a one line code but now i think i'm starting to nest too many things i have to think about print, int , and input

You making me to think too much 
everytime you make me to think too much And any time you complicate the look of the code like this You're just increasing the probability of mistake    


# float data type 
>calculator..py
x = float(input("What's x? ")) 
y = float(input("What's y? ")) 


print(x + y)

- that works 

# i want answer in int OR Round round the result to nearest posible integer 
>calculator.py
x = float(input("What's x? ")) 
y = float(input("What's y? ")) 

z = round(x + y)

print(z)


> taking some big no.
let me just add 999 + 1. And notice, I don't have to type decimal points, even though I'm converting to float, my program will just allow me to type decimal points, but I don't need to oblige.



# adding commas after in the no.s
>calculator.py
x = float(input("What's x? ")) 
y = float(input("What's y? ")) 

z = round(x + y)

#print(f"{z}") we can also write like this but it's just more cryptic

print(f"{z:,}")



* here we when we input 999 and 1 
now we got answer as 1,000 instead of 1000

# using division
>calculator.py
x = float(input("What's x? ")) 
y = float(input("What's y? ")) 

z = x / y


print(z)


# round the divion
>calculator.py
x = float(input("What's x? ")) 
y = float(input("What's y? ")) 

z = round(x / y , 2) # , 2 is the second parameter (or better say argument)


print(z)



# another way to do this , using f string 
>calculator.py
x = float(input("What's x? ")) 
y = float(input("What's y? ")) 

z = x / y 


print(f"{z:.2f}")


* there is a difference if u use .2f or just .2 inside the f string
- google it 



# creating our own function and calling our own functions
>hello.py
name = input("what's your name? ")
hello()
print (name)

* error --- as python cond.t recognise the function hello is as ever exist 
we have to define this function named hello


# Using the 'def' keyword to create own functionn 
def means define 
>hello.py
def hello():
    print("hello")


name = input("what's your name? ")
hello()
print (name)






# adding parameter to the def hello
>hello.py
def hello(to):
    print("hello," , to)


name = input("what's your name? ")
hello(name)

# what if the person doesn't called ourthe function with parameter
>hello.py
def hello(to = "World"): #WE know we can give parameter default value just by putting them with something with equal sign 
    print("hello," , to)

hello()
name = input("what's your name? ")
hello(name)

# error of difine function down and calling the function above
>hello.py
hello()
name = input("what's your name? ")
hello(name)

def hello(to = "World"): 
    print("hello," , to)


* error because hello() is defined below the function is used 
because if you use a function, it must already exist by the time you are calling 

- way to fix it is 
to define the function above before we use it - but that is like coding in reverse


# fixing this in more standard way 
- generally speaking you do want to put your code at the top of the file 
- infact im going so far as to define my fuction , called main
its not requirement but its a data convention and this just connotes to the reader that this is the main part of my program

>hello.py
def main():
    name = input("what's your name? ")
    hello(name)

def hello(to = "World"): 
    print("hello," , to)


* no error but also nothing gonna happen as we never call main and so we never call hello to

# fixing continue --- calling the main function
>hello.py
def main():
    name = input("what's your name? ")
    hello(name)

def hello(to = "World"): 
    print("hello," , to)

main()

* no error
we difine our function hello its also taking an argument too , then i passed into that function the value of the variable 


# doing some changes in above code
>hello.py
def main():
    name = input("what's your name? ")
    hello()

def hello(): 
    print("hello," , name)

main()


* error 
the catch is that the name only exist in the main() function 

- this is an issue what is called scope 
scope refers to a variable only existing in the context in which you defined 

# using return ---
>calculator.py
def main():
    x = int(input("What's the x? "))
    print("x squared is" , square(x))

def square(n):
    return n*n

main()


- so i have implemented a very own function that returns the square of a value and because im using the return keyword , that ensures the i can pass the return value of this, to another function like print instead 

# raising the power of the value 
>calculator.py
def main():
    x = int(input("What's the x? "))
    print("x squared is" , square(x))

def square(n):
    return pow(n,3)                 # or we can use this ** instead such as n**3

main()
 





