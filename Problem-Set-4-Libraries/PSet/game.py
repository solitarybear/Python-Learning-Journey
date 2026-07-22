import random
import resource

resource.setrlimit(resource.RLIMIT_AS, (2*1024*1024*1024, resource.RLIM_INFINITY))
is_level_valid = True

while is_level_valid:
    level = 1
    try:
        level = int(input("level: "))
        if level >= 1:
            is_level_valid = False
        else:
            pass
    except ValueError:
        print("level should be int")        

target_number = random.randint(1, level)

game_active = True

while game_active:
    need_valid_guess = True
    while need_valid_guess:
        try:
            guess = int(input("guess: "))
            need_valid_guess = False
        except ValueError:
            print("guess should be int")

    if guess > target_number:
        print("Too Large!")
    elif guess <target_number:
        print("Too small!")
    else:
        print("Just right!")
        game_active = False


