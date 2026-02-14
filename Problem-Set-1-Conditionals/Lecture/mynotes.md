# conditionals
Conditionals are "decision-making" tools that allow a program to execute different blocks of code depending on whether a specific condition is True or False. 
- >     greater than
- >=    greater than or equal to 
- <     less than
- <=    less than or equal to
- ==    equal to or represents equality
- !=    not equal to 


- if 

> other operators
- +
- -
- *
- /
- %

>
if          keyword
elif        keyword
else        keyword

or          keyword
and         keyword
match       keyword

# always think
it's a good habit to get into thinking about. Could my code be better?

Could my code be simpler? Could I improve this code further? It's subtle, but could I improve the design? Could I ask fewer questions? Could I tighten it up, so to speak


# the colon ':' in python
Yes, the colon (:) is absolutely necessary in Python because it serves as a syntactic marker to tell the interpreter that a new block of code or a specific structure is starting. 

The colon is required at the end of every statement that introduces a new indented code block: 

# the indentation 'the white spaces equals to 
In Python, indentation refers to the whitespaces (spaces or tabs) at the beginning of a line of code. Unlike other programming languages like C++ or Java that use curly braces {} to define code blocks, Python uses indentation to indicate the structure and scope of the code. 

## Core Rules & Best Practices
Standard Spacing: While Python allows any number of spaces (minimum one), the official PEP 8 style guide recommends using 4 spaces per indentation level.

Consistency: You must use the same number of spaces for every line within the same block.

No Mixing: Never mix tabs and spaces in the same file, as this can lead to hard-to-debug errors.

First Line: The first line of a Python script cannot be indented.

Trigger: A colon (:) at the end of a statement (like if, for, or def) always indicates that the next line must start a new indented block. ￼

# and keyword
we introduce one other keyword here in Python, to see exactly how we might combine additional thoughts. And that's going to be literally the word and, a conjunction of one, or two, or more questions that we might want to ask at once.

# parity 
Odd or Even: In math, parity is the property of an integer being either odd or even.

operator we use is ---- %

# bool
we can actually return what are called boolean values 

we have seen in python that we have str or strings , int or integers, float or floating point values all of which are different types of data in python
python also have another fouth type of data that is bool for the boolean value 

nice thing about bools is that they can only be true or false 

* And it must be capital 'T' and capital 'F' if you're writing itself 

# Question:- when we pass the argument can we pass the addree too ?
>Doubt
I have just one query, based on the background of Java.
There, when we used to pass the argument, we can also pass the address of the variables. So is there any sort of this concept in Python? 

>Reply:
DAVID MALAN: Short answer, no. Those who are unfamiliar with Java or other languages, or C, or C++, there's generally ways to pass values in different mechanisms that allow you, or disallow you, to change them. In Python, no. Everything we're going to see is actually, in fact, an object. But more on that down the line.

>asked to ai
1. i was studying python in the lecture someone asked a question like this 
I have just one query, based on the background of Java.
There, when we used to pass the argument, we can also pass the address of the variables. So is there any sort of this concept in Python?
i know about c++ so can u explain me this question and its answer 
so i can understand what there are talking about

2. actulllay i come from the c++ backgroung but 
the who who asked the doubt in the lecture came from the java backgroung so i want to find out about what its talking about and what its questiona and what would be the correct answere

3. def increment(x):
    x = x + 1  # This doesn't change the old 'x', it creates a new 'x'
num = 10
increment(num)
print(num)  # Output: 10 -> It didn't change!
in this code u said that it does change the x it it creates a new x 
so how can i print that x

4. that means we can change the value of num but as inside the function we can't change it 
but when we try outside the function yes we can did that (its just overwriting or we can say reassingng another value

5.  didn't understand that in the reassigning how that is changing name tag is different from the the mutating where we are changing value inside the nametaband happen to the just previuos name tag that we had when we reassigning some thing

6. does that means adress of the num chnaged when we reassig

7. can u just explain me how memory is managed and used by python 
i know what happens in the c++ so  i need an idea what happen here in python in brief



# Question can we use that dot strip or etc that we used previously to our own defined function
>SPEAKER 7: So if you define one, within your code, like you made it up, are you allowed to use the dot operator like we did name dot strip, and use it like that? 

>DAVID MALAN: Good question. If you've created your own function, can you use other functions, like dot strip, or dot title, or dot capitalize,

that we've seen in the past? You can use those on strings. Those functions come with strings. You can't necessarily use them on your own functions, unless your function returns a string, for the examples you gave. I'm returning a bool. Bools have no notion of white space to the left or the right. You can't call strip, you can't call capitalize. But if you were writing a different function

that returns a string, absolutely. You could use those functions, as well.

# If we alresdy have boolean expresion (see code 13) why ask question when we already getting true or false from the boolean expresion
That is, by definition, a Boolean expression. It has a yes/no answer, a true/false answer. Well, if your Boolean expression itself has a true or false answer, why are you asking a question in the first place? Why ask if? Why say else? Just return the value of your own Boolean expression.


# 'match' keyword
And the keyword that you can now use, in recent versions of Python, is called this-- match. Match is a mechanism that, if you've programmed before, is similar in spirit to something called switch in other languages. For instance, let me go ahead here
Well, it turns out another technique you can use is, indeed, this keyword called match, which is very similar in spirit, but the syntax is different. And it allows you to express the same ideas a little more compactly

- you can equivalent of "Harry" or "Harmione" or "Ron" for inside the match keyword other wise outside the match keyword '|' is treated as bitwise or operator

And it's worth noting, if you've programmed in some other language, the syntax here is, indeed, correct. You do not need, for instance, a break statement, as has been peppered throughout.
And you don't need something like default, or something explicit. You, indeed, just use this underscore as your catchall at the end of the match.

* google both the lines above for better understand (~solitarybear)

#
