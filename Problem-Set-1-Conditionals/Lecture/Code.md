# 1 comparing ---- if keyword
>compare.py
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y: #syntax- if (keyword) x < y (Question) :
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x equal to y")




* in the line
    if x < y : ---- the x < y is technically called a boolean expression, named after a mathematician called bool, is simply a question that has a yes or no answer, or technicaly a true or false answer 
it's  nice because there is two possible answer, it's very easy for me and in turn computer to make a decision or do this or so that 

* there is flow diagram for this above code 
we found out 
it does what is suppose to do its answer the question correctly by printing on the screen x less than y 
- but what is, poorly design about it ?
Let's make this first distinction. It's not enough, necessarily, for the code that you write to be correct and do what you intend. Longer term, especially as our programs get longer and more sophisticated,

more complicated, we're going to want them to be well-designed, too.


# 2 make it better and improved --- elif keyword
>compare.py
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

elif x == y:
    print("x equal to y")


- not an issue but something logically thinking 
We don't need to ask if x is equal to y any more because, logically,

if the two conditionals evaluate to false, there is only one conditional that will evaluate to true. And that is x is equal to y

# 3 using 'else' keyword at the last 
>compare.py
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else :
    print("x equal to y")


- using else 
And instead of bothering to ask the third and final question, let's not ask a question at all


# 4 Another version
>compare.py
x = int(input("What's x? "))
y = int(input("What's y? "))


if x < y or x < y:
    print ("x is not equal to y")

else :
    print ("x is equal to y")

- why asking two question x < y or x > y
as we can ask simply one question that is x!=y

# 5 trying to improve the code futher more 
>compare.py
x = int(input("What's x? "))
y = int(input("What's y? "))


if x != y:
    print ("x is not equal to y")

else :
    print ("x is equal to y")



# 6 another way to write #5
>compare.py
x = int(input("What's x? "))
y = int(input("What's y? "))


if x == y:
    print ("x is equal to y")

else :
    print ("x is not equal to y")





# 7  
>grade.py
score = int (input("Score: "))

if score >= 90 and score <= 100:
    print ("Grade: A")
elif score >= 80 and score < 90:
    print ("Grade: B")
elif score >= 70 and score < 80:
    print ("Grade: C")
elif score >= 60 and score < 70:
    print ("Grade: D")
else:
    print ("Grade: F")



- can we make code more visible??
yes lets try



# 8 
>grade.py
score = int (input("Score: "))

if 90 <= score <= 100: 
    print ("Grade: A")
elif 80 <= score < 90:
    print ("Grade: B")
elif 70 <=score < 80:
    print ("Grade: C")
elif 60 <=score < 70:
    print ("Grade: D")
else:
    print ("Grade: F")



- if 90 <= score <= 100: #we make this from this --> if 90 <= score and score >= 100; # we can do this in python and in other languages we can combine these ranges 


# 9 another improvment 
>grade.py
score = int (input("Score: "))

if score >= 90 :
    print ("Grade: A")
elif score >= 80 :
    print ("Grade: B")
elif score >= 70 :
    print ("Grade: C")
elif score >= 60 :
    print ("Grade: D")
else:
    print ("Grade: F")



* if we know that the score / input somehow btw the 0 to 100 then 
we can simply improve our code as above 
- we done here is instead of checking two question everytime the upper bound and the lower bound we are kinda little more clever 

# 10 parity ---- Modulo operator 
>parity.py
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
    





# 11 creating own function of even or odd 
>parity.py
def main():
    x = int(input("What's x? "))
    
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 ==0:
        return True
    else:
        return False
    
main()


- now i have a function that no one gave me i gave myself 
so that i can use and reuse , perharps share with others 

im using that function on line 3 (some looks like if is_even(x))
and our boolean some that is true or false is not going explicity something like x less y or etc it's going to be a function call 
im using a function as my boolean expression 
and its ok because i know i wroted that that function is_even return true or false and that's all i need in a conditional 

# 12 improving the design of above code -- let's do something that generally known as pythonic 
> parity.py
def main():
    x = int(input("What's x? "))
    
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n%2 == 0 else False
    
main()

> there's actually a term of art, in the python world where something is pythonic if it's just the way you do things in python
- so we collapse that four lines of code into just one more elegent line 



# 13 refining the code further more 
>parity.py 
def main():
    x = int(input("What's x? "))
    
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return (n%2 == 0) 
    
main()

- notice this expression n % 2 == 0 is a boolean expression and its going to evaluate true or false 
so just return the question if will

> Because of order of operations you don't even need the parentheses 
just write 

-    return n % 2 == 0


# 14 'match' keyword
>house.py
name = input("What's your name? ")

if name == "Harry":
    print ("Griffindor")
elif name == "Harmione":
    print ("Griffindor")
elif name == "Ron":
    print ("Griffindor")
elif name == "Draco":
    print ("Slytherin")
else :
    print ("Who?")


- there is some other ways to implement this , indeed there's some redundency here 
we are checking harry , harmione , ron all are in Gryffindor 
it feel we can tighten up this code a little bit using techniques we seen already


# 15 making code more tighen up
>house.py
name = input("What's your name? ")

if name == "Harry" or name == "Harmione" or name == "Ron":
    print ("Griffindor")
elif name == "Draco":
    print ("Slytherin")
else :
    print ("Who?")


- that is what consolidating all three cases if you will into just one if statement

# 16 using the match keyword 
>house.py
name = input("What's your name? ")

match name:
    case "Harry":
        print ("Gryffindor")
    case "Harmione":
        print ("Gryffindor")
    case "Ron":
        print ("Gryffindor")
    case "Draco":
        print ("Slytherin")




- now in this case all works fine but when we gave input as some name not mention in the programm then program just ignore after taking the input


# 17 fixing the kinda error in the above programm
>house.py
name = input("What's your name? ")

match name:
    case "Harry":
        print ("Gryffindor")
    case "Harmione":
        print ("Gryffindor")
    case "Ron":
        print ("Gryffindor")
    case "Draco":
        print ("Slytherin")
    case _:
        print ("Who?")




- similarly to the else construct just want a catchall that handles anyone who name is not explicily specified 

- so in the match statement we can use 
underscope '_' after the case 
which is used in othr context in python

but for her it meant to say whatever case has not yet been handled go ahead and printout (or whatever we just told )

# 18 we can tighten up this code as well as we did in the if and else statement made all the three on the same line 
>house.py
name = input("What's your name? ")

match name:
    case "Harry" | "Harmione" | "Ron":
        print ("Gryffindor")
    case "Draco":
        print ("Slytherin")
    case _:
        print("Who?")



so here we are using the single vertical bar '|'

this is how the relatively new match statement 
-               case "Harry" | "Harmione" | "Ron" :

you can equivalent of "Harry" or "Harmione" or "Ron" for inside the match keyword other wise outside the match keyword '|' is treated as bitwise or operator


#






