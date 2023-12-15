# Hangman(người treo cổ)
import random
import Hangman_art
import Hangman_words

print(Hangman_art.logo)
random_list = random.choice(Hangman_words.word_list) # Random 1 chữ từ danh sách

# In "_" tương ứng với số chữ cái trong từ đã chọn
list_choice = []
for n in random_list:
    list_choice += "_"

incorrect_guess =6
end_game = False
# Vòng lặp chính
while not end_game:
    choice_guess = input("Please choose any letter: ").lower() #Người chơi đoán chữ bất kỳ
    
    # Nếu chữ đã đoán trùng với chữ đã đoán trước đó thì thông báo
    if choice_guess in list_choice:
        print(f"You've already guessed {choice_guess}")

    # Nếu chữ đã đoán trùng với chữ trong từ đã chọn thì thay thế "_" bằng chữ đó
    for letter in range(len(random_list)):
        if random_list[letter] == choice_guess:
            print(f"You have chosen the correct letter: {choice_guess}")
            list_choice[letter] = choice_guess
            print(Hangman_art.stages[incorrect_guess])
    
    # Nếu chữ đã đoán không trùng với chữ trong từ đã chọn thì thông báo
    if choice_guess not in random_list:
        print(f"You guessed {choice_guess}, that's not in the word. You lose a life.")
        print(Hangman_art.stages[incorrect_guess-1])
        incorrect_guess -= 1
        # Nếu số lần đoán sai bằng 0 thì thông báo thua
        if incorrect_guess == 0:
            end_game = True
            print("You lose")

    # Chuyển list thành string và in ra màn hình
    print(f"{' '.join(list_choice)}")

    # Nếu "_" không còn trong list thì thông báo thắng
    if "_" not in list_choice:
        end_game = True
        print("You Win")


