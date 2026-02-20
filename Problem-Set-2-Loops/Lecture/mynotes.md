# Question about FOR loops that we use in C++ and other languages 
AUDIENCE: Can we use stuff like for loops which have a certain i-value initialized to it at the start and it runs from the particular condition you put into the thing and increment it as you go along? 
DAVID MALAN: Short answer, no, you cannot do what you're describing, but there is another type of for loop that we will soon see

- Well, let me go ahead, if I may, and propose that we transition to another approach of types of loops using another keyword here, namely a for loop. And this is a word that does exist in other languages, but doesn't necessarily have as many features as other languages might use it for. But there is a different type of loop-- not a while loop, but a for loop.

# list (also another type of data)
and here too no pun intended we're adding to the list of data types that python supports 
its a way of containing multiple values all in the same place, all in the same value 

# For Loop
The way FOR loop works is that it allows you to iterate over a list of items 
so what is it look like 

for i in [0, 1, 2]:
    print ("meow")

this my starting point and on each iteration of this loop that is on each execution of this loop again and again 
i wanna print out meow 

code runs then for i =0 meow is printed 
then again on the first line 
i = 1 meow is printed 
then again on the second line 
i = 2 meow is printed 

now as the list ended (no more in list) so for loops ends 

# range() function
- easiest way to overcome that poorly design 
and the one way to solve this problem to improve the design is don't just manually specify the list of values, use a function 
someone else's function that comes with python that gives you the list you want and the easiest way to do that in python is to use a funciton called range that returns a range of values 
its expects an input atleast one argument and that no. is going to be the no. of values you want back 
those values are going to start with zero and go to 1 ,2 and forth
but they will go upto but not through the no. you specify 


# convention in python where if you need a variable just because the programing features requires 
And just to show you something else that's Pythonic-- this is not strictly necessary, but it's commonly done, 
there's a minor improvement we can make here, even if we're just meowing three times. And notice that even though I'm defining a variable i, I'm not ever using it. And it's kind of necessary logically, because Python, presumably,

has to use something for counting. It has to know what it's iterating over. But there's this convention in Python where if you need a variable, just because the programming feature requires it to do some kind of counting or automatic updating, but you, the human, don't care about its value, a Pythonic improvement here

would be to name that variable a single underscore. Just because it's not required, it doesn't change the correctness of the program, but it signals to yourself later, it signals to colleagues or teachers that are looking at your code, too, that yes, it's a variable, but you don't care about its name because you're not using it later,


# multiplication operator inside the print 
- print("-" * 69)

And think back. We've used plus to concatenate strings. You can apparently use multiplication to concatenate strings, but more than once again and again and again.

# A very common paradigm in python -- while true

while True:
    n = int(input("What's n? "))
    if n < 0:
        continue 
    else:
        break
> while True, continue keyword and break keyword 
A very common paradigm in Python, when you want to get user input that matches a certain expectation you have, that it's all positive, that it's all negative, or just something like that,

you just immediately say while true. You deliberately, and a little dangerously but a very conventionally, induce an infinite loop. Now what is an infinite loop? It's just one that goes forever. And we've seen how that can happen accidentally mathematically. It's absolutely going to happen when you say while true.

Well, the answer to the true question is always true. So this is a way of deliberately inducing a loop that by default is going to go forever. So we're going to need a way of breaking out of this loop when we have the number we want. The convention, though inside of this otherwise an infinite loop is to ask the question you care about,

like give me an int by prompting the user for input. Like what's n, question mark? And then just ask your question. So if n is less than 0, then I think we want Python to just continue to prompt the user again. That is, we want the code to stay in the loop, recall the input function, and hope that the user gives us a better answer.

If this time around it's less than 0, so let's just literally use Python's keyword continue, which says just that-- continue to stay within this loop. Else, if it's not less than 0, let's go ahead and just break out of the loop altogether using another keyword in Python, break. Break will break you out of the most recently begun loop in this case

if it's not the case that n is less than 0.



# another feature of for loop 
- students = ["Harmione", "Harry", "Ron"]
for student in students:
    print (student)


- what i wrote 
students= ["Harmione" , "Harry", "Ron"]
for _ in students:
    print(_)



