# To find the greatest between three numbers

num1=int(input("Enter the value for number 1:"))
num2=int(input("Enter the value for number 2:"))
num3=int(input("Enter the value for number 3:"))

if num1 > num2 & num1 > num3:
    print(num1," is greatest")
elif num2 > num3 & num2 > num1:
    print(num2," is greatest")
else:
    print(num3," is the greatest")