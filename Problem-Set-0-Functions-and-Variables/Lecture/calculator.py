def main():
    x = int(input("What's the x? "))
    print("x squared is" , square(x))

def square(n):
    return pow(n,3)                 # or we can use this ** instead such as n**3

main()
