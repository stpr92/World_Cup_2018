# World_Cup_2018

Creating a sample table for group stage matches.

# Problem :

In Group B of the World Cup, the teams Iran, Portugal, Spain, and Morocco are present. Write a program that, by receiving the results of the matches, prints the name of the team, the number of wins and losses, the goal difference, and their points in one line. Each team should be printed in a line in order of points (if points are equal, the number of wins should be considered. If both points and wins are equal, the teams should be printed in alphabetical order).

Note: A team earns zero points for a loss, one point for a draw, and three points for a win. The goal difference is the difference between the goals scored and goals conceded by a team.

The match results should be read in the following order: (In the sample input, the number on the left corresponds to the team on the left.)

Iran – Spain

Iran – Portugal

Iran – Morocco

Spain – Portugal

Spain – Morocco

Portugal – Morocco

# sample input

2-2

2-1

1-2

2-2

3-1

2-1

# sample output

Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3



I have created Group B of football World Cup 2018 with 2 kinds of different approches:

# First just with python code

It became a bit difficult and complicated because I had to use 4 different dictionaries. The file for this code is named "match.py".

# Second with python and mysql 

Initially, I created a raw database named "world_cup" in MySQL, which contains a table named "b_group". Using Python, I retrieved and organized the data and connected it to the database. I then used another function to output the results.
In this approach, because I used a database and a function, the code became both easier and more comprehensive, which allows it to be generalized to other groups and matches as well.

The SQL database file and the Python files are named "world_cup" and "match_with_database" respectively are available here.



