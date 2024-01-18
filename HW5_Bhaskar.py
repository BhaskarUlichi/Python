# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:35:35 2022

@author: Bhaskar Teja Ulichi [101127292]
"""
###########################################################################################################################
############################################### HOME WORK - CHAPTER 5 #####################################################
###########################################################################################################################

# 5.12 Implement function test() that takes as input one integer and prints 'Negative', 'Zero', or 'Positive' 
#depending on its value. 
#>>> test(-3)
#Negative 
#>>> test(0) 
#Zero 
#>>> test(3
#) Positive

def test(i):
    if i == 0:
        print('Zero')
    elif i < 0:
        print('Negative')
    else:
        print('Positive')
        
#5.14 Write function mult3() that takes as input a list of integers and prints only the multiples of 3, one per line. 
#>>> mult3([3, 1, 6, 2, 3, 9, 7, 9, 5, 4, 5]) 
#3 
#6 
#3 
#9 
#9

def mult3(lst):
    for x in lst:
        if x%3 == 0:
            print(x)
            

#5.16 Implement function indexes() that takes as input a word (as a string) and a one-character letter (as a string) 
#and returns a list of indexes at which the letter occurs in the word.
#>>> indexes('mississippi', 's') 
#[2, 3, 5, 6] 
#>>> indexes('mississippi', 'i') 
#[1, 4, 7, 10] 
#>>> indexes('mississippi', 'a') 
#[]

def indexes(word,letter):
    lenw = len(word)
    indx = [] 
    for x in range(0,lenw):
        if letter == word[x]:
            indx.append(x)
    return indx

#5.18 Implement function four_letter() that takes as input a list of words (i.e., strings) and returns 
#the sublist of all four letter words in the list.
#>>> four_letter(['dog', 'letter', 'stop', 'door', 'bus', 'dust']) 
#['stop', 'door', 'dust']

def four_letter(lst):
    final = []
    for x in lst:
        if len(x) == 4:
            final.append(x)
    return final
        

#5.23 Write function pay() that takes as input an hourly wage and the number of hours an employee worked in last week. 
#The function should compute and return the employee’s pay. Overtime work should be paid in this way: 
#Any hours beyond 40 but less than or equal 60 should be paid at 1.5 times the regular hourly wage. 
#Any hours beyond 60 should be paid at 2 times the regular hourly wage. 
#>>> pay(10, 35) 
#350 
#>>> pay(10, 45) 
#475.0 
#>>> pay(10, 61) 
#720.0

def pay(wage,hours):
    if hours <= 40:
        salary = wage*hours
    elif hours <= 60:
        salary = wage*40 + wage*1.5*(hours-40) 
    else:
        salary = (wage*40) + (wage*1.5*20) + (wage*2*(hours-60)) 
    return salary


#5.30 Develop the function many() that takes as input the name of a file in the current directory (as a string) and 
#outputs the number of words of length 1, 2, 3, and 4. Test your function on file sample.txt.
#>>> many('sample.txt') 
#Words of length 1 : 2 
#Words of length 2 : 5 
#Words of length 3 : 1 
#Words of length 4 : 10

def many(filename):
    infile = open(filename)
    contents = infile.read()
    infile.close()
    temp = contents 
    table = str.maketrans('.,!?:;',6*' ')
    temp = temp.translate(table) #All punctuation marks are replaced to get the accurate length of a particular word#
    tem_lst = temp.split()
    c1, c2, c3, c4 = 0, 0, 0, 0 #The variables c1, c2, c3, c4 are assigned "0" each for subsequent use. 
    for x in tem_lst:
        if len(x) == 1:
            c1 = c1 + 1
        elif len(x) == 2:
            c2 = c2 + 1
        elif len(x) == 3:
            c3 = c3 + 1
        elif len(x) == 4:
            c4 = c4 + 1
    print('Words of length 1 : ' + str(c1),'Words of length 2 : ' + str(c2),'Words of length 3 : ' + str(c3),'Words of length 4 : ' + str(c4), sep = '\n')
 

#5.32 Implement function fib() that takes a nonnegative integer n as input and returns the nth Fibonacci number.
#>>> fib(0) 
#1
#>>> fib(4) 
#5
#>>> fib(8) 
#34

def fib(n):
    lst = [1,2] #From the given example values for fib(0), fib(4), fib(8), we can deduce that the author has taken the fibonacci sequence starting from 1 and 2. So, the initial 2 terms of the sequence are already assigned to a list named 'lst'
    for x in range(1,n+1): #For loop function is used to build the fibonacci sequence   
        num = lst[x] + lst[x-1]
        lst.append(num) #Fibonacci sequence gets updated one by one     
    if n < 0:
        value = print('Enter a non-negative integer')
    elif n == 0:
        value = 1 #Value of 1 is defined for n = 0 as required by the author
    else:
        value = lst[n-1]
    return value

################################################ END OF HOMEWORK #####################################################