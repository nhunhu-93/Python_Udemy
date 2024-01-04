# list comprehension ( cách ghi tắt)
# new_list = [new_item for item in list]

# Ví dụ 1:
# data ="Angela"
# new_data = [n for n in data]

# Ví dụ 2:
# new_data1 = [n*2 for n in range(1,5)]

# Ví dụ 3:
data_name = ["Nhu", "Khang", "Khanh", "Cao", "Ngan", "Doanh", "Em", "Quyen"]
new_data = [name.upper() for name in data_name if len(name)>4]
print(new_data)
