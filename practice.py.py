name=input("Enter your name : ")

attendance=int(input("Enter 0 if not present : "))
#any other number pressed except 0 will automatically be considered as present


if attendance != 0:
    num1=int(input("Enter the marks of the student : "))
    num2=int(input("Enter the passing marks of the subject : "))
    if num1 > num2:
        print("Congratulatios!!",name,"You are Passed")
    elif num1 == num2:
        print("Luckily",name,"You are just Passed")
    else:
        print("Sorry",name,"You are failed")
else:
    print("You were absent")
