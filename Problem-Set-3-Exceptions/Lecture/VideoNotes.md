# 00:00:00 
[MUSIC PLAYING] DAVID MALAN: All right, this is CS50's introduction to programming with Python. My name is David Malan. And this is our week on exceptions. Exceptions in Python as well as in other programming languages refer to problems in your code. Indeed, when something is exceptional in your program, it actually doesn't mean it's a good thing. It means something has gone wrong that, ideally, you will somehow solve. So what are some of the things that can go wrong?

So I'm going to go ahead and open up VS Code on my computer here. And in the terminal window, I'm going to go ahead and run code of hello.py. That's going to, of course, open up a brand new tab for me, hello.py, in which I can write my code. And let me go ahead and write some very simple code just to say hello to the world. Let's go ahead and say print "hello, world.

And then let me go ahead and-- I'm forgetting to close that quote. So a mistake that you yourself might have already made or might surely in the future make-- and it's a little subtle because you might not necessarily notice that you've just missed that one character. Well, let me go ahead and somewhat optimistically

go down to my terminal window now and run Python of hello.py and hit Enter. And that's the first of my errors. My gosh, I've only written one line of code. And I seem to have more lines of errors on the screen. But the salient point is this bottom-most thing here. Notice where it says syntax error. A syntax error is a problem with the code that you have typed, your syntax.

Just like English and other human languages have syntax associated with them, so does my code. And it's not quite correct. Something is awry. I didn't follow the instructions properly. And it does elaborate for me, unterminated string literal. Now, that's a bit arcane. That is a bit of a confusing error message.

But unterminated would generally mean that I started something but didn't stop it. I didn't terminate it. String, of course, is a sequence of text, like we've discussed before-- or stir in Python. And literal generally refers to something that you literally typed. It's not a variable. It's something like quote unquote--

or just "hello world. So the fix here, of course, is going to be to go ahead and terminate that string and actually close the quote. And if I now go back down into my terminal window and rerun Python of hello.py, now I'm saying hello to the world. So the catch with syntax errors here is that syntax errors are entirely

on you to solve. A syntax error is a problem that you've got to go back into your code and fix from the get-go. You can't just kind of hope that it's going to resolve itself or expect that other parts of your code will catch it for you. Syntax errors just must be fixed. But there's a lot of other types of errors in Python

that might be described as runtime errors, that happen while your code is running. And it's really up to you to write some additional code defensively to detect when those errors happen because you don't necessarily know, for instance, what input humans are going to type into your program. And so you better be ready, defensively, to accommodate things

that they type or even misstype. So, for instance, let's go back over here to VS Code. And let me propose that we take a look at a new file all together. I'm going to close hello.py. And I'm going to write code of say number.py. So let's play around with some numbers in Python. And the first thing I'm going to go ahead here and do with number.py,

after opening this new tab, is I think I'm going to go ahead and print-- type up a relatively simple program that maybe prompts the user for an integer, like x, and then just prints out what x is. So we're going to start simple, but, again, in starting simple, we'll be able to really see where I've done something wrong.

Well, here we go. I'm going to go ahead and say a variable called x is going to get assigned the value of the return value of input, quote unquote, "what's x?" And I'm going to include a space to move the cursor over a little bit. And then, ultimately, I'm going to go ahead and-- oh, wait a minute. If I'm wanting to get an int from the user, recall that I need to do something proactively. I need to actually convert that input to an integer using the int function in Python. So now I'm passing the return value of input as the argument to int.

And that will store in x, ultimately, an integer, not a string that looks like an integer. All right, let me go ahead now and just quite simply print out what this is. I'm going to go ahead and print out, quote unquote, "x is x." But I don't want to literally say x is x. I want to plug in the value of x.

So maybe the easiest way to do that is to surround it with curly braces. And then if I'm using these curly braces and I want Python to interpolate the value of that variable, that is substitute what x actually is in between those curly braces, recall that I need to use a format string or an F-string by fixing this whole thing with an F. Now that I've done that, let's go ahead

and see what happens. I'm going to go ahead in my terminal window and run Python of number.py. I hit Enter. And so far, so good. All is well and being prompted for x. Let me go ahead and type in a number like 50. All right, that seems to work. Program seems to be correct. Or is it? What could go wrong in this program, even though nothing did just go wrong?

