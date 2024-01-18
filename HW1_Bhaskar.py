# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 19:58:52 2022

@author: Bhaskar Teja Ulichi {101127292}
"""
################################## CHAPTER 2 HOMEWORK EXERCISES #############################################################
#############################################################################################################################
## PROBLEM 2.11 #############################################################################################################

### Write Python expressions corresponding to these statements   ############################################################

#(a) The sum of negative integers −7 through −1 #
-7-6-5-4-3-2-1 

#(b) The average age of a group of kids at a summer camp given than 17 are 9 years old, 24 are 10 years old, 21 are 11 yrs#
# old, and 27 are 12 years old #
(17*9+24*10+21*11+27*12)/(17+24+21+27) ########## Weighted Average has been computed. If x = ages and f = number of kids of corresponding age, then average age = Σf*x/Σx ########

#(c) 2 to the power −20 #
2**-20

#(d) The number of times 61 goes into 4356 #
4356//61

#(e) The remainder when 4365 is divided by 61#
4365%61

###########################################################################################################################
## PROBLEM 2.14 #############################################################################################################
# Start by executing s = 'goodbye' ###### Then write a Boolean expression that checks whether:###############################

s='goodbye'

# (a) The first character of string s is 'g'  #
s[0]=='g'

# (b) The seventh character of s is 'g' #
s[6]=='g'  #### No of characters in s = 7. So, index of the 7th character is 7-1 = 6 ####################################   

#(c) The first two characters of s are 'g' and 'a' #
s[0]=='g'and s[1]=='a'

#(d) The next to last character of s is 'x' #
s[-2]=='x'

#(e) The middle character of s is 'd' #
midS=int((len(s)+1)/2) # As the no. of characters in s is odd, the middle character lies in (n+1)/2 th place. A Variable midS has been assigned for the middle character of S. midS has been explicitly defined as an integer as it is required to compute the index number of the middle character in the next step ##########################
s[midS-1]=='d'  ###  The index of midS is midS-1 #######

#(f) The first and last characters of string s are equal #
s[0]==s[-1]

#(g) The last four characters of string s match the string 'tion'#
s[-4]+s[-3]+s[-2]+s[-1]=='tion' ### Concatenation of last four digits has been verified with the given string ############

###########################################################################################################################
# PROBLEM 2.16 ############################################################################################################
# Write the corresponding Python assignment statements ###################################################################
# (a) Assign 6 to variable a and 7 to variable b. #
a,b=6,7

#(b) Assign to variable c the average of variables a and b #
c=(a+b)/2

#(c) Assign to variable inventory the list containing strings 'paper', 'staples', and 'pencils'#
inventory=['paper','staples','pencils']

#(d) Assign to variables first, middle and last the strings 'John', 'Fitzgerald', and 'Kennedy'#
first,middle,last='John','Fitzgerald','Kennedy'

#(e) Assign to variable fullname the concatenation of string variables first, middle, and last. Make sure you incorporate blank spaces appropriately.#
fullname = first + ' ' + middle + ' ' + last

###########################################################################################################################
## PROBLEM 2.17 ##########################################################################################################
# Write Boolean expressions corresponding to the following logical statements and evaluate the expressions:######################################## 
#(a) The sum of 17 and −9 is less than 10. #
(17-9)<10

#(b) The length of list inventory is more than five times the length of string fullname. #
len(inventory)>5*len(fullname)

#(c) c is no more than 24.#
c<=24 # Not more than can be interpreted as less than or equal to ####

# (d) 6.75 is between the values of integers a and b. ##
a<6.75 and 6.75<b #Here if 6.75 is between a and b, then it should satisfy the rule a<6.75<b.The same rule has been written as two seperate expressions with a boolean operator 'and' #   

#(e) The length of string middle is larger than the length of string first and smaller than the length string last ##
len(middle)>len(first) and len(middle)<len(last)

#(f) Either the list inventory is empty or it has more than 10 objects in it. ############
len(inventory) == 0 or len(inventory)>10

#########################################################################################################################
#PROBLEM 2.22 ##########################################################################################################
# The range of a list of numbers is the largest difference between any two numbers in the list. ######################
#Write a Python expression that computes the range of a list of numbers lst. If the list lst is, say, [3, 7, -2, 12] ####
lst=[3,7,-2,12] #Before computing the range, the given list has been assigned to the variable 'lst' #
max(lst)-min(lst) # The largest difference between any two numbers in a list is the difference between the max value and min value of the list, which is the formula for range computation ####

##########################################################################################################################
# PROBLEM 2.29 ###########################################################################################################
# Add one or more pairs of parentheses to each expression so that it evaluates to True. For each expression, explain in what order the operators were evaluated ##################################
#(a) 0 == 1 == 2 #
0 == (1 == 2) ### Here a parantheses has been used for the boolean expression 1 ==2. So, at first the expression '1 == 2' is evaluated.The expression results in False which is technically '0'. Now, the comparison operator 'is 0 equal to 0' is evaluated which turns out to be true #####
  
#(b) 2 + 3 == 4 + 5 == 7 #
2 + (3 == 4) + 5 == 7 # Here a parantheses has been used for the expression 3 == 4. So, the order of operations is as follows: At first, 3==4 is evaluated. As it is false, the result tends to be '0'. Nowm the arithmetic operation 2 + 0 + 5 is evaluated. The result is 7. Finally, 7 == 7 is evaluated, which is true ####

#(c) 1 < -1 == 3 > 4#
(1 < -1) == (3 > 4) #Here a pair of parantheses were used for comparison operations (1 < -1) and (3 > 4). Each of these operations are evaluated first. So, the results are false and false. Now, the operation Flase == False is executed, which is true. #

#############################################################################################################################
###################################################### END OF HOMEWORK #######################################################
#############################################################################################################################