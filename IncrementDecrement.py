"""
The moto of this program is to simply return the same value before and after incrementation
and decrementation after each operation, so if user enter 2 , counter will increment it and then decrement
after going through operation for each value
"""

num1=int(input("Enter a number :"))
counter=0

i=100

for counter in range(1,101):
    num1=num1*2
    # print(num1)
    # print("Counter :",counter)
    """
    You can remove this comment , if you want to view the result of the above calculation after each
    counter, but honestly its not worth it
    """

    if counter==i:
        print("Result is:",num1)
        print("Counter :",counter)


else:
    print("After 1st condition of for loop is executed, and ready to begin else part")
    print()
    for counter in range(100,0,-1):
        if counter==i:
            print("The Result which is going to get executed from:",num1)
        num1=num1/2
        # print(num1)
        # print("Counter :",counter)
        if counter==1:
            print("Result is:",int(num1))
            print("Counter :",counter)


# doing the same thing in addition but by utlising while loop

print()
num1=int(num1)
print("While Loop :")
print()
while counter<=100:

    counter=counter+1
    num1=num1+2
    if(counter==100):
        print("Your Counter has Finally Reached to :",counter)
        print("The Result is :",num1)
else:
    print("After 1st condition of while loop is executed, and ready to begin else part")
    print()
    while counter>=1:
        counter=counter-1
        num1=num1-2
        if(counter==1):
           print("Your Counter has Finally Reached to :",counter)
           print("The Result is :",num1)


