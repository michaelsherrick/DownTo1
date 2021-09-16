#!/usr/bin/env python
# coding: utf-8

# # Determine the Number of Steps Required to get Down to 1
# #### For any number, i, the next number in the sequence is *i/2* if i is even or *3i+1* if i is odd

# In[1]:


for i in range(5, 21):                 # Iterate over the numbers from 5 to 20
    num_steps = 0                      
    curr_val = i                       # Current value in the sequence begins at i
    
    while(curr_val != 1):              # Continue looping the sequence until it reaches 1
        if(curr_val % 2 == 0):         # Check if the current value is even and 
            curr_val /= 2              # divide by 2 if True
        else:
            curr_val = 3*curr_val+1    # Otherwise multiply by 3 and add 1
        num_steps += 1                 # Increment the number of steps taken
    
    # Print each number followed by the number of steps taken for it to reach 1
    print("{:2d}: {:2d} steps".format(i, num_steps))

