#שאלה 9
#Write a program that asks the user for their age.
# If the age is greater than or equal to 18, display the message "You are eligible to vote."
# Otherwise, display the message "You are not eligible to vote yet."

def age_vote():
    age = int(input("Enter your age:"))
    if age > 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote yet.")

age_vote()

# היה ממש קל פתרתי לבד