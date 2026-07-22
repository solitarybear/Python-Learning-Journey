import pyfiglet
import sys
import random

text = '''i'm solitary bear
sleeping in my cave
do not distub me
'''

valid_font =pyfiglet.FigletFont.getFonts()

if len(sys.argv) >3:
    sys.exit("too many argument")

if len(sys.argv) == 1:
    random_font = random.choice(valid_font)   
    ascii_art = pyfiglet.figlet_format(text,random_font , width = 200)
    print(ascii_art)
    sys.exit()
if len(sys.argv) < 4:
    if sys.argv[1] != ("-f" or "--font"):
        sys.exit("flag not set correctly")
    
    if len(sys.argv) ==2:
        sys.exit("mention the name of font")

    try:
        chosen_font = str(sys.argv[2])
    except TypeError:
        print("argument should be str")
        
    
    if chosen_font not in valid_font:
        print(f"Error: {chosen_font} is not a valid pyfiglet font")
        sys.exit()

    print(pyfiglet.figlet_format(text, chosen_font , width = 200))

        



# if len(sys.argv) > 2:
#     if len(sys.argv) == 2:

