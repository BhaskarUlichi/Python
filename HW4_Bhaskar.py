# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 20:10:20 2022

@author: Bhaskar Teja Ulichi [101127292]
"""
################################################################################################
#################################### HOME WORK 4 - CHAPTER 4 ###################################
###############################################################################################

# 4.22 # Write a function month() that takes a number between 1 and 12 as input and returns the three-character #
#abbreviation of the corresponding month. Do this without using an if statement, just string operations. 
#Hint: Use a string to store the abbreviations in order.
#>>> month(1)
#'Jan' 
#>>> month(11)
#'Nov'

def month(n):
    month_names = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'
    m_lst = month_names.split(' ')
    return m_lst[n-1]

#4.23 Write a function average() that takes no input but requests that the user enter a sentence. 
#Your function should return the average length of a word in the sentence.
#>>> average() 
#Enter a sentence: A sample sentence 
#5.0 

def average():
    sen = input('Enter a Sentence: ')
    sen_lst = sen.split(' ') #Sentence will be split into a list with each word as an individual item# 
    tot_len = 0  #tot-len is set to '0' for subsequent usage#
    for x in sen_lst:                    
        tot_len = tot_len + len(x) #For-loop is used to measure the length of each word in the list of words#
    avg = tot_len/len(sen_lst) # avg = sum of the words/ number of words# 
    return avg     


#4.24 # Implement function cheer() that takes as input a team name (as a string) and prints a cheer as shown:
#>>> cheer('Huskies') 
#How do you spell winner? 
#I know, I know! 
#H U S K I E S !
#And that's how you spell winner! 
#Go Huskies!

def cheer(teamname):    
    print('How do you spell winner?','I know, I know!',sep = '\n') 
    Tname = teamname.upper() + '!' 
    for x in Tname:
        print(x, end = ' ') #The default '\n' for a for-loop print function is changed to blank space#
    print('\nAnd that\'s how you spell winner!','Go ' + teamname + '!', sep = '\n')     
     

#4.25 # Write function vowelCount() that takes a string as input and counts and prints the number of occurrences of 
#vowels in the string.
#>>> vowelCount('Le Tour de France') 
#a, e, i, o, and u appear, respectively, 1, 3, 0, 1, 1 times.


def vowelCount(string):
    adjust = string.lower() 
    ca = adjust.count('a') 
    ce = adjust.count('e')
    ci = adjust.count('i')
    co = adjust.count('o') 
    cu = adjust.count('u')
    print('a, e, i, o, and u appear, respectively,', str(ca) + ',', str(ce) + ',', str(ci) + ',', str(co) + ',', str(cu), 'times.')


#4.27# Write a function fcopy() that takes as input two file names (as strings) and copies the content of the first 
#file into the second.
#File: example.txt
#>>> fcopy('example.txt','output.txt') 
#>>> open('output.txt').read() 
#'The 3 lines in this file end with the new line character.\n\n
#There is a blank line above this line.\n' 

def fcopy(file_1,file_2):
    infile = open(file_1)
    temp1 = infile.read()
    infile.close()
    outfile = open(file_2,'w')
    outfile.write(temp1)
    outfile.close()
    

#4.29 Write a function stats() that takes one input argument: the name of a text file. The function should print, 
#on the screen, the number of lines, words, and characters in the file; your function should open the file only once.
#>>> stats('example.txt') 
#line count: 3 
#word count: 20 
#character count: 98

def stats(filename):
    infile = open(filename)
    line_lst = infile.readlines()
    infile.close()
    cl = len(line_lst) #No of lines is stored in variable 'cl'    
    samp_str = ''      #A dummy string with 0 size is created for subsequent use
    for x in range(0,len(line_lst)): #For-loop is used to convert the list into a string
        samp_str = samp_str + line_lst[x]  #Each line will be concatenated and becomes a single string. The resultant string is the same as the string in 'example.txt'
    cc = len(samp_str)
    samp_str = samp_str.replace('\n','') #Empty lines are deleted
    samp_str = samp_str.replace('.',' ') #Fullstops are not words and they are replaced with white spaces
    samp_lst = samp_str.split(' ') #The edited string is now split into a list of words
    tem = 0 # A temporary variable '0' is created to count the number of empty words in the list
    for x in samp_lst[0:len(samp_lst)]:
        if len(x) == 0:
            tem = tem + 1 #All items in the list that are not words are counted and stored in variable 'temp'
    cw = len(samp_lst) - tem   # Number of words = length of the list - Number of empty words    
    print('line count: '+ str(cl),'word count: '+ str(cw),'character count: '+ str(cc),sep='\n')


#4.30 # Implement function distribution() that takes as input the name of a file (as a string). 
#This one-line file will contain letter grades separated by blanks. 
#Your function should print the distribution of grades, as shown.
##>>> distribution('grades.txt') 
#6 students got A
#2 students got A-
#3 students got B+ 
#2 students got B 
#2 students got B-
#4 students got C 
#1 student got C-
#2 students got F

def distribution(file_name):
    infile = open(file_name)
    temp_file = infile.read()
    infile.close()
    A1 = temp_file.count('A ')
    A2 = temp_file.count('A-')
    B1 = temp_file.count('B+')
    B2 = temp_file.count('B ')
    B3 = temp_file.count('B-')
    C1 = temp_file.count('C ')
    C2 = temp_file.count('C-')
    F = temp_file.count('F')
    sg = ' students got '
    print(str(A1) + sg + 'A')
    print(str(A2) + sg + 'A-')
    print(str(B1) + sg + 'B+')
    print(str(B2) + sg + 'B')
    print(str(B3) + sg + 'B-')
    print(str(C1) + sg + 'C')
    print(str(C2) + sg + 'C-')
    print(str(F) + sg + 'F')

        

#4.31 Implement function duplicate() that takes as input the name (a string) of a file in the current directory 
#and returns True if the file contains duplicate words and False otherwise.
#>>> duplicate('Duplicates.txt') 
#True >>> 
#duplicate('noDuplicates.txt') 
#False

def duplicate(fileName):
    infile = open(fileName)
    contents = infile.read()
    infile.close()
    contents = contents.split()
    count = 0 #A dummy variable with value 0 is created to count the number of duplicates
    for x in contents:
        if contents.count(x)>1: #If the count of a word is more than 1, then there is a duplicate of that word in that list 
            count = count + 1 #The number of duplicate set of words is counted 
    if count >= 1: #If the number of duplicate set of words is 1 or more than 1, then the file contains duplicate words
        print(True)
    else:
        print(False)
    
        
#4.32 The function censor() takes the name of a file (a string) as input. 
#The function should open the file, read it, and then write it into file censored.txt with this modification: 
#Every occurrence of a four-letter word in the file should be replaced with string 'xxxx'.
#>>> censor('example.txt')
#Note that this function produces no output, but it does create file censored.txt in the current folder.

            
def censor(filename):
    infile = open(filename)
    contents = infile.read()
    infile.close()    
    temp1 = contents
    temp1 = temp1.replace('.', ' .')
    temp2 = temp1.split()
    for x in temp2:
        if len(x) == 4:
            temp1 = temp1.replace(' ' + x + ' ', ' xxxx ')
    temp1 = temp1.replace(' .','.')
    outfile = open('censored.txt','w')
    outfile.write(temp1)
    outfile.close()
    
            
############################################# END OF HOMEWORK #########################################################