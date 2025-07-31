import random
from ui import logo

print(logo)

your_list, computer_list = [], []
for i in range(0, 4):
    if i < 2:
        your_list.append(random.randint(1, 10))
    else:
        computer_list.append(random.randint(1, 10))

user_score = sum(your_list)
game_over = False
pick = 0

print(f"Your cards {your_list}")
print(f"Computer's card {computer_list[0]}")

while not game_over:
    user_input = input("Do you want to pick card? Press `y` or `n`")
    if user_input == "y":
        your_list.append(random.randint(1, 10))
        user_score = sum(your_list)
        print(your_list)
    else:
        if user_score <= 21 and user_score > sum(computer_list):
            game_over = True
            print(f"You win with {user_score}")
        else:
            game_over = True
            print(f"Computer wins with {sum(computer_list)}")