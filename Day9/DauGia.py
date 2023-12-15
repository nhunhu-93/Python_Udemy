import art

print(art.logo)

list_auction = []

def auction(name_person, price_person):
    dic_auction = {}
    dic_auction["Name"] = name_person
    dic_auction["Price"] = price_person
    list_auction.append(dic_auction)

def max_price(list_at):
    max_price = 0
    winner_name = "Ngoc"
    for i in range(len(list_at)):
        if max_price < list_at[i]["Price"]:
            max_price = list_at[i]["Price"]
            winner_name = list_at[i]["Name"]
    print(f"The winner of the bidding match is {winner_name} with a price of {max_price}")

play_again = True

while play_again:
    name = input("Please tell me your name? : ")
    price = int(input("Enter the amount you want to bid: "))

    auction(name, price)
    print(list_auction)

    again = input("Do you want to play again? YES/NO: ").lower()
    if again == "no":
        max_price(list_auction)
        play_again = False
