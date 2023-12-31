PLACEHOLDER = "[name]"

with open("Day24/Mail Merge Project/Input/Names/invited_names.txt") as data:
    name = data.readlines()
    print(name)
    
with open("Day24/Mail Merge Project/Input/Letters/starting_letter.txt") as letters:
    letter_content = letters.read()
    for name in name:
        new_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, new_name)
        with open(f"Day24/Mail Merge Project/Output/letter_to_{new_name}.txt", mode="w") as mail:
            mail.write(new_letter)
    
