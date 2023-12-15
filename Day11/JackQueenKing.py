import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hàm chọn ngẫu nhiên 1 lá bài
def deal_card(cards):
    return random.choice(cards)

# Hàm tính điểm
def calculate_score(list_cards):
    total = sum(list_cards)
    # Nếu tổng là 21 và có 2 lá bài thì trả về 0
    if total == 21 and len(list_cards) == 2:
        return 0
    # Nếu có 11 trong list_cards và tổng lớn hơn 21 thì 11 sẽ được tính là 1
    if 11 in list_cards and total > 21:
        list_cards.remove(11)
        list_cards.append(1)
    return sum(list_cards)

# Hàm so sánh điểm
def compare(score_user, score_computer):
    if score_user > 21 and score_computer > 21:
        print("You went over. You lose 😤")
    elif score_computer == score_user:
        print("Draw 🙃")
    elif score_computer == 0:
        print("You lose, opponent has BlackJack 😱")
    elif score_user == 0:
        print("You win with a BlackJack 😁")
    elif score_user > 21:
        print("You went over. You lose 😭")
    elif score_computer > 21:
        print("Opponent went over. You win 😁")
    elif score_computer > score_user:
        print("You lose 😭")
    else:
        print("You win 😁")

# Hàm chơi game
def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    end_game = False

    # Chia 2 lá bài cho người chơi và máy
    for i in range(2):
        user_cards.append(deal_card(cards))
        computer_cards.append(deal_card(cards))

    while not end_game:
        score_user = calculate_score(user_cards)
        score_computer = calculate_score(computer_cards)
        print(f"Computer first card: {computer_cards[0]}")
        print(f"Your cards: {user_cards}  total is {calculate_score(user_cards)}")

        # Nếu người chơi hoặc máy có tổng 21 thì kết thúc game
        if score_computer == 0 or score_user == 0 or score_user > 21:
            end_game = True
        else:
            add = input("Do you want to draw more cards? YES(y) or NO(n) ").lower()
            if add == "y":
                user_cards.append(deal_card(cards))
            else:
                end_game = True

    # Máy sẽ rút thêm bài khi tổng điểm nhỏ hơn 17
    while score_computer != 0 and score_computer < 17:
        computer_cards.append(deal_card(cards))
        score_computer = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {score_user}")
    print(f"Computer's final hand: {computer_cards}, final score: {score_computer}")
    # So sánh điểm
    compare(score_user, score_computer)

# Vòng lặp chơi game
while input("Do you want to play again? yes(y) or no(n)").lower() == "y":
    play_game()
