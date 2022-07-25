def add(x, y):
    return x+y

def subtract(x, y):
   return x-y

def divide(x,y):
    return x/y

def multy(x, y):
   return x*y

print("Wich operation you want?")
print(" 1.add")
print(" 2.subtract")
print(" 3.divide")
print(" 4.multyply")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4' ):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, '-', num2, '=', subtract(num1,num2))
        elif choice == '3':
           print(num1, '/', num2, '=', divide(num1, num2))
        elif choice == '4':
            print(num1, '*', num2, '=', multy(num1, num2))
        next_calculation = input("Let's do next calculation? (yes/no): ")

        if next_calculation == "no":
            print("Al prossimo calcolo!2")
            break