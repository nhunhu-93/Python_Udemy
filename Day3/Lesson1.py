print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
yearold = int(input("How old are you? "))

if height > 120:
    print("You can ride the rollercoaster!")
    if yearold > 18:
        bill = 12
        print("Adult tickets are $12.")
    elif yearold >= 12 and yearold <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 5
        print("Child tickets are $5.")

    photo = input("Do you want to take a photo? Y or N: ")
    if photo == "Y":
        bill += 3
    
    print(f"Please pay: ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")