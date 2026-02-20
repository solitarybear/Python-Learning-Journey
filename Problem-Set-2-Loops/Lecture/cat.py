def main():
    number = get_number()
    meow(number)

def meow(i):
    for _ in range (i):
        print ("meow")

def get_number():
    while True:
        n = int(input("What's n? "))
        if n >0:
            break
    return n

main()