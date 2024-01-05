#!/usr/bin/env python
# coding: utf-8

# ## 1. Write a program to produce the following output using for loop

# In[40]:


# Define the number of rows
num_rows = 9

# Outer loop for each row
for i in range(num_rows):
    # Check if it's the first or last row
    if i == 0 or i == num_rows - 1:
        print("+----+")
    else:
        # Check if it's an even or odd row
        if i % 2 == 0:
            print("\\    /")
        else:
            print("/    \\")
            


# # 2. Write a program to produce the following output using for loop

# In[36]:


# Number of rows
num_rows = 5

# Number of columns
num_columns = 10

# Using nested for loop to print the pattern
for row in range(num_rows):
    for col in range(num_columns):
        print('*', end='')
    print()  # Move to the next line after each row


# # 3. Complete the code for the following for loop:
# 

# In[2]:


# a.
for x in range(1,7):
    print(x)


# In[8]:


# b. 

number = 2

for i in range(1, 7):
    result = number * i
    print(f"{result}")


# In[14]:


# c. 

number = 15

for i in (-11,4,19,34,49,64):
    result = number + i
    print(f"{result}")


# In[12]:


# d. 

number = -10

for i in (40,30,20,10,0, -10):
    result = i + number 
    print(f"{result}")


# In[17]:


# e

number = -4

for i in (-3,1,5,9,13,17):
    result = i + number 
    print(f"{result}")


# In[22]:


# f
number = -3

for i in (100,97,94,91,88,85):
    result = i + number 
    print(f"{result}")


# In[27]:


number = -18

for i in (14,32,50,68,86,104):
    result = i + number 
    print(f"{result}")


# ## 4. Write a program to produce the following output using for loops.Then use a class constant to make it possible to change the number of lines in the figure.

# In[3]:


# Write a program to produce the following output using for loops
class Figure:
    # Class constant to control the number of lines
    NUM_LINES = 7

    def print_figure(self):
        for i in range(1, self.NUM_LINES + 1):
            for j in range(i):
                print(i, end="")
            print()

# Create an instance of the Figure class and print the figure
figure_instance = Figure()
figure_instance.print_figure()


# ## 5. Write a method named pay that accepts two parameters: a real number for a TA's salary, and an integer for the number of hours the TA worked this week. The method should return how much money to pay the TA. For example, the call

# In[27]:


# Write a method named pay that accepts two parameters: a real number for a TA's salary, and an integer for the number of hours the TA worked this week
def pay(salary, hours_worked):
    normal_hours = 8
    overtime_rate = 1.5

    if hours_worked <= normal_hours:
        total_pay = salary * hours_worked
    else:
        normal_pay = salary * normal_hours
        overtime_pay = salary * overtime_rate * (hours_worked - normal_hours)
        total_pay = normal_pay + overtime_pay

    return total_pay

# Example usage:
result = pay(5.50, 6)
print(result)  # Output: 33.0

result = pay(4.00, 11)
print(result)  # Output: 50.0


# # 6. Write a similar method named area that takes as a parameter the radius of a circle and that returns the area of the circle

# In[28]:


import math

def area(radius):
    return math.pi * radius ** 2

# Example usage:
result = area(2.0)
print(result)  


# # 7. Modify the code to use a input to prompt the user for the values of low and high.

# In[32]:


low = int(input('Low? '))
high = int(input('High? '))
sum = 0
for i in range(low,high):
    sum += i
print("sum = " , sum)


# # 8. Write a program using while loop that prompts the user for numbers until the user types 0, then outputs their sum.

# In[34]:


# Initialize sum to 0
sum_of_numbers = 0

# Prompt user for numbers until 0 is entered
while True:
    # Get user input
    user_input = float(input("Enter a number (or 0 to exit): "))

    # Check if the user wants to exit
    if user_input == 0:
        break

    # Add the entered number to the sum
    sum_of_numbers += user_input

