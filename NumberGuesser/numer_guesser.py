from random import randint

#initial config
attempts = 0
attempt = 0
secret_number = randint(1,10)

#user config
usr_name = input("Tell me your name ")
print(f"welcome, {usr_name}, i'm thinking in a number between 1 and 10, you have 3 attempts to guess")

while attempts <= 2:
    attempt = int(input("Tell me the number i'm thinking to "))
    attempts += 1
    print(f"You have {3-attempts} attemps remaining")

    if attempt < secret_number:
        print("You have failed, the number is higher than that")
    elif attempt > secret_number:
        print("You have failed, the number is lower than that")
    else:
        print(f"Congratulations, that's the number i was thinking, and you found it in just {attempt} attempts. Now tell me, {usr_name}, what's you wish?")
        break

if attempt != secret_number:
    print(f"Sorry, you have no attempts remaining, the number i was thinking was {secret_number}")
else:
    print("Fine, i'll grant your wish")
