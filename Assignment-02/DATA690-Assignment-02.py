#!/usr/bin/env python
# coding: utf-8

# # DATA 690 - Python-Stats-Dataviz 
# 
# ## Assignment 02
# 
# ### Prompts a user to enter 10 integers. If the user enters anything other than integers, remind her that only integers are allowed and let her retry. Don't allow the user to enter more than 10 or less than 10 integers. Display the 10 integers back to the user at the end. Calculate the following statistics from the 10 integers entered:
# 
# - Minimum
# - Maximum
# - Range
# - Mean
# - Variance
# - Standard Deviation
# 
# 
# **Note:**
# 
# - Use the basic Python concepts and methods. Special Python libraries such as statistics, scipy, or numpy are not allowed. You may need to use:
# 
# *loops (finite and/or infinite loop)*
# 
# *break/continue*
# 
# *try/except*
# 
# *input() function*
# 
# *int() function*
# 
# - Implement the solution in the following two different formats:
# 
# A Jupyter Notebook (.ipynb)
# 
# A Python script (.py)
# 
# Your source code should be well formatted and easy to read and understand.
# 
# 
# - Provide good comments/documentations:
# 
# Use both Markdown and comments in the Jupyter Notebook.
# Use comments in the Python script.
# Your user prompts, use inputs and output displays should be nicely formatted when users run your program.
# 
# - Create a subfolder named "Assignment-02" in your GitHub repository and upload the two files to the subfolder.
# 
# - Copy your GitHub repository URL to your assignment submission in Blackboard. No files should be uploaded to the BB.

# In[1]:


# DECLARING AN EMPPTY LIST 
list_of_integers=[]
# RUNNING AN FOR LOOP WITH 10 AS RANGE
for i in range(10):
    try:
# USING INPUT TAG, ALLOWING USER TO ENTER 10 INTEGERS
        user_input=int(input("Please enter 10 integers:"))
#IF THE USER ENTERS ANY NON INTEGER-VALUES IT WILL GO INTO THIS EXCEPT BLOCK AND PRINT AN VALIDATING MESSAGE
    except ValueError:
        print("Invalid integer entered. Please enter 10 integers.")
        user_input=int(input("Please enter your integers: "))
# USING THE LIST DECLARED ABOVE TO SAVE ALL THE ENTERED INTEGER VALUES
    list_of_integers.append(user_input)
# DISPLAYING ALL THE INTEGER VALUES IN THE LIST 
print("The 10 integer values enteredare ", list_of_integers)


# ### Calculated the statistics mentioned in the question from the 10 integers entered by user.

# In[2]:


min_val = list_of_integers[0]
for i in range(len(list_of_integers)):
    if list_of_integers[i] < min_val:  
        min_val = list_of_integers[i]
print("The Minimum Value among the 10 integers entered is",min_val)


# In[3]:


max_val = list_of_integers[0]
for i in range(len(list_of_integers)):
    if list_of_integers[i] > max_val:  
        max_val = list_of_integers[i]
print("The Maximum Value among the 10 integers entered is",max_val)


# In[4]:


range = max_val - min_val
print("The Range of the 10 integers entered is",range)


# In[5]:


total = 0
for i in list_of_integers:
    total+=i
mean = total/len(list_of_integers)
print("The Mean Value of the 10 integers entered is",mean)


# In[6]:


total=0
for i in list_of_integers:
    total = total + (i - mean) ** 2
variance = total/len(list_of_integers)
print("The Varience of the 10 integers entered is",variance)


# In[7]:


sd  = variance ** 0.5
print("The Standard Deviation of the 10 integers entered is",sd)

