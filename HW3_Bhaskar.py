# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 18:32:50 2022

@author: Bhaskar Teja Ulichi [101127292]
"""
################################################################################################
############################ HOMEWORK CHAPTER 3 PART 2 ##########################################
################################################################################################
#HW 3.9) Implement function reverse_string() that takes as input a string and returns the ######
#string with its characters reversed.
#>>> reverse_string('chad')
#'dahc'
#>>> reverse_string('birger')
#'regrib'

def reverse_string(words):
    'returns the input string in reverse order'
    empty = ""
    for x in words:
        empty = x + empty
    return empty        
   
##############################################################################################    
   
#HW 3.10) Implement function pay() that takes as input two arguments: an hourly wage and the#
#number of hours an employee worked in the last week. Your function should compute and
#return the employee’s pay. Any hours worked beyond 40 is overtime and should be paid at
#1.5 times the regular hourly wage.
#>>> pay(10, 35)
#350
#>>> pay(10, 45)
#475.0

def pay(w,h):
    'computes and returns the employee pay'
    if h>40:
        wage = (w*40)+(1.5*w*(h-40))
    else:
        wage = w*h
    return wage

#############################################################################################
#HW 3.11) The probability of getting n heads in a row when tossing a fair coin n times is 2^-n 
#Implement function prob() that takes a nonnegative integer n as input and returns the
#probability of n heads in a row when tossing a fair coin n times.
#>>> prob(1)
#0.5
#>>> prob(2)
#0.25  

def prob(n):
    'returns the probability of n heads in a row when tossing a fair coin n times'
    if n>=0:
        probability = 2**-n
        return probability
    print("Enter a non-negative integer")

##############################################################################################
#HW 3.12) Implement function points() that takes as input four numbers x1, y1, x2, y2 that
#are the coordinates of two points (x1; y1) and (x2; y2) in the plane. Your function should
#compute:
#• The slope of the line going through the points, unless the line is vertical
#• The distance between the two points
#Your function should print the computed slope and distance in the following format. If the
#line is vertical, the value of the slope should be string 'infinity'. Note: Make sure you
#convert the slope and distance values to a string before printing them.
#>>> points(0, 0, 1, 1)
#The slope is 1.0 and the distance is 1.41421356237
#>>> points(0, 0, 0, 1)
#The slope is infinity and the distance is 1.0        

def points(x1,y1,x2,y2):
    'Computes and prints the slope and distance between two points'
    import math
    num = y2-y1
    den = x2-x1
    str1 = 'The slope is'
    str2 = 'infinity'
    str3 = 'and the distance is'
    if den !=0:
        slp = num/den
        dis = math.sqrt((num)**2 + (den)**2)        
        print(str1,str(slp),str3,str(dis))
    else:
        dis = math.sqrt((num)**2 + (den)**2)
        print(str1,str2,str3,str(dis))


#Alternative Solution

def points(x1,y1,x2,y2):
    'Computes and prints the slope and distance between two points'
    import math
    num = y2-y1
    den = x2-x1
    if den !=0:
        slp = str(num/den)
        dis = str(math.sqrt((num)**2 + (den)**2))
        print('The slope is',slp,'and the distance is',dis)
    else:
        dis = str(math.sqrt((num)**2 + (den)**2))
        print('The slope is infinity and the distance is',dis)

#############################################################################################
#HW 3.13) Write function lastF() that takes as input two strings of the form 'FirstName' and
#'LastName', respectively, and returns a string of the form 'LastName, F.'. (Only the
#initial should be output for the first name.)
#>>> lastF('Chad', 'Birger')
#'Birger, C.'         

def lastF(first,last):
    name = last + ',' + ' ' + first[0] + '.' 
    return name

#############################################################################################
#HW 3.14) Write function ppsi() that takes as input two numbers price and diameter. #########
#These will represent the price of a circular shaped pizza and the diameter of the pizza. 
#The function should return the price per square inch of the pizza. 
#>>> ppsi(10, 9)
#0.15719006725125467
#>>> ppsi(5, 5)
#0.25464790894703254

def ppsi(price,diameter):
    'Computes and returns the price per square inch of a pizza'
    import math
    piz_area = math.pi*(diameter/2)**2
    price_psi = price/piz_area
    return price_psi
    
############################################################################################
#################################### END OF HOMEWORK #######################################
############################################################################################    
    




        


