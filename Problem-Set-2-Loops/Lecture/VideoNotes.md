# 00:00:00
[MUSIC PLAYING] DAVID MALAN: All right. This is CS50's Introduction to Programming with Python. My name is David Malan, and this week we focus on loops, this ability in Python and a lot of other programming languages to do something again and again, a cycle of sorts. And let's see if we can't begin by motivating

exactly why we have this ability to do things cyclically using these loops. I'm going to go ahead here and open up VS Code. And in my terminal window, let's go ahead and create via code cat.py, a Python program that meows like a cat. And I'm going to go ahead here in this Code tab, and very simply, perhaps,

I'm going to start by implementing this cat just by using print. We're going to have this cat not make audible sounds, but just print meow, meow, meow on the screen three times. Well, I think the simplest way I can do this is just to print meow once, and to print meow again, and to print meow one last time on the screen.

And now let me go down to my terminal window, let me run Python of cat.py, Enter, and meow, meow, meow. All right, so this program works. This program indeed works if my goal is to get the cat to meow three times. And let me propose, just to help us wrap our minds around what's going on inside of the computer, let

me propose that we consider this flowchart. So as before, we have this flowchart that starts with this oval, which just means start reading here. And then notice, it goes via arrows to a meow, meow, meow, and then it stops. It's perfectly correct, and honestly, it's wonderfully simple, but I daresay we can find fault with my code nonetheless.

Why is my code arguably poorly designed? Now the answer is going to be loops in some way, but let's see if we can identify in what way the code is actually poorly designed in some sense. Let's see. Any thoughts. Alex? AUDIENCE: OK. So, I mean, repeating the same action like three times or even more is not a good habit.

DAVID MALAN: Yeah, I'm just repeating myself. And honestly, it's not that big a deal. If we go back to my code here, am I really doing such a bad thing by just printing meow, meow, meow three times? Not really, but let's consider the logical extension of this. Suppose I wanted to meow four times or five times or 50 times or 500 times.

Do you really think, even if you've never programmed before, is the solution to this problem really going to be to hit copy-paste 50 times? Like probably not. We can probably do better than that. And beyond it just being ugly at that point, having so many lines of identical code, just imagine if you wanted to change the code.

Maybe I change my mind and I don't want to make a cat, I want to make a dog. So now it has to say woof, woof, woof multiple times. Now I have to change that in 50 different places. And yeah, sure, I could do find and replace, but come on, like we're programmers now, there's got to be a better way than just repeating ourselves.

So I bet we can do better than that if we think about a little harder how we go about structuring this program. And we can do that if we augment our vocabulary just a little bit. It turns out in Python, and in other languages, too, there's a keyword called while. And while is one way that we can express what's called a loop, a block of code that's going to do something again and again and again-- 0 times, 1 time, 2 times, 50 times, as many times as we want. But while rather leaves to us the particulars

of how we express ourselves to do something again and again. So let me go back over to VS Code here and let me propose that I do this. While is a construct that allows me to ask a question again and again. And any time we've seen a question, it's been in the form of a Boolean expression, a question to which the answer is

true or false. Well, how could I do this? How could I print out meow three times and ask three times a question to which the answer is true or false? Well, what if I did some counting? Like literally on my fingers. And if I'm trying to count maybe down from three, I want to meow three times, I can put three fingers up and I can meow. And then I can put like one of the fingers down and then meow. And I can put one of the fingers down and I can meow. Put one of the fingers down. And maybe the question I can ask every time I meow is, do I have any fingers up still? Do I have any fingers up still? And if the answer is true, keep going. If the answer is false, stop. So how can I translate that to code?

Well, once we've added this while keyword-- I think we have all the building blocks already, let me propose that I do this. Let me propose that I give myself a variable. And I'll call it i for integer, but I could call it anything I want, and I'm going to initialize it to 3. Then I'm going to use this new feature of Python, while,

# 00:05:00
and I'm going to ask a question, the answer to which must be true or false. And I'm going to say, while i does not equal 0. So I'm going to ask the question, while i does not equal 0, do the following. Notice the colon at the end of the line. Notice my indentation. And just like with functions, just like with conditionals,

you indent the lines that you only want to execute as part of this other thing. What do I want to do while i does not equal 0? Well, I think I just want to meow. But it's not enough just to write this code. If I were to very dangerously run Python of cat.py and hit Enter right now, what might happen on the screen?

Whether you've programmed before or not. Why is this a very bad thing potentially? It's not going to break things, but it might lose control of my computer somehow. Any thoughts? Yeah, Timo? AUDIENCE: Hi. I think it's going to continue to print out meow since i is always equal to 3 and the while is always true.

DAVID MALAN: Yeah, exactly. If I'm initializing i to 3-- that is, setting it equal to 3 on line 1, then I'm asking the question, while i does not equal 0, and that's going to be true, it does not equal 0, it obviously equals 3, print meow. And the way a while loop works is that the Python interpreter just keeps going back and forth. It goes from line 1 to line 2, then to line 3, and then it goes back to line 2 to ask the question again. If the answer is still true, it goes to line 3. It then goes back to line 2. If the answer is still true, it goes back to line 3. And to Timo's point, if you're never actually changing the value of i, it's always 3, you're just going to be looping literally forever, and this is an accidental infinite loop. So we've got to be smarter than that.

And I'm not going to hit Enter because I don't want to lose control over my computer here such that it's printing out meow forever. Fortunately, if you ever do do that and you find yourself in an accidental infinite loop, Control-C for cancel or interrupt is going to be your friend. If you ever seem to lose control, you don't need to reboot or turn off the computer. You can just hit Control-C in your terminal window and that will likely fix it. All right, well what do I want to do, then, after meowing each time? I think what I'd like to do here is maybe something like this. Let me update i to equal whatever the current value is minus 1 here-- whoops, sorry. Minus 1. So if i on each iteration--

I'm updating i to be one less, one less, one less, it should eventually hit 0, at which point the answer to 9.2's question will now be false. So let's see if this works. I'm going to go down to my terminal window and run Python of cat.py, and I indeed get three meows. Why? Because I've wired this up like a machine in software, if you will.

I've set i equal to 3, then I keep asking this question. But I keep turning the gears, I keep changing the value of the variable to make sure that ultimately it is actually being decremented-- that is, decreased by 1 until we eventually hit 0. Now for those of you who think I'm a little more graphically,

let me pull up one of our usual flow charts. This is just a representation graphically of the exact same thing. Notice what's happening. I first start the program, and then I initialize i to 3, and then I ask the first of my questions. Again, the diamonds always represent questions. And the answer is going to be true or false.

Does i not equal 0? Well, it doesn't, it equals 3. So if I follow the true line, I meow. And then I follow this arrow, and I update i to equal i minus 1. At this point in the story, i presumably equals 2 mathematically. I follow the arrow. And there's the loop. This is why it's nice to see this graphically,

perhaps because you can literally see the loop back and forth. Now I ask the question again. Does 2 not equal 0? Well, it does not equal 0, it's 2, so we meow again. We change i from 2 to 1. Well, does 1 not equal 0? Well obviously 1 is not 0, so we meow again. We decrement i again. i is now 0. Does 0 not equal 0?

No, it equals 0, so the answer is false and we stop. So there, perhaps more so than any of our flowcharts before, do you really see the structure of what's happening inside of the program? And you don't have to get into the habit of making these charts or creating these charts, but just as a first pass at what's

