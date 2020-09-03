import random
from gmcolors import colors

available_positions = list(range(1, 10))
tic_tac_toe = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
winning_sets = [
    [1, 2, 3],
    [1, 4, 7],
    [1, 5, 9],
    [2, 5, 8],
    [3, 5, 7],
    [3, 6, 9],
    [4, 5, 6],
    [7, 8, 9]
]

selected_level = 1 # قيمة الافتراضية هي 1
human_steps = [] # هنا غا نخزنو الاختيارات لي ختارهم لمستخدم
computer_steps = [] # هنا لي ختارينا عشوائيا

def game_start(nums: list):

    if not isinstance(nums, list):
        raise TypeError(f"{colors['BOLD']}{colors['FAIL']}The input type MUST be a list{colors['ENDC']}")

    print(f"{colors['BOLD']}{colors['OKGREEN']}################################")
    print(f"---       Tic Tac Toe        ---")
    print(f"################################{colors['ENDC']}")
    print()
    print(f"{colors['BOLD']}{colors['HEADER']}Start playing by selecting a level")
    print(f"The available numbers: \n{colors['ENDC']}")

    return print_numbers(nums)

def print_numbers(nums: list):

    if not isinstance(nums, list):
        raise TypeError(f"{colors['BOLD']}{colors['FAIL']}The input type MUST be a list{colors['ENDC']}")

    if len(nums) == 0:
        print(f"{colors['BOLD']}{colors['WARNING']}Ooops!!! Nothing to print{colors['ENDC']}")
        return False

    for i in range(0, len(nums)):

        print('|', end="")
        print(nums[i], end="")

        if nums[i] % 3 == 0: 
            print('|')

    print()
    print_game_table(nums)

def print_game_table(nums: list):

    # ما غا نحتاجوش هذا ولكن زدتو
    if not isinstance(nums, list):
        raise TypeError(f"{colors['BOLD']}{colors['FAIL']}The input type MUST be a list{colors['ENDC']}")

    # مغا نحتاجوهاش تا هنا، لحقاش أصلا حنا معيطين ليها وسط فانكش لأخرى
    if len(nums) == 0:
        print(f"{colors['BOLD']}{colors['WARNING']}Ooops!!! Nothing to print{colors['ENDC']}")
        return False

    for i in range(0, len(available_positions)):

        print('|', end="")
        print('-', end="")

        if available_positions[i] % 3 == 0: 
            print('|')
    # هنا غا نعيطو لدالة باش يختار مستوى ويبدا
    return select_level()

def print_current_stage():

    ttt_range = list(range(1, len(tic_tac_toe) + 1 ))
    print()
    for i in range(0, len(tic_tac_toe)):

        print('|', end="")

        if tic_tac_toe[i] == 'X':
            print(f"{colors['OKGREEN']}X{colors['ENDC']}", end="")  
        elif tic_tac_toe[i] == 'O':
            print(f"{colors['FAIL']}O{colors['ENDC']}", end="")
        else:
            print(f'{tic_tac_toe[i]}', end="")
        

        if ttt_range[i] % 3 == 0: 
            print('|')

def select_level():

    global selected_level

    level = int(input(f"\n{colors['WARNING']}Select level to start [1 OR 2]:{colors['ENDC']}"))
    selected_level = level
    print(f"The level game is {level}")
    
    if selected_level == 2:
        print(f"\n{colors['OKBLUE']}The computer will start playing {colors['ENDC']}")

    print(f"\n{colors['BOLD']}{colors['FAIL']}Click {colors['WARNING']}0{colors['ENDC']}{colors['FAIL']} to exit {colors['ENDC']}")
    print(f"{colors['BOLD']}{colors['FAIL']}Click {colors['WARNING']}L{colors['ENDC']}{colors['FAIL']} to change level {colors['ENDC']}")
    print(f"\n{colors['BOLD']}{colors['OKBLUE']}Enjoy playing:{colors['ENDC']}\n")

game_start(available_positions)


