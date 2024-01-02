# with open("Day25/weather_data.csv") as weather_data:
#     list_weather = weather_data.readlines()
#     print(list_weather)

# # Cách 2 dùng CSV:
# import csv
# with open("Day25/weather_data.csv") as weather_data:
#     object_weather = csv.reader(weather_data)
#     temperatures = []
#     for row in object_weather:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Cách 3: Dùng pandas đọc file csv
import pandas
data = pandas.read_csv("Day25/Weather/weather_data.csv")
print(data["temp"])

# Chuyển file thành từ điển
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list() # chuyển chuỗi về list
# print(data["temp"].mean())  # Tính average
# print(data["temp"].max())  # Tìm số lớn nhất

# Chú ý data["temp"] giống với data.temp

# Tìm dòng theo điều kiện
# print(data[data["day"] == "Monday"])
# print(data[data.temp == data.temp.max()])

# Chuyển từ độ C sang F
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

#Cách 4: Dùng pandas đọc dữ liệu từ python
# import pandas
# dict = {
#     "student": ["Nhu", "Viet"],
#     "score": [10,10]
# }

# data = pandas.DataFrame(dict)
# data.to_csv("Day25/new_data.csv") # chuyển dữ liệu thành csv và lưu vào 1 file máy tự tạo
        