# 00:05:00
But if I run it and run it and run it again, during the running of my program, what could still go wrong, especially if I'm not the human interacting with it but some other human instead? Any volunteers here for this one? What could go wrong? And in what way is this program not really correct, even though at first glance it seems so.

AUDIENCE: [INAUDIBLE] DAVID MALAN: So I'm not calling an integer. I'm still having trouble hearing you. But what I think I heard is that if what the user types in is not, in fact, an integer, I can't just blindly convert it to an int. If I'm not putting too many words into your mouth, I think what I should perhaps do here is be a little defensive.

And let me see if I can't simulate exactly the problem that could go wrong here. Let me go ahead and run, again, Python of number.py. Let me try another number. In fact, when testing your code, generally it's a good idea to test corner cases, maybe numbers that aren't quite as plain as or 49 or 51. Let's choose some numbers that might be a little more interesting, if only

mathematically, like zero. All right, zero seems to work. My code still prints out that x is zero. What might be another corner case to consider? Well, let me go ahead and try a negative number. That, too, is pretty different in spirit from negative. Negative 1? OK, that works too. Well, let me try it one more time.

I've tried positive numbers, negative numbers, 0. Let me try something like a cat. So literally, C-A-T-- typing in a string that doesn't even look like a number. And yet, let's see now what happens when I hit Enter. All right, we'll see now we've got another kind of error. It's not a syntax error, because I didn't make a typographical mistake.

I didn't forget some piece of syntax. I actually now have an error with one of my values. And it's an a value I didn't even anticipate. The human, me, in this case typed it in long after I wrote the code. So what does this refer to? A value error. Well, let's see what the explanation is. Invalid literal for int with base 10, quote unquote, "cat."

Now, this, too, is a bit of a mouthful. And, unfortunately, in Python and a lot of programming languages, the error messages are written for pretty comfortable programmers. And, of course, when you're learning programming for the first time, you might not be so comfortable with the programming language

let alone the error messages. But let's see if we can't glean some insight. So invalid literal. Well, again, a literal is just something that's been typed in, it would seem, for int. What is int exactly? Well, int is the function I'm using to convert the user's input to a corresponding integer. Base 10, that refers to the decimal system, which is this

the default that Python is using. And it looks like at the end of the day, what Python really doesn't like is that I passed cat, quote unquote, "to the int function." So how do I go about actually fixing this problem? Well, I could just add instructions in my program. Maybe I could add a line of print telling

the user more explicitly, be sure to type an integer, or, please don't type cat. Please don't type strings. Of course, the user might still not oblige. They might not be reading the instruction. So that too is probably not an effective strategy. What we really want to do is write our code with error handling in mind.

We want to write lines of code that not only accomplish the problems we care about but that also handle errors that might unexpectedly happen. And, in general, when programming, programming defensively. Assume that the users aren't going to be paying attention or, worse, they're malicious. They're trying to crash your program.

So we want to handle as many errors as we can. Now, how do we go about doing that in Python? Well, it turns out whether you want to catch a value error or other types of errors as well-- though not syntax error-- Python actually has this keyword called try. And it's sort of aptly named. If you want to try to do something in Python, you can literally use this keyword. And you can check whether or not something exceptional, something erroneous, has happened. So using both try and this other keyword, except,

can I go and try to do something except if something goes wrong? I can do something else instead. So let's consider, how can I go about trying to convert the user's input to an int except if something goes wrong? Well, let me go back to my code here. And let me propose that I now modify this example as follows.

Let me go ahead and, above my first line of code, I literally write, try and a colon, telling Python, try to do the following. I'm going to go ahead and indent my existing lines of codes here by the same number of spaces, four in this case. And then I'm going to add one more new line down here that literally says,

except Value Error. And notice it's important that I've capitalized the V and I've capitalized the E. These symbols are case sensitive. And this is now an opportunity, after this colon, to tell Python what I want to do in exceptional cases, when the number or the input from the user is not, in fact, a number.

# 00:10:00
And I'm going to say something plain like print, quote unquote, "x is not an integer." I'm at least going to tell the user roughly what the problem actually is. So notice another detail. The indentation is important. Because I have try on line one and I've indented lines two and three, those are the two lines of code that I'm trying, except if I see a value error,

line five, because it's indented is what is going to get executed in cases of those errors. Let me go ahead now back to my terminal window and run Python of number.py, Enter. And let's go ahead and type in again. Still seems to work. And, of course, I'm trying and succeeding. Let me go ahead and try once more, this time, though, with the word cat

