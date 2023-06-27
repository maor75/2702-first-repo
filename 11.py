# שאלה 11
# Write a program that asks the user for a number and prints the multiplication table for that number up to 10.

def multiplication():
    num = int(input("enter number:"))
    for i in range(1,11):
        resulte = num * i
        print(num, "*",i ,"=",resulte)

multiplication()