going on inside of the computer, that's indeed one way to visualize it instead. Well let me propose that, like always, there's many different ways to solve this problem. And suppose you just like to think a little differently. Maybe you don't like starting at 3 and then counting down to 0. Maybe you're just brain doesn't work that way and you prefer to count up instead of down. Totally fine. Let me go ahead and change my code here to set i equal to 1 instead of 3. And here, let me just change my logic. Rather than checking for not equal to 0, like maybe you don't like thinking in terms of not because it's a little confusing, and it might be, let's just check that i is less than or equal to 3.

# 00:10:00
So we'll be a little more explicit. We'll count from 1 up through 3, each time printing meow, but I'm going to need to change this line here. Let me see if we can't call on someone to change line for me. How do I want to change line 4 to be consistent with counting from 1 up to and through 3? AUDIENCE: I would be plus 1 every time you meow.

In this case, we want to add one not subtract 1. And in fact, if you think about this, this 2 could end very poorly. If you start counting at 1 and you keep subtracting 1, subtracting 1, subtracting 1, I think we're going to find ourselves with the same problem, which is that we're never going to stop because we're going to keep getting more and more negative as opposed to ever getting up to the number 3. So I think you're right, I need to change this to be i equals i plus 1.

And now notice just for clarity, too, the equal sign is, again, our assignment operator from right to left. Logically, this might otherwise strike you as strange. Like how can i equal itself plus 1? Well, it doesn't until you execute this code from right to left. You add 1 to i or you subtract 1 from i, and then you update the value of i

on the left. The assignment copies the value from the right to the left. Well, how else might I do this? Well, I will say that most programmers, computer scientists more generally, tend to start counting from 0. It's a convention and it actually has upsides even in Python and other languages where generally speaking, it's a good thing to start counting from 0 instead of counting like we might in the real world from 1. Let's go ahead and adopt that convention now.

Let me set i equal to 0, and I need to make a change now. Notice, if I don't change my logic, this program just became buggy. The cat has a bug. It's now meowing four times if I run it as is. But the easiest fix here would be to change my inequality to be this, less than instead of less than or equal to.

Now I'm starting at 0, but I'm going up to but not through 3. And even though this might, of all the things we've seen thus far, seem maybe the least familiar, most of us might start at 1, 2, then 3, it's a good habit to get into now, start at 0, and go up to but not through the value that you care about ultimately,

3 in this case here. Well, let me tighten things up a bit here. Not only will this now fix my counting problem, it now meows 3 times as expected, there's a more succinct way to express i equals i plus 1, and this, is because it's such a popular thing to do in code. You can instead just say i plus equals 1, and that's it.

You don't need to put everything on the right-hand side. This is a special syntax that says the exact same thing, increment i, but it does it with a few fewer keystrokes. It's just a little more pleasant to type, it's a little faster to read, it's just a convention. Those of you who have programmed in C, C++, Python--

no, not Python. C, C++, Java, JavaScript might have seen plus-plus before or minus-minus. Sorry, Python doesn't have it, so you cannot use that. This is as succinct as your line of code might get. All right. Let me pause here to see, then, if there's any questions about these implementations of while loops.

AUDIENCE: Can we use stuff like for loops which have a certain i-value initialized to it at the start and it runs from the particular condition you put into the thing and increment it as you go along? DAVID MALAN: Short answer, no, you cannot do what you're describing, but there is another type of for loop that we will soon see.

But let's come to that in just a moment. Other questions on loops using while here? AUDIENCE: So I had a question about that flowchart. DAVID MALAN: OK. AUDIENCE: There were-- yeah. There were certain symbols for the certain kind of the statements were-- are they certainly used for that kind of statement that they--

DAVID MALAN: They are. So I deliberate-- I deliberately use certain types of symbols, certain shapes here whereby an oval is conventional for start and stop. I used rectangles for any statement of code, like an assignment or a printing and so forth. And I used diamonds to represent questions that you might ask,

# 00:15:00
conditions as we've seen. If you're doing this for yourself, if you're just trying to make sense of your code and writing it down, you certainly don't need to use these formal symbols, but I tried to be consistent with some best practices. And in fact, let me come back to the same picture, because this was the first version of our picture,

but we've since modified our code a couple of times. This, recall, was the version where the question we were asking was i not equal to 0, let me go ahead and just change this code now to represent the next version we did, which, recall, changed our logic to start counting from 1, it changed our question to check as i less than or equal to 3,

but then everything else was the same except for the counting, which is now plus instead of minus. And then we refined it a little bit further by counting now from 0 up to but not through 3. And we tightened up this code here by just incrementing 1 by using the slightly more succinct syntax. So at this point, these flowcharts might become less and less useful

for us, because once you've wrapped your mind around the concept and hopefully the picture helps bring that concept to life, it certainly fine to focus entirely on the code and only think about or even draw something like this if you need to wrap your mind around something more complicated than you're used to.

Well, let me go ahead, if I may, and propose that we transition to another approach of types of loops using another keyword here, namely a for loop. And this is a word that does exist in other languages, but doesn't necessarily have as many features as other languages might use it for. But there is a different type of loop-- not a while loop, but a for loop.

And a for loop is going to allow us to express ourselves a little differently, but to do so, I propose that the easiest way is if we introduce one other idea in Python, which is that of a list. And here, too, no pun intended, we're adding to the list of data types that Python supports. We've seen strs or strings.

Ints or integers. Floats or floating point values. Bools or Boolean expressions. Python also has lists, which is another type of data, but wonderfully, this one is probably pretty familiar. A list of things in the real world is a list of things in Python. It's a way of containing multiple values all in the same place, all

in the same variable. So what do I mean by this? Well let me propose that we go back to our VS Code here, and let me start fresh with my code here and not use a while loop at all, but let me use this new keyword for. The way for loop works is that it allows you to iterate over a list of items. So what does this look like?

It might look like this-- for i and the following list of items, 0, 1, 2. This is my starting point, and on each iteration of this loop-- that is, on each execution of this loop again and again, I want to print out meow. Now I'll admit, I kind of like the look of this code already even though there's some new syntax here,

because it's just shorter than the while loop. The while loop had multiple lines a moment ago and it was entirely up to me to decide what i is. I have to check a condition, I have to increment or decrement i. Like I was doing a lot of work, relatively speaking, to make that thing turn, to make that loop going to go. It was very mechanical in a sense. You can in your mind's eye maybe see the gears turning as all of these variables are changing and these questions are being asked. A for loop simplifies all of that, and it just says, if you want a variable like i, a number, and you know in advance how many times want this loop to execute-- three times, we'll just kind of specify what it is you want i to take on as values explicitly. In this loop, i will be automatically initialized by Python to be 0, then meow will be printed. Then Python would automatically update i to equal 1, then meow will be printed. Then Python will automatically update i to be 2 and meow will be printed. And because that's it for the values in that list, Python will stop and it will only meow a total of three times. What is the list? The list in this program is exactly that, 0, comma, 1, comma, 2, and notice the square brackets. Those aren't parentheses, those are square brackets that represent a list. That's how visually as the programmer-- that's how Python knows as the language that you intend for that to be a list. So let me go ahead and run this Python of cat.py, and it works just the same.

But it's only two lines. It's pretty readable once you have familiarity with that construct, but to my constant point about correctness not necessarily being the same as design, in what sense is this program perhaps poorly designed? It seems to work. It meows three times, but why might this not be the best way to solve this problem?

Even if you've never programmed before, again, think about corner cases, things that may or may not happen. Think about extreme cases that really test the quality of this code. I think that because we are saying 0, 1, 2 3 times. And then if you want to take a million, you say 1, 2, 3. And that's what I mean about thinking about the extreme cases. If you're trying to decide for yourself if your own code is good or someone else's code is good, it might look so at first glance,

