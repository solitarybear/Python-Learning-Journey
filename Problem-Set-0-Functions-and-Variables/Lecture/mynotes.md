# 
One of the best way you can do learning a programming language is, honestly learn to read the documentation 
because truely all of the answers to your question will in some way be there even though admittedly, it's not always obvious

and i will say too(also i (solitarybear)) Python documentation isn't necessarily the easiest thing, especially for the first time or novice programmer 
it too just takes practices, so try not to get overwhelmed  if you're not sure what you are looking at 

>code 
python (*objects, sep = " ", end = "\n" , file=sys.stdout, flush=False)

now inside these parenthesis they are argument, the potential arguments to the functions
However when we were looking at these arguments in the documentation like this there's technically a different term that we would use. They are technically the parameter to the function
so when you are talking about what you can pass to a function and what those inputs are called, those are parameters
* when you actually use these function and pass in values inside those parentheses, those inputs, those values are arguments 

same same but different (ha haha ha )
looking at the problem from different direction
when we are looking at what the function can take versus what you are actually passing into the function.


>*objects 
astriek and then the word object -> means that the print function can take any no. of objects 
you can pass 0 strings of text, one strings of text , two or infinitly many

>sep = ''
sep short for separator


>end = '\n'
\n means new line
this end means whole thing (when we use print something) is ended by a new line


# Parameters 
when we have been passing values to print those are called positional parameters -- positional in the sense that first thing you pass print first , the second thing you pass to print after comma get printed second so forth 

>named parameters
named   SEP , separator
named   END , for line ending 
those are named parameters becasuse one , they are optional and you can pass them in the end of you print statement but you can use them all by name 


# docs.python.org --- Text Sequence Type - str
Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways:

Single quotes: 'allows embedded "double" quotes'

Double quotes: "allows embedded 'single' quotes"

Triple quoted: '''Three single quotes''', """Three double quotes"""

Triple quoted strings may span multiple lines - all associated whitespace will be included in the string literal.

further more to triple quotes 
>hello.py
import textwrap
def my_function() :
    # WITHOUT dedent (What you have now)
    text = """
    this is line one.
    this is line two.
    """
    # WITH dedent (Cleans up the leading whitespace)
    cleantext = textwrap.dedent(text).strip()

    print ("----original----")
    print (text)
    print ("---clean---")
    print(cleantext)

my_function()

>dedent tool
If you want your code to look clean (indented), but you want the output to be "left-aligned" (no tabs/spaces at the start), you usually have to use a tool called dedent.


# the backlash \
n Python, the backslash (\) is indeed a special character with two very distinct roles: it acts as an Escape Character inside text and a Line Continuation Character in your code structure. 
1. The Escape Character (Inside Strings)
When you use a backslash inside a string (text surrounded by quotes), it "escapes" the character that follows it to give it a new meaning. 
Common Escape Sequences:
\n: Creates a New Line.
\t: Inserts a Tab (space).
\' or \": Allows you to put a quote inside a string without ending the string itself.
\\: Represents a literal backslash.
Raw Strings: If you don't want Python to treat \ as special (common for Windows file paths), prefix the string with an r, like r"C:\Users\Name". 
2. Line Continuation (Inside Code)
If you have a very long line of code that is hard to read, you can put a backslash at the very end of the line to tell Python that the command continues on the next line. 
Example:
python
total = 10 + 20 + 30 + \
        40 + 50
Use code with caution.

Pro Tip: Python experts usually prefer using parentheses () instead of backslashes for this, as it is considered "cleaner" and less prone to errors if you accidentally hit a space after the backslash

# str
strings themselvess comes with the lot of build in functionality 
We can manipulate the user input to do more than just join it with something else like hello, we can actually clean it up or reformat it in a way that hopefully looks  a little better for us

# strip()
>name.strip()
meaning 
on right hand side we written variable name name and then used a period or a dot and then i seem to be doing what's function

Any time we have seen a function thus far , we see the function's name --- print or input then we see () parenthesis and another parenthesis that's exactly what i see here 
but this function im using something differently 
Technically this function is in this context  called method 
means 


if name is a string or str (both means same) well it turns out according to documentation. There are lot of functions that come with strings in python and you can access that functionality by using 
name of the string like literally name here , then a period, then  the name of the function and then an open parenthesis and a close parenthesis

maybe some argument inside those parenthesis but in this case it doesn't need any arguments 
i just want to strip the space from the left and the space from the right of the user's input 

that's not enough i wanna rem that white space on the right and left so i'm gonna equal sign again and notice that just as before, this  doesn't mean equality that means assignment right to left 

# capitalize() 
i made a mistake while wrtting the program in which i wrote 
name = name.Capitalize()

still first line of code worked and then when came to this line of code then it said there is error 

this is why python is called as interpreted language 

* Note: Python does do a quick "syntax check" for things like missing colons or bad indentation before running, but it can't always catch misspelled function names until it actually tries to use them!


* A method is a function that's built in to a type of value, like these functions

# split
one called split, which can, as the name suggests,

split a string into multiple smaller substrings, so to speak. For instance, if the human here is in the habit of typing in their first name, then a space, and then their last name, and you want to go ahead and greet them only by first name, well we could actually leverage that single space between the first name and last name and split that string

into two smaller substrings.

# Interactive mode 
Well it turns out that in Python you cannot necessarily-- you don't necessarily have to keep writing code in a file like Hello.py and then running it in a terminal window. One of the features that many people like about Python

is that it supports this so-called interactive mode. Like you can start writing Python code and immediately execute each of those lines interactively, especially if you don't care about saving all of your lines of code. You just want to execute code and get back some answers. So for instance, 

