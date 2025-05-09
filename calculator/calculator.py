from art import logo
print(logo)

def add(n1, n2):
    return n1+n2

def substract(n1,n2):
    return  n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2



operators = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

continue_calculation = True
f_num = int(input("Enter first number: "))

while(continue_calculation):

    print("+\n-\n*\n/")
    operator = input("Enter one operator: ")
    s_num = int(input("Enter second number: "))

    if operator in operators:
        answer = operators[operator](f_num,s_num)

        print(f"the result is {answer}")
        continue_cal = input("Do you want to continue with the calculation: 'Y' or 'N': " )
        if continue_cal.lower() == 'y':
            f_num = answer
            
        else:
            print("Thanks for using the calculator")
            print(f"The final answer is {answer}")
            continue_calculation = False