or, really, anything that's not a decimal number. And now you'll see much more cleanly x is not an integer. I'm not seeing some scary error message that I, the user, am going to have no idea how to handle. Now you, the programmer, have anticipated that something exceptional can happen. And you've gone about actually handling the error for the user,

giving them an appropriate error message instead. Let me pause here and see, are there any questions now on what we've just done by introducing try and accept to handle this value error? AUDIENCE: Is value ever the only type of error you can get? Or are there other types? DAVID MALAN: Is value error the only thing you can catch?

There are other errors as well. And we'll see a few of them today. And there's many, many more, honestly, that if you continue programming and programming in Python, you're going to see a lot of them over the weeks the months the years to come. But the technique for handling them is going to be largely the same other questions on try, accept,

or these exceptions more generally? AUDIENCE: Yes, sir. Actually, to use the except block, you need to know the type of error, right? [INAUDIBLE] what if you can't anticipate this particular type of error? DAVID MALAN: A really good question. So I'm being very good about catching, so to speak, the very error that I might happen.

I don't know when it might happen because it's going to depend on the user. But I know what kind of error will happen from the int function. There is a way in Python where you can say, except if anything goes wrong. And you can literally omit value error and just catch everything. The problem with that is that it sometimes hides other bugs in your code

because you don't necessarily know what's going wrong. And if you don't necessarily know what's going wrong, how can you possibly handle it correctly? So bad practice. And it put another way, it's lazy to do that, to just say, catch everything and I'll deal with it here. So a much better practice would be to figure out what kind of errors

could happen and include mention of them explicitly, as I have done. Now, with that said, if you read Python's official documentation, as you'll eventually invariably do, it is not great about telling you proactively what kinds of errors can be raised in this way. So it's a bit of contradictory advice.

You should do it this way. But it's not always obvious what you should be checking for. But you get better at it with practice. And some of the times, the documentation does spell out what could go wrong. Let me turn our attention now back to this and point out that even though this is better code, it is more correct in the sense that I'm not just leaving it to the user

to see some really ugly default Python error message that most people are going to have no idea what to do with, I'm at least handling it more elegantly. And I'm printing out x is not an integer. So it's at least more instructive. But this isn't necessarily the best way to implement this code. Why? Well, here, too, I'm actually still being a little lazy.

So notice that I'm trying to do not one line of code but two lines of code. And this isn't a huge deal because we're only talking about two lines of code. But in the interest of preaching best practices, you should really only be trying to do the one or very few lines of code that can actually raise an exception that can actually fail in some way.

I am pretty sure that calling print here is not going to raise a value error. Whether x is an int or a string or a float or anything else, the format string feature of Python is going to handle printing it just fine. So, really, what I'm going to do is this. I'm going to move this line three down to the bottom of my code. I no longer need to indent it. I'm just going to execute it at the bottom of my file here. Unfortunately, by doing this-- I've done a good thing by now only trying to do the minimal amount of work

necessary that might raise the exception of value error. But I fear I've introduced a new mistake. Well, let's see. What is now incorrect? Let me go ahead and again run Python of number.py, Enter. Let me go ahead and do it correctly with 50. And all seems to be well. But, again, let's try those corner cases--

the zeros, the negative numbers, or, in this case, the cat. Let me go ahead and type in C-A-T again. Now I have a name error. So now it's yet another type of error in my code that I've introduced here. And what does this name error mean? Well, just as a value error refers to that-- the value of some variable,

# 00:15:00
the value that someone has typed in is incorrect-- name error tends to refer to your code, like you're doing something with the name of a variable that you shouldn't. And why might that be? Well, let me turn our attention back to the code here and consider, what is it complaining about? Well, the name errors what I see down here. And it's telling me, name, quote unquote, "x is not defined." And notice if I look further here, it is mentioning line six. So I know the problem is with my code on line six.

And that worked a moment ago. And I'm defining x on line two. But let me ask the group here, why does x, in fact, exist online six? Why is it not defined, even though I'm pretty sure I was intending to define it on line two? AUDIENCE: Maybe the scope of the variable is between the [INAUDIBLE].. DAVID MALAN: So, good terminology.

Scope refers to the portion of code in which a variable exists. That, too, though isn't quite right in Python. That would be true in C, C++, and Java, where indentation or curly braces tend to define the scope of a variable. But, again, here in general-- and this worked a moment ago. X exists once it's defined on line two because, remember, I printed out x is 50 a little bit ago. Let's try one more hypothesis here.