#maximize the terminal if you want a big screen
type 
python

and 

>>> (shown up)

now here we can write our code and exceute it line by line

Interactive Mode in VS Code is a powerful hybrid tool that lets you run Python code in small, immediate chunks rather than executing a full script from top to bottom.
It works by opening a dedicated window alongside your editor where you can see text outputs, data tables, and plots instantly.
You can trigger this mode by highlighting code and pressing Shift + Enter, or by typing # %% into your script to create "cells" that can be run individually.
Because the session stays active in the background, all your variables and data remain stored in memory between runs, which saves you from having to re-import large files or re-run slow calculations every time you make a tiny change.
It essentially gives you the "live" feel of a Jupyter Notebook while allowing you to keep your work in a standard .py file that is easier to manage and version control.
I can help you dive deeper if you tell me:
Whether you want to see the specific keyboard shortcuts for your OS
If you need help setting up the Jupyter extension required for this mode
If you want a quick code example to see how the # %% cells work turn-by-turn






# Other Data Types 

# INT -- another type of data type int---- integer

# 
AUDIENCE: I think the issue is that it's concatenating strings because you use the + operator instead of adding. DAVID MALAN: Perfect. So perfect intuition. We've seen that + is used a little differently in the context of strings

because it concatenates, that is, it joins the two strings, and that seems to Indeed be what's happening here, even though the user typed a number. But the interesting thing here is that, when you get user input, because they're using a keyboard on their Mac or PC or their phone, it is always going to be text.

It might look like a number, but by default, it's coming from the keyboard as a string-- that is, as text. And so, how do we go about resolving this if ultimately we don't want to treat those inputs as strings, we want to treat them as actual numbers? Well we need another function and it turns out in Python

that you can convert sometimes from one type of data to another type of data

* * so it turns out that INT is not only a type of data  in python, its also a function and it is a function that if you pass in an input, like a string, so long is that string looks like a number like 1 or 2 

it will convert it to actuall number, that you can mathematics on instead


# float data type 
A float is a number with a decimal point, properly called a floating point value.


# round function 
>syntax by david malam
round(number [, ndigits])

>sytax in docs.python.org 
round (number , ndigits = none)


* notice Notice this time there's no star, there's no star objects like there was for print. The Round function takes just one number as its first argument, period.

That's its positional parameter. But notice this syntax. And this is a convention in programming or technology more generally, generally speaking, when you see square brackets and documentation like this, this means that you're about to see something optional. And so what this means is that if you want

to specify more precisely the number of digits that you want the round function to round to, you can specify it here by adding a comma and then that number. So if we read the documentation, if you don't specify a number of digits, you just specify the number to round, it rounds to the nearest integer.

--------------------------

> round(number, ndigits=None)
Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.

For the built-in types supporting round(), values are rounded to the closest multiple of 10 to the power minus ndigits; if two multiples are equally close, rounding is done toward the even choice (so, for example, both round(0.5) and round(-0.5) are 0, and round(1.5) is 2). Any integer value is valid for ndigits (positive, zero, or negative). The return value is an integer if ndigits is omitted or None. Otherwise, the return value has the same type as number.

For a general Python object number, round delegates to number.__round__.

* Note The behavior of round() for floats can be surprising: for example, round(2.675, 2) gives 2.67 instead of the expected 2.68. This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float. See Floating-Point Arithmetic: Issues and Limitations for more information.

# understanding formating when we use f string or str.format()
1. Breaking Down the Code
In the expression f"{z:,}":
f"...": This is an f-string (Formatted String Literal). It tells Python, "Look inside the curly braces for variables."
z: This is your variable (the number 1000).
:: This is the separator. Everything before the colon is the value, and everything after the colon is the formatting instruction.
,: This is the grouping option from the documentation you found.

2. Why do we need these terms?
We use these terms to make data human-readable.
If you have a number like 1000000000, it is hard to read. By using the grouping option ,, Python automatically formats it as 1,000,000,000.

3. Mapping your code to the "Mini-Language"
Look at the list you found in the docs. Here is how your code fits into that "Form":

- Part of Doc	        Your Code	        What it does
grouping	            ,	                Tells Python to put a comma every 3 digits.
width	                (empty) 	        You didn't set a width, so Python uses just enough space for the number.
precision	            (empty)	            You didn't set decimals, so it stays as an integer.
type	                (empty)	            Since you left it blank, Python guesses the type (integer).


## Format Specification Mini-Language¶
* detail info under the above section in the docs.python.org

The general form of a standard format specifier is:

format_spec:             [options][width_and_precision][type]
options:                 [[fill]align][sign]["z"]["#"]["0"]
fill:                    <any character>
align:                   "<" | ">" | "=" | "^"
sign:                    "+" | "-" | " "
width_and_precision:     [width_with_grouping][precision_with_grouping]
width_with_grouping:     [width][grouping]
precision_with_grouping: "." [precision][grouping] | "." grouping
width:                   digit+
precision:               digit+
grouping:                "," | "_"
type:                    "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g"
                         | "G" | "n" | "o" | "s" | "x" | "X" | "%"

# python interpreter take this seriously
The problem here, though, is that Python is just taking me literally. I have defined my function Hello all the way down here, but I'm trying to use it way up here. And that's not allowed. Python's interpreter is going to take you literally and if you use a function, it must already exist by the time you are calling it.

So how do I fix this? Well, apparently I can't do that. I have to define any functions I want at the very top of my file, but that too could get me into a bit of trouble eventually because if I constantly have to define a function above where I want to use it


# scope 
scope refers to a variable only existing in the context in which you defined 

# return
we can use return keyword to return a value explicitly yourself
#
#
#
#




