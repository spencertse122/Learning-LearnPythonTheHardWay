import os
from sys import exit
from random import random, randint

def show_score(s):

    # overall_score = s["happiness"] -

    print(" ")
    print("*" * 20)
    print("SCORE CARD")
    print('-' * 20)
    print("Total Work Hours (w):", s["work_hours"])
    print("Remaining Moves (m):", s["moves"])
    print("Happiness (h):", s["happiness"])
    print('*' * 20)
    print(" ")

def make_coffee(s):
    os.system("clear")
    print("It's a long walk, but you have arrived the kitchen!")
    print("Are you ready to make a coffee? y/n")
    choice = input("> ")
    print('-' * 20)

    if "y" in choice:
        print("Brewing now........And! Coffee Time!\n")
        s['moves'] -= 1

        coffee_quality = random()

        if coffee_quality > 0.5:
            print("The coffee tastes GREAT!")
            s["happiness"] += 10
            print("+10 hapiness\n-1 moves")

        elif coffee_quality < 0.5:
            print("The coffee is grainy and tastes like shit, fucking reusable k-cup")
            s['happiness'] -= 5
            print("-5 happiness\n-1 moves")

    elif "n" in choice:
        print("Boss Lady just caught you slacking! ")
        print("-1 working-hours on BigTime")
        s["work_hours"] -= 1

    else:
        print("Not sure what you are doing")
        print("Let's try it again")
        print('>>>')
        make_coffee(s)

def snack(s):
    os.system("clear")
    print("Candies are always WELCOMED!!! You've got chocolates, and popcorn, but the company is too broke for avocado...")
    print("+5 happiness \n-1 moves")
    s['moves'] -= 1
    s['happiness'] += 5

def bribe_controller(s):
    os.system("clear")
    print("Start the small talk, chat the football!")
    print("yeah....I 'LOVE' football, I really do")
    print("-10 happiness \n+1 moves")
    s['moves'] += 1
    s['happiness'] -= 10

def big_projects(s):
    os.system("clear")
    print("Big projects cool, but it takes time")
    print("But good job tackling the big monster")
    print("-5 happiness \n-1 moves \n+2 working hours")
    s['moves'] -= 1
    s['happiness'] -= 5
    s['work_hours'] += 2

def churning_reports(s):
    os.system("clear")
    print("Ready....set.....go")
    print("Welcome to the GRUNT WORK FACTORY\nthis shit sucks, but it doesn't take much time")
    print("-10 happiness \n-0 moves \n+2 working hours")
    s['happiness'] -= 10
    s['work_hours'] += 2

def creating_drama(s):
    os.system("clear")

    options = ["Rock", "Paper", "Scissors"]

    print("Welcome to our sorority 2.0 challenge")
    print("As a 'well established' company, we love dramas")

    print("""
          1. Rock
          2. Paper
          3. Scissors
    """)
    print("Pick your move:")

    m = input("> ")
    c = options[randint(0,2)]

    if m == c:
        print("It's a draw")
        creating_drama(s)
    else:
        pass


####################################################################

def start(s):
    print("\nWelcome to Office Survivors", flush = True)
    print("""
          1. Make some coffee
          2. Get some snack
          3. Bribe the Controller to get more Moves
          4. Churning hand-cranking reports
          5. Working on fun projects
          6. Creating Drama
    """)
    show_score(s)
    print("Press Ctrl + c to quit your job if you're done with this bullshit")
    print("Enter the number of things you want to do:")
    choice = input("> ")

    try:
        actions[int(choice)](s)
    except:
        print("Sorry, what as that? let's choose again~")
        print('-' * 20)
        start(s)

def gameover(s):
    os.system("clear")

    if s['moves'] <= 0:
        if s["work_hours"] < 9:
            print("GAME OVER\nYou are fired because you didn't work 9 hours today\nHere is your score:")
            show_score(s)
        elif s['work_hours'] > 9:
            s['happiness'] += (s['work_hours'] - 9) * 2.5
            print("YOU WIN\nHere is your score:")
            show_score(s)
        else:
            print("GAME OVER\nYou run out of moves")
    else:
        pass


actions = {
           1 : make_coffee,
           2 : snack,
           3 : bribe_controller,
           4 : churning_reports,
           5 : big_projects,
           6 : creating_drama
}


#  defining variables

score = {
         "work_hours" : 0,
         "moves" : 15,
         "happiness" : 100,
         "unlog_hours" : 0,
         "sneakout_numbers" : 0
}

# Start the game here

try:
    while score["moves"] > 0:
        start(score)

except KeyboardInterrupt:
    print("\nYou have quit your job, and ended the game")
else:
    gameover(score)
