# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 18:29:24 2022

@author: Bhaskar Teja Ulichi [101127292]
"""

def lst_count(lst):
    n = 0
    for x in lst:
        n += 1
    return n

def lst_sum(lst):
    agg = 0
    for x in lst:
        agg += x
    return agg

def lst_mean(lst):
    return lst_sum(lst)/lst_count(lst)


def lst_min(lst):
    lmin = lst[0]
    for x in lst:
        if x < lmin:
            lmin = x
    return lmin


def lst_max(lst):
    lmax = lst[0]
    for x in lst:
        if x > lmax:
            lmax = x
    return lmax


def lst_range(lst):
    return lst_max(lst) - lst_min(lst)

def lst_median(lst):
    lst.sort()
    n = lst_count(lst)
    if n%2 == 0:
        i = int(n/2)
        j = i-1
        midvalues = [lst[i],lst[j]]
        return lst_mean(midvalues)
    else:
        i = int((n-1)/2)
        return lst[i]
    
def lst_variance(lst):
    if lst_count(lst) == 0:
        return 'Please enter a list of values'
    elif lst_count(lst) == 1:
        return 'Undefined'
    else:
        x_bar = lst_mean(lst)
        sq_diff = []
        for x in lst:
            diff = (x - x_bar)**2
            sq_diff.append(diff)    
        num = lst_sum(sq_diff)
        den = lst_count(lst) - 1
        return num/den

def lst_stdev(lst):
    if lst_count(lst) == 0:
        return 'Please enter a list of values'
    elif lst_count(lst) == 1:
        return 'Undefined'
    else:
        import math
        return math.sqrt(lst_variance(lst))


def summary(lst):
    if len(lst) != 0:            
        print('A Statistical Summary for the list of values entered is as follows')
        print('Mean               : ' + str(lst_mean(lst)))
        print('Median             : ' + str(lst_median(lst)))
        print('Standard Deviation : ' + str(lst_stdev(lst)))
        print('Variance           : ' + str(lst_variance(lst)))
        print('Range              : ' + str(lst_range(lst)))
        print('Minimum Value      : ' + str(lst_min(lst)))
        print('Maximum Value      : ' + str(lst_max(lst)))
        print('Sum of all Values  : ' + str(lst_sum(lst)))
        print('Count of Values    : ' + str(lst_count(lst)))
    else:
        print('Please enter a list of values')
        

##############################################################################################################################
############################################ SIMPLE CORRELATION AND REGRESSION ###############################################
##############################################################################################################################

def lm():     
    number = eval(input('Please enter the number of data points (x,y): '))
    if number > 20:
        print('Sorry. A maximum of only 20 data points is allowed')
        number = eval(input('Please enter the number of data points (x,y): '))
                  
    x = []
    y = []
    xy = []
    x2 = []
    y2 = []
    
    for num in range(number):
        x_i = eval(input('Please enter the x co-ordinate: '))
        y_i = eval(input('Please enter the y co-ordinate: '))
        xy_i = (x_i)*(y_i)
        x2_i = (x_i)**2
        y2_i = (y_i)**2
        x.append(x_i)
        y.append(y_i)
        xy.append(xy_i)
        x2.append(x2_i)
        y2.append(y2_i)
    
    n = lst_count(x)
    sum_xy = lst_sum(xy)
    sum_x = lst_sum(x)
    sum_y = lst_sum(y)
    sum_x2 = lst_sum(x2)
    sum_y2 = lst_sum(y2)
    
    r_num = n*(sum_xy) - (sum_x)*(sum_y)
    import math
    r_d1 = (n*sum_x2) - (sum_x)**2
    r_d2 = (n*sum_y2) - (sum_y)**2
    r_den = math.sqrt((r_d1)*(r_d2))
    
    r = (r_num)/(r_den)
    
    s_x = lst_stdev(x)
    s_y = lst_stdev(y)
    
    m = r*(s_y)/(s_x)
    
    x_bar = lst_mean(x)
    y_bar = lst_mean(y)
    
    b = y_bar - m*(x_bar)
    
    print('The Correlation Coefficient for your data set is       : ' + str(r))
    print('The least-squares regression line for your data set is : ' + 'y = ' + str(m) + 'x + ' + str(b))


 
 
##########################################################################################################################








number = eval(input('Please enter the number of data points (x,y): '))
if number > 20:
    print('Sorry. A maximum of only 20 data points is allowed')
    number = eval(input('Please enter the number of data points (x,y): '))
              
x = []
y = []

for num in range(number):
    x_i = eval(input('Please enter the x co-ordinate: '))
    y_i = eval(input('Please enter the y co-ordinate: '))
    x.append(x_i)
    y.append(y_i)

def lm(x,y):    
    xy = 1
    sum_xy = 0
    for i in range(len(x)):
        xy = x[i]*y[i]
        sum_xy += xy
        
    sum_x2 = 0
    for i in x:
        x2 = i**2
        sum_x2 += x2
        
    sum_y2 = 0
    for i in y:
        y2 = i**2
        sum_y2 += y2
            
    n = lst_count(x)
    sum_x = lst_sum(x)
    sum_y = lst_sum(y)
    r_num = n*(sum_xy) - (sum_x)*(sum_y)
    import math
    r_d1 = (n*sum_x2) - (sum_x)**2
    r_d2 = (n*sum_y2) - (sum_y)**2
    r_den = math.sqrt((r_d1)*(r_d2))
    r = (r_num)/(r_den)
    s_x = lst_stdev(x)
    s_y = lst_stdev(y)
    m = r*(s_y)/(s_x)
    x_bar = lst_mean(x)
    y_bar = lst_mean(y)
    b = y_bar - m*(x_bar)
    
    print('The Correlation Coefficient for your data set is       : ' + str(r))
    print('The least-squares regression line for your data set is : ' + 'y = ' + str(m) + 'x + ' + str(b))


