One more hand? Why is x somehow still not defined? AUDIENCE: Yeah, so is it because it's local variable, meaning that it doesn't define outside of the scope because what people have mentioned. It prompts the input in try, right? The outside of it is undefined. DAVID MALAN: So still good instincts. And good terminology, too.

There's this notion of local variables, which tend to exist inside of functions, for instance, global variables, which tend to exist in entire files. In this case, too, though, that's not quite the case. What's happening here boils down to order of operations. Let me come back to the code here and recall that any time we've discussed the assignment operator, the single equal sign, that copies a value from the right to the left. But consider for a moment at what point something is going wrong.

Well, the input function is probably working just fine because we've used that a lot now to get users' input. It always returns a string or a stir in Python. But what could be going wrong? Well, if I'm passing that string to the int function as its argument, it's probably the int's function that's erroring.

And, indeed, if you think back earlier when we had the value error, it was, in fact, the int function that did not like, quote unquote, "cat" as input. So this is all to say that this portion of my code highlighted now to the right of the equal sign, that's the code that's creating a problem. That's the code that was creating a value error.

And in this case, we're catching the value error. But because the value error is happening on the right of the equal sign, there's no value being copied to the left. The error is interrupting that whole process. So even though we see x equals dot dot dot on line two, the portion of that line to the left of the equal sign

isn't getting evaluated, ultimately, because the value error is happening too soon. And so when we finally get down to line six, even though it looked like I was defining on line two-- and I would have defined x on line two if all had gone well-- we didn't get to the part where the value is copied from right to left

because the value error happened first. So this code is just incorrect now. So how do I go about solving something like this? Well, it turns out that there's another feature of the try and accept syntax that Python supports, which is that it also supports the keyword else. Now, we've seen else before.

If you think back to our discussion of conditionals, we saw if. We saw elif. We saw else, which was kind of this catchall, what you should do in the event that nothing else is relevant. That's kind of the same intuition here for the try-except feature of Python. What you can do is this. You can try to do the following, as I've done, except if this goes wrong. But if nothing goes wrong, else go ahead and do this.

So this is one way I can solve this same problem now. No matter what now, Python is going to try to execute line two. If something goes wrong, it's going to execute lines three and four to handle that value error. However, if you try and this code succeeds, then there is no exception to handle. So you're then going to execute this line here.

So it's a little confusing, perhaps, in that we're now using else both for conditionals-- if, elif, elif, elif, else. And we're also using else with these try-except blocks. But that's OK. That's part of the language. That's one of the features. So now if I rerun this code in my terminal window, Python of number.py--

let's do something correct, like 50-- I see that x is 50. So line one is executed. We're trying to do the following. Line two is executed because the conversion happened successfully and the number 50 gets copied from right to left. The exception does not happen. So we ignore lines three and four. We jump immediately to line five and six, which prints out the result.

# 00:20:00
By contrast, though-- let's do this one last time. Python of number.py-- let's type in cat or, again, any other word and hit Enter now. We don't see what x is. Rather, we see, quote unquote, "x is not an integer," which is what's being handled in my except clause. All right, let me pause here because that's a lot of new syntax,

and see here if there's any questions on try, on except, on else, name error, or value error. AUDIENCE: Can you please repeat the try function? DAVID MALAN: Repeat the name error? What's the problem with the name error? AUDIENCE: Yes. Yes. DAVID MALAN: Yes. So let's just rewind a couple of lines here

before I fix this problem by now getting rid of the else. A moment ago, we had code that looked like this, whereby I was getting a name error, Python of number.py, Enter, typing in cat, that looked like this, where name x is not defined. And the problem was on line six, according to this output in Python.

Well, let's think about this now deductively. Let's try a different approach. On line six, I'm seeing an error that name x is not defined. OK, Python's already telling me x does not exist at that point. So how could that possibly be? Well, where should x be defined? Well, presumably, x is defined on line two, up here.

So what could go wrong? Well, if the user has inputted something that doesn't look like a number, like the word cat, passing cat, the return value of input, as the argument to int to convert the word to an int makes no sense. You can't convert a cat, C-A-T, to an integer at all. So the int function is raising a value error at that point.

