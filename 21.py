# 1. Create a function that takes two integers as parameters and returns their sum.
# מצורף 2 דרכים לפתרון עדיף את האופציה השנייה כי יהיה ניתן לשנות את המספרים ללא תלות בפונקציה
def takes_two_numbers():
    num_1 = 2
    num_2 = 4
    results = num_1 + num_2
    return results


print(takes_two_numbers())


def takes_two_numbers(num_1, num_2):
    results = num_1 + num_2
    return results


print(takes_two_numbers(3, 5))


# 2. Write a function that checks if a given string is empty and returns a boolean value.
def checks_if_string(inpot_string):
    if inpot_string == "":
        return True
    else:
        return False


input_string_1 = ""
input_string_2 = "hii"
print(checks_if_string(input_string_1))
print(checks_if_string(input_string_2))


# 3. Create a function that converts a floating-point number to an integer.
# מידה ונרצה FLOAT נשנה את ה INT ל FLOAT
def converts_float(num):
    results = int(num)
    return results


num = 3.34567
print(converts_float(num))


# 4. Write a function that accepts a list of integers and returns the average of those numbers.
def average_number(my_list):
    total = sum(my_list)
    amount = len(my_list)
    average = total / amount
    return average


aa_list = [2, 54, 5, 76, 4, 2, 7, 4]
print(average_number(aa_list))


# 5. Create a function that takes a string as input and returns the string in uppercase.
def returns_upper():
    name = str(input("Write your name:"))
    up = name.upper()
    return up


print(returns_upper())


# 6. Write a function that checks if a given integer is even and returns a boolean value.
def integer_is_even(num_3, num_4):
    if num_3 == num_4:
        return True
    else:
        return False


num_3 = 4
num_4 = 2
print(integer_is_even(num_3, num_4))


# 7. Create a function that calculates the length of a given list and returns the result.

def calculates_the_length(my_list):
    length = len(my_list)
    return length


my_1_list = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 2, 2]
print(calculates_the_length(my_1_list))


# 8. Write a function that concatenates two strings and returns the combined string.

def concatenates_two_strings(my_1_string, my_2_string):
    my_first = str(my_1_string)
    my_secand = str(my_2_string)
    return my_first + ' ' + my_secand


my_1 = "maor"
my_2 = 6
print(concatenates_two_strings(my_1, my_2))


# Create a function that takes a list of floating-point numbers as input and returns the sum of those numbers.
def returns_sum(my_list):
    amount = sum(my_list)
    return amount


w_list = [145.4, 123.435, 235.57, 56.2356]
print(returns_sum(w_list))


# 10. Write a function that checks if a given string contains a specific character and returns a boolean value.
def specific_character(character, input_string):
    if character in input_string:
        return True
    else:
        return False


ma = "maor"
amm = "a"
print(specific_character(amm, ma))


# 11. Create a function that finds the maximum value in a given list of integers and returns it.
def maximum_value(my_list):
    return max(my_list)


aq_list = [1, 2, 3, 4, 5, 32, 21, 1, ]
print(maximum_value(aq_list))


# 12. Write a function that takes an integer as input and returns its absolute value.
def absolute_value(number):
    value = abs(number)
    return value


num_5 = -8
print(absolute_value(num_5))


# 13. Create a function that checks if a given list is empty and returns a boolean value.
def list_is_empty(my_list):
    if my_list == []:
        return True
    else:
        return False


my_4_list = [1, 31, 2]
print(list_is_empty(my_4_list))


# 14.  Write a function that removes all occurrences of a specified character from a given string
# and returns the modified string.
# פתרתי ואני רוצה שנשב להבין מה הבעיה
def removes_all_occurrences(my_list, occurrences):  # לברר למה אי אפשר לשים REMOVE במקום REPLACE
    return my_list.replace(occurrences, "")


my_list = "maor is avidan"
occurre = "a"
print(removes_all_occurrences(my_list, occurre))

'''def removes_all_occurrences(my_list, occurrences):
    return my_list.remove(occurrences)


qw = ["maor is avidan"]
wwq = "a"
print(removes_all_occurrences(qw, wwq))
'''


# 15. Create a function that takes two lists as parameters and concatenates them into a single list,
# which is then returned.
def concatenates_lists(list_1, list_2):
    num_list = list_1 + list_2
    return num_list


list_12 = ["maor is age"]
list_2 = [34, 3, 2, 1]
print(concatenates_lists(list_12, list_2))


# 16. Write a function that checks if a given floating-point number is positive and returns a boolean value.
def floating_point_positive(num):
    return num > 0


num1 = -0.1
num2 = 0.1
print(floating_point_positive(num1))
print(floating_point_positive(num2))


# 17. Create a function that sorts a given list of integers in ascending order and returns the sorted list.
# נעזרתי באינטרנט למצוא את SORTED
def sorts_given_list(my_list):
    sort = sorted(my_list)
    return sort


my_list_31 = [1, 3, 24, 324, 56, 8, 98, 1, 32, ]
print(sorts_given_list(my_list_31))


# 18. Write a function that takes a string as input and counts the number of vowels in it, returning the count.

def returning_the_count(my_string, count):
    num = 0
    for i in my_string:
        if i in count:
            num += 1
    return num


my_string_21 = "hii how are you"
counts = "y"

print(returning_the_count(my_string_21, counts))


# 19.Create a function that appends a given integer to the end of a list and returns the modified list.
def appends_integer(integer, my_list):
    my_list.append(integer)
    return my_list


integer_3 = 7
my_list_65 = [3, 2, 1]
print(appends_integer(integer_3, my_list_65))


# 20. Write a function that checks if a given string is a palindrome (reads the same forwards and backwards) and returns a boolean value.
def forwards_and_backwards(string):
    revers = string[::-1]
    if revers == string:
        return True
    else:
        return False
stri= "wow"
print(forwards_and_backwards(stri))