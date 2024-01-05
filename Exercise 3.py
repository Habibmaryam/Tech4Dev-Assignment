#!/usr/bin/env python
# coding: utf-8

# # Software Development – List, Tuple

# In[1]:


# Finding the maximum value in a list
my_list = [2, 4, 7, 4, 23, 5, 1, 4, 8, 9]

# Find the maximum value
max_value = max(my_list)

# Print the result
print("Maximum value is", max_value)


# In[2]:


# Calculating the average value in a list
my_list2 = [4, 7, 1, 5, 11, 53, 12, 46, 84, 23]

# Calculate the average
average_value = sum(my_list) / len(my_list)

# Print the result
print("Average value is", average_value)


# In[8]:


# printing a list in reverse order
my_list3 = [2,6,7,45,23,53,14,45,89,5]
my_list3.reverse()
print(my_list3)


# In[9]:


# Function to check if each element in the first list is less than the corresponding element in the second list

list1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
list2 = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
def check_lists(list1, list2):
    # Check if the lists are of the same length
    if len(list1) != len(list2):
        return False
    
    # Check if each element in the first list is less than the corresponding element in the second list
    for i in range(len(list1)):
        if list1[i] >= list2[i]:
            return False

    # If all elements pass the condition, return True
    return True

# Example lists
list1 = [2, 4, 7, 4, 23, 5, 1, 4, 8, 9]
list2 = [3, 6, 8, 5, 25, 7, 2, 5, 9, 10]

# Check and print the result
result = check_lists(list1, list2)
print(result)


# In[1]:


# Write a program that accepts a list of integers and two indexes and swaps the elements at those indexes

def swap_elements(lst, index1, index2):
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        lst[index1], lst[index2] = lst[index2], lst[index1]
        return lst
    else:
        print("Invalid indexes. Please enter valid indexes within the range of the list.")
        return None

# Example usage:
input_list = [1, 2, 3, 4, 5]
index1 = 1
index2 = 3

result = swap_elements(input_list, index1, index2)

if result is not None:
    print(f"List after swapping elements at indexes {index1} and {index2}: {result}")


# In[11]:


# Function to concatenate two lists
def concatenate_lists(list1, list2):
    # Concatenate the two lists
    result_list = list1 + list2
    return result_list

# define lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 10]

# Concatenate lists and print the result
result = concatenate_lists(list1, list2)
print("Concatenated list:", result)


# In[1]:


# that accepts a list of integers and an integer value as its parameters and prints the last index at which the value occurs in the list. The program should print –1 if the value is not found

def last_index_of_value(lst, value):
    last_index = -1
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            last_index = i
            break
    print(f"The last index of {value} in the list is: {last_index}")

# Example usage
input_list = [74, 85, 102, 99, 101, 85, 56]
input_value = int(input("Enter an integer value to search for: "))

last_index_of_value(input_list, input_value)


# In[2]:


# Write a program that prints the range of values in a list of integers
def calculate_range(input_list):
    # Find the minimum and maximum values in the list
    min_value = min(input_list)
    max_value = max(input_list)

    # Calculate the range
    value_range = max_value - min_value + 1

    print(f"The range of values in the list is: {value_range}")

# Example usage
input_list = [36, 12, 25, 19, 46, 31, 22]
calculate_range(input_list)


# In[3]:


# Write a program that accepts a list of integers, a minimum value, and a maximum value and prints the count of how many elements from the list fall between the minimum and maximum (inclusive).

def count_elements_in_range(input_list, min_value, max_value):
    count = 0

    for element in input_list:
        if min_value <= element <= max_value:
            count += 1

    print(f"The count of elements between {min_value} and {max_value} (inclusive) is: {count}")

# Example usage
input_list = [14, 1, 22, 17, 36, 7, -43, 5]
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))

count_elements_in_range(input_list, min_value, max_value)


# In[4]:


# Write a program that accepts a list of real numbers and prints true if the list is in sorted (nondecreasing) order and false otherwise.

def is_sorted(input_list):
    for i in range(len(input_list) - 1):
        if input_list[i] > input_list[i + 1]:
            return False
    return True

# Example usage
list1 = [16.1, 12.3, 22.2, 14.4]
list2 = [1.5, 4.3, 7.0, 19.5, 25.1, 46.2]

print(f"Is list1 sorted? {is_sorted(list1)}")
print(f"Is list2 sorted? {is_sorted(list2)}")


# # THE END
