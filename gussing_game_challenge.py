from random import randint

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("\n\tLET'S PLAY!")

rnumber = randint(0,100)
previous_number = 0
count = 1
while True:
    user_input = int(input("\nI\'m thinking of  number between 1 and 100\nWhat is on your head? "))
     
    if user_input > 100:
        print("OUT OF BOUNDS")
        continue
        
    elif user_input == rnumber:
        print(f"\nCorrect! the number is {rnumber}\nYou guessd it in {count} chances")
        break
        
    elif previous_number == 0:
        previous_number = user_input
        if abs(user_input - rnumber) <= 10:
            print("WARM!")
            continue
        else:
            print("COLD!")
            continue
          
    elif abs(rnumber - user_input) < abs(rnumber - previous_number):
        print("WARMER!")
    else:
        print("COLDER!")
    previous_number = user_input
    count += 1