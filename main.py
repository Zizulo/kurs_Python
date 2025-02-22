import math, time, random, example
from bp_car import Car

# name = 'Bro Code'
# print(type(name))

# print(name.upper())

# age = int(input("How old are you?: "))

# if age >= 18: 
#     print("You are an adult")
# elif age < 0:
#     print("You havent been born yet")

# temp = input("What is the temperature outside?: ")

# if temp >= 0 and temp <= 30:
#     print("the temperature is good today")
#     print("go outside")
# elif temp < 0 or temp > 30:
#     print("the temperature is bad today")
#     print("stay inside")

# name = ""

# while len(name) == 0:
#     name = input("Enter your name: ")

# print("Hello " + name)

# for i in range(10):
#     print(i)

# for i in range(50, 100):
#     print(i)

# for i in range(50, 100+1, 2):
#     print(i)

# for i in "Bro Code":
#     print(i)

# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy new Year")

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

# food[0] = "sushi"
# food.append("ice cream") #add new item to the end
# food.remove("hotdog")
# food.pop() #remove last item
# food.insert(0, 'cake')
# food.sort()
# food.clear()

# for x in food:
#     print(x)

# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)

# dinner_table = utensils.union(dishes)
# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))

# for x in dinner_table:
#     print(x)

# capitals = {'USA': 'Washington DC',
#             'India': 'New Dehli',
#             'China': 'Pekin',
#             'Russia': 'Moscow'}

# capitals.update({'Germany': 'Berlin'})
# capitals.update({'USA': 'New Jork'})
# capitals.pop('China')
# capitals.clear()
# print(capitals['Russia'])
# print(capitals.get('Russia'))
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# print(capitals)

# for key, value in capitals.items():
#     print(key, value)

# name = "Barak Shemana"

# if(name[0].islower()):
#     name = name.capitalize()
# else:
#     name = name.lower()
# print(name)

# first_name = name[:5]
# last_name = name[5:]
# print(first_name + ", " + last_name)

# def hello(name, lastname, age):
#     print(name + " " + lastname + " " + str(age))

# hello("CICI", "CZIKX", 21)

# def multiply(nr1, nr2):
#     result = nr1 * nr2
#     return result

# x = multiply(6, 8)
# print(x)

# num = 5

# print("Positive" if num > 0 else "Negative")

# price1 = 3.145
# price2 = 114
# price3 = -76056

# print(f"Price is ${price1:>10}")
# print(f"Price is ${price2:+10}")
# print(f"Prices is ${price3:+,.2f}")

# name = input("Jakie jest twe imie")

# while name == "":
#     name = input("Jakie jest twe imie")
# print(f"Hello {name}")

# my_time = int(input("Podaj czas w sekundach: "))

# for x in range(my_time, 0, -1):
#     seconds = x%60
#     minutes = int(x/60)%60
#     hours = int(x/3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("Czas się obudzić")

# for y in range(3):
#     for x in range(1, 10):
#         print(x, end="--")

# for y in range(5):
#     for x in range(1, 6):
#         print("--", end="")
#     print()

# fruits = ["apple", "coconut", "orange", "lemon"]
# fruits.sort()
# fruits.reverse()
# print(fruits)

# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Wpisz produkty do zakupienia (q aby zamknąć):")
#     if food.lower() == "q" : break
#     else: 
#         price = float(input(f"Wpisz cene {food}: $")) 
#         foods.append(food)
#         prices.append(price)

# print("---- YOUR CART ----")

# for food in foods:
#     print(food, end=" ")

# for price in prices:
#     total += price

# print()
# print(f"Całkowity koszt karty to: {total} $")

# questions = ("How many elements are in the periodic table",
#              "Which animal lays the largest eggs?",
#              "What is the most abundant gas in Earth`s atmosphere?",
#              "How many bones are in the human body?",
#              "Which planet in the solar system is the hottest?")

# options = (("A, 116", "B. 117", "C. 118", "D. 119"),
#             ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), 
#             ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogem"), 
#             ("A. 206", "B. 207", "C. 208", "D. 209"), 
#             ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# answers = ("C", "D", "A", "A", "B")
# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("---------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)
    
