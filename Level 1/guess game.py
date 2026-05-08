import random
number = random.randint(1, 100)
attempts = 0
max_attempts = 10
print("🎮 Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")
print("You have 10 attempts")
while attempts < max_attempts:
    guess = int(input("Enter your guess number : "))
    attempts += 1

    if guess < number:
        print("Soory ! this number is Small 📉")

    elif guess > number:
        print("Soory ! this number is big📈")

    else:
        print("🎉 Congratulations ! You guessed the number is absolutely correct!")
        break
if guess != number:
    print("❌ Game Over ! The number was :", number)