'''problem set is you want input from the use btw 2 to 9 and other then these input the only input that is valid is "quit" other wise show error to the user 
use the raise keyword to show error 
'''

name = input("enter x between 2 and 9!! ")
if name=="quit":
    print("you are succesfully out of the program")
else :
    try:
        x = int(name)
        if (x>9 or x<2) : 
            raise ValueError("value should be between 2 and 9")
    except ValueError:
            raise ValueError ("Value should be integer") 



