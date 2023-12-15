ermi  = 10 # Global variable
def ermis():
    ermi = 8 # Local variable
    print(ermi)
ermis()
print(ermi)

# Neu muon thay doi gia tri cua bien global thi phai dung global
ermi = 10 # Global variable
def ermis():
    global ermi
    ermi = 8 # Local variable
    print(ermi)
ermis()
print(ermi)

# Cach khac la dung return
ermi = 10 # Global variable
def ermis():
    ermi = 8 # Local variable
    return ermi + 1

ermi = ermis()
print(ermi)