# 00:20:00
but think about the extreme. Well, what if it's not three things, it's a million things? I mean, are you really going to write out 0 through a million or 0 through 9-- 999,999? Like no, you're not going to write that many numbers on the screen there's got to be a better way. So let's do the better way from the get-go

rather than set the stage for doing something poorly. And the one way we can solve this problem to improve the design is don't just manually specify the list of values, use a function, someone else's function that comes with Python that gives you the list you want. And the easiest way to do that in Python is to use a function called range that returns to a range of values. It expects as input at least one argument, and that number is going to be the number of values you want back. Those values are going to start at 0 and go to 1, to 2, and so forth,

but they will go up two but not through the number you specify. So by specifying range 3, you're essentially being handed back 1, 2, 3 values. And by default, those values are 0, 1, and 2, and that's it. But what's brilliant about this is that now, to Hope's point, if I do want to meow a million times--

I mean, that is an angry cat, I can now do a million by just typing a million. I don't have to literally type 0, comma, 1, comma, 2, comma, 3, comma, 4, all the way up to 999,999, I just do this. So that's got to be a better way long-term. So that's indeed one improvement we can indeed make here still using a for loop, but now using this range function.

And just to show you something else that's Pythonic-- this is not strictly necessary, but it's commonly done, there's a minor improvement we can make here, even if we're just meowing three times. And notice that even though I'm defining a variable i, I'm not ever using it. And it's kind of necessary logically, because Python, presumably,

has to use something for counting. It has to know what it's iterating over. But there's this convention in Python where if you need a variable, just because the programming feature requires it to do some kind of counting or automatic updating, but you, the human, don't care about its value, a Pythonic improvement here

would be to name that variable a single underscore. Just because it's not required, it doesn't change the correctness of the program, but it signals to yourself later, it signals to colleagues or teachers that are looking at your code, too, that yes, it's a variable, but you don't care about its name because you're not using it later,

it's just necessary in order to use this feature, this loop in this case here. So just a minor improvement or change there. But to really gets you intrigued by what's possible in Python, let's take this one step further. So if we really want to be Pythonic, this one, if you've programmed before, is kind of going to blow your mind, so to speak,

whereby if I want the cat to meow three times, what if I actually do this? print, open parenthesis, quote-unquote, meow times 3. You have to be kind of a geek to think this is cool, but this is kind of cool. So you can literally just print what you want, multiply it by the number of times that you want it,

and you will get back exactly that result. Now I've kind of made a mistake here. So let's see what this does. It's not quite as beautiful as this code might look to you-- to some of you, to me. Let me run Python of cat.py, Enter. OK, it's a really like hungry cat or something. It's meowing really fast.

But I can fix this, I bet. Let's think about now some of the basic building blocks we've discussed. The problem is clearly that literally meow, meow, meow is being repeated three times, but it's not as pretty as I want it. I want it to be meow, meow, meow on separate lines. What might be a possible solution here while still

using this multiplication operator? And think back. We've used plus to concatenate strings. You can apparently use multiplication to concatenate strings, but more than once again and again and again. How could I clean this up without reverting to my for loop or my while loop and still use multiplication in this way?

AUDIENCE: We can use the escape sequence which would be backslash n. DAVID MALAN: Amazing. Yes. Think back to backslash n, which is the way you as the programmer can express a new line in code. And I think, if I take your advice, I put a backslash in there inside of my quotes, so that at the end of every M-E-O-W, there's a new line,

# 00:25:00
let's see how this looks. Let me clear my screen and run Python of cat.py. OK, so close. I like this. Let me call on someone else. The only thing I don't like-- and I know I'm being really nitpicky now-- is that it's meow, meow, meow on separate lines, but there's this extra blank line, which I'm just not loving aesthetically.

AUDIENCE: I think we can make n equal to column-- column, not-- like a slash n. DAVID MALAN: Yeah. So here, too, like all of these things we've seen in past weeks are kind of coming together. Recall that the print function lets you control what the line ending is. By default, it's backslash n itself.

Which is why at the very end of this print, the cursor is being moved again to the next line. Well, we need to just override that. So let me go into my code here and let me change this to comma n equals quote-unquote so that it's no longer the default backslash n, it's instead now going to be nothing whatsoever.

That should eliminate, then, hopefully that additional blank line. So let me run this one last time here, Python of cat.py, Enter, and there we have it. So now, at least as programming goes, it's kind of cool that I can distill this into a short line and express myself all at once. Now to be fair, it's a little less readable.

Like now I've got backslash n, I've got times 3, I've got n equals quote-unquote. So you don't have to do things this way. My previous approach with a for loop, totally fine. My previous approach with a while loop, totally fine, and in some sense, perfectly well-designed. But this is just yet another way to do it,

but it's not a good thing if you or your teacher, your colleague, your friend are going to struggle to read your own code. But this is a feature of Python that some languages do not, in fact, have. All right, well let me propose that things get more interesting still if we're not just meowing three times only,

but we're meowing some variable number of times. Let's ask the user how many times this cat should meow. So let me clear the screen here, and let me figure out, well, how do I get a number from the user? The catch here is that if I want the user to give me a number, I'm not doing math, per se, I'm meowing, and therefore, the user

has to give me a positive value. The user has to give me a positive value. So how can I insist on this? Well, if I just do this, n equals int of input, what's n, question mark? Well, I want to check like-- I could say if n is less than 0-- like if it's negative, well I could do this. Well, then ask again.

Int, input, what's n, question mark? OK, well what if the user still doesn't give me a positive number? What if being really difficult they're not paying attention and they typed in two negative numbers? Well, if n is less than 0, well, let's do it again. n equals-- this does not end well. You can't infinitely many times keep checking, is it negative,

is it negative, or is it negative? The program would never be done written. So we can do this I think better maybe with a loop. So let me propose this. A very common paradigm in Python, when you want to get user input that matches a certain expectation you have, that it's all positive, that it's all negative, or just something like that,

you just immediately say while true. You deliberately, and a little dangerously but a very conventionally, induce an infinite loop. Now what is an infinite loop? It's just one that goes forever. And we've seen how that can happen accidentally mathematically. It's absolutely going to happen when you say while true.

Well, the answer to the true question is always true. So this is a way of deliberately inducing a loop that by default is going to go forever. So we're going to need a way of breaking out of this loop when we have the number we want. The convention, though inside of this otherwise an infinite loop is to ask the question you care about,

like give me an int by prompting the user for input. Like what's n, question mark? And then just ask your question. So if n is less than 0, then I think we want Python to just continue to prompt the user again. That is, we want the code to stay in the loop, recall the input function, and hope that the user gives us a better answer.

If this time around it's less than 0, so let's just literally use Python's keyword continue, which says just that-- continue to stay within this loop. Else, if it's not less than 0, let's go ahead and just break out of the loop altogether using another keyword in Python, break. Break will break you out of the most recently begun loop in this case

if it's not the case that n is less than 0. So this will work, and it will allow us to get a value that 0 or greater from the user, but I think we can tighten it up further so as to not bother having an if, and, and else. Why don't we instead just say, if n is greater than 0, go ahead and break? In fact, it's not that interesting a program

if we even allow the user to type in 0. So let's wait until they give us an integer that is greater than 0 and then break out of this loop. And what can I now do down here? For i in range of whatever that value n is, print meow. And honestly, I don't need i here, so let me come back to that principle

# 00:30:00
before. And let me just change it to an underscore just to be Pythonic, if you will. So what's going on? Lines 1 through 4 deliberately implement an infinite loop that otherwise by default is going to go forever. But I'm asking a question, inside of that loop, after getting an int from the user on line 2, I'm then checking,

