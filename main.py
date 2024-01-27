import time, random, sys


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    return ("stop")


print("WELCOME to the best Arcade in the world!Have as much fun as you can in the WORLD BEST ARCADE!!")
print()

tickets = 0

print("please select the following locations!!: ")

print(" 0. TICKET STATION! ")

print(" 1. MATH WHIZZZZ! ")

print(" 2. FINDER OF THE UNICORNS!")

print(" 3. DEUL THE MIGHTY FORK! ")

print(" 4. BATHROOM BREAK!!!WooooHoooo!!")

print()

location = int(input("Which station would you like to go?"))
print()
if (location == 0):
    print("Welcome to the ticket station!!")
    print()
    prizes = ["Chantelle's lucky pencil", "robux", "cotton candy", "overdue vacation ticket", "teddy bear", "Nerds"]
    prizes_cost = [300, 415, 115, 100, 150, 100]
    print("Here are the available prizes: ")
    print()
    for i in range(len(prizes)):
        print(prizes[i] + " costs: " + str(prizes_cost[i]))

elif (location == 1):
    print("Welcome to MATTTHHH WHIZZ!!!")
    countdownstopped = "not stopped"
    while (countdownstopped != "stop"):
        num = list(range(100))
        num1 = random.choice(num)
        num2 = random.choice(num)
        print("What is " + str(num1) + " + " + str(num2))
        answer = int(input("Answer here: "))

        if (num1 + num2 == answer):
            print("Correct you get a ticket")
            tickets += 1
            print("You current have this many tickets: " + str(tickets))

elif (location == 4):
    print_slow("Be extremely careful because there are cameras in the washrooms!!! we aree watching you!!!!!")



















