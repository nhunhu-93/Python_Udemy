import art

def add(n,m):
    return n + m

def subtract(n,m):
    return n - m

def multiply(n,m):
    return n * m

def divide(n,m):
    return n / m

operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculation_programe():
    print(art.logo)
    num1 = int(input("What is the first number?: "))
    for key in operation:
        print(key)

    play_again = True
    while play_again:
        calculation = input("Which calculation do you want to use?")
        num2 = float(input("What is the next number?: "))
        operation_function = operation[calculation]
        result = operation_function(num1, num2)
        print(result)

        again = input("Do you want continue(y) or start new program(n)").lower()

        if again == "y":
            num1 = result
        else:
            play_again = False
            calculation_programe()
        
calculation_programe()
