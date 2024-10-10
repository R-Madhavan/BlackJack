import random
from art import logo
#written by me
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def final():
    print(f"Your final hand: {user}, final score: {user_total}")
    print(f"Computer final hand: {computer}, final score: {computer_total}")

def current_print():
    print(f"Your cards:{user}, current score: {user_total}")
    print(f"Computer's first card: {computer[0]}")

def computer_brain():
    computer_thought = random.randint(0,1)
    print(computer_thought)
    if computer_thought == 1:
        computer.append(random.choice(cards))

should_continue = True
while should_continue:
    wanna_play_blackjack = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    if wanna_play_blackjack == "y":
        print("\n"*40)
        print(logo)
        computer = random.sample(cards,2)
        computer_total = sum(computer)
        user = random.sample(cards,2)
        user_total = sum(user)

        while wanna_play_blackjack == "y":
            if wanna_play_blackjack == "y":
                    current_print()
                    get_new_card = input("Type 'y' to get another card, type 'n' to pass: ")
                    if get_new_card == "y":
                        user.append(random.choice(cards))
                        user_total = sum(user)
                        computer_brain()
                        if user_total > 21:
                            current_print()
                            final()
                            print("😭 You went over. You lose 😭")
                            wanna_play_blackjack = "n"
                    else:
                        final()
                        if computer_total == user_total:
                            print("😑 Draw 😑")
                        elif computer_total > 21 or computer_total < user_total:
                            print("🥳 You Won 🥳")
                        else:
                            print("😭 You Lost 😭, Computer Won")
                        wanna_play_blackjack = "n"
            else:
                break
    else:
        should_continue = False
