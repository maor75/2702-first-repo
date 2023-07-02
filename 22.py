# 1. Given a list [10, 20, 30, 40, 50], calculate the sum of all the numbers and print it.
# If the sum is greater than 100, print "Sum is greater than 100," otherwise print "Sum is not greater than 100."

def sum_list(sum_of_the_list):
    total = sum(sum_of_the_list)
    if total >= 100:
        print("Sum is greater than 100")
    else:
        print("Sum is not greater than 100.")


the_lists = [10, 20, 30, 40, 50]
sum_list(the_lists)

# 2. Create a tuple with the elements "red," "green," and "blue". Print the length of the tuple.
# If the length is equal to 3, print "Tuple has 3 elements," otherwise print "Tuple does not have 3 elements."

color_tuple = ("red", "green", "blue")
if len(color_tuple) == 3:
    print("Tuple has 3 elements")
else:
    print("Tuple does not have 3 elements.")

# 3. Given two sets {1, 2, 3, 4} and {3, 4, 5, 6}, find the union of the sets and print the result.
# if the resulting set contains the number 5, print "Union contains 5," otherwise print "Union does not contain 5."

# unionאשמח לחזור על זה להבין מה זה
set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
union_set = set_1.union(set_2)
if 5 in union_set:
    print("Union contains 5")
else:
    print("Union does not contain 5.")


# 4. Define a function called is_palindrome that takes a string as input and returns True
# if it is a palindrome (reads the same forwards and backwards) and False otherwise.
# Print the result of calling the function with the argument "racecar". If the result is True, print "It is a palindrome,"
# otherwise print "It is not a palindrome."

def get_string_from(is_palindrome):
    if is_palindrome == is_palindrome[::-1]:
        return True
    else:
        return False


def racecar(is_palindrome):
    if get_string_from(is_palindrome):
        print("It is a palindrome")
    else:
        print("It is not a palindrome.")


# 5.Create a list of numbers and print the smallest number in the list. If the list is empty, print "List is empty."
group_of_numbers = [1, 2, 3, 4, 5]

if group_of_numbers == []:
    print("List is empty.")
else:
    smallest = min(group_of_numbers)
    print(smallest)

# 6. Create a set with the elements "apple," "banana," and "cherry". Check if "banana" is present in the set and print the result.
# If "banana" is in the set, print "Banana is present," otherwise print "Banana is not present."

fruits_set = {"apple", "banana", "cherry"}
if "banana" in fruits_set:
    print("Banana is present")
else:
    print("Banana is not present.")


# 7. Define a function called calculate_average that takes a list of numbers as input and returns the average value.
# Print the result of calling the function with the list [4, 6, 8, 10, 12].
# If the result is greater than 10, print "Average is greater than 10," otherwise print "Average is not greater than 10."
def calculate_average(input_list):
    numbers_in_list = sum(input_list)
    average_value = len(input_list)
    average_number = numbers_in_list / average_value
    return average_number


def greater_than_10(result):
    if calculate_average(result) > 10:
        print("Average is greater than 10")
    else:
        print("Average is not greater than 10.")


result_list = [4, 6, 8, 10, 12]
greater_than_10(result_list)


# 8. Given a tuple (1, 2, 3, 4, 5), convert it into a list and print the list. If the length of the list is greater than 5,
# print "List has more than 5 elements," otherwise print "List does not have more than 5 elements."

def Given_a_tuple(the_tuple):
    my_list = list(the_tuple)
    if len(my_list) >= 5:
        print("List has more than 5 elements")
    else:
        print("List does not have more than 5 elements.")


# 9. Create a set with the elements 1, 2, 3, and 4. Add the number 5 to the set. Print the updated set.
# If the set contains the number 5, print "Set contains 5," otherwise print "Set does not contain 5."
numbers_set_1 = {1, 2, 3, 4}
numbers_set_1.add(5)
all_numbers_set = numbers_set_1
if 5 in all_numbers_set:
    print("Set contains 5")
else:
    print("Set does not contain 5.")


# 10. Define a function called count_vowels that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string.
# Print the result of calling the function with the argument "Hello, world!". If the count is greater than 0,
# print "String contains vowels," otherwise print "String does not contain vowels."

def count_vowels(the_string):
    return len(the_string)


def result_of_the_string(vowels):
    if count_vowels(vowels) > 0:
        print("String contains vowels")
    else:
        print("String does not contain vowels.")


result_of_the_string(vowels="")

# 11. Create a list of names and print the number of names that start with the letter "A".
# If there are no names starting with "A", print "No names start with A."

name_list = ["Maor", "Tom", "Or", "Adam", "Moshe"]
name_start_A = 0
for name in name_list:
    if name.startswith("A"):
        name_start_A = +1
        print(name_start_A)
if name_start_A == 0:
    print("No names start with A.")

# 12. Create a tuple with the elements "apple," "banana," and "cherry". Add the element "orange" to the tuple. Print
# the updated tuple. If "orange" is in the tuple, print "Orange is present," otherwise print "Orange is not present."


fruits_tupel = ("apple", "banana", "cherry")
new_fruits_tupel = fruits_tupel + ("orange",)

if "orange" in new_fruits_tupel:
    print("Orange is present")
else:
    print("Orange is not present.")
