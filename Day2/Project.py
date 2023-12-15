#Máy tính tiền boa

print("Welcom to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

#tinh toan
result_total = total_bill + total_bill * (tip/100) 
result_person = result_total / people

# print(f"Each person should pay: ${round(result_person,2)}")
print(f"Each person should pay: ${result_person:.2f}")
# print("Each person should pay: ${:.2f}".format(result_person))

# Có các cách làm tròn số như sau:
# round(number, số chữ số sau dấu phẩy): round(1.2345, 2) = 1.23
# tên:.2f: 1.2345 -> 1.23
# :.2f.format(tên): 1.2345 -> 1.23