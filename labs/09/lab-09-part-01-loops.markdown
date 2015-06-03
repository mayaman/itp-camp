---
layout: lab
title: JavaScript For Loops
prefix: ../../
---
# Lab 8 - Part 1 - JavaScript For Loops

In this lab, you'll be creating several programs:

1. tens
2. party 
3. average
4. \*largest
5. \*fizzbuzz


## Instructions

Note that __ALL OF THESE FILES MUST BE CREATED IN THE REPOSITORY THAT YOU CREATED FOR THIS LAB__.

### tens

Write a program that counts by 10's from 20 to 100

* using SublimeText, create a new file called __tens.html__ in your repository directory: __~/Desktop/jversoza/lab-08-for/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should count from 20 to 100 by 10's
* example output below...

{% highlight bash %}
20
30
.
.
100
{% endhighlight %}
* save your file in SublimeText
* use status, add commit and push to save your file in version control and submit it

<hr>

### party

Write a program that acts for user input... and counts down from that number to exactly 1.  After it counts down to 1, it says "PARTY TIME!!!".

* using SublimeText, create a new file called __party.html__ in your repository directory: __~/Desktop/jversoza/lab-08-for/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* say - "Let's party..."
* ask for a number: "How long 'til the party?"
* based on the input, it should count down from that number to __1__
* remember to convert from a string to an int!
* if the number that is input is less than 1, then say "PARTY NOW!!!"
* at the end, say "PARTY TIME!!!"
* save your file in SublimeText
* use git status, add, commit, and push to save your file in version control and submit it
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):

{% highlight bash %}
# Run 1: 
# -----
Let's party...
(prompt) How long 'til the party?
> 3
3
2
1
PARTY TIME!!!

# Run 2: 
# -----
Let's party...
(prompt) How long 'til the party?
> -1
PARTY NOW!!!
{% endhighlight %}

<hr>

### average

Ask for four numbers, output the average of those numbers.  Use a for loop to do this.

* using SublimeText, create a new file called __average.html__ in your repository directory: __~/Desktop/jversoza/lab-08-for/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* ask for a number 4 times: "Number please...."
* calculate the average of those 4 numbers
* remember to convert from a string to an int!
* say: "The average is x", with x replaced by the actual average of the inputs.
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):

{% highlight bash %}
(prompt) Number please...
> 4
(prompt) Number please...
> 6
(prompt) Number please...
> 1
(prompt) Number please...
> 9
The average is 5.
{% endhighlight %}

<hr>

### \*largest

Ask for four numbers, output the largest of those numbers.  Use a for loop to do this.

* using SublimeText, create a new file called __largest.html__ in your repository directory: __~/Desktop/jversoza/lab-08-for/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* ask for a number 4 times: "Number please...."
* using comparison operators and a conditional (in each iteration), determine the current largest number...
* remember to convert from a string to an int!
* say: "The largest number is x", with x replaced by the current largest number
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):

{% highlight bash %}
(prompt) Number please...
> 4
(prompt) Number please...
> 6
(prompt) Number please...
> 1
(prompt) Number please...
> 9
The largest number is 9
{% endhighlight %}

<hr>

### \*fizzbuzz

Count from 1 to 100, but print out fizz or buzz depending on special conditions.

* using SublimeText, create a new file called __fizzbuzz.html__ in your repository directory: __~/Desktop/jversoza/lab-08-for/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* print out 1 to 100 ...with the following exceptions:
* for multiples of three, print out "Fizz" instead of the number 
* for multiples of five, print out "Buzz" instead of the number
* for multiples of both three and five print “FizzBuzz”
* example output is below:

{% highlight python %}
1
2
Fizz
4
Buzz
Fizz
.
.
14
FizzBuzz
16
.
.
98
Fizz
Buzz
{% endhighlight %}
