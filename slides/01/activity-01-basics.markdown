---
layout: lab
title: JavaScript Basics
prefix: ../../
chrome: 0
---
# JavaScript Values, Types, Operations, Variables, Calling Functions, and Input/Output

Let's write a couple of programs:

1. greetings
2. say twice
3. miles
4. \* ...and a couple of challenging ones: 
	* numbers 
	* tree

## Instructions

### greetings

* using SublimeText (or your favorite text editor), create a new file called __greetings.html__ 
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* ask the user for their name
* save that input in a variable
* print "Hi (name that the user entered)!" out to the JavaScript console 
* save your file in SublimeText
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
(prompt) What's your name?
> Joe
Hi Joe!
{% endhighlight %}

<hr>

### say twice

Write a program that takes user input and repeats the user input twice (both words on the same line) in the JavaScript console.

* create a new file called __saytwice.html__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should ask for a word: "Give me a word to say twice"
* the program should repeat the input twice on the same line with a space in between...  back to the __JavaScript console__ 
	* for example, if someone enters "hello" in the prompt dialog
	* the output in the console would be "hello hello"
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
(prompt) Give me a word to say twice
> hello
hello hello
{% endhighlight %}

<hr>

### miles

Write a program that calculates miles-per-gallon based on user input for miles driven and gallons of gas used.

* create a new file called __miles.html__ 
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* miles-per-gallon (mpg) can be calculated using the following formula... 
* mpg = miles driven / gallons of gas used 
* ask the user for the number of miles driven and the gallons of gas used
* calculate miles-per-gallon and output the result to the JavaScript console
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
(prompt) How many miles did you drive?
>20
(prompt) How many gallons of gas did you use?
>2
Your car gets 10.0 miles per gallon.
{% endhighlight %}

<hr>

### \*numbers
(This one may be tricky!) Write a program that outputs the number in the thousands, hundreds, tens and ones places of a number. 

* create a new file called __numbers.html__ 
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* ask the user for a number
* calculate the numbers in the thousands, hundreds, tens and ones places
* output each place to the JavaScript console
* one solution is to use some numeric operators to determine each place (maybe modulo, division and subtraction would help)
* you may have to calculate each place separately
* don't worry about input that's not a positive whole number below 10,000
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
(prompt) Please enter a number
> 256

0 thousands
2 hundreds
5 tens
6 ones
{% endhighlight %}

<hr>

### \*tree

Print out a tree!

* create a new file called __tree.html__ 
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* print out an ascii art tree to the JavaScript console
<pre>
   /\
  /  \
  /  \
 /____\
   ||
</pre>

