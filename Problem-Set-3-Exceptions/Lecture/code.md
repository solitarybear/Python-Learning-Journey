# 1
hello.py

print("Hello solitary)



- error 
    print("Hello solitary)
          ^
SyntaxError: unterminated string literal (detected at line 1)


# 2
hello.py

print("Hello solitary)"

# 3
number.py

x = int(input("what's x? "))

print(f"x is {x}")

- no error for input as integer but 

* error 
if input is string ----- "solitary bear"

    x = int(input("what's x? "))
        ^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'solitary bear'


> how to fix this (important note why to fix this rather than how to fix this )
So how do I go about actually fixing this problem? Well, I could just add instructions in my program. Maybe I could add a line of print telling

the user more explicitly, be sure to type an integer, or, please don't type cat. Please don't type strings. Of course, the user might still not oblige. They might not be reading the instruction. So that too is probably not an effective strategy. What we really want to do is write our code with error handling in mind.

We want to write lines of code that not only accomplish the problems we care about but that also handle errors that might unexpectedly happen. And, in general, when programming, programming defensively. Assume that the users aren't going to be paying attention or, worse, they're malicious. They're trying to crash your program.

So we want to handle as many errors as we can.



# 4 using try and except keyword 
number.py

try:
    x = int(input("what's x? "))

    print(f"x is {x}")
except ValueError:
    print("x is not an integer")


- 
And notice it's important that I've capitalized the V and I've capitalized the E. These symbols are case sensitive. And this is now an opportunity, after this colon, to tell Python what I want to do in exceptional cases, when the number or the input from the user is not, in fact, a number

nd I'm going to say something plain like print, quote unquote, "x is not an integer." I'm at least going to tell the user roughly what the problem actually is. So notice another detail. The indentation is important. Because I have try on line one and I've indented lines two and three, those are the two lines of code that I'm trying, except if I see a value error,

line five, because it's indented is what is going to get executed in cases of those errors.

* 
I'm not seeing some scary error message that I, the user, am going to have no idea how to handle. Now you, the programmer, have anticipated that something exceptional can happen. And you've gone about actually handling the error for the user,

giving them an appropriate error message instead

* Actually, to use the except block, you need to know the type of error

# 5 NameError
number.py

try:
    x = int(input("what's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")






* error output ---- input solitary bear 
what's x? sol
x is not an integer
Traceback (most recent call last):
  File "/home/user/Programming/Python-Learning-Journey/Problem-Set-3-Exceptions/Lecture/number.py", line 6, in <module>
    print(f"x is {x}")
                  ^
NameError: name 'x' is not defined

- firsly what we did is 
mention in #before name error and something interesting  ----- in mynotes 

* about error
But I fear I've introduced a new mistake. Well, let's see. What is now incorrect? Let me go ahead and again run Python of number.py, Enter. Let me go ahead and do it correctly with 50. And all seems to be well. But, again, let's try those corner cases--

the zeros, the negative numbers, or, in this case, the cat. Let me go ahead and type in C-A-T again. Now I have a name error. So now it's yet another type of error in my code that I've introduced here. And what does this name error mean? Well, just as a value error refers to that-- the value of some variable

the value that someone has typed in is incorrect-- name error tends to refer to your code, like you're doing something with the name of a variable that you shouldn't. And why might that be? Well, let me turn our attention back to the code here and consider, what is it complaining about? Well, the name errors what I see down here. And it's telling me, name, quote unquote, "x is not defined." And notice if I look further here, it is mentioning line six. So I know the problem is with my code on line six.

And that worked a moment ago. And I'm defining x on line two.

# 6 else keyword -- with the try and except keywords 
number.py

try:
    x = int(input("what's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")



* now the error is solve 

- how  
If you think back to our discussion of conditionals, we saw if. We saw elif. We saw else, which was kind of this catchall, what you should do in the event that nothing else is relevant. That's kind of the same intuition here for the try-except feature of Python. What you can do is this. You can try to do the following, as I've done, except if this goes wrong. But if nothing goes wrong, else go ahead and do this.

So this is one way I can solve this same problem now. No matter what now, Python is going to try to execute line two. If something goes wrong, it's going to execute lines three and four to handle that value error. However, if you try and this code succeeds, then there is no exception to handle. So you're then going to execute this line here.

So it's a little confusing, perhaps, in that we're now using else both for conditionals-- if, elif, elif, elif, else. And we're also using else with these try-except blocks. But that's OK. That's part of the language. That's one of the features. 


- also think comparing code 5 and 6 
And the error is being handled with this code here. But notice this line six is not indented. It's left aligned with the rest of my code, which means no matter what, line six is going to execute. It's going to execute whether I typed in 50 or I typed in cat. But if I typed in cat, again, x never gets a value.

So it's not defined here on line six. So when I introduced, finally, the else statement, that makes sure that these things are mutually exclusive. I only execute the else if I tried and succeeded up above.


# 7 using loop and break keyword 
number.py

while True:
    try:
        x = int(input("what's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")


- It's a little unfriendly of me to be rejecting the user's input after they fail to provide an integer and just quitting the program, really, right? It'd be more user friendly if I just prompt or reprompt the user again and again

And in the chat, if you could, what's the feature of Python that you can use if you want to do something again and again and again until such time as the user cooperates and gives you what you're looking for, like a number? So yeah, loop

# 8 what if we hadn't used break keyword 
number.py

while True:
    try:
        x = int(input("what's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        print(f"x is {x}")


- AUDIENCE: 
Do we really need to break? Can't we just print? Or what keeps us from just printing? 

- DAVID MALAN: 
Good question. So let me try that. Couldn't I just print? Well, let's see what happens if I do that. Let me move this print line at the end into my loop

here, thereby shortening the program. And, in general, that's been a good thing. Let me go ahead and type in 50. OK, x is 50. OK, maybe it's 49. X is 49. OK, maybe 48. Unfortunately, I think-- you're laughing. You see it. I never break out of the loop, which maybe that's a feature. Maybe you want this to be your program. But I didn't.

I'd eventually like this game to stop. So I need to break out in that way.




# 9 again using break keyword but something different then code 7
number.py

while True:
    try:
        x = int(input("what's x? "))
        break
    except ValueError:
        print("x is not an integer")       
print(f"x is {x}")


- AUDIENCE:
Hi, can I use a break [INAUDIBLE] except and else?

For example, in another print, may you use printing the else, you can use prints together with break or something like this? 
- DAVID MALAN:
So you can use break inside of loops to break out of loops. And you can use it inside of a conditional, like an if, an elif, or an else. You can do it inside of a try, except, else statement to.

Any time you're in a loop that you want to break out of, you can use this keyword, break. I'm using it in the context of exceptions. But it's not restricted to that. And let me show you, too. It doesn't even have to be in the else. If I wanted to, I could actually do this. I could get rid of my else.

And I could go back to line three, add another line that's indented, line four, and break out here. Now, why is this logically OK? Well, consider what I'm now trying to do. I'm trying to execute line three and converting the user's input to an int. And I'm trying to store the result from right to left in x.

If something goes wrong, the code we've already seen is immediately going to jump to line five and then six to handle the exception. But if nothing goes wrong, my code presumably should just keep on executing line by line. So I could technically logically put the break here. And watch what happens when I run this version.

Python of number.py, 50, Enter, it worked. I broke out of the loop.



# 10 inventing our own function to get int so everytime in future we don't need to create 
number.py

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("what's x? "))            
        except ValueError:
            print("x is not an integer")
        else:
            break
        return x        

main()

- It would be nice, as we've seen, to maybe just invent my own function, get int to get an integer from the user both today and tomorrow and beyond.
Let me define a function called get int that takes no arguments for now.

- But it's not just breaking that I want to do here.
Now that I'm in a function, recall our discussion of return values. If you're inventing your own function whose purpose in life isn't just a print something on the screen like a side effect but is to hand back a value, to hand you back a value, like on that same post-it note from our discussion of functions,
well, you need to return x explicitly

- I'm manifesting a couple of good properties

here. One, I've kind of abstracted away this notion of getting an integer. And even though I just artificially hit Enter a whole bunch of times just to hide that function for now-- it needs to be there, but we don't need to see it at this point-- notice that now this entire program really boils down to just these three lines of code now.

Because I've abstracted away that whole process of getting an int from the user into this new function of my own called get int.

# 11 using only return why to to use break 
number.py

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("what's x? "))            
        except ValueError:
            print("x is not an integer")
        else:
            return x        

main()




# 12 can me make the code more shorter 
number.py

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("what's x? "))  
            return x          
        except ValueError:
            print("x is not an integer")       

main()


- Any suggestions for tightening up my implementation of get int? 
- AUDIENCE: 
You can just return the value on the try function, when you're trying. You take the input x and then return x.
- DAVID MALAN: 
Good. We can just return x a little higher up. And let me correct folks as we go. It's not a try function. It would be a try statement, technically. A function typically has a parentheses and another one.

In this case, it's just a statement. But we can do exactly that. I don't technically need the else. If I really want, I could do this. Right after line nine, I could return x here.

# 13 why we need define a variable if never use it after definin it (why not just return the input directly)
number.py

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("what's x? "))  
        except ValueError:
            print("x is not an integer")       

main()

- recall our discussion of defining variables unnecessarily sometimes. Why define a variable here if you're immediately going

to use it here and then never again? So we could avoid a new line here. And I could avoid even defining x explicitly. I could just say something like this. I could return int, input, quote unquote, "what's x?" I can do it all at once. Now, which is better? I don't know. I mean, again, this is where reasonable people might disagree.

I'd argue that, on the one hand, we're tightening up the code. We're using fewer lines. It's easier to read, lower probability that I've made a mistake. On the other hand, it's a little more complicated to understand, perhaps. It's a little less obvious where I'm returning from. So I think arguments can be made either way.

At the end of the day, what's important is that you've done this consciously. You've made a decision to do it this way or this way. And you can justify it in your mind-- not that your answer is, eh, it worked, so I left it alone. Have a good reason. Come up with a good reason. And that will come with experience and practice.

# 14 using pass keyword 
number.py 

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("what's x? "))  
        except ValueError:
            pass


main()


- Well, let me propose to you that we make one other refinement here. Suppose that you're finding your programs to be a little noisy. And it's a little obnoxious that you keep telling the user, x is not an integer. What if you want to make things a little gentler and just prompt the user again with the same words, what's x? What is x? Again and again. Well, you can do that as well. And it turns out that if you want to handle an exception in Python but you want to pass on doing anything with it-- so you want to catch it,

but you essentially want to ignore it. You don't want to print anything. You don't want to quit the program. You just want to silently ignore it, like if you're talking in a room full of people and it's your turn to talk and you're just like, pass. They're still calling on you. But you're not doing or saying anything more.

Well, we can add this keyword to our code here. Let me go back to my program here. And instead of printing out again and again, x is not an integer, I could just do this. I could pass on handling the error further. I'm still catching it. So the user is not going to see a scary message even mentioning value error.

My code is catching it. But I'm passing on saying anything about it. I'm going to stay in the loop. I'm going to stay in the loop and keep prompting and reprompting the user

- So it's just a little, maybe, more user friendly and that you're just reminding the user what you want. Maybe it's worse. Maybe it would be helpful to tell the user why you're prompting them again and again. It's not obvious. So it could go both ways. But, again, it's just another mechanism, now, for handling these errors.

We use the except keyword to catch a specific error. But we don't have to handle it more than that. We can just pass on doing something further.


# 15 getting get_int function little more usable 
number.py 

def main():
    x = get_int("what's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))  
        except ValueError:
            pass

        
main()


- one additional step to improve the implementation of this get int function. Let me propose that we not hard code, so to speak-- that is type manually x

all over the place. Let's make this function, get int, a little more reusable. Right now, notice that I'm just kind of using the honor system that, well, main is defining a variable called x. And get int is asking for a variable called x. But it would be nice if the caller, main, doesn't have to know what the call-ee is naming its variables and vise versa.

So caller-- to call a function means to use it. The caller is the function that's using it. The call-ee is just the function being called. It would be nice if I'm not just hoping that x is the same in both places. So let me propose this. Let me propose that we actually add a parameter to get int, like this.

That is to say, if main wants to use the get int function, well, then main should probably tell the get int function what prompt to show the user. Just like the input function, recall, that comes with Python, it's up to you to pass in a prompt that the user then sees when the human is asked for input. So how do I make this work here?

I can go down to my definition of get int. And I can say, all right, get int is going to take a parameter now, called prompt. I could call it anything I want. But prompt in English is pretty self-explanatory. It means the message the user will see. And now, down here, when I actually use input, I don't have to presumptuously say, what's x?

Because what if the program, the caller, wants to ask for y or z or some other variable? I can just pass to input whatever prompt the caller has provided. So now I'm making more reusable code. It still works just the same. I haven't changed the functionality, per se. But now it's a little more dynamic

#

#

#

#

#

#

#

#

#

#

#

#

#

#

##
#
#
#
#
#