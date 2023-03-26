def add(a,b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer) + "\n")
def sub(a,b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer) + "\n")
def mult(a,b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer) + "\n")
def div(a,b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer) + "\n")


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")


    choice = input("Enter a choice from the list above: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter next number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter next number: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiply")
        a = int(input("Enter first number: "))
        b = int(input("Enter next number: "))
        mult(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter next number: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Program ended")
        exit()


