---
layout: lab
title: JavaScript Conditionals
prefix: ../../
---
# Lab 7 - Conditionals, Boolean Logic

In this lab, you'll be creating several programs:

1. snake eyes
2. add dice
3. fortune
4. days
5. guess
6. \*grade 
7. \*tip


## Instructions

Note that __ALL OF THESE FILES MUST BE AVED IN THE LOCAL REPOSITORY THAT YOU CREATED FOR THIS LAB__.

### snake eyes

Write a program that asks for the result of two dice rolls.  If both rolls are 1, it will shout, "SNAKE EYES!".  Otherwise, it should just say "That's a normal roll".

* using SublimeText, create a new file called __snakeeyes.html__ in your repository directory: __~/Desktop/jversoza/lab-07-if-while/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should ask for the result of the first die roll: "Give me a number for the first roll (1-6)"
* the program should ask for the result of the second die roll: "Give me a number for the second roll (1-6)"
* the program should say "SNAKE EYES!" if both rolls are 1, and "That's a normal roll" otherwise
* use the parseInt function to convert input from a string to a number (for example: num1 = parseInt(roll1, 10)) before comparing!
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
(prompt) Give me a number for the first roll (1-6)
> 1
(prompt) Give me a number for the second roll (1-6)
> 1
SNAKE EYES!
{% endhighlight %}
* save your file in SublimeText
* use git status, add, commit, and push to save your file in version control and submit it

<hr>

### add dice

Write a program that asks for the result of two dice rolls.  Add the results of both rolls and print out the sum.

* using SublimeText, create a new file called __adddice.html__ in your repository directory: __~/Desktop/jversoza/lab-07-if-while/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should ask for the result of the first die roll: "Give me a number for the first roll (1-6)"
* the program should ask for the result of the second die roll: "Give me a number for the second roll (1-6)"
* use the parseInt function to convert both inputs from a string to a number (for example: num1 = parseInt(roll1, 10)) 
* then... add both numbers together and print out the output to the JavaScript console
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
(prompt) Give me a number for the first roll (1-6)
> 1
(prompt) Give me a number for the second roll (1-6)
> 5
The sum of both rolls is 6.
{% endhighlight %}
* save your file in SublimeText
* use git status, add, commit, and push to save your file in version control and submit it

<hr>

### fortune

Write a program that asks for number.  The program will translate that number into a fortune.

* using SublimeText, create a new file called __fortune.html__ in your repository directory: __~/Desktop/jversoza/lab-07-if-while/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should ask for a number: "Give me a number between 1 and 3, and I'll predict your future..."
* use the parseInt function to convert the input from a string to a number (for example: num = parseInt(answer, 10)) 
* compare the resulting number to a number corresponding to a __of your own creation__:
	* 1 - you will type in the word "git" many times
	* 2 - you will be hungry by the end of class
	* 3 - ...
* print out the corresponding fortune to the JavaScript console...
* if the number doesn't correspond to a fortune, ignore the input
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
# Run 1
(prompt) Give me a number between 1 and 3, and I'll predict your future...
> 2
you will be hungry by the end of class

# Run 2
(prompt) Give me a number between 1 and 3, and I'll predict your future...
> 24
(no output)
{% endhighlight %}
* save your file in SublimeText
* use git status, add, commit, and push to save your file in version control and submit it



### days

Write a program that asks for number.  The program will translate that number to a day of the week.

* using SublimeText, create a new file called __days.html__ in your repository directory: __~/Desktop/jversoza/lab-07-if-while/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should ask for a number: "Give me a number for the day of the week"
* use the parseInt function to convert the input from a string to a number (for example: num = parseInt(day, 10)) 
* compare the resulting number to a number corresponding to a day of the week:
	* 1 for Monday
	* 2 for Tuesday ...
	* up through 7 for Sunday
* print out the corresponding day to the JavaScript console: "That day is Thursday!" 
* if the number does not match a day, the program should say "That's not a day!"
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
# Run 1
(prompt) Give me a number for the day of the week
> 2
Tuesday

# Run 2
(prompt) Give me a number for the day of the week
> 34
That's not a day!
{% endhighlight %}
* save your file in SublimeText
* use git status, add, commit, and push to save your file in version control and submit it


<hr>


### guess

Write a number guessing game.

* using SublimeText, create a new file called __guess.html__ in your repository directory: __~/Desktop/jversoza/lab-07-if-while/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* create a variable to hold a secret number
* the program should ask for a number: "Guess the secret number"
* use the parseInt function to convert the input from a string to a number (for example: num = parseInt(guess, 10)) 
* if the number inputted matches the secret number, print out "You got it!"
* if the number inputted is within 1 of the secret number, print out "Close, the secret number was [the secret number]"
* if the number inputted is not the secret number, and is not within 1, print out "Nope, it was [the secret number]"
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
# Assuming secret number is 5

# Run 1
(prompt) Guess the secret number
> 2
Nope, it was 5


# Run 2
(prompt) Guess the secret number
> 4
Close, the secret number was 5


# Run 3
(prompt) Guess the secret number
> 5
You got it!
{% endhighlight %}
* save your file in SublimeText
* use git status, add, commit, and push to save your file in version control and submit it

<hr>

### grade

Write a program that converts a numeric score to a letter grade.

* using SublimeText, create a new file called __grade.html__ in your repository directory: __~/Desktop/jversoza/lab-07-if-while/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should ask for a score: "What was your score?"
* use the parseInt function to convert the input from a string to a number (for example: num = parseInt(guess, 10)) 
* use the chart below to translate from number to letter grade:
{% highlight bash %}
90 - 100: A
80 - 89:  B
70 - 79:  C
60 - 69:  D
< 60:     F
{% endhighlight %}
* print out the corresponding grade
* if the number doesn't fall between 0 and 100, ignore the input
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):

{% highlight bash %}
(prompt) What was your score?
> 84
B
{% endhighlight %}
* save your file in SublimeText
* use git status, add, commit, and push to save your file in version control and submit it

<hr>

### tip

Create a tip calculator.

* using SublimeText, create a new file called __tip.html__ in your repository directory: __~/Desktop/jversoza/lab-07-if-while/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should ask the following:
	* how many people?	
	* how much did it cost?
	* how was the service? 
		* the values for this can be: terrible, poor, ok, good, great
		* only ask about service if there are less than 6 people
* if the number of people are > 6 tip should always be 20%, regardless of service.
* otherwise, calculate the tip using the following table:
	* terrible = no tip (0%)
	* poor - 10%
	* ok - 15%
	* good - 20%
	* great - 25%
* output the calculated tip.
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
Run 1: 
-----
(prompt) How many people? > 2
(prompt) How much did it cost? > 25
(prompt) How was the service (terrible, poor, ok, good, great)? > great
You should probably tip $6.25!

 
Run 2: 
-----
(prompt) How many people? > 4
(prompt) How much did it cost? > 70
(prompt) How was the service (terrible, poor, ok, good, great)? > meh
Couldn't understand meh service; using default 15 percent.
You should probably tip $10.5!

Run 3: 
-----
(prompt) How many people? > 200
(prompt) How much did it cost? > 950
You should probably tip $190.0!
{% endhighlight %}

