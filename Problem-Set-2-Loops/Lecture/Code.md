# 1 what cat told me once 
>cat.py 

print("meow")
Print("meow")
print("meow")

- this above code is arguably poorly designed as we are repeating the same code, what if we have to print 50 or 500 times does u really think that solution to this is copy-pasting the code 50 times??
- probably not 
- what if i want to change the code instead of cat there it is a dog so i have to print whoof whoof whoof and change every code again 

# 2 while keyword 
>cat.py 

i = 3 
while i != 0 :
    print ("meow")
    
* error - the program will print meow infintely untill we stop this using cmd + c (for linux) as i = 3 and i != 0 is always true 

# 3 Fixing the Bug
>cat.py 

i = 3 
while i != 0 :
    print ("meow")
    i = i - 1


# 4 what if we have to count up instead of down 
>cat.py

i = 0 
while i < 3 :
    print ("meow")
    i = i + 1 

- it's a good habbit to getinto now, start at 0 and go up but not through the value that you care about ultimately 

# 5 popular thing to do code (minute changes)
>cat.py

i = 0 
while i < 3 :
    print("meow")
    i += 1

- this new way to write i = i + 1 its just a convention 

- Note: those who have code in C++ or any other language and seen i++ or i-- before 

*sorry* - Python doesn't have it, so you can't use that 




# 6 using list keyword -- having multiple values at same place inside same variable 
>cat.py

for i in [0,1,2]:
    print ("meow")


- meow is printed 3 times 

- this code might short but its poorly designed

# 7 improving code 6 
>cat.py

for i in range(69):
    print ("meow")


- easiest way to overcome that poorly design 
and the one way to solve this problem to improve the design is don't just manually specify the list of values, use a function 
someone else's function that comes with python that gives you the list you want and the easiest way to do that in python is to use a funciton called range that returns a range of values 
its expects an input atleast one argument and that no. is going to be the no. of values you want back 
those values are going to start with zero and go to 1 ,2 and forth
but they will go upto but not through the no. you specify 


# 8 improving code --- just to show something pythonic 
>cat.py

for _ in range(69):
    print ("meow")

- not stictly necessary but its commonly done 
there's a minor improvement we can make here, even if we're just meowing three times. And notice that even though I'm defining a variable i, I'm not ever using it. And it's kind of necessary logically, because Python, presumably,

has to use something for counting. It has to know what it's iterating over. But there's this convention in Python where if you need a variable, just because the programming feature requires it to do some kind of counting or automatic updating, but you, the human, don't care about its value, a Pythonic improvement here

would be to name that variable a single underscore. Just because it's not required, it doesn't change the correctness of the program, but it signals to yourself later, it signals to colleagues or teachers that are looking at your code, too, that yes, it's a variable, but you don't care about its name because you're not using it later,

# 9 lets do something kinda intrigue and more pythonic -- this will blow your mind if you ever coded 
>cat.py

print ("meow" * 3)


* output --- meowmeowmeow 
  (Hungry cat)
- You have to be kind of a geek to think this is cool, but this is kind of cool. So you can literally just print what you want, multiply it by the number of times that you want it,

and you will get back exactly that result. Now I've kind of made a mistake here. So let's see what this does. It's not quite as beautiful as this code might look to you-- to some of you, to me. Let me run Python of cat.py, Enter. OK, it's a really like hungry cat or something. It's meowing really fast.




# 10 correcting the code 9
>cat.py

print("meow\n" * 3 )

* so close but we got an extra line that for asthetic i don't like it 


# 11 making more asthetic 
>cat.py 

print ("meow\n" * 3 , end = "" )


# 12 asking the user to how many time cat meows
>cat.py

while True:
    n = int (input("What's n? "))
    if n < 0:
        continue
    else:
        break


- using a common paradigm -- while True


# 13 tighten up further  
>cat.py 

