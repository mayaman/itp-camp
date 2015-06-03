"""
roll_a_seven.py
=====

Write a program that simulates rolling 2 6-sided repeatedly until the sum of 
the dice is equal to 7.  The program will count the number of rolls it took
to get a 7.  The program will repeat this process 10 times... keeping track
of the total number of rolls.  Once the 10 trials have been exhausted, the 
program will print out the average number of rolls that it took.

* do the following 10 times:
    * roll 2 6-sided dice repeatedly
	* print out the result of each roll, and the sum of both rolls
	* keep track of the number of rolls
	* stop when the sum is 7
	* print out the total number of rolls it took to get 7
	* add that to a running total (so that you can get an average later)
* print out the average number of times it took to roll a 7
* the result should be around 6 (1 in 6 chance of getting a 7)
* example output:

1,3: 4
2,1: 3
3,4: 7
-----
3 rolls

.
.
.
(total of 10)
.
.
.

6,5: 11
2,6: 8
4,4: 8
6,3: 9
1,4: 5
1,5: 6
3,4: 7
-----
7 rolls

2,6: 8
5,1: 6
2,5: 7
-----
3 rolls


Average: 5.6 rolls
"""
