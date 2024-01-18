# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 13:52:30 2022

@author: Bhaskar Teja Ulichi [101127292]

"""
#12.11 Using module sqlite3, create a database file weather.db and table WeatherData in it. 
#Define the column names and types to match those in the table in Figure 12.16; then enter all 
#the rows shown into the table.

import sqlite3
con = sqlite3.connect('weather.db')
cur = con.cursor()

sql_1 = '''CREATE TABLE WeatherData
(
 City TEXT,
 Country TEXT,
 Season INT,
 Temperature REAL,
 Rainfall REAL
 )'''

cur.execute(sql_1)

sql_2  = '''
INSERT INTO WeatherData VALUES
('Mumbai','India',1,24.8,5.9),
('Mumbai','India',2,28.4,16.2),
('Mumbai','India',3,27.9,1549.4),
('Mumbai','India',4,27.6,346.0),
('London','United Kingdom',1,4.2,207.7),
('London','United Kingdom',2,8.3,169.6),
('London','United Kingdom',3,15.7,157.0),
('London','United Kingdom',4,10.4,218.5),
('Cairo','Egypt',1,13.6,16.5),
('Cairo','Egypt',2,20.7,6.5),
('Cairo','Egypt',3,27.7,0.1),
('Cairo','Egypt',4,22.2,4.5)
'''

cur.execute(sql_2)


#12.12 Using sqlite3 and within the interactive shell, open the database file weather.db 
#you created in Problem 12.11 and execute the queries from Problem 12.10 by running appropriate 
#Python statements.


#12.10 Write SQL queries on table WeatherData in Figure 12.16 that return: 

#(a) All the records for the city of London 
sql_a = '''
SELECT * FROM WeatherData
WHERE City = 'London'
''' 
cur.execute(sql_a)
a = cur.fetchall()


#(b) All the summer records 
sql_b = '''
SELECT * FROM WeatherData
WHERE Season = 3
''' 
cur.execute(sql_b)
b = cur.fetchall()


#(c) The city, country, and season for which the average temperature is less than 20◦ 
sql_c = '''
SELECT City, Country, Season FROM WeatherData
WHERE Temperature < 20
''' 
cur.execute(sql_c)
c = cur.fetchall()


#(d) The city, country, and season for which the average temperature is greater than 20◦ 
#and the total rainfall is less than 10 mm
sql_d = '''
SELECT City, Country, Season FROM WeatherData
WHERE Temperature > 20 AND Rainfall < 10
''' 
cur.execute(sql_d)
d = cur.fetchall()

#(e) The maximum total rainfall 
sql_e = '''
SELECT MAX(Rainfall) FROM WeatherData
''' 
cur.execute(sql_e)
e = cur.fetchall()


#(f) The city, season, and rainfall amounts for all records in descending order of rainfall 
sql_f = '''
SELECT City, Season, Rainfall FROM WeatherData
ORDER BY Rainfall DESC
''' 
cur.execute(sql_f)
f = cur.fetchall()

#(g) The total yearly rainfall for Cairo, Egypt 
sql_g = '''
SELECT SUM(Rainfall) FROM WeatherData
WHERE City = 'Cairo' AND Country = 'Egypt'
''' 
cur.execute(sql_g)
g = cur.fetchall()


#(h) The city name, country, and total yearly rainfall for every distinct city
sql_h = '''
SELECT City, Country, SUM(Rainfall) FROM WeatherData
GROUP BY City
''' 
cur.execute(sql_h)
h = cur.fetchall()

cur.close()
con.close()

######################################## END OF HOMEWORK #######################################


