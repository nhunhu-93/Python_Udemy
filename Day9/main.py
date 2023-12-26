programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Bug"]) # in value của "Bug"

# Thêm 1 mục vào từ điển

programming_dictionary["Loop"] = "The action of doing something over and over again"

# Tạo 1 từ điển mới
create_list = {}

# # Xoá trống 1 từ điển
# programming_dictionary = {}

# Chỉnh sửa giá trị
programming_dictionary["Bug"] = "A moth in your computer"

# Vòng lặp
for key in programming_dictionary:
    print(key)  # in key 
    print(programming_dictionary[key])   # in value

# Thêm list trong dictionary
programming = {
    "Tu Nhu" : ["Cute", "Cake"]
}

# thêm dictionary trong dictionary
programming = {
    "Quoc Viet": {"Location": ["An Giang", "Bac Lieu"],
                  "Girl friend": "Tu Nhu"},
    "Tu Nhu" : {"Location": ["An Giang", "Bac Lieu"],
                  "Boy friend": "Quoc Viet"}
}

# thêm dictionary trong list
programming = [
    {"Name": "Quoc Viet",
    "Location": ["An Giang", "Bac Lieu"],
    "Girl friend": "Tu Nhu"
    },
    {"Name": "Tu Nhu",
    "Location": ["An Giang", "Bac Lieu"],
    "Boy friend": "Quoc Viet"
    }
]