if next year there's some new students at Hogwarts, we can use a loop to do something automatically without having to manually type out 0 and then 1 and 2. Well, here's another feature of Python. You can use a for loop not just to count from 0 to 1 to 2, you can use Python to just iterate over anything.

Not just numbers, but strings.


# questions and answers 
- AUDIENCE:
Yeah. So is it not necessary to initiate student in this case? Or we can just declare a variable in the loop?

- DAVID MALAN: 
Good question. You do not need to manually initialize it. Python takes care of initializing the student variable to Hermione first, then Harry second, then Ron third. Unlike other languages, you don't need to initialize it to something yourself, it just exists and it will work.

- AUDIENCE: 
Since you describe break, so is there any concept of continuing so that we can skip a particular case in loops? 
- DAVID MALAN: 
Yes. You can continue using another syntax as well. We haven't shown that. For now we focused only on break. 

- Audience: 
So can this for loop work with either hash tables or different kind of tables or arrays? 
- DAVID MALAN: 
Indeed.So we're getting ahead of ourselves there, but there are yet other types of data in Python, and indeed, you can use a for loop to iterate over those as well. Anything that is iterable, so to speak, is a piece of data that can be used with a loop like this. But more on those-- more on those soon




# len -- function in python 
In Python,
len() is a built-in function used to return the number of items in an object. It is one of the most frequently used functions because it provides a quick and efficient way to determine the size of various data structures.

# dict -- keyword
In Python, a
dict (dictionary) is a built-in data structure used to store data in key-value pairs. It functions like a real-world dictionary where you look up a specific "word" (the key) to find its "definition" (the value). 

Summary
If someone asks you what a dict is:

    Technically, it is a built-in data type.
    Conceptually, it is a mapping data structure.

A computer scientist, though, and a programmer would describe those more generically as keys and values, something associated with something else. That's all a dictionary is. It allows you to associate something with something else. And notice, this is already more powerful, more interesting than a list. A list is just a set of multiple values. But a dictionary is two-dimensional, if you will.

Just like a human dictionary, a book, it associates something with something else like words with their definitions.

# None Keyword 
This represent Officially the absence of a value 

we could a little sloppily do something like "" (quote-Unquote)
its a little clear semantically to say literally None, a special Keyword in Python


# Functions importance 
- But let's see if we can't now integrate our discussion of writing functions of our own to begin writing something a little more dynamic

and solving more complicated problems ultimately. One of the nice things about functions is that they allow us to not just write code that we can use and reuse, they allow us to create abstractions, if you will. An abstraction is a simplification of a potentially more complicated idea. And we've seen this a few times over the course of the weeks. For instance, we had a function called hello, which, granted, didn't do all that much, it just printed hello. But it allowed me to think about the function as exactly what it does,

not generically printing something, but literally saying hello. I've been able to get a number using something similar by defining my own function like get number.

* for better undersanting --- google it.(talking for above statements)


> more understanding about the function <basic_but_great>
I could implement now print column in different ways, especially if I am using print column all over my code, or maybe still, a colleague of mine, a friend, someone else on the internet is using my print column function. What's also nice about functions you've written is you can change the underlying implementation details of them, but so long as you don't change the name of the function or its parameters or what it returns, if anything no one else knows the difference. You can change the internal implementation as much as you want if you want to improve it or make fixes over time.<refer_code_36_37> 

# question answer for code 39
DAVID: But let me ask you a question of the group now, why on line 16 do I have a print here all by itself? Why do I have a print all by itself? Notice that it's below the inner loop, but inside of the outer loop, so to speak. What is that loop on line 16 doing ultimately? 

AUDIENCE: Every time you finish a line, you have to add a new line at the end of it. 

DAVID: So print, it prints a new line. I don't want a new line after every brick. I only want to do that at the end of the row, and that's why my comments now are perhaps enlightening. Notice that this loop here is just iterating for each brick in the row. Once I'm done with that inner loop, so to speak, once I'm done with these highlighted lines here, to Evelyn's point, I need to print out one blank new line. And we've not done this before, but when you call print with no arguments, all you get is that automatic line ending, the backslash n where the cursor moves to the next line.
