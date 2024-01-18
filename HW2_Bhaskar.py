# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:21:17 2022

@author: Bhaskar Teja Ulichi [101127292]
"""
################################################################################################
##################### HW 2 CHAPTER 3 HOME WORK EXERCISES #####################################################
###############################################################################################

# HW 3.1) Assume a, b, and c have been defined as shown: a, b, c = 7, 8, 9

a, b, c = 7, 8, 9

# Within your Python script, write if statements that print 'OK' if:

#(a) a is less than b.
if a<b:
    print('OK')
    
#(b) c is less than b.
if c<b:
    print('OK')

#(c) The sum of a and b is equal to c.
if a+b==c:
    print('OK')

#(d) The sum of the squares a and b is equal to c squared.
if a**2 + b**2 == c**2:
    print('OK')
         
###############################################################################################

#HW 3.2) Repeat the previous problem with the additional requirement that 'NOT OK' is printed if the condition is false. 

#(a) a is less than b.
if a<b:
    print('OK')
else:
    print('NOT OK')


#(b) c is less than b.
if c<b:
    print('OK')
else:
    print('NOT OK')
    

#(c) The sum of a and b is equal to c.
if a+b==c:
    print('OK')
else:
    print('NOT OK')


#(d) The sum of the squares a and b is equal to c squared.
if a**2 + b**2 == c**2:
    print('OK')
else:
    print('NOT OK')

###############################################################################################

#HW 3.3) Write a for loop that iterates over a list of numbers of a list named lst3 ###########
#and prints the odd numbers in the list.

#For example, if lst3 is [2, 3, 4, 5, 6, 7, 8, 9], then the numbers 3, 5, 7, and 9 should be printed.

lst3=eval(input('Enter a list of numbers: ')) #Here, as the question suggests an example list, the lst3 has not been defined for the specific list of [2,3,4,5,6,7,8,9]. Instead, the code has been written in such a way that it applies for any numbers list that is feeded into the lst3.#  
for x in lst3:
    if x%2 != 0:
        print(x)
        
####################################################################################################
# HW 3.4) Write a for loop that iterates over a list of numbers named lst34 and prints #############
#the numbers in the list whose square is divisible by 9. ###########################################
#For example, if lst34 is [2, 3, 4, 5, 6, 7, 8, 9] then the numbers 3, 6 and 9 should be printed.###

lst34 = eval(input('Enter a list of numbers: ')) #Here also, as the question suggests an example list, the lst3 has not been defined for the specified list of numbers. Instead, the code has been written in such a way that it applies for any numbers list that is feeded into the lst34#
for x in lst34:
    if x**2 % 9 == 0:
        print(x)
    
#####################################################################################################    

#HW 3.5) Implement a program that requests a list of words from the user and then ###################
#prints each word in the list that is not contained in 'another'. For example:###############
# Enter list of words: ['her','another','him','other','not',’is’]
#him
#is
# are to be printed

lst35 = eval(input('Enter a list of words: ')) #This list has been named as 'lst35'& it takes any list of words that the user inputs for this particular problem#  
for x in lst35:
    if x not in 'another':
        print(x)
        
############################################################################################

#HW 3.6) Implement a program that requests a positive integer n from the user and prints ###
#the first five multiples of n (n*0, n*1, n*2, n*3, and n*4).
# For example:
#Enter n: 9
#0
#9
#18
#27
#36        

p = eval(input('Enter a positive integer: ')) #To distinguish from subsequent problems, the letter 'n' has not been used anywhere in the code. Instead, a unique variable p has been assigned the input value for this particular problem #
lst36 = [p*0,p*1,p*2,p*3,p*4] #A list named 'lst36' has been created that automatically computes and stores the first five multiples of the input value#
for x in lst36:         # A for loop function is used to print the output in desired format #
    if x%p == 0:
        print(x)

# Alternative solution for 3.6 #

p = eval(input('Enter a positive integer: '))
lst36 = [p*0,p*1,p*2,p*3,p*4]
print(lst36[0])
print(lst36[1])
print(lst36[2])
print(lst36[3])
print(lst36[4])


Actual solution

p = eval(input('Enter a positive integer: '))
mul = [0,1,2,3,4]

if p>0:
    for x in mul:
        print(x*p)







################################################################################################
#HW 3.7) Implement a program that requests a positive integer n and prints all the #############
#Positive integer divisors of n. Note: 0 is not a divisor of any integer, and n divides itself##
#For example:
#Enter n: 49
#1
#7
#49


q = eval(input('Enter a positive integer: ')) #To distinguish from other problems, the letter 'n' has not been used anywhere in the code. Instead, a unique variable q has been assigned the input value for this particular problem #
lst37 = range(1,q+1) #The highest divisor of an integer is the integer itself. So, the range of the list of positive divisors of an integer takes till that particular integer. As the range function doesn't include the upper limit, q+1 has been used as the upper limit. 0 has been ignored as it is not a divisor of any integer#
for x in lst37: 
    if q%x == 0:  
        print(x)
#A for loop function has been used to arrive at the solution in the desired format#
#Each value of lst37 is verified as to whether it is a divisor of the specific input value q#

############################################################################################
#HW 3.8) Implement a program that requests four numbers (integer or floating-point) from the 
#user. Your program should compute the sum of the first three numbers and compare the
#sum to the fourth number. If they are equal, your program should print 'Equal' on the
#screen.>>> 
#Enter first number: 5.5
#Enter second number: 3
#Enter third number: 4
#Enter last number: 12.5
#Equal


r1 = eval(input("Enter first number: "))
r2 = eval(input("Enter second number: "))
r3 = eval(input("Enter third number: " ))
r4 = eval(input("Enter last number: "))
if r1+r2+r3 == r4:
    print('EQUAL')

############################################################################################
################################## END OF HOMEWORK #########################################


