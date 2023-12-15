# Mật mã caesar cipher
import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Hàm mã hóa và giải mã
def Ceasar(plain_text, shift_amount, direction_i):
    list = ""
    for letter in plain_text:
        # Kiểm tra xem ký tự có trong bảng chữ cái không -> thay đổi vị trí
        if letter in alphabet:
            if direction_i == "encode":
                new_index = alphabet.index(letter) + shift_amount
            else:
                new_index = alphabet.index(letter) - shift_amount
            list += alphabet[new_index]
        # Nếu không có trong bảng chữ cái thì giữ nguyên
        else:
            list += letter
    print(f"The {direction_i} text is {list}")

# Hàm chạy chương trình
play_again = True
while play_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Giúp cho shift không vượt quá 26
    shift = shift % 26

    # Gọi hàm mã hóa và giải mã
    Ceasar(plain_text= text, shift_amount= shift, direction_i= direction)

    again = input("Do you want play again? Yes/No").lower()
    if again == "no":
        play_again = False
    
        