## Mở và đọc 1 file
# # Cách 1
# file = open("Day24/text.txt")
# contents = file.read()
# print(contents)
# file.close()

# # # Cách 2
# with open("Day24/text.txt") as file:
#     contents = file.read()
#     print(contents)

## Ghi 1 file, loại bỏ những cái đã có trong file, tạo mới hoàn toàn
# with open("Day24/text.txt", mode="w") as file:
#     file.write("Hello")

## Thêm nội dung vào 1 file
with open("Day24/text.txt", mode="a") as file:
    file.write("\nHello")
    
## Thêm 1 file không tồn tại
with open("Day24/new.txt", mode="w") as file:
    file.write("Hello")
    