is it greater than 0? Or is it 0? Is it negative? None of which makes sense for meowing cat. Like I want the cat to meow at least one time. So if it is greater than 0, break. And this break statement, even though it's indented, indented twice, has the effect of breaking out of the most recently begun while loop.

So once the user gives you a positive value, then we get to line 6, at which point we meow that many times because of line 6 and 7. So if I run this now Python of cat.py, Enter, well, what's n? Let's start with 3 where we began, meow, meow, meow. Well this time, let me go ahead and increase the size of my terminal window

just temporarily. Let me run Python of cat.py, let me do it 10 times, meow 10 times now appears on the screen. And the takeaways here are not just that we can meow 10 times or do something again and again, but this is a very common paradigm in Python when you want to do something again and again and again, but only until the user actually gives you

a value that you care about here. And let me propose actually now that we practice a little more what we've been preaching, especially when it comes to, say-- especially when it comes to say writing your own functions. Now that I'm doing all this meowing, it might be nice to actually have a meow function that the inventors of Python

didn't envision, so let me do this. Let me actually get rid of all this code and let me go ahead and do this. Let me go ahead and say define a main function, as I've done before, and let me just blindly call meow 3. Meow doesn't exist yet, but when it does, that'll be great. So let me go ahead now and define meow.

So am I meow function should take as input a parameter called n or anything I want, and this part's pretty easy now. How do you meow n times? Well, for underscore n, the range of n, go ahead and just print meow. So same code as before, nothing new here, I'm just putting that logic inside of a meow function

that's going to have this side effect of printing meow. And now, as before, let me go down here and let me make sure I call main. And if I now run this code, Python of cat.py, meow, meow, meow. It's always going to do three because I've hardcoded to 3. Well, let's make one improvement here. Let me go ahead now and maybe do this.

Let me ask the user for a number. So let's say something like this, number equals get number. Unfortunately, there is no function in Python called get number that gets a positive number from the user, but I can invent that. So define get number, open paren, close paren. And then inside of this function, let me do this.

While true, go ahead and get a number from the user, converting it to an int asking them, what's n, question mark? And then if n is what I want, it's a greater than 0 value, a positive number, I don't want to break this time necessarily, although I could. I instead want to return the value so I can actually do this instead.

And this, too, is a feature of Python. This ability not to just break out of a block of code, but also to return a value in code. To actually return a value gives you the ability, ultimately, to return explicitly a value so that your function has not just a side effect, necessarily, but it actually hands back, just like input does,

just like int does, just like float does, an actual value to the user. Now to be clear, I don't have to return n here. I can still break out of the loop as I've done in the past with code like this, but then after the loop, I still have to return. And so what's happening here is that if you use break to get out of the loop,

but you need to hand back a value from a function, you still have to use the return keyword now explicitly either in the loop as I did or now outside of the loop but still inside of the function. The last thing I'm going to do here now is change that 3, which we hardcoded earlier, to actually be the value of the variable we've gotten from the user

so that now down here, if I run Python of cat.py, Enter, what's n? I can type in 3, I get my three meows, or if I only want one, I now get one meow instead. So if we now have this ability to do things again and again in these loops, let's see if we can't solve some other problems via which to express ourselves cyclically, but get back some interesting answers as well.

And let me propose, for instance, that we look a little more closely at these lists. It turns out that in Python, and really, in programs in general, it's useful to have a list of values, because we're going to be able to work with more and more data, larger and larger data sets. So let me propose that we come back to VS Code here

# 00:35:00
and let's do something that's perhaps a little familiar to some folks, the world of Hogwarts. And let me go ahead and code up a file called Hogwarts, and let's see if we can't have a list of students at Hogwarts here. So I have a new tab called hogwarts.py. and let me go ahead and propose that I just define in this program

a list of students whose names I know in advance. So I'm not going to get user input for now. I'm just going to know from the get-go that the three students I want to consider are these. Our variable is going to be called students. It's going to equal, as I've done in the past, a square bracket, which

means, hey, here comes a list. And those values are going to be Hermione in quotes, because it's a string; Harry in quotes, because it's a string; and then Ron in quotes, because it's a string as well. So this is a list of length 3. It's similar in spirit to my list of length 3 earlier, but that had 3 ints, 0, 1, 2.

Now I have a list of three strings instead. And this isn't very useful at the moment, but let me just do something as a check for myself. Let me print out each of these students. Well wait a minute, how do I print the contents of a list? Well, in the past, when we've printed a variable, we've just printed out the name of the variable.

But I don't want to print out all of Hermione and Harry and Ron all at once. Maybe I want to print out Hermione first, then Harry, then Ron. So I need a way to express more precisely which value do I want from this list? And the way you do this in Python is you use square brackets in another way. If you have a variable-- in this case, called students,

and you want to go inside of that variable and get a specific value-- that is to say, you want to index into the list, you use square brackets this way using numbers inside of the square brackets. And here's where we see that it is useful to think and count in terms of 0 on up instead of 1 on up. These lists in Python are, shall we say, zero-indexed. The first item in a list is at location 0, the second item in a Python list

is that location 1, and the third is that location 2. So you're always kind of off by one mentally, but you get used to it, if you've never programmed before, over time. So let me print out all three students. So let me print out students bracket 0, then students bracket 1. Then lastly, let me print students bracket 2,

and this is my third and final line. And of course, if I run this code, it probably does what you would guess. If I run Python of hogwarts.py, there's Hermione, Harry, and Ron each on their own lines there. But there's got to be a better way, especially if I don't know in advance who's going to be in this list,

if next year there's some new students at Hogwarts, we can use a loop to do something automatically without having to manually type out 0 and then 1 and 2. Well, here's another feature of Python. You can use a for loop not just to count from 0 to 1 to 2, you can use Python to just iterate over anything.

Not just numbers, but strings. So I could actually do this. For student in students, colon, and then indented underneath that, I can say print student. Now it doesn't matter if I have 3 students or 4 or 400, these two lines of code, this loop will print all of those students for me one at a time. So if I now run Python of hogwarts.py, there's the same list,

but I don't need to know in advance how long that actual list is. Now notice, I made a conscious decision here. I didn't call this variable underscore, because this time I'm using the variable. And while I could do this, now, no, no, no, no, your code is getting way too cryptic. If you're naming the variable underscore and you're

using the variable underscore, now you're helping no one. Now you're confusing the reader, yourself down the line, you should call your variables what they are. So a very appropriate name, though I'm sure you could come up with others, would be student, and here, you could say you would stay student as well.

If you'd prefer to be more succinct, it's not unreasonable to do something succinct in a loop like this. For s in students, using maybe the same letter that the list itself begins with, but again, why bother? Python is meant to be more readable. If you have a list of students, iterate over them one student at a time.

Let me pause here to see if there's now questions about lists as I've now defined them, a list of strings in this case, or using a for loop now to iterate over and print each of those names. AUDIENCE: Yeah. So is it not necessary to initiate student in this case? Or we can just declare a variable in the loop?

DAVID MALAN: Good question. You do not need to manually initialize it. Python takes care of initializing the student variable to Hermione first, then Harry second, then Ron third. Unlike other languages, you don't need to initialize it to something yourself, it just exists and it will work. Other questions on loops and lists in this way? AUDIENCE: Since you describe break, so is there

# 00:40:00
any concept of continuing so that we can skip a particular case in loops? DAVID MALAN: Yes. You can continue using another syntax as well. We haven't shown that. For now we focused only on break. So can this for loop work with either hash tables or different kind of tables or arrays? DAVID MALAN: Indeed.

