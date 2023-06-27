# שאלה 15

#Write a function called calculate_average that takes a list of numbers as an argument and returns the average value.
# נעזרתי באינטרנט

list = [5, 6, 7, 4, 5, 6, 1, 1]
def calculate_average(list):
    total= sum(list)
    a =len(list)
    average = total / a
    print(total,":",a,"=",average)

calculate_average(list)