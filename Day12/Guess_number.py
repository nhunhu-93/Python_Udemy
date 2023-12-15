# Trò chơi đoán số
import art 
import random

EASY = 10
HARD = 5

# Phân loại độ khó
def choices(choice):
    if choice == "easy":
        return EASY
    else:
        return HARD
    
# Kiểm tra số đoán
def check(number, answer,count):
    if number > answer:
        print("Too high.")
        return count - 1
    elif number < answer:
        print("Too low.")
        return count - 1
    else:
        print(f"You got it. The answer was {answer}")

# Chương trình chính
def play_game():
    print("Welcome to the Number Guessing Game!")

    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"Pssst, the correct answer is {answer}")

    # Cho người chơi chọn độ khó
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    count = choices(choice)
    
    # Kiểm tra số đoán
    number = 0
    # Nếu số đoán khác số đáp án và số lượt đoán còn > 0 thì tiếp tục chơi
    while count != 0 and number != answer:
        print(f"You have {count} attempts remaining")

        number = int(input("Make a guess: "))
        count = check(number, answer, count)

        if number != answer:
            print("Guess again.")

    # Nếu số lượt đoán = 0 mà vẫn chưa đoán đúng thì thua
    if count == 0:
        print("You've run out of guesses, you lose.")

    # Hỏi người chơi có muốn chơi lại không
    play_again = input("Do you want play again? yes(y) or no(n)").lower()

    if play_again == "y":
        play_game()

# Gọi hàm chính
play_game()