while len(available_positions) >= 1:

    # الفرق لي كاين بين المستوى الأول والثاني هو
    # لكان المستوى الأول بنادم غا يبدا
    # المستوى الثاني الكومبيوتر غا يبدا
    if selected_level == 1:

        slctd = str(input("Select Number: ")) # slctd = selected
        slctd = int(slctd) if isinstance(slctd, str) and slctd.isdigit() else slctd

        if slctd == 0:
            print(f"{colors['BOLD']}{colors['OKGREEN']}You exit the game.{colors['ENDC']}")
            break

        if isinstance(slctd, str):
            if slctd.strip().lower() == 'l':
                print(f"{colors['BOLD']}{colors['OKBLUE']}Start from scratch to change Your Level.{colors['ENDC']}")
                break
            else:
                print('You must select numbers or L letter')
            break

        if slctd in available_positions:
            # تنخزنوا الاختيار في الخيارات ديال مستخدم
            human_steps.append(slctd)
            # تنمحيو الخيار لي ختار ليوزر من مصفوفة قبل ما نبقلبو على عنصر عشوائيا
            available_positions.remove(slctd)
            # User
            tic_tac_toe[slctd - 1] = 'X'

            # هنا تنقلبوا واش الخيارات تيسواو 3 أو أكثر باش نشوفوا واش ربح يوزر
            # نت عندك خدمة، وهي هنا تنقلبوا غا 3 عناصر ولكن ممكن يكونوا 4 وهذي خدمتك لا في يوزر لا في كومبيوتر
            # راه مخصنيش ندير ليك كل شي خدمي شوية أبنتي
            if len(human_steps) >= 3:
                if human_steps in winning_sets:
                    print(f"{colors['BOLD']}{colors['OKGREEN']}YOU WON!!!.{colors['ENDC']}")
                    print_current_stage()
                    break

            # Computer
            computer_slctd = random.choice(available_positions)
            # تنخزنوا الخيارات العشوائية ديال كومبيوتر
            computer_steps.append(computer_slctd)
            tic_tac_toe[computer_slctd - 1] = 'O'
            # هذي بحال يوزر تنحسبو لكومبيوتر
            if len(computer_steps) >= 3:
                if computer_steps in winning_sets:
                    print(f"{colors['BOLD']}{colors['FAIL']}YOU LOSS :( .{colors['ENDC']}")
                    print_current_stage()
                    break
            # Print round messages
            print(f"\n{colors['OKGREEN']}You played position {slctd}.{colors['ENDC']}")
            print(f"\n{colors['WARNING']}Computer has select {computer_slctd}.{colors['ENDC']}")
            print_current_stage()
            available_positions.remove(computer_slctd)

        else: 
            print(f"{colors['BOLD']}{colors['WARNING']}The available positions are: \n _> {available_positions}{colors['ENDC']}")
    else : # Computer round
        
        computer_slctd = random.choice(available_positions)
        computer_steps.append(computer_slctd)
        available_positions.remove(computer_slctd)    
        tic_tac_toe[computer_slctd - 1] = 'O'
        if len(computer_steps) >= 3:
            if computer_steps in winning_sets:
                print(f"{colors['BOLD']}{colors['FAIL']}YOU LOSS :( .{colors['ENDC']}")
                print_current_stage()
                break

        print(f"\n{colors['WARNING']}Computer has select {computer_slctd}.{colors['ENDC']}")
        print_current_stage()

        slctd = str(input("Select Number: ")) # slctd = selected
        slctd = int(slctd) if isinstance(slctd, str) and slctd.isdigit() else slctd

        if slctd == 0:
            print(f"{colors['BOLD']}{colors['OKGREEN']}You exit the game.{colors['ENDC']}")
            break

        if isinstance(slctd, str):
            if slctd.strip().lower() == 'l':
                print(f"{colors['BOLD']}{colors['OKBLUE']}Change Your Level.{colors['ENDC']}")
                break
            else:
                print('You must select numbers or L letter')
            break
        
        # User round
        if slctd in available_positions:
            human_steps.append(slctd)

            tic_tac_toe[slctd - 1] = 'X'
            if len(human_steps) >= 3:
                if human_steps in winning_sets:
                    print(f"{colors['BOLD']}{colors['OKGREEN']}YOU WON!!!.{colors['ENDC']}")
                    print_current_stage()
                    break

            # Round messages
            print(f"\n{colors['OKGREEN']}You played position {slctd}.{colors['ENDC']}")
            print_current_stage()
            available_positions.remove(slctd)

        else: 
            print(f"{colors['BOLD']}{colors['WARNING']}The available positions are: \n _> {available_positions}{colors['ENDC']}")