And the error is being handled with this code here. But notice this line six is not indented. It's left aligned with the rest of my code, which means no matter what, line six is going to execute. It's going to execute whether I typed in 50 or I typed in cat. But if I typed in cat, again, x never gets a value.

So it's not defined here on line six. So when I introduced, finally, the else statement, that makes sure that these things are mutually exclusive. I only execute the else if I tried and succeeded up above. Well, let me propose that we refine this just a little bit further as well and consider how we might improve this example a little bit more.

It's a little unfriendly of me to be rejecting the user's input after they fail to provide an integer and just quitting the program, really, right? It'd be more user friendly if I just prompt or reprompt the user again and again. And in the chat, if you could, what's the feature of Python that you can use if you want to do something again and again and again until such time as the user cooperates and gives you what you're looking for, like a number? So yeah, loop, loop, loop.

So a loop is something that happens again and again and again. And maybe we can use that same mechanism, a loop, in order to prompt the user for x. And if they don't give us a number, prompt them again. And if they don't, prompt them again and again and again. We don't need to just quit out of the program. So, quickly-- so let me propose this.

Let me propose here that I improve this code by deliberately doing this. Let me induce a infinite loop at the very top of my code with while true. Recall that the wild keyword induces a loop, a cycle that behaves like this. And it asks a question, a Boolean expression that needs to evaluate either to true or false. Well, if I want this thing to loop forever, at least initially, we'll just say while true because true is true. So this has the effect of doing something

no matter what forever unless we break out of it early. Now I'm going to go ahead and do this. I'm going to go ahead and move my try except code indented underneath this loop so that I'm trying to get an x. If I have a value error instead, I print out x is not an integer. But this time, what do I want to do if the user does

try and succeed in giving me a number? Well, I can do this. I can just break out of my code here. And down here now, I can use that same line of code from before, an F-string that says x is, and then in curly braces, x again. So what's going on here? I think this code now, because I've added the loop, is going to have the effect of trying at least once, maybe

a second time, maybe a third time maybe 500 times until the user finally gives me what I want, which is an integer. And once they do, once there's no value error happening, then I break out of the loop. And line nine executes as I would hope. So let me go ahead and try executing this version-- Python of number.py, Enter.

What's x? Let me go ahead and type in the easy thing first-- 50. X is 50. What just happened in terms of the control flow of this program, the flow of my logic? Well, I first found myself on line one inside of a loop. Hopefully, I'll get out of this loop. What did I then do? On lines two and three, I tried to get input from the user

# 00:25:00
and convert it to an int. Well, I was a nice guy this time. And I typed in 50, which looks like and is a number. So the int function converted it just fine and stored it from right to left in x. Except value error? There is no value error because if I typed in a number, there's nothing exceptional happening.

This is a boring, good execution of my program. So what happens? I break out of the loop. So, again, the else clause is associated with the try not with the except. And once I'm out of the loop, of course, I'm just printing out what x is. Well, let's try the other scenario that might happen. Let's try cat or any other word.

Ah, this is now a new feature. I'm being informed what I did wrong. X is not an integer. So I'm getting some useful user feedback. But notice, again, I'm prompted, what's x? Well, let me try typing in dog. Let me try bird. And suffice it to say, this will happen now forever if I'm in an infinite loop

until I try and succeed, at which point I break out. So let's try again. 50, Enter. Now I'm out of the loop. And I'm printing out what x actually is. All right, let me pause here and see if there are any questions. The logic is almost the same. But what is different now is I'm in a loop. And I'm using the keyword break in Python

to deliberately break out of the loop when I'm ready to, once the user has cooperated. AUDIENCE: Do we really need to break? Can't we just print? Or what keeps us from just printing? DAVID MALAN: Good question. So let me try that. Couldn't I just print? Well, let's see what happens if I do that. Let me move this print line at the end into my loop

here, thereby shortening the program. And, in general, that's been a good thing. Let me go ahead and type in 50. OK, x is 50. OK, maybe it's 49. X is 49. OK, maybe 48. Unfortunately, I think-- you're laughing. You see it. I never break out of the loop, which maybe that's a feature. Maybe you want this to be your program. But I didn't.

I'd eventually like this game to stop. So I need to break out in that way. But I can do it a little differently. And let me propose that we modify this a little bit. But, first, any other questions on this syntax here? Let me rewind to the prior version. AUDIENCE: Hi, can I use a break [INAUDIBLE] except and else?