So we're getting ahead of ourselves there, but there are yet other types of data in Python, and indeed, you can use a for loop to iterate over those as well. Anything that is iterable, so to speak, is a piece of data that can be used with a loop like this. But more on those-- more on those soon. In fact, let me transition here to show just another way of solving

this same problem, because up until now when we've used loops, we really have relied on numbers, and that's fine if you prefer to stay in that space. Suppose I did want to iterate using numbers like i and 0, 1, 2, and so forth. Let me propose that we could change this code as follows. If you would prefer to think about, or if the program you're

trying to implement requires that you use numbers like this, you might do this. For i in-- well, I don't want to just say students, because then i is not going to be a number. i is going to be literally Hermione, then Harry, then Ron. I need to iterate from 0 to 1 to 2. If I a list with three elements has these locations, 0, 1, 2, I need to create a loop somehow that starts at 0 and ends at 2. Previously when I wanted to do that, I needed range, but this 2 is not going to work.

I can't just say in the range of students, because students is not a number, it's not an integer, so you can't pass it to range. Range expects an integer. But there is a solution here. It turns out that there is a function in Python called length or len, L-E-N, that will tell you the length of a list and other things down the line, too.

And now I think I can assemble these building blocks and a way that can allow me to use numbers in this way. So range doesn't take a list of strings, it takes a number, and ideally, that number is going to be 3, so I get a range of values, 0, 1, and 2. So I think I can nest my functions like this. If I first get the length of the students list, that's going to be 3,

then I pass that return value as the argument to range, that's going to give me back a range of values, 0, then 1, then 2. And what that's going to allow me to do then in code if I want is not just this. I could do print now students bracket i, and this is now where the syntax we're seeing is getting very expressive-- new and perhaps

unfamiliar. But if I can do open bracket, 0, close bracket, or open bracket, 1, close bracket, or open bracket, 2, close bracket, turns out, I can actually put a variable in there and I can express any number inside of those brackets so as to print these all out dynamically in a loop. Let me do this, Python of hogwarts.py, Enter,

there's Hermione, Harry, and Ron. And now if I'm just curious, I just want to poke around or maybe I want to do a ranking, like who are the top three students in the school or in Gryffindor? Well, I can print multiple things at a time, we've seen. Let me print out not just the students at location i, but rather, let's print i first and then the student at location i.

So two things to print, and we know that print can take two arguments, we've seen that before, they'll be separated by a space. Let me go ahead and rerun this. Now I see that, OK, Hermione is the top student, but she's in zeroth place. That's a little weird. Like we don't need to show the human using my program

that we started counting at 0. I can clean this up. I can just add 1 to the i up here, and now we see a top three list of students. Hermione is number 1, Harry's number 2, and of course, Ron is number 3. So we can get access to all of those same values as well. Are there any questions now on these lists?

Any questions now on these lists? This length, these ranges, or otherwise? AUDIENCE: My question is, for i in range, can you explain this once more? DAVID MALAN: Sure. So let me rewind in time. We started off doing this. For i in 0, 1, 2, and then we print it out meow three times in that way. The way that for loop works is that it creates

for you a variable that I've called i, but I could call it anything I want. It then assigns i initially to the first thing in the list. It then automatically assigns i to the next thing in the list. And then it assigns i to the third thing in the list. And each time it does all of the indented code underneath.

We realize, though, that this is not going to scale well if I want to do something like a million times. So we introduced range instead. That has the effect of doing the same thing. It returns to me a range of values-- a list of three things, really, so the behavior is exactly the same. If we now fast forward to this Hogwarts example now, though, what I'm doing

# 00:45:00
is just combining these smaller ideas. I'm still creating a for loop. I'm still creating a variable called i. I want to do it over a range of values, but how many values? Well, if I use the length function and pass to the length function the list of values, length's purpose in life is to tell me how long is this list, and it's 3.

So that's almost as though before, I had just done something like this, but I don't want to hardcode 3, I want to dynamically figure out how many students are at Hogwarts. So I'm just composing, composing, composing, or nesting all of these various ideas. All right, if I may, let me transition now to--

in Hogwarts still to introduce one final type of data before we combine everything with a few final programs. It turns out in Python, there's not just strings, not just ints, not just floating point values, not just bools, not just lists there are also what are called dictionaries or dics, are a data structure that allows you to associate one value with another. Literally a dictionary like in the human world. If you were to open a dictionary, be it in English or any other human language, what's inside of a dictionary? Well, it's a bunch of words and definitions. A computer scientist, though, and a programmer would describe those more generically as keys and values, something associated with something else. That's all a dictionary is. It allows you to associate something with something else. And notice, this is already more powerful, more interesting than a list. A list is just a set of multiple values. But a dictionary is two-dimensional, if you will.

Just like a human dictionary, a book, it associates something with something else like words with their definitions. Now what does this actually mean in practice? Well suppose that we wanted to keep track of who is in what house at Hogwarts. Well, I could do it using lists alone. Let me go back to VS Code here and let me

just temporarily-- but in a way that I'm not going to like ultimately-- let me create another variable called houses, set it equal to Gryffindor, corresponding to Hermione's house, Gryffindor, corresponding to Harry's house, and Gryffindor, corresponding to Ron's house. And let's add Draco in there. So we now have four instead of three students

just so we have a little variety, and he was in Slytherin. So now we have two lists. And we could just agree amongst ourselves that whoever is first in the students variable lives in the first value in houses. Whoever is second in students lives in the second house. Who's ever third in students lives in the third house.

We could do that. But honestly, that is going to break down quickly when we have a lot of students, when we have a lot of houses, and what if we want to keep track of more things than that? What if we want to keep track of every student's house and the patronus, this image that they conjure up magically?

Well, then we need a third list like-- this is just going to get messy quickly if we're just on the honor system using multiple lists where everything lines up logically. It doesn't end up well when your code gets more complicated. But I do want to implement this idea. I want to associate something with something.

A student with a house, a student with a house, a student with a house and so forth, so how can I go about doing this? Well, let me go back to my code here and let me propose that we do this using a Python dictionary. And this is the last of the new syntax, really, that we'll see . Here's the new syntax.

Instead of using square brackets, we're going to use curly braces for dictionaries as well. We've seen curly braces in the context of f strings completely unrelated. Sometimes you run out of keys on the keyboard and the authors of a language need to start reusing symbols in different ways, that's what's about to happen. We're using curly braces in a different way. Now so let me create a variable called students.

And let me go ahead and set it equal to open curly brace and closed curly brace. This is an empty dictionary at the moment. And here's how a dictionary works. It allows you to associate something with something else, and you do that like this. Hermione, quote-unquote, colon, and then the value thereof. What do you want to associate with Hermione? Well, Gryffindor. What do I want to associate Harry with? Well, I want to associate him with Gryffindor. What do I want to associate Ron with? Well, this is actually not going to-- this is going to get very ugly quickly. Once we add in Draco and Slytherin, my code is going to get too long, it's going to start wrapping. So this is purely aesthetic.

It is perfectly acceptable in Python and other languages to format your code a little more readily and just add new lines if it makes it more readable. And one way of doing this might be as follows. I still have my curly brace up here, I still have my curly brace down here, but notice, it's a little more readable now

in that I have my keys on the left, my somethings, and my values on the right, my other somethings. It's just a little easier to skim top to bottom. You could format it differently as well. But I'm going to go ahead and add in now Draco who lives, of course, in Slytherin. So now I have each of these keys on the left

# 00:50:00
and values on the right, which is really, again, just a code implementation of this idea, a little chart that you might write up with paper pencil when associating something with something else. So how do I now use this code in an interesting way? The syntax is almost the same. If I want to print out the very first student, Hermione's house,

