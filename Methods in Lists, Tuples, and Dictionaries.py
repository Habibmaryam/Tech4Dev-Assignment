#!/usr/bin/env python
# coding: utf-8

# ## List methods 1-7

# In[15]:


# Adding a single data to a list
states = ['Abia', 'Umahia', 'Adamawa', 'Yola', 'Akwa Ibom', 'Uyo', 'Anambra']
states.append('Bauchi')
print(states)


# In[22]:


# Add multiple string data to a list

states = ['Abia', 'Umahia', 'Adamawa', 'Yola', 'Akwa Ibom', 'Uyo', 'Anambra']
states.extend(['Bauchi','Cross River', 'Delta'])
print(states)


# In[12]:


# indexing the position of an entry in a list
index = states.index('Yola')
print(index)


# In[14]:


# print lists in reversed order
states.reverse()
print(states)


# In[32]:


# Ranges of index
print(states[1:5])


# In[16]:


# Check if an item still exists

if 'Kano' in states:
    print('Yes, Kano is in states')
else:
    print('Kano is not in states')


# In[21]:


distance = [20, 30, 50, 70, 90, 88, 44]
max_val = max(distance)
print(max_val)


# # Tuples 8-12

# In[23]:


# defining a tuple
grades = (20, 30, 50, 70, 90, 88, 44)
print(grades)


# In[36]:


# using the len function to count the number of items in a tuple
len(grades)


# In[40]:


# changing an item in a tuple

grades = (20, 30, 50, 70, 90, 88, 44)
y = list(grades)
y[3] = 75
grades = tuple(y)
print(grades)


# In[42]:


# joining three tuples together

score = (1.1, 2.2, 3.3, 4.4, 5.5, 6.6)
age = (5, 6, 7, 7.5, 8, 9, 8.5)
grade_level = (1, 2, 3, 4, 5, 6, 7, 8)

data = (score + age + grade_level)
print(data)


# In[45]:


# Multiply tuples by 2
age = (5, 6, 7, 7.5, 8, 9, 8.5)
answer = age*2
print(answer)


# # Dictionaries 13-20

# In[1]:


# I will be using the below dictionary to show the dictionary methods in python

first_dict = {'Name': 'Tech4dev', 'Co-founder':'Diwura Oladepo',
              'Type': 'Digital skills empowerment', 'Age': '10', 'Price': 'Free', 'Study style': 'Online'}


# In[3]:


# Using the get() dictionary method to retrieve a specified key

Name = first_dict.get('Name')
print(Name)


# In[4]:


# Using the items() method to retrive all items in a dictionary in a tuple data ormat

items = first_dict.items()
print(items)


# In[5]:


# Using the keys() method to retrieve all th keys in a dictionary in a tuple data format

keys = first_dict.keys()
print(keys)


# In[6]:


# Using the values() method to retrieve all the values in a dictionary in a tuple data format

values = first_dict.values()
print(values)


# In[8]:


# Using the pop() menthod to remove a key-value pair in a dictionary

first_dict.pop('Age')
print(first_dict)


# In[11]:


# using the update() method to add a key-value item to a dicionary

first_dict.update({'Program leads':'Blessing Ashi'})
print(first_dict)


# In[12]:


# using the copy() method to copy a dictionary into a specified variable

another_dict = first_dict.copy()
print(another_dict)


# In[13]:


# using the clear() method to clear all the entries in a dictionary

first_dict.clear()
print(first_dict)


# # THE END