For example, in another print, may you use printing the else, you can use prints together with break or something like this? DAVID MALAN: So you can use break inside of loops to break out of loops. And you can use it inside of a conditional, like an if, an elif, or an else. You can do it inside of a try, except, else statement to.

Any time you're in a loop that you want to break out of, you can use this keyword, break. I'm using it in the context of exceptions. But it's not restricted to that. And let me show you, too. It doesn't even have to be in the else. If I wanted to, I could actually do this. I could get rid of my else.

And I could go back to line three, add another line that's indented, line four, and break out here. Now, why is this logically OK? Well, consider what I'm now trying to do. I'm trying to execute line three and converting the user's input to an int. And I'm trying to store the result from right to left in x.

If something goes wrong, the code we've already seen is immediately going to jump to line five and then six to handle the exception. But if nothing goes wrong, my code presumably should just keep on executing line by line. So I could technically logically put the break here. And watch what happens when I run this version.

Python of number.py, 50, Enter, it worked. I broke out of the loop. Now, which way is better? Honestly, I think it could go either way at this point. This program is so relatively short that even though I'm trying to do two things now, one of which, the break, is not going to fail. You either break or you don't.

There's no piece of data from the user that's going to influence that. We don't strictly need to have those two lines of code there. But it's only two lines. So I think it's OK. And if you recall our discussion in the past, not just of correctness-- does the code work as it should?-- but design, I think you could argue it either way.

If you prefer the readability of this and the fact that you don't have an else, that's fine. If, though, you prefer to minimize just how many lines of code you're trying to execute in case something goes wrong, the else is a reasonable approach too. Well, allow me to propose, too, now that we refine this further.

I think we're at the point where it's pretty darn correct. But suppose now that I find myself today and tomorrow trying to get numbers from the user quite a bit. It would be nice, as we've seen, to maybe just invent my own function, get int to get an integer from the user both today and tomorrow and beyond.

# 00:30:00
And, heck, maybe I can even share that function with other people. If they want to write programs, they get integers from users. So how might I go about doing this? Well, let me go ahead and propose that we do this. Let me get rid of the print line but keep most of my loop here. Let me define a function called get int that takes no arguments for now.

And I'm going to go ahead and indent all of the code I already wrote underneath get int. So now I have a function called get int that tries to do the following. Try to get in it from the user. If something goes wrong and there's a value error, yell at them with x is not an integer. Else, break. But it's not just breaking that I want to do here.

Now that I'm in a function, recall our discussion of return values. If you're inventing your own function whose purpose in life isn't just a print something on the screen like a side effect but is to hand back a value, to hand you back a value, like on that same post-it note from our discussion of functions,

well, you need to return x explicitly. How do I now use this function? Well, as soon as we start making our own functions, it tends to be convenient to define our own main function as well. That's the main part of our program. And I'm going to keep this simple. I'm now going to say, x equals get int.

And then on the next line, I'm going to do that print from before, quote unquote, "x is"-- in curly braces-- "x." And at the very bottom of my program recall, I'm going to call main, so that no matter what, I'm invoking my main function after everything's been defined. Well, let's see how this works.

Let me go ahead and run Python of number.py. Let's type in 50. And it seems to work as before. Let's go ahead and run it again, typing in cat, C-A-T, this time. And I'm being prompted. Dog, and I'm being prompted. Bird, and I'm being prompted. Fine, fine, fine. That's an int. And so it is printed. So what's worth noting here-- well, I'm manifesting a couple of good properties

here. One, I've kind of abstracted away this notion of getting an integer. And even though I just artificially hit Enter a whole bunch of times just to hide that function for now-- it needs to be there, but we don't need to see it at this point-- notice that now this entire program really boils down to just these three lines of code now.

Because I've abstracted away that whole process of getting an int from the user into this new function of my own called get int. But can I improve upon this? Well, let me go and undo all of those blank lines and pull this up just so we can see more on the screen at once. Can I tighten up my implementation of get int?

It is correct. I claim this is correct. It's handling errors. And it's returning x. But I don't, strictly speaking, need to write the code as long. What else could I do? Well, let me propose that if all you're doing on this line 13 is breaking and then immediately after that, per the indentation, you're executing return x on line 14, why are you wasting everyone's time?

Once you know you're ready to return the value, you could just return x. And so in my else, I could break out and return a value. So here, too, return is used to return values from functions. Break is used to break out of loops. But it turns out that return is sort of stronger than break. It will not only break you out of a loop.

