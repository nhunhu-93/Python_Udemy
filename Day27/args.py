# *args: là một tuple chứa các tham số truyền vào
# vị trí của tham số trong tuple rất quan trọng

# tuple: là một dãy các giá trị không thay đổi
def add(*arg):
    # return sum(arg)
    sum = 0
    for i in arg:
        sum += i
    return sum
print(add(1,2,3,4))

# **kwargs: là một dictionary chứa các tham số truyền vào
# key của dictionary là tên của tham số
# value của dictionary là giá trị của tham số

def calculation(n,**kwargs):
    # for (key, value) in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
calculation(3,add = 3, multiply = 5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        # self.model = kwargs["model"] 
        # nếu dùng kwargs["make" mà lúc tạo đối tượng không có make thì bị lỗi
        self.model = kwargs.get("model") # get sẽ tránh gây lỗi khi hiện giá trị là None nếu không có dữ liệu
        
car = Car(make = "Nissao")
print(car.model)