#     guess = input("Enter (A, B, C, D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print("Correct")
#     else:
#         print("Incorrect")
#         print("f{answers[question_num]}")
#     question_num += 1

# print("------------")
# print("Result")
# print("---------")
# print("answers: ", end="")
# for answer in answers:
#     print(answer, end=" ")
# print()

# print("guesses: ", end="")
# for guess in guesses:
#     print(guess, end=" ")
# print()

# score = int(score/len(questions) * 100)
# print(f"Your score is: {score}")

# capitals = {
#     "USA": "Dupa",
#     "UK": "Siuka",
#     "FRA": "Farara"
# }

# for key, value in capitals.items():
#     print(f"{key} : {value}")

# menu = {
#     "pizza": 3.00,
#     "nachos": 4.50,
#     "popcorn": 6.00,
#     "fries": 2.50,
#     "chips": 1.00,
#     "pretzel": 3.50,
#     "soda": 3.00,
#     "lemonade": 4.25
# }

# cart = []
# total = 0

# print("---MENU---")
# for key, value in menu.items():
#     print(f"{key:10} : {value:.2f}$")
# print("-----------")

# while True:
#     food = input("Select an item (q to quit): ").lower()
#     if food == "q":
#         break 
#     elif menu.get(food) is not None:
#         cart.append(food)
    
# for food in cart:
#     total += menu.get(food)

# for items in cart:
#     print(items, end=" ")

# print(total)

# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True

# print("Python Number Guessing Game")
# print(f"Select a number between {lowest_num} and {highest_num}")

# while is_running:
#     guess = input("Enter your guess: (q to quit)")

#     if guess == "q" or guess == "Q": break

#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1

#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"Select a number between {lowest_num} and {highest_num}")
#         elif guess < answer:
#             print("Too low! Try again!")
#         elif guess > answer:
#             print("Too high! Try again!")
#         else:
#             print(f"Correct! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False
#     else:
#         print("Invalid guess")
#         print(f"Select a number between {lowest_num} and {highest_num}")

# options = ("rock", "paper", "scissors")

# running = True

# while running:
#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter a choice (rock, paper, scissors)")

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")

#     if player == computer:
#         print("Its a tie")
#     elif player == "rock" and computer == "scissors":
#         print("You win")
#     elif player == "paper" and computer == "rock":
#         print("You win")
#     elif player == "scissors" and computer == "paper":
#         print("You win")
#     else:
#         print("You lose")
#         running = False
    
#     play_again = input("Play again? (y/n): ").lower()

#     if not play_again == "y":
#         running = False

# print("Thanks for playing")

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘

# "┌───────────┐"
# "│           │"
# "│           │"
# "│     ●     │"
# "│           │"
# "│           │"
# "└───────────┘"

# dice_art = {
#     1: ("┌───────────┐", 
#         "│           │", 
#         "│           │", 
#         "│     ●     │",
#         "│           │", 
#         "│           │", 
#         "└───────────┘"),
#     2: ("┌───────────┐", 
#         "│           │", 
#         "│           │", 
#         "│     ●     │",
#         "│           │", 
#         "│        ●  │", 
#         "└───────────┘"),
#     3: ("┌───────────┐", 
#         "│ ●         │", 
#         "│           │", 
#         "│     ●     │",
#         "│           │", 
#         "│        ●  │", 
#         "└───────────┘"),
#     4: ("┌───────────┐", 
#         "│ ●       ● │", 
#         "│           │", 
#         "│           │",
#         "│           │", 
#         "│ ●       ● │", 
#         "└───────────┘"),
#     5: ("┌───────────┐", 
#         "│ ●       ● │", 
#         "│           │", 
#         "│     ●     │",
#         "│           │", 
#         "│ ●       ● │", 
#         "└───────────┘"),
#     6: ("┌───────────┐", 
#         "│ ●       ● │", 
#         "│           │", 
#         "│ ●       ● │",
#         "│           │", 
#         "│ ●       ● │", 
#         "└───────────┘")
# }

# dice = []
# total = 0
# num_of_dice = int(input("How many dice?: "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))

# # for die in range(num_of_dice):
# #     for line in dice_art.get(dice[die]):
# #         print(line)