It will also return a value for you. So it's doing two things for once, if you will. But can I make this even more compact? If my goal is to just tighten the code up, even though it's already correct, can anyone think of a further refinement, whether you've programmed in Python before or not? Can I shorten this implementation further just a little bit,

if only to decrease the probability that I've made a mistake by having fewer lines and just make it a little easier to read because it's shorter? Any suggestions for tightening up my implementation of get int? AUDIENCE: You can just return the value on the try function, when you're trying. You take the input x and then return x. DAVID MALAN: Good. We can just return x a little higher up. And let me correct folks as we go. It's not a try function. It would be a try statement, technically. A function typically has a parentheses and another one.

In this case, it's just a statement. But we can do exactly that. I don't technically need the else. If I really want, I could do this. Right after line nine, I could return x here. Or recall our discussion of defining variables unnecessarily sometimes. Why define a variable here if you're immediately going

to use it here and then never again? So we could avoid a new line here. And I could avoid even defining x explicitly. I could just say something like this. I could return int, input, quote unquote, "what's x?" I can do it all at once. Now, which is better? I don't know. I mean, again, this is where reasonable people might disagree.

I'd argue that, on the one hand, we're tightening up the code. We're using fewer lines. It's easier to read, lower probability that I've made a mistake. On the other hand, it's a little more complicated to understand, perhaps. It's a little less obvious where I'm returning from. So I think arguments can be made either way.

# 00:35:00
At the end of the day, what's important is that you've done this consciously. You've made a decision to do it this way or this way. And you can justify it in your mind-- not that your answer is, eh, it worked, so I left it alone. Have a good reason. Come up with a good reason. And that will come with experience and practice.

Well, let me propose to you that we make one other refinement here. Suppose that you're finding your programs to be a little noisy. And it's a little obnoxious that you keep telling the user, x is not an integer. What if you want to make things a little gentler and just prompt the user again with the same words, what's x? What is x? Again and again. Well, you can do that as well. And it turns out that if you want to handle an exception in Python but you want to pass on doing anything with it-- so you want to catch it,

but you essentially want to ignore it. You don't want to print anything. You don't want to quit the program. You just want to silently ignore it, like if you're talking in a room full of people and it's your turn to talk and you're just like, pass. They're still calling on you. But you're not doing or saying anything more.

Well, we can add this keyword to our code here. Let me go back to my program here. And instead of printing out again and again, x is not an integer, I could just do this. I could pass on handling the error further. I'm still catching it. So the user is not going to see a scary message even mentioning value error.

My code is catching it. But I'm passing on saying anything about it. I'm going to stay in the loop. I'm going to stay in the loop and keep prompting and reprompting the user so now the effect looks a little something like this. Python of number.py. Let's type in cat. What's x again? Let's type in dog.

Type in bird. So it's just a little, maybe, more user friendly and that you're just reminding the user what you want. Maybe it's worse. Maybe it would be helpful to tell the user why you're prompting them again and again. It's not obvious. So it could go both ways. But, again, it's just another mechanism, now, for handling these errors.

We use the except keyword to catch a specific error. But we don't have to handle it more than that. We can just pass on doing something further. Let me pause here and see if there's any questions now on try, accept, else, or pass? AUDIENCE: OK, yeah. No. I was just kind of curious, I guess, about the idea

of when you were inventing with the get int function, for example. Because I'm noticing, obviously, going through it with the whole logic and breakdown of the entire function, while true, do this. But I'm just kind of curious in elaborating with the indentations for the code more. DAVID MALAN: Yeah. So the invitation is deliberate logically.

Some languages don't require as rigorous indentation. You can use curly braces or other symbology to make clear what is associated with what. In general, any time you indent something in Python on this line-- rather, anytime you write a code a line of code in Python that's here and the lines below it are somehow indented, that means that those lines are somehow associated with that first line.

And, presumably, those indented lines should only be executed if the first line told the computer to do so. So, concretely, what does this mean? On line six here, we're defining a function called get in that takes no arguments, colon. Everything that's indented by at least four spaces hereafter is part of that function.

That's just the design of the Python language. Frankly, I think the designers got tired of seeing really ugly code in languages like C and C++ and Java that don't necessarily enforce indentation to this extent. So now it's baked into the language. And my chronology might be a little off there. But there's been many languages that are looser than Python when