I could do this. Print out the name of the variable, but I need to go inside of the variable. I need to index into it. And what's neat about dictionaries is that whereas lists have locations that are numeric-- 0, 1, 2; Hermione, Harry, Ron respectively, dictionaries allow you to use actual words as your indices, so to speak,

your indexes to get inside of them. So if you want to print out Hermione's house, the key you care about is, quote-unquote, Hermione, and what this syntax here will do-- notice, it's not a number 0 or 1 or 2. It's literally Hermione's name. This is like going to the chart earlier and saying, all right, give me Hermione

is my key, Gryffindor is the value. That's what we're doing here syntactically. We're looking up Hermione and getting the value thereof. So if I go back to my code, that should print out Gryffindor. And if I do this a few times, students, bracket, quote-unquote, Harry should give me Harry's house. Print students, open bracket, Ron, that should give me Ron's house.

And then lastly, if I do this with students, bracket, Draco, that should give me Draco's house. Now it's a little manual still, and I bet we can improve this, but let me run Python on hogwarts.py and we should see Gryffindor, Gryffindor, Gryffindor, Slytherin, which is exactly what we'd expect. Now all we've done, again, is we've just now moved

from having just a simple list of names to, again, two dimensions, associating like we would on paper-pencil something with something else, keys with values respectively. Allow me, if you will, even though I realize this is getting a little fancy, allow me to escalate things slightly here and transition from looking at just, for instance, that pattern there, just a hard coding those values there to actually printing these out more dynamically. Let me go ahead and use our loop, and this question came up earlier as well, let me go ahead and say for each student in students, go ahead and print out, for instance, the students variable at-- well, let's just say student first.

Let's keep it simple. So this is not going to be that interesting yet, but when I run Python of hogwarts.py and hit Enter, notice, what should I see? Let me take a question here to see what am I going to see when I hit Enter now when I'm doing for student in students? AUDIENCE: Yeah, I think we will only see keys.

DAVID MALAN: Perfect. So good intuition. It could have gone both ways. Could have been values, the houses. But when you use a for loop in Python to iterate over a dictionary, by design, it iterates over all of the keys. So we should see, I think, Hermione, Harry, Ron, and Draco. Let me hit Enter now, Enter, and indeed, you're exactly right,

we see just the keys. But that's not really that useful if what I really care about is who lives where, can I print out both? Well, I think I can. Let me go ahead and do this. Let me print out not just the student's name, the key, but let me use the key, their name, to index into the dictionary. If I know the word in the dictionary, let me look up its definition.

If I know the student's name, let me look up their house, and the syntax for this, just like a list, is students, bracket. And just like in the past we used i when i was a number, we can also with a dictionary use a string. So if the student's name is the key, then this syntax, students, open bracket, student, close bracket will go to Hermione's location

and get back her house. Will go to Harry's location and get back his house and so forth. So if I do Python of hogwarts.py, Enter, now I see Hermione, Gryffindor; Harry, Gryffindor; Ron, Gryffindor; and Draco Slytherin. Now it looks like I've given them all new last names, but I can clean that up. This is just a print thing.

Let's go ahead and change our separator from the default space to maybe a space, comma. And just using print features now, let me run the same program again, Enter, now I've just got some nice pretty commas in there to make clear that Hermione's last name is not, in fact, Gryffindor, but that's just a print detail.

Any questions, then, on these dictionaries and what I've just done? Questions on these dictionaries and this looping over then here? AUDIENCE: I just can't get my head around the for student in students. If I'm-- just correct me if I'm right. Does that mean it imports the list of students and uses the indexes-- or in other words, Hermione, Harry, and Ron as the indexes in the actual-- the list of students? DAVID MALAN: Correct. So this is just a feature of Python.

# 00:55:00
When you use a for loop with a dictionary, what happens is this. If this is the dictionary here with the keys on top and the values on bottom, you get to choose what the variable is called. I called my variable student just because it makes sense, because I want one student at a time. And what for loop does, just like it did with numbers before, the 0, the 1, and the 2, it allows me to, for instance, set student equal initially to Hermelin's name. And then the next iteration of the loop, the next cycle,

sets student equal to Harry's name, then Ron, then Draco. It just happens automatically. Like that is what the Python interpreter does for you when it sees a for loop like that. So it's very similar in spirit to iterating with a for loop over a list, but rather than iterate over the numeric location,

0, 1, 2, it iterates over the bold-faced keys in this representation here graphically. And allow me to give us one other example on Hogwarts before we look at one other familiar domain. At the risk of things escalating a little bit, let me propose that we continue the story with one final Hogwarts example like this. What if we have more information about each of our students? And this is inevitable. If you're implementing a program that's a database with people or customers, or employees or anything else, you can imagine having a lot of data about anything you're representing in your program here. For the sake of discussion, suppose that every student at Hogwarts, of course, has a name, they have already a house, but they also have a patronus.

For those unfamiliar, this is the animal or entity that comes out of the end of their wand when they make a certain magical spell. The point here being is that we want to associate not just one thing with the student, but multiple things as well-- their name, their house, and their patronus in this case.

Well, what might code like this look like? Well, let me go back to hogwarts.py and let me start fresh for just a moment. And let me propose that I enhance this with a bit more data. And this data is going to look as follows. My students variable now, I'm going to propose we think of it as a list. What if we have a list of dictionaries as follows? Indeed I want to literally implement this picture here. So notice that my previous picture just represented a single dictionary.

But suppose I wanted to compose a list of dictionaries. That is, for students-- so a list of four students. And suppose that each of those students is itself a dictionary, a collection of key value pairs, keys and values, something and something else. Well, here's one other way we can do this in code.

Let me go back to VS Code here and let me define a variable called students that is equal to a list. And I'm going to preemptively move my cursor onto separate lines, because I know this is going to be long, and I want to fit all of the elements of this list inside of it. I'm now going to create a dictionary, one dictionary per student.

And how do I create a dictionary? I just use those curly braces. But it's up to me to define what those keys are. And let me propose that one key this time won't be the student's name explicitly, it will literally be the word name, and there, going to have the name Hermione. The same student is going to have another key called house

and the value is going to be Gryffindor. And the same student is going to have a third key called patronus, and the value of that is going to be-- I had to look it up-- an otter, according to the book. Now I'm going to create a second dictionary inside of this list. And again, a dictionary is like literally

like the human dictionary of words. It's a book that contains keys and values, words and definitions. What are the three words I'm storing in each of my dictionaries? Name, house, and patronus. What are the definitions of those words for Hermione? Hermione, Gryffindor, and otter respectively. For Harry, the definitions are going to be different in this new dictionary. Let me give myself another pair of curly braces

and say this, name, quote-unquote, colon, Harry. House here is, again, going to be Gryffindor. And this one I knew, his patronus, is going to be, in this case, a stag. Next, a third dictionary. The name here will be Ron. And I'm going to go ahead and do that just like this. Next, I have the house, and he, too, was Gryffindor.

Lastly, had to look this one up, Ron's patronus was a Jack Russell terrier. Lastly is Draco. In a fourth dictionary now-- so another pair of curly braces, the name of the student is, of course, Draco. The house of this student is Slytherin. And Draco, interestingly enough, at least according to the internet,

has no patronus. Was never revealed in the books or the movies. So it turns out, this is actually a wonderful teachable moment. There is a special key word in Python that is literally None, and N-O-N-E, with the first letter capitalized. This represents officially the absence of a value. So I could a little sloppily do something like quote-unquote,