# for line in range(7):
#     for die in dice:
#         print(dice_art.get(die)[line], end="")
#     print()

# for die in dice:
#     total += die

# print(f"Total: {total}")

# def count(end, start = 0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE")

# count(10)

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}.{first} {last}")

# hello("Hello", title = "Mr", first = "Spongebob", last = "Squarepants")
# print("1", "2", "3", "4", "5", sep="-")

# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=48, area=123, first=456, last=789)
# print(phone_num)

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3, 4, 5))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Dr","Spongebob", "Harold", "Squarepants")

# alfabet = ["A", "B", "C", "D"]

# def display_alf(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_alf(alfabet)

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")

# print_address(street= "123 Fake St.", city= "Detroit" , state= "MI", zip= "54321")

# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     print(f"{kwargs.get('street')}")
#     for value in kwargs.values():
#         if value == "123 Fake St.":
#             pass
#         else:
#             print(value, end=" ")

# shipping_label("Dr.", "Spongebob", "Squarepants", "III",
#                street="123 Fake St.",
#                apt="100",
#                city="Detroit",
#                state="MI",
#                zip="54321")

# word = "APPLE"
# students = {"Spongebob", "Patrick", "Sandy"}
# grades = {"Sandy": "A", "Squidward": "B", "Spongebob": "C", "Patrick": "D"}
# email = "BroCode@gmail.com"

# letter = input("\nGuess a letter in the secret word: ")

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")

# student = input("\nEnter the name of a student: ")

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} was not found")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")

# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)
# print(doubles)

# doubles2 = [x * 2 for x in range(1, 11)]
# print(doubles2)

# triples = [y * 3 for y in range(1, 11)]
# squares = [z * z for z in range(1, 11)]

# fruits = ["apple", "orange", "banana", "coconut"]
# fruit_chars = [fruit[0] for fruit in fruits]
# print(fruits)

# numbers = [1, -2, 3, -4, 5, -6, 8, -7]
# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 == 1]
# print(positive_nums)
# print(negative_nums)
# print(even_nums)
# print(odd_nums)

# grades = [85, 42, 79, 90, 56, 61, 30]
# passing_grades = [grade for grade in grades if grade >= 60]
# print(passing_grades)

# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is Sunday"
#         case 2:
#             return "It is Monday"
#         case 3:
#             return "It is Tuesday"
#         case 4:
#             return "It is Wednesday"
#         case 5:
#             return "It is Thursday"
#         case 6:
#             return "It is Friday"
#         case 7:
#             return "It is Saturday"
#         case _:
#             return "Not a valid day"

# print(day_of_week(1))

# def its_weekend(day):
#     match day:
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#             return "It is not weekend"
#         case "Saturday" | "Sunday":
#             return "It is weekend"
#         case _:
#             return "Not a valid day"

# print(its_weekend("Monday"))

# result = example.pi
# result = example.square(3)
# result = example.circumference(3)
# result = example.cube(3)
# result = example.area(3)

# print(result)

# def func1():
#     a = 1
#     print(a)

#     def func2():
#         print(a)
#     func2()

# func1() 

# def favorite_drink(drink):
#     print(f"Your favorite drink is {drink}")

# def main():
#     print("This is script")
#     favorite_drink("coffee")
#     print("Goodbye")

# if __name__ == '__main__':
#     main()

def show_balance(balance):
    print(f"Your balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0: 
        print("Thats not a valid amount") 
        return 0
    else: return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdraw: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    # balance = 0
    # is_running = True

    # while is_running:
    #     print("Banking Program")
    #     print("1. Show Balance")
    #     print("2. Deposit")
    #     print("3. Withdraw")
    #     print("4. Exit")

    #     choice = input("Enter your choice (1-4): ")

    #     match choice:
    #         case '1': show_balance(balance)
    #         case '2': balance += deposit()
    #         case '3': balance -= withdraw(balance)
    #         case '4': is_running = False
    #         case _:
    #             print("That is not a valid choice")

    # print("Thank you, have a nice day")

    car1 = Car("Mustang", 2024, "red", False)

    car1.drive()
    car1.stop()
    car1.describe()

if __name__ == '__main__':
    main()
    