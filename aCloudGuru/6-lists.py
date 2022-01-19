#!/bin/python3

my_list = [1, 2, 3, 4]

print(my_list)

print(my_list[2])
# 3

print(len(my_list)) # lenght of list

print(my_list[0:2]) # it is named slicing

print(my_list[::2]) # step of 2

my_list[0] = "a"
print(my_list)

my_list[0:2] = [] # remove 2 
print(my_list)

print(my_list.pop()) #return last




