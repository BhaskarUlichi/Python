# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:02:52 2022

@author: Bhaskar Teja Ulichi [101127292]
"""
#6.11 Implement function easyCrypto() that takes as input a string and prints its encryption defined as follows: 
#Every character at an odd position i in the alphabet will be encrypted with the character at position i + 1, and 
#every character at an even position i will be encrypted with the character at position i − 1. In other words, 
#‘a’ is encrypted with ‘b’, ‘b’ with ‘a’, ‘c’ with ‘d’, ‘d’ with ‘c’, and so on. Lowercase characters should remain 
#lowercase, and uppercase characters should remain uppercase.
#>>> easyCrypto('abc') 
#bad 
#>>> easyCrypto('ZOO') 
#YPP

def easyCrypto(strg):
    output = '' #An empty string called 'output' is assigned
    for x in strg:
        y = ord(x) #ASCII code for the character is plugged into variable 'y'
        if y % 2 == 0: #For character at even position
            output += chr(y-1) #ASCII codes are sequential. So, they character at position y will be replaced with character at position y-1
        else:
            output += chr(y+1) #For characters at odd positions, character at position y will be replaced with character at position y+1
    print(output)



#6.21 Write function ticker() that takes a string (the name of a file) as input. 
#The file will contain company names and stock (ticker) symbols. In this file, a company name will occupy a line, 
#and its stock symbol will be in the next line. Following this line will be a line with another company name, and so on. 
#Your program will read the file and store the name and stock symbol in a dictionary. Then it will provide an interface 
#to the user so that the user can obtain the stock symbol for a given company. Test your code on the NASDAQ 100 list of 
#stock given in file nasdaq.txt.
#>>> ticker('nasdaq.txt') 
#Enter Company name: YAHOO
#Ticker symbol: YHOO 
#Enter Company name: GOOGLE INC 
#Ticker symbol: GOOG ...
            
def ticker(filename):
    infile = open(filename)
    temp = infile.readlines() 
    infile.close()
    for x in range(len(temp)):
        if len(temp[x]) == 1:
            temp.pop(x) #items with unnecessary spaces with no content are removed
        else:
            temp[x] = temp[x].strip() #Leading and trailing spaces are removed
    symbols = {} #Empty dictionary 'symbols' is created
    for x in range(len(temp)):
        if x%2 == 0:
            a = temp[x] #srtings at even index numbers 
            b = temp[x+1] #strings at odd index numbers
            d2 = {a:b} #A (Key, Value) pair is created with (string at an even index, subsequent string)
            symbols.update(d2) 
    popup = input('Enter Company name: ')
    while popup != '':
        print('Ticker symbol: {}'.format(symbols[popup]))
        popup = input('Enter Company name: ') #User has to press "ENTER" key to make the iteration stop.

        

#6.24 Implement function names() that takes no input and repeatedly asks the user to enter the first name of a student 
#in a class. When the user enters the empty string, the function should print for every name the number of students with 
#that name.
#>>> names() 
#Enter next name: Valerie 
#Enter next name: Bob 
#Enter next name: Valerie 
#Enter next name: Amelia 
#Enter next name: Bob 
#Enter next name: 
#There is 1 student named Amelia 
#There are 2 students named Bob 
#There are 2 students named Valerie

def names():
    popup = input('Enter next name: ')
    counters = {} 
    while popup != '':
        if popup in counters:
            counters[popup] += 1 
        else:
            counters[popup] = 1
        popup = input('Enter next name: ')
    names = counters.keys()
    for x in names:
        if counters[x] == 1:
            print('There is {} student named {}'.format(counters[x],x))
        else:
            print('There are {} students named {}'.format(counters[x],x))
        
            

#6.25 Write function different() that takes a two-dimensional table as input and returns the number of distinct entries 
#in the table.
#>>> t = [[1,0,1],[0,1,0]] 
#>>> different(t) 
#2
#>>> t = [[32,12,52,63],[32,64,67,52],[64,64,17,34],[34,17,76,98]] 
#>>> different(t) 
#10

def different(lst):    
    distinct = {} 
    for x in lst:
        for j in x:
            if j in distinct:
                distinct[j] += 1
            else:
                distinct[j] = 1
    return len(distinct) #Once a dictionary is created with counters, the size of the dictionary gives us the number of distinct entries in it.
                
        

#6.33 Write function diceprob() that takes as input a possible result r of a roll of pair of dice (i.e. an integer 
#between 2 and 12) and simulates repeated rolls of a pair of dice until 100 rolls of r have been obtained. 
#Your function should print how many rolls it took to obtain 100 rolls of r.
#>>> diceprob(2) 
#It took 4007 rolls to get 100 rolls of 2 
#>>> diceprob(3) 
#It took 1762 rolls to get 100 rolls of 3 
#>>> diceprob(4) 
#It took 1058 rolls to get 100 rolls of 4 
#>>> diceprob(5) 
#It took 1075 rolls to get 100 rolls of 5 
#>>> diceprob(6) 
#It took 760 rolls to get 100 rolls of 6 
#>>> diceprob(7) 
#It took 560 rolls to get 100 rolls of 7

def diceprob(r):
    import random
    rolls = {}
    rolls[r] = 0 #A zero number of rolls is created for possible result r
    count = 0 #Zero count is created for number of rolls.
    while rolls[r] < 100:
        dice1 = random.randrange(1,7)
        dice2 = random.randrange(1,7)
        dice = dice1 + dice2
        count += 1
        if dice == r:
            rolls[r] += 1
    print('It took {} rolls to get {} rolls of {}'.format(count,rolls[r],r))
        


########################################################## END OF HOMEWORK ###################################################