# 01:00:00
but does that mean I didn't get around to typing it or not? It's a little clear semantically to say literally None, a special keyword in Python to make clear that I know Draco has no patronus, it's not just an oversight on my part. Now that I have this, what do I have in the computer's memory? I have a list.

How do I know it's a list? Because I see a square bracket at the beginning and another square bracket at the end. That's just my visual clue, OK, I don't know necessarily what else is going on here, but there's a list of something. What is in that list? Well, here, too, the syntax is our clue. Because this line 2 starts with a curly brace and ends with a curly brace,

I just know, that is a dictionary, a collection of key value pairs. Now this all fit on my screen perfectly, so I didn't bother moving all of the key value pairs onto new lines, it would have made it really tall, so I kept it all together here this time. But how many keys does this first dictionary have?

Put another way, in Hermione's physical dictionary, how many words are in that dictionary? Three. The words are name, house, and patronus. What are the three definitions or values of those words in Hermione's dictionary? And the same story goes for Harry, then for Ron, then for Draco, I have, by design, chosen

to give them dictionaries that have all the same keys, all the same names, but they all have unique values. And that's my design, that's my prerogative as a programmer. So why is this useful at the end of the day now? I have access to a whole collection of interesting data about all of these students, and I can still do a loop.

I can say for students in students, that's going to allow me to iterate over this list of students. And let me go ahead and print out just one thing at a time. Let me print out the current student's name. So as complicated as the dictionary is, this should be pretty comfortable. For student in students is just going to iterate over every student in the list.

1, 2, 3, 4 total. The next line is just going to print out the value of the name key. It's like opening a physical dictionary, looking up the word name, and giving us Hermione, Harry, Ron, and Draco respectively from each dictionary. So if I run this version of Hogwarts and hit Enter, there, I get all three

of their names. But what if I want more information than that? I want both their names and their houses. Well, just add to print's arguments student, open bracket, house, close bracket. All right, let's go ahead and run this. Python of hogwarts.py and hit Enter. So I now see Hermione, Gryffindor; Harry, Gryffindor; and so forth.

Well, we can aesthetically clean this up a little bit by adding a separator with print, like a comma and a space, just so that when I run this again, I now see some comma separating these values. But recall that students have not just a name, not just a house, but also that patronus. So if we want to print out that, too, we now

have the syntax via which to go into that same dictionary for each student and output their patronus as well as their house in their name. So if I run this program one final time, now I see all of the data in this here dictionary. So this is a lot to absorb all at once, I'm sure. It's the last of our new data types.

On top of lists, we have these dictionaries, but again, a dictionary, at the end of the day, is just a collection of values similar to these values here that allow you to associate keys with values. And the first version of this program associated literally the student's names with their houses, but then I realized

in my next version, wait a minute, what if every student has not just a name in a house, but a patronus? Let's actually standardize the names of our keys to be name, house, and patronus, and then the values of those keys can actually be the data, like Hermione, Gryffindor, otter, and so forth. Questions now on these dictionaries and iteration thereof?

AUDIENCE: I just was wondering, suppose the dictionary is very huge, and if I want to look up for a specific student, so how do I know where to look that student from? Like can we sort it out in alphabetical order or numeric order or anything like that? DAVID MALAN: In short answer, yes. One of the features of Python is that it makes these dictionaries very highly

performant for you. That is, even if they're very large, as they will be in future weeks when we manipulate more data, Python will find the data you care about quickly for you. And in fact, that is a feature of the language, that is a feature of a dictionary to get you the data quickly. And there are functions that you can use. You can sort the data, you can sift through it, you can do very performant operations as we eventually will. Allow me, then, to propose, as we wrap up these loops, that we solve just a few final problems that will perhaps evoke fond memories of yesteryear, at least for me, wherein one of my favorite games growing up was this one here on the original Nintendo. And this is a two-dimensional world where the characters move up, down, and right, not so much to the left, in jumping over

# 01:05:00
pyramids and obstructions like these. And allow me to propose that we use this just for inspiration, not to do something that's quite as colorful or graphical as this, but just to focus on, for instance, this barrier in the middle of the world here that Mario or Luigi had to jump over. And so this here seems to be like three bricks stepped on top of one another.

And we won't do things quite graphically, but let's just implement a very simple Python-based version of this textually using maybe just hashes for bricks. Because there's a pattern here, one on top of the other, and I bet we can solve this in any number of ways. Well, let me switch back over to VS Code here

and let me propose that we create a program called mario.py using code in the terminal window. And then up here, let me start by implementing that same picture as simply as I can, printing out just literally the hash, and then the hash, and then a third final hash. This is going to be a very textual approximation of it,

but I think if I run Python mario.py, I've got a very simple version of that same column of bricks, so to speak. But you can imagine that certainly in a game where maybe these columns get higher or lower, it would be nice to write code that's actually a little more dynamic than that and doesn't just use print, print, print, which is literally

copy and paste, it would seem. So let me at least adopt some of today's lessons learned and instead do something like this. For underscore in range of 3, let's now print out just one of these at a time. But the fact that I've now used a 3 to range means if I want to change it to something bigger or smaller,

I change it in one place not in three or more places. And this code, too, of course, if I got it right, is just going to print out the exact same thing. So we're iterating here. But let's see if we can't now integrate our discussion of writing functions of our own to begin writing something a little more dynamic

and solving more complicated problems ultimately. One of the nice things about functions is that they allow us to not just write code that we can use and reuse, they allow us to create abstractions, if you will. An abstraction is a simplification of a potentially more complicated idea. And we've seen this a few times over the course of the weeks. For instance, we had a function called hello, which, granted, didn't do all that much, it just printed hello. But it allowed me to think about the function as exactly what it does,

not generically printing something, but literally saying hello. I've been able to get a number using something similar by defining my own function like get number. Well let me go ahead and, for instance, assume for the moment that I've had the forethought to, in my function main, use a function called print column.

That seems as good a name as any to use a function that prints a column of bricks. Well, how can I go about now implementing this abstraction, this simple idea of print column with actual code? Well, we've seen before with def, we can do just that. Let me define a function called print column. Let me accept as its input, generically speaking, a parameter called height.

I could call it n or h, but it would be a little more explicit now with height just so I remind myself what it's doing. And now I think I can just borrow some of that same code from before. For underscore n range of height, go ahead and print out a single hash. And then at the end of this whole program, let's just call main.

So I've kind of complicated the code. It doesn't do anything more just yet, but it's setting me up for solving what I think are going to be more sophisticated problems. If I run Python of mario.py, we're back where we began. But I now have a function, an abstraction, print column, that's going to allow me to think about printing

some chunk of the world of Mario at a time. And I can do this in different ways, too. Notice that if I really want, I could do something like this. I could implement now print column in different ways, especially if I am using print column all over my code, or maybe still, a colleague of mine, a friend, someone else on the internet

is using my print column function. What's also nice about functions you've written is you can change the underlying implementation details of them, but so long as you don't change the name of the function or its parameters or what it returns, if anything no one else knows the difference. You can change the internal implementation

as much as you want if you want to improve it or make fixes over time. So for instance, another way we could implement print column, recall, would be something like this. A bit clever with one hash and then a new line, and then maybe we could do multiplication of strings, and then end this line with quote-unquote.

Again, it's OK if you're not comfortable with this syntax. This was a more clever approach we saw in the past. But if I run Python of mario.py here, I'll still see a column of three. But what's important here is that main does not need to know that the underlying implementation of print column has changed.

# 01:10:00
Well, let's transition to a different dimension, if you will, and rather than print out just these vertical bricks, let's fast forward in the game to this part of the world here. At some part, Mario encounters these bricks in the sky, that if he jumps up underneath, they become coins. And so he gains to his score.