it comes to indentation. The indentation is meaningful on line seven too. Notice that because the while true is indented by four spaces. That just means it's part of the get int function. But notice below the while true statement, there is eight, there's 12, there's eight, there's 12 spaces here. And I'm just quickly counting the dots.

That means that all of the lines I've just highlighted are inside of that while loop. While true means to execute lines eight through 11, potentially, again and again and again. And now, lastly, on line eight, because we have try and indented below it is line nine, that just means that what you should try is what's on line nine. And similarly, on line 10, below it, we have indented line 11. You should only pass when there is an exception of a value error. So the indentation just means what is associated with what.

And once you get comfortable with that, you'll see that the indentation alone helps explain the logic of your program. And it has a wonderful side effect that for yourself the next morning, for your colleagues, your family, your friends, your teachers, your code is much more readable as a result. It's not one big mess of a blob of text.

Other questions now on try, except, else, or pass? AUDIENCE: Yeah, thanks. Two question. Question one-- once you say pass, can the caller still learn anything about this era through a system variable or whatever? And question two-- problem set zero referenced some string methods, including is numeric--

# 00:40:00
is it any different to [INAUDIBLE]? So on the first question, if I'm handling the error in this way, the caller is not going to know anything about it. That's the point of my handling it, so that main or other callers don't know that anything technically went wrong. On the second question, is numeric is another function

that you can call that can look at a string and determine is this, in fact, a number. I could use a mechanism like that. I could use a conditional. If this looks like a number, then pass it to the int function. And go ahead and convert it to an integer. That's totally fine. I would generally say that the Pythonic way of doing things is often, for better or for worse, to try things, hope they work. But if they don't, handle the exception.

So other languages are more in favor of checking if, if, if, if, elif, else, and all of these conditionals. Python tends to be a little more of the mindset, eh, try it. But just make sure you're handling the error. So this would be the Pythonic way of doing it. Your way, though-- checking with the conditional, is it a number first?--

is totally reasonable too, if you want to go that way. Well, let me propose some final refinements to this program that really just kind of tighten things up, one additional step to improve the implementation of this get int function. Let me propose that we not hard code, so to speak-- that is type manually x

all over the place. Let's make this function, get int, a little more reusable. Right now, notice that I'm just kind of using the honor system that, well, main is defining a variable called x. And get int is asking for a variable called x. But it would be nice if the caller, main, doesn't have to know what the call-ee is naming its variables and vise versa.

So caller-- to call a function means to use it. The caller is the function that's using it. The call-ee is just the function being called. It would be nice if I'm not just hoping that x is the same in both places. So let me propose this. Let me propose that we actually add a parameter to get int, like this.

That is to say, if main wants to use the get int function, well, then main should probably tell the get int function what prompt to show the user. Just like the input function, recall, that comes with Python, it's up to you to pass in a prompt that the user then sees when the human is asked for input. So how do I make this work here?

I can go down to my definition of get int. And I can say, all right, get int is going to take a parameter now, called prompt. I could call it anything I want. But prompt in English is pretty self-explanatory. It means the message the user will see. And now, down here, when I actually use input, I don't have to presumptuously say, what's x?

Because what if the program, the caller, wants to ask for y or z or some other variable? I can just pass to input whatever prompt the caller has provided. So now I'm making more reusable code. It still works just the same. I haven't changed the functionality, per se. But now it's a little more dynamic because now

get int doesn't have to know or care what variable's being asked for, what's being asked for. It just needs to know what prompt it should show to the user. So if I now run this program down here, again, prompt number.py, Enter, what's x? 50 still seems to work. Let's run it again. It still seems to work.

And if I type in cat, dog, bird, or anything else, it will keep prompting me with that same prompt, making this code, therefore, all the more usable. Now it turns out, too, you can even raise exceptions yourself using Python's raise keyword. But more on that another time. So in the coming days, the coming weeks, the coming months,

as you write more code in Python, you'll see that errors are inevitable. Sometimes they're syntax errors, which you've got to just fix if you even want to run your program at all. But they could be name errors-- for instance, variables that you meant to define but somehow didn't-- value errors, where maybe the user didn't cooperate and provided you with something that

you weren't expecting, or a whole list of other possible errors or exceptions. But now, hopefully, you know how you can handle these errors and respond to them in any way you like. This, then, was our look at exceptions. And we'll see you next time.
