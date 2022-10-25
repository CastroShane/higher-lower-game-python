from art import logo, vs
import random
from game_data import data
from replit import clear


# Get 1 random account from data
def get_random_ig():
    return random.choice(data)

# Format the message/clue
def format_message(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}."


def check_ans(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    continue_game = True
    account_a = get_random_ig()
    account_b = get_random_ig()

    while continue_game:
        account_a = account_b
        account_b = get_random_ig()

        while account_a == account_b:
            account_b = get_random_ig()

        print(f"Compare A: {format_message(account_a)}.")
        print(vs)
        print(f"Against B: {format_message(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_ans(guess, a_follower_count, b_follower_count)
        clear()
        print(logo)
        if is_correct:
          score += 1
          print(f"You're right! Current score: {score}.")
        else:
          continue_game = False
          print(f"Sorry, that's wrong. Final score: {score}")
game()
