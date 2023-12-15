import art
import data
import random

def compare_followers(personA, personB):
    followA = personA["follower_count"]
    followB = personB["follower_count"]

    if followA > followB:
        return "A"
    else:
        return "B"

def play_game():
    print(art.logo)
    personA = random.choice(data.data)

    end_game = False
    score = 0
    while not end_game:
        personB = random.choice(data.data)
        if personA == personB:
            personB = random.choice(data.data)

        print(f"Compare A: " + personA['name'] + ", a " + personA['description'] + ", from " + personA['country'])
        print(art.vs)
        print(f"Against B: " + personB['name'] + ", a " + personB['description'] + ", from " + personB['country'])

        type = input("Who has more followers? Type 'A' or 'B': ").upper()

        returns = compare_followers(personA, personB)
        if type == returns:
            score += 1
            personA = personB
            print(f"'You're right. Score: {score}")
            end_game = False
        else:
            print(f"Sorry, that's wrong. Game over(final score: {score})")
            end_game = True

    again = input("Do you want to play again? Yes(y) or No(n)").lower()
    if again == "y":
        play_game()

play_game()