while True:
    n = int (input("What's n? ))
    if n > 0 :
    break
for _ in range(n):
    print ("meow")
 

- in fact its not that interesting program if we even allow the user to type in 0


# 14 making a meow function that the inventors of python didn't envision
>cat.py

def main():
    meow(3)
def meow(i):
    for _ in range (i):
        print ("meow")
main()


# 15 making some improvement here 
>cat.py

def main():
    number = get_number()
    meow(number)
def meow(i):
    for _ in range (i):
        print ("meow")
def get_number():
    while True:
        n = int(input("What's n? "))
        if n >0:
            return n
main()

- unfortunately there is no function in python as get_number that gets a positive number from the user   
    but i can invent that

- this time i don't want to break this time necessarily although i could but instead i want to return the value n 

And this, too, is a feature of Python. This ability not to just break out of a block of code, but also to return a value in code. To actually return a value gives you the ability, ultimately, to return explicitly a value so that your function has not just a side effect, necessarily, but it actually hands back, just like input does,

just like int does, just like float does, an actual value to the user

# 16 if we want to break the loop first 
>cat.py

def main():
    number = get_number()
    meow(number)
def meow(i):
    for _ in range (i):
        print ("meow")
def get_number():
    while True:
        n = int(input("What's n? "))
        if n >0:
            break
    return n
main()


- I can still break out of the loop as I've done in the past with code like this, but then after the loop, I still have to return. And so what's happening here is that if you use break to get out of the loop,

but you need to hand back a value from a function, you still have to use the return keyword now explicitly either in the loop as I did or now outside of the loop but still inside of the function.

# 17 looking more closely at these list
>hogwarts.py

students = ["Harmione" , "Harry" , "Ron" ]

- let see we can have a list of students at Hogwarts here 

- in "" inside a list because its a string 
- this is the list of length 3 
- now we have list of 3 string 

# 18 want to printout list of student 
>hogwarts.py

students = ["Hermione" , "Harry" , "Ron"]
print(students[0])
print(students[1])
print(students[2])

- how do i print the content of the list 
- we don't want to print out all of Harmione , Harry, Ron all at once 
    may i wanna printout Harmione first then Harry and then Ron
- so i want a way to express more precisely which value do i want from this list 

* for this we use square brackets in different way -- we will index which value inside the list we want to print out 

* these list in python are shall we say, zero indexed


# 19 what if we don't know how many students are in the list -- we will use a loop
>hogwarts.py

students = ["Harmione" , "Harry", "Ron"]
for student in students :
    print(student)


# 20 conscious decision we made in code 19
>hogwarts.py

students = ["Hermione" , "Harry" , "Ron"]
for _ in (students):
    print(_)

- we didn't wrote that variable _ as we did now 
because this time i'm using the variable 
but well we could do this(as we wrote the above code)

- no, no, your code is now way too cyptic  

# 21 suppose we wanna iterate using numbers like i or 0
>hogwarts.py

students = ["Hermione" , "Harry" , "Ron"]
for i in range(len(students)):
    print(students[i])

# 22 i want to do ranking 
>hogwarts.py

students = ["Hermione" , "Harry" , "Ron"]
for i in range(len(students)):
    print(i ,students[i])

- ok hermione is the top student but i don't want to have the top student as rank 0 

# 23 i can clean its up 
>hogwarts.py

students = ["Hermione" , "Harry" , "Ron"]
for i in range(len(students)):
    print(i + 1 ,students[i])

 
# 24 see who is in what house -- using list 
>hogwarts.py

students =["Harmione", "Harry" , "Ron", "Draco"]
houses= ["Gryffindor", "Gryffindor", "Gryffindor" , "Slytherin"]

- so here whatever its at the first no. in students is associated to the houses in the same first no. 
- there's an issue --- what if we have another list of something to associate with these 
this will get messy quickly using musltiple list where everything lines up logically. It doesn't endup well when your code gets more complicated 

- we wanna implement this idea -- i do wanna associate something with something 

# 25 we can do this using python dictionary -- dict keyword -- build in data-type
>hogwarts.py

students ={"Harmione" : "Gryffindor" , "Harry" : "Gryffindor" , "Ron" : "Griffindor"}

- what i want associate "Harmione" with -> "Gryffindor"

- you can see the code -- this is going to get very ugly quickly , once we add in Draco and Slytherin, my code is going get to long its going to start wrapping , 

# 26 improving the code -- so this is purely acceptable in python in other languages 
>hogwarts.py 

students = {
    "Harmione" : "Gryffindor" ,
    "Harry" : "Gryffindor" ,
    "Ron" : "Griffindor",
    "Draco" : "Slytherin"
}

print (students["Harmione"])
print (students["Harry"])
print (students["Ron"])
print (students["Draco"])


- so this something more readable now 
- i have my keys on the left, my something , and my values on the right, my other something      


- So how do I now use this code in an interesting way? The syntax is almost the same. If I want to print out the very first student, Hermione's house,

I could do this. Print out the name of the variable, but I need to go inside of the variable. I need to index into it. And what's neat about dictionaries is that whereas lists have locations that are numeric-- 0, 1, 2; Hermione, Harry, Ron respectively, dictionaries allow you to use actual words as your indices, so to speak,

your indexes to get inside of them. So if you want to print out Hermione's house, the key you care about is, quote-unquote, Hermione, and what this syntax here will do-- notice, it's not a number 0 or 1 or 2. It's literally Hermione's name. This is like going to the chart earlier and saying, all right, give me Hermione

is my key, Gryffindor is the value. That's what we're doing here syntactically. We're looking up Hermione and getting the value thereof. So if I go back to my code, that should print out Gryffindor.

# 27 printing out these value more dynamically -- using loop 
> hogwarts.py

students = {
    "Harmione" : "Gryffindor" ,
    "Harry" : "Gryffindor" ,
    "Ron" : "Griffindor",
    "Draco" : "Slytherin"
}
for student in students:
    print(student)


- for this for loop what we had written 
it could have gone both ways. could have been values, the houses, But when you use a for loop in python to iterate over a dictionary, by design it iterates over all of the keys 

# 28 can we print out the both the keys and the values 
>hogwarts.py

students = {
    "Harmione" : "Gryffindor" ,
    "Harry" : "Gryffindor" ,
    "Ron" : "Griffindor",
    "Draco" : "Slytherin"
}
for student in students:
    print(student , students[student])


# 29 more improvement 
> hogwarts.py

students = {
    "Harmione" : "Gryffindor" ,
    "Harry" : "Gryffindor" ,
    "Ron" : "Griffindor",
    "Draco" : "Slytherin"
}
for student in students:
    print(student , students[student] , sep = ", ")

- so its very similar in spirit to iterating with a for loop over a list but rather than iterate over the numeric location(as in case of list) 0 ,1,2 , it iterates over the bold-faced keys in this representation (in the case of dictionaries) here

# 30 what if we have more information about each of our students --(proposing if it was a list) 
>hogwarts.py

students = [
    {"name": "Hermione" , "house":"Gryffindor", "patronus" : "Otter"},
    {"name": "Harry" , "house": "Gryffindor" , "patronus": "Stag"},
    {"name": "Ron" , "house" :"Gryffindor" , "patronus":"Jack Russell Terrier"},
    {"name": "Draco", "house":"Slytherin" , "patronus" : None }
]
for student in students:
    print(student["name"])


- what is patronus
this is the animal or entity that comes out of the end of their wand when they make a certain magical spell 

- we want to associate multiple things as well - their name , their house and their patronus in this case

- My students variable now, I'm going to propose we think of it as a list--
what if we have a list of a dictionaries 

# 31 what if i want more information
>hogwarts.py

students = [
    {"name": "Hermione" , "house":"Gryffindor", "patronus" : "Otter"},
    {"name": "Harry" , "house": "Gryffindor" , "patronus": "Stag"},
    {"name": "Ron" , "house" :"Gryffindor" , "patronus":"Jack Russell Terrier"},
    {"name": "Draco", "house":"Slytherin" , "patronus" : None }
]
for student in students:
    print(student["name"] , student["house"])


# 32 we can asthetically make it clean amending the sep
>hogwarts.py

students = [
    {"name": "Hermione" , "house":"Gryffindor", "patronus" : "Otter"},
    {"name": "Harry" , "house": "Gryffindor" , "patronus": "Stag"},
    {"name": "Ron" , "house" :"Gryffindor" , "patronus":"Jack Russell Terrier"},
    {"name": "Draco", "house":"Slytherin" , "patronus" : None }
]
for student in students:
    print(student["name"] , student["house"], sep= ", ")


# 33 printing more information
>hogwarts.py

students = [
    {"name": "Hermione" , "house":"Gryffindor", "patronus" : "Otter"},
    {"name": "Harry" , "house": "Gryffindor" , "patronus": "Stag"},
    {"name": "Ron" , "house" :"Gryffindor" , "patronus":"Jack Russell Terrier"},
    {"name": "Draco", "house":"Slytherin" , "patronus" : None }
]
for student in students:
    print(student["name"] , student["house"], student["patronus"], sep= ", ")


# 34 implementing that mario obstacle
>mario.py

print("#")
print("#")
print("#")

- we got a very simple version of that same column of brick, so to speak.
- but you can imagine certainly in a game where may be these columns get higher or lower, it would be nice to write a code that's actually a little more dynamic than that and doesn't just use print, print, print, which  is literally copy and paste, it would seem. 

# 35 improving the code and implementing todays lessons 
>mario.py

for _ in range(3):
    print("#")

# 36 making and using print column function ---- implementing and understanding using of function
>mario.py

def main():
    print_column(3)
def print_column(height):
    for _ in range(height):
        print("#")
main()

- > i kinda complicated the code. It doesn't do anything more just yet, but it's setting me up for solving what i think to be more sophisticated problems.
   > I now have a function, an abstraction, print column, that's going to allow me to think about printing some chunk of the world of Mario at a time.

- But let's see if we can't now integrate our discussion of writing functions of our own to begin writing something a little more dynamic

and solving more complicated problems ultimately. One of the nice things about functions is that they allow us to not just write code that we can use and reuse, they allow us to create abstractions, if you will. An abstraction is a simplification of a potentially more complicated idea. And we've seen this a few times over the course of the weeks. For instance, we had a function called hello, which, granted, didn't do all that much, it just printed hello. But it allowed me to think about the function as exactly what it does,

not generically printing something, but literally saying hello. I've been able to get a number using something similar by defining my own function like get number. Well let me go ahead and, for instance, assume for the moment that I've had the forethought to, in my function main, use a function called print column.

# 37 another way we could implement print column
>mario.py

def main():
    print_column(3)
def print_column(height):
    print("#\n" * height , end = "")
main()

# 38 print_row --- those that if he (mario and luigi) jumps up underneath, they become coins.
>mario.py

def main():
    print_row(4)
def print_row(width):
    print("?" * width )
main()

>why we are over engineering 
- the solution to these problems by having print column and print row. Well it's a useful problem-solving technique.
as soon as your world is does not look one dimensional 


# 39 print a wall -- 3 by 3 square 
>mario.py

def main():
    print_square(3)
def print_square(size):
    # For each row in square 
    for i in range(size):
        # For each brick in a row
        for j in range(size):
            # Print Brick
            print("#" ,end = "")
        print()
main()



> in this code we think of this outer loop as representing each of our rows 
> now what i want to printout on each row -- that is --- brick brick brick
> and here is where comments and more generally Psuedocode can really help to explain to yourself and to others what your lines of code is doing  


- Later in Super Mario Brothers does Mario have to jump down into this world where there's a lot of these underworld barriers. And this one here, for instance, looks like a square. It's two-dimensional there's a height and a width to it.

def main():
    print_square(3) #That's and abstraction
main()

- If I want to print out all of these rows, but also, all of these columns, I now have to think not just cyclically like a loop allows, but I need to think two-dimensionally. And if you're familiar with like an old school typewriter or even a printer nowadays, it generally prints from top to bottom. So even if you have multiple columns, you print out one line at a time,

and while you're on that line, the printer or the typewriter prints from left to right. And that's the mental model to have with your black and white terminal window. All of the output for every example thus far starts at the top and goes down to the bottom. From top to bottom, left to right. So we have to generate our output, our square in that same way.


# 40 HOW we might tighten this code further
>mario.py

def main():
    print_square(3)
def print_square(size):
    for i in range(size):
        print("#" * size)
main()

- print square is really nice and compact. It has one explicit loop, and it's still printing out using string multiplication all of the hashes at once on that row.


# 41 if you like abstraction and you'd like to wrap your mind more around what the code is doing 
>mario.py

def main():
    print_square(3)
def print_square(size):
    for i in range(size):
        print_row(size)
def print_row(width):
    print("#" * width)
main()

#