But let's go ahead and focus only on those coins, and let me propose that we print out, oh, just these four question marks here. And let me go back to VS Code here. And let me propose that within VS Code here, just like before, we try to abstract this away. So let me go ahead and get rid of this version,

because we're now going horizontal instead of vertical with our output. And let me just say, well, print row four times. Let me just abstract away the problem at hand. I don't know yet how I'm going to print those four question marks, but let's call it print row 4, and I'll assume I'll now solve this problem.

Let's now go down that rabbit hole of solving the problem. Define a function called print row. It's going to take a width instead of a height, because it's horizontal instead of vertical. And how can I do this? Well now, we have an opportunity to do string multiplication even more elegantly. I can say quote-unquote, question mark, times width.

And this is a very pretty Pythonic way of printing what could otherwise be a loop, and that's fine, but this is going to go ahead and print those question marks for me. Let's do Python of mario.py, Enter, and now I've got four question marks. It's not nearly as pretty as the more graphical version, but it is at least a building block toward having

now a reusable function like print row. And why am I doing all this? Like why are we over engineering the solution to these problems by having print column and print row? Well, it's a useful problem-solving technique. As soon as your world does not look one-dimensional like this or with the column version, but what about this?

Later in Super Mario Brothers does Mario have to jump down into this world where there's a lot of these underworld barriers. And this one here, for instance, looks like a square. It's two-dimensional there's a height and a width to it. And that is to say there's a bunch of different ways we could implement this thing if, maybe for discussion, it's like a 3-by-3 grid, a 3-by-3 square of sorts. Well, how can we go about solving this here problem? Well, let me propose we come back to VS Code and let me propose that we think about this in a couple of different ways. I could do this like this. If I know where I'm going, maybe I'm a seasoned programmer, let me go ahead and do this. Let me print out a square, the width, and the height of which is 3. That's an abstraction. I'm just taking for granted for a moment that there is already a function called print square that's going to be with 3 and height 3 as well. But someone's got to implement this, and at the moment,

there's only me at the keyboard, so let's go ahead and implement that square. Let me go ahead and define a function called print square that takes in a specific size, both for height and for width. And here's where we have an opportunity to use some of those loops. And we can use those loops in a way we haven't yet.

If I want to print out all of these rows, but also, all of these columns, I now have to think not just cyclically like a loop allows, but I need to think two-dimensionally. And if you're familiar with like an old school typewriter or even a printer nowadays, it generally prints from top to bottom. So even if you have multiple columns, you print out one line at a time,

and while you're on that line, the printer or the typewriter prints from left to right. And that's the mental model to have with your black and white terminal window. All of the output for every example thus far starts at the top and goes down to the bottom. From top to bottom, left to right. So we have to generate our output, our square in that same way.

So let me propose that we do this. Let me propose that we know we need to iterate this many times, 3 or more generally size. So let me do this. For i in the range of size, what do I need to do three times? Well, I want to print out what? 1, 2, 3 rows of bricks. But within each row of bricks, what do I want to print?

1, 2, 3 bricks specifically. So if we go back to our diagram here and I stipulate that it's indeed meant to be a 3-by-3 square, 3 wide and 3 tall, what did I want to do to print the first row? I want to print brick brick, brick. What do I want to print on the second row? brick, brick, brick. And the third row, brick, brick, brick.

So I'm doing three things three times. There's a lot of printing that must happen. So let me go back to my code here and let me propose now that we think of this outer loop that I've just started as representing each of our rows. For i in range of size is going to ensure, no matter what I do next, that I can print out 1, 2, 3 rows, or more generally,

# 01:15:00
size, where size could be 3, but it could be smaller or larger. What do I want to do on each of the rows? Well, just like an old school typewriter or printer, on each row, I want to print out brick, brick, brick; brick, brick, brick; brick, brick, brick. Well, that sounds like a cycle, some kind of loop.

So maybe I can have inside of one loop another loop. I don't want to use i again because I don't want to use the same variable and mess up my counting. So I'm going to by convention use j. Very common to use i and then j-- maybe k, but after that, you shouldn't keep nesting inside of each other. Let me go ahead and say for j in range of size 2,

because it's a square, and then each of these rows, let me print out a single hash, but no new line, but after each row, let me print only a new line. So there's a lot going on here, especially if you've never touched Python, let alone loops, but notice what I've done here, too, and I'll add some comments for clarity.

For each row in square, for each brick in row, print brick. And here is where comments, and more generally, pseudocode can really help explain to yourself and to others what your lines of code are doing. On line 8, I'm iterating from i equals 0 on up to size. So 0, 1, 2. On line 11, I'm doing the exact same thing, but using j from 0, 1, 2.

But that's good, because i represents how each of my rows. And while I'm on each of those rows, inside of this outer loop, I'm going to do brick, brick, brick; 1, 2, 3; 1, 2, 3; 1, 2, 3. But I don't want my cursor to keep moving to the next line while I'm on a row, so I'm just overriding that line ending.

But let me ask you a question of the group now, why on line 16 do I have a print here all by itself? Why do I have a print all by itself? Notice that it's below the inner loop, but inside of the outer loop, so to speak. What is that loop on line 16 doing ultimately? AUDIENCE: Every time you finish a line, you

have to add a new line at the end of it. So print, it prints a new line. I don't want a new line after every brick. I only want to do that at the end of the row, and that's why my comments now are perhaps enlightening. Notice that this loop here is just iterating for each brick in the row. Once I'm done with that inner loop, so to speak,

once I'm done with these highlighted lines here, to Evelyn's point, I need to print out one blank new line. And we've not done this before, but when you call print with no arguments, all you get is that automatic line ending, the backslash n where the cursor moves to the next line. So if I now go back to my terminal window and run mario.py,

I think I should get a 3-by-3 square. And it doesn't quite look like a square on my screen because these hashes are a little taller than they are wide, but it is, in fact, 3-by-3. But let me propose, as we've always done here, how we might tighten up this code further. Just for clarity's sake, let me get rid of my comments for a moment

just so we can see how many lines of code we have total. And let me propose that we maybe do this. Let me propose that, you know what, this inner loop, especially if you're having trouble wrapping your mind around one loop inside of another loop, you don't strictly need it. What if we do this trick again?

What if we print out inside of the outer and only loop each of those hashes times the number of times we want them? We draw inspiration from an earlier approach and we run Python now of mario.py, same result, but now, print square is really nice and compact. It has one explicit loop, and it's still printing out

using string multiplication all of the hashes at once on that row. If you like abstraction and you'd like to wrap your mind more around what the code is doing, well, let's do this. If you're not quite clear on what's going on, let's propose that you implement a function called print row, passing in size.

And let me propose that this print row function, it simply take in that width and print out the individual hash times that many times. In other words, here's an opportunity for abstraction, whereby, well, what does it mean to print a row? Well, when you're implementing print square, I don't really care what it means to print a row, I just need to know that someone's taking care of printing the row. You can pass the buck to another function altogether.

And how does print row work? Well, it could use a for loop, it could use this string multiplication trick. This is a way to take a larger program-- and this is probably the most complicated one we've looked at thus far-- and to decompose it into these smaller components, that once assembled, achieve your final idea. Seeing no questions, that's the end of our look at loops in Python, this ability to do things cyclically again and again, and when we combine those with conditionals, this ability to ask and answer questions and combine them with our functions and variables, we really now have most of the building blocks

# 01:20:00
we need to solve much larger, much more interesting, much more personal questions. So in the weeks to come, we'll start to see exactly what could go wrong, though, when we do so, but we'll introduce you to all the more tools via which you can troubleshoot those same problems.