# Output the sum
print("Sum of the entered numbers:", sum_of_numbers)


# # 9. Write a program using while loop that prompts the user for numbers until the user types -1, then outputs their sum

# In[35]:


# Initialize sum to 0
sum_of_numbers = -1

# Prompt user for numbers until -1 is entered
while True:
    # Get user input
    user_input = float(input("Enter a number (or -1 to exit): "))

    # Check if the user wants to exit
    if user_input == -1:
        break

    # Add the entered number to the sum
    sum_of_numbers += user_input

# Output the sum
print("Sum of the entered numbers:", sum_of_numbers)


# # 10. Write a method named repl that accepts a String and a number of repetitions as parameters and returns the String concatenated that many times. For example, the call repl("hello", 3) returns "hellohellohello". If the number of repetitions is 0 or less, an empty string is returned

# In[39]:


def repl(input_string, repetitions):
    if repetitions <= 0:
        return ""
    
    result = input_string * repetitions
    return result

# Example usage:
result = repl("hello", 3)
print(result)  

result = repl("example", 0)
print(result)  


# # 11. Write a method called printRange that accepts two integers as arguments and prints the sequence of numbers between the two arguments, separated by spaces

# In[56]:


def printRange(start, end):
    if start < end:
        for num in range(start, end + 1):
            print(num, end=" ")
    elif start > end:
        for num in range(start, end - 1, -1):
            print(num, end=" ")
    else:
        print(start)

# Examples
printRange(2, 7)
print()  # Print an empty line for separation
printRange(19, 11)
print()
printRange(5, 5)


# # 12. Write a method named smallestLargest that asks the user to enter numbers, then prints the smallest and largest of all the numbers typed in by the user

# In[57]:


def smallestLargest():
    num_of_numbers = int(input("How many numbers do you want to enter? "))

    # Ensure at least one number is entered
    while num_of_numbers <= 0:
        print("Please enter a valid number greater than 0.")
        num_of_numbers = int(input("How many numbers do you want to enter? "))

    # Initialize variables for smallest and largest
    smallest = float('inf')  # Initialize with positive infinity
    largest = float('-inf')  # Initialize with negative infinity

    # Loop to get user input for each number
    for i in range(1, num_of_numbers + 1):
        num = float(input(f"Number {i}: "))
        smallest = min(smallest, num)
        largest = max(largest, num)

    # Print the smallest and largest numbers
    print(f"Smallest = {smallest}")
    print(f"Largest = {largest}")

# Call the method to execute the program
smallestLargest()


# # 13. Write a method called printAverage that uses a sentinel loop to repeatedly prompt the user for numbers

# In[3]:


def printAverage():
    total = 0
    count = 0

    while True:
        num = float(input("Type a number: "))
        
        if num < 0:
            if count > 0:
                average = total / count
                print(f"Average was {average}")
            else:
                print("No nonnegative numbers entered.")
            break

        total += num
        count += 1

# Call the method to execute the program
printAverage()


# # 14. Write a method named numUnique that takes three integers as parameters and returns the number of unique integers among the three.

# In[2]:


def numUnique(num1, num2, num3):
    unique_numbers = len(set([num1, num2, num3]))
    return unique_numbers

# Example usage:
result = numUnique(18, 3, 4)
print(result)  # Output: 3

result = numUnique(6, 7, 6)
print(result)  # Output: 2


# # 15. A Random object generates pseudo-random numbers. Find out how to use the Random class and write a program that simulates rolling of two 6-sided dice until their combined result comes up as 7

# In[45]:


import random

def roll_dice():
    return random.randint(1, 6)

def simulate_dice_game():
    tries = 0

    while True:
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2

        print(f"{dice1} + {dice2} = {total}")

        tries += 1

        if total == 7:
            print(f"You won after {tries} tries!")
            break

# Run the simulation
simulate_dice_game()


# # THE END
