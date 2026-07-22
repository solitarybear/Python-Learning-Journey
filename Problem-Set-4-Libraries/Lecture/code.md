# 1 using random library and choice fuction 
> generate.py

import random # importing the random library

/# random.choice(seq) -- seq means list so here in parameter we will write list as an argument 
/# using . to call the specific function 
coin = random.choice(["solitary" , "bear"])

print(coin)

# 2 usig from keyword 
> generate.py

from random import choice

coin = choice(["solitary" , "bear"])
print(coin)



# 3 using the function random.randint()
>generate.py

import random

number = random.randint(1, 10)
print(number)

# 4 using the function random.shuffle()
>generate.py

import random

cards = ["solitary" , "Bear" , "Great" , "The"]
random.shuffle(cards)

for card in cards:
    print(card)



# 5 statistics library using statistics.mean()
>average.py

import statistics

print (f"avg no. of supplymentary in each semester = {statistics.mean([0,0,0,3,3,0])}")

# 6 command line arguments (taking arguments while initially starting the program)
>name.py

import sys

print("Hello, my name is" , sys.argv[1])

* error 
- IndexError
when len of arguments is less then 2 

# 7 printing the first command line argument 
>name.py

import sys

print("Hello, my name is" , sys.argv[0])

# 8 get rid of IndexError message 
>name.py 

import sys

try:
    print("Hello, my name is" , sys.argv[1])
Except IndexError:
    print("too few arguments")



# 9 doing same using if else statements and more precise about no. of arguments 
>name.py 

import sys

if len(sys.argv)<2:
    print("too few arguments")
elif len(sys.argv)>2:
    print("too many arguments")
else:
    print("Hello, my name is", sys.argv[1])





# 10 refine way to code the above
>name.py

import sys
#check for error
if len(sys.argv)<2:
    print("too few arguments")
elif len(sys.argv)>2:
    print("too many arguments")
#print name tag  
print("Hello, my name is", sys.argv[1])

* error  (bug even better)
mistake is no matter there are too many arguments or too few arguments the print line will still execute 

solution for that if those cluase of if else statements executes then the program should stop then imediately 

Logically, what bug did I just introduce by getting rid of the else and introducing line 10 on its own with no indentation outside of the conditional? What bug have I just introduced? What mistake to be clear? AUDIENCE: Name error. DAVID MALAN: Ironically, it's a name error but not a name error exception. It's an error with my name, but I think you're frozen for me. It's going to raise an exception because even

though I'm checking the length of sys.argv up top and even though I'm checking it again for being greater than 2, not just less than 2, but greater, I'm still then blindly and incorrectly assuming it's now going to exist. So just to be clear, if I run Python of name.py and I don't type any argument-- I've got too few-- I think I'm going to see that I have too few, but I'm also going to see that same exception. At the very top of my terminal window's output, there's my error message, too few arguments. But again, on line 10, I blindly proceed to still index into my list at location1 which does not exist.

# 11 using function sys.exit()
>name.py

import sys

if len(sys.argv)<2:
    sys.exit("too few arguments")
elif len(sys.argv)>2:
    sys.exit("too many arguments")

print("Hello, my name is", sys.argv[1])





# 12 printing many name tags at once by taking more than one command-line arguments
>name.py

import sys

if len(sys.argv)<2:
    sys.exit("too few arguments")

for arg in sys.argv:
    print("Hello, my name is", arg)


* error ---- we had also printed file name that we might not needed



# 13 correcting the error - using slicing 
>name.py

import sys

if len(sys.argv)<2:
    sys.exit("too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)


- here in slicing, we had made a subset of out list and sliced it from the "1" indexed element of the list 


# 14 using slicing backward 
>name.py

import sys

if len(sys.argv)<2:
    sys.exit("too few arguments")

for arg in sys.argv[1:-1]:
    print("Hello, my name is", arg)





# 15 teaching cow how to say hello (before this you have to install the cowsay package u can use pip for that installation)
>say.py

import cowsay
import sys

if len(sys.argv)==2:
    cowsay.cow("hello, " + sys.argv[1])


* why didn't we used comma to join the two strings and used catenation
And I'm going to pass in a string, hello, comma. And then as in the past, I'm going to pass in just one string because according to its documentation, it's not like print.

I can't pass in comma this, comma that. I can only pass in one string. So I'm going to concatenate it the contents of sys.argv, bracket1



# 16 teaching a Tyrannosaurus rex to speak
> say.py

import cowsay
import sys

if len(sys.argv)==2:
    cowsay.trex("hello, " + sys.argv[1])



# 17 using requests packages and calling api to get data about song by artist name and geting data in json format 
>itunes.py

import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(response.json())




<downloaded requests packages by running the command in terminal
pip install requests>

# 18 making the data more readable using json module that is already comes with python
>itunes.py

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(json.dumps(response.json(), indent = 2) )


# 19 making the data more specific --- printing only trackName for everydata set 
>itunes.py

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o =  response.json()

for result in o["results"]:
    print (result["trackName"])



# 20 trying to make our know library 
> sayings.py

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

main()
    

- made a python file 
what if we want to use this file's function in some other python files so instead of copy pasting we can use this file as our own custom library

and also we can open source this library and if want to donwload from the internet , then we can upload this on the server , also we can upload on PyPI to some less can you this (if completed all the steps to do so)



# 21 using the custom library and importing a function
> say.py
import sys

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])



- there is some issue that is those main function also executed even we hadn't called that 
because when we even import a function from a module this tell python find that module read it from left to right top to bottom and then specifiacally import that hello function 
iske liye solution in next code


# 22 solution to the issue in the above code using the special variable __name__ 
>saying.py

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()


> and then running the say.py 
and it works perfectly 


# 23 goodbye world using cli- argument
> say.py

import sys

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])

    

#

#

#
