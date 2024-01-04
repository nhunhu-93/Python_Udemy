# dictionary comprehension 
# new_data = {new_key:new_value for item in list}
# new_data = {new_key:new_value for (key,value) in dict.items() if test}
# chú ý: dict.items() (bắt buộc dùng items())

# import random

# list_data = ["Angela", "Petter","Anna", "Gil", "Tom", "Tony", "Emma"]
# students_score = {student:random.randint(1,100) for student in list_data}
# passed_students = {student:score for (student, score) in students_score.items() if score >=60}
# print(passed_students)

# Dùng dict comprehension để lặp qua khung panda
import pandas
dict = {'Petter': 86,
        'Gil': 91,
        'Tom': 70,
        'Tony': 65}

student_data_frame = pandas.DataFrame(dict)
print(student_data_frame)

