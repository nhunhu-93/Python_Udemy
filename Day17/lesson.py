class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0 # thuộc tính mặc định
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# Thêm thuộc tính
user_1 = User("001", "Nhu")
user_2 = User("002", "Cao")

## Thêm thuộc tính khi không có hàm tạo
# user_1.id = "001"
# user_1.name = "Nhu"

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
