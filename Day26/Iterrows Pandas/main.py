student_dict = {
    "student": ["Angela", "Anna", "Tom"],
    "score": [10,9,10]
}

# for(name, score) in student_dict.items():
#     # print(name)
#     print(score)
    
# Iterrrows: cho phép lọc qua từng hàng của khung dữ liệu thay vì từng cột
import pandas
student_data_frame = pandas.DataFrame(student_dict)

for (index,row) in student_data_frame.iterrows():
    # print(index) # in ra từng chỉ mục
    # print(row) # in ra đối tượng chuỗi của 1 hàng
    # print(row.student) # lấy ra cột tên
    # print(row.score) # lấy ra cột điểm số
    if row.student == "Anna":
        print(row.score)
