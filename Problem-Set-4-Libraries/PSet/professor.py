import random
import resource
resource.setrlimit(resource.RLIMIT_AS, (2*1024*1024*1024, resource.RLIM_INFINITY))

# firstly trying via using random intergers list seperate for x and y 


def main():
    level = get_level()
    x_list, y_list =generate_integer(level)
    answered = 0
    for _ in range(10):
        chances = 3
        while chances > 0:
            try:
                answer = int(input(f"{x_list[_]} + {y_list[_]} = "))
                chances -= 1
                if answer == x_list[_] + y_list[_]:
                    answered += 1
                    break
                else:
                    print("EEE")
                    if chances==0:
                        print(f"{x_list[_]} + {y_list[_]} = {x_list[_] + y_list[_]}")
                        break
            except ValueError:
                chances -= 1
                print("EEE")

                if chances== 0:
                    print(f"{x_list[_]} + {y_list[_]} = {x_list[_] + y_list[_]}")
                    break
                pass

    print(f"score: {answered}")




def get_level():
    need_level = True
    while need_level:
        try:
            level= int(input("level: "))
            if 1<=level<=3:
                return(level)
        except ValueError:
            pass



def generate_integer(digits):
    minimum_bound = 10**(digits -1)
    maximum_bound = 10**(digits) - 1

    x_list = []
    y_list = []
    for _ in range(10):
        x_list.append(random.randint(minimum_bound, maximum_bound))
        y_list.append(random.randint(minimum_bound,maximum_bound))

    return x_list, y_list


    
    



if __name__== "__main__":
    main()
