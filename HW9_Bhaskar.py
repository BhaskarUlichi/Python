# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 11:58:53 2022

@author: Bhaskar Teja Ulichi [101127292]
"""
#Write and execute the following queries for data from the chinook database in a Python file.

import sqlite3
con = sqlite3.connect('chinook.db')
cur = con.cursor()

# (1) Write a query to display all of the records from the tracks table

sql1 = '''SELECT * FROM tracks'''
cur.execute(sql1)
res1 = cur.fetchall()


# (2) Write a query to display all of the records from the albums table

sql2 = '''SELECT * FROM albums'''
cur.execute(sql2)
res2 = cur.fetchall()


# (3) Write a query to display all of the records from the artists table

sql3 = '''SELECT * FROM artists'''
cur.execute(sql3)
res3 = cur.fetchall()


# (4) Write a query to display Album Name (Title) from the albums table and Song (Name)  from 
#the tracks table for each album.

sql4 = '''
SELECT a.Title, t.Name
FROM albums a INNER JOIN tracks t
ON a.AlbumId = t.AlbumId
ORDER BY a.Title
'''
cur.execute(sql4)
res4 = cur.fetchall()


# (5) Write a query to display the Artist Name (Name) from the artists table and the Album Name 
#(Title) from the albums table.

sql5 = '''
SELECT art.Name, alb.Title
FROM artists art INNER JOIN albums alb
ON art.ArtistId = alb.ArtistId
ORDER BY art.Name
'''
cur.execute(sql5)
res5 = cur.fetchall()


# (6) Write a query using the chinook database to list all albums, the performing artist, and the 
#number of tracks on the album.
#•Display in 3 columns named:
#•Artist
#•Album
#•TrackCount
#•Output the results of the query to a python list named “FinalResults”


sql6 = '''
SELECT art.Name AS Artist, 
a.Title AS Album, 
Count(t.Name) AS TrackCount
FROM tracks t INNER JOIN albums a 
ON t.AlbumId = a.AlbumId
INNER JOIN artists art 
ON art.ArtistId = a.ArtistId
GROUP BY a.Title  
'''
cur.execute(sql6)

FinalResults = cur.fetchall()


######################################### END OF HOMEWORK ########################################







