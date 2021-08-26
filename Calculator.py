# Calculator

a = input("Please put the operator here + - * / \n")
b = int(input("Please put First number here 0-9 \n"))
c = int(input("Please put Second number here 0-9 \n"))

    
str = '{} {} {}'.format(b,a,c)
add = b + c
subtract = b - c
multiply = b * c
divide = b / c

if a == "+":
    print(str)
    print(add)
    
elif a =="-":
    print(str)
    print(subtract)
    
elif a =="*":
    print(str)
    print(multiply)
  
elif a =="/":
    print(str)
    print(divide)
    
else:
    print("Error")
