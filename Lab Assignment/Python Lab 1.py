#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1


# In[2]:


print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# In[3]:


#Question 2


# In[13]:


number = int(input("Enter a number: "))
if number > 0:
    print("positive")
if number < 0:
    print("negative")
if number == 0:
    print("zero")


# In[14]:


#Question 3


# In[55]:


x = int(input("input an x value: "))
y = int(input("input a y value: "))
if x > y:
    print("a. x is greater than y")
if y > x:
    print("a. y is greater than x")
if (x % 2) == 0:
    print("b. x is an even number") 
else:
    print("b. x is an odd number") 
if (y % 2) == 0:
    print("b. y is an even number") 
else:
    print("b. y is an odd number")
partc = "c. "
divide = ((x+y)/(x-y))
c = f'{partc}{divide}'
print(c)
partd = "d. "
exponent = ((x-y)**3)
d = f'{partd}{exponent}'
print(d)


# In[56]:


#Question 4


# In[77]:


inp =input("What's the time?")
hours, mins = inp.split(":")
if int(hours)<10:
    print("Good morning")
elif 12<= int(hours)<15:
    print("soon time for lunch")
elif 15<=int(hours)<=19:
    print("Good evening")
else:
    print("Goodnight")


# In[ ]:


#Sources
https://stackoverflow.com/questions/53566941/how-do-i-ask-the-user-to-input-time
https://stackabuse.com/converting-strings-to-datetime-in-python/
https://www.codegrepper.com/code-examples/python/24+hour+time+format+in+python
https://www.programiz.com/python-programming/datetime/current-time

