---
layout: lab
title: JavaScript Functions
prefix: ../../
---
# Lab 10 - Part 1 - JavaScript Functions

In this lab, you'll be creating the following programs:

1. heart
2. sandwich
3. triangle
4. \* min

## Instructions

Note that __ALL OF THESE FILES MUST BE CREATED IN THE REPOSITORY THAT YOU CREATED FOR THIS LAB__.

### heart

Write a program that adds a heart to the beginning of two strings - "stuff" and "JavaScript".  Do this by creating a function

* using SublimeText, create a new file called __heart.html__ in your repository directory: __~/Desktop/jversoza/lab-10-events/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* create a function called heart (use: function yourFunctionName(param1, param2 ...))
* it should take only one parameter; call it word
* it should return a value ... the word with an ascii art heart attached to the beginning of it  &gt;3 (use return ... to do this)
* call your function twice... (function name, then arguments within parentheses: yourFunctionName(arg1, arg2 ...))
	* ...and assign the output to a variable (var varname1 = yourFunctionName(arg1, ...))
	* the first time, pass in "stuff" as an argument
	* the second timee, pass in "" as an argument
* print out both variables to the JavaScript console (console.log(...))
* example output below...

{% highlight bash %}
<3 stuff
<3 JavaScript
{% endhighlight %}

<hr>

### sandwich

Write a program that adds an arbitrary character to the beginning and end of a string. It will ask the user for a word and another word to surround it with. 

* using SublimeText, create a new file called __sandwich.html__ in your repository directory: __~/Desktop/jversoza/lab-10-events/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* define a function called sandwich
* it should have two parameters, word and surround
* it should __give back__ a value - the the string, word, with the string, surround, at the beginning and end of it
* ask for a word: "Word please:"
* ask for a surrounding word: "What should I surround it with?"
* it should call your sandwich function will give back the word surrounded appropriately 
	* for example youFunctionName("HELLO", "*") gives back "*HELLO*"
* save the result of calling your sandwich function 
* print out the result to the JavaScript console

{% highlight bash %}
(prompt) Word please:
> hello
(prompt) What should I surround it with?:
> x
xhellox
{% endhighlight %}

<hr>

### triangle

Write a program that asks for a base and height of a triangle.  It will output the area.


* using SublimeText, create a new file called __triangle.html__ in your repository directory: __~/Desktop/jversoza/lab-10-events/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* define a function called area_of_triangle
* it should have two parameters, b and h (base and height)
* look up the formula for the area
* your function should calculate the area and store it in a variable
* it should __give back__ the resulting area (return)
* your program should ask for a base: "What is the base of the triangle?""
* your program should ask for a height: "What is the height of the triangle?""
* use the function you just created to calculate area based on input
* save the result of your function call in variable
* print out the result to the JavaScript console

{% highlight bash %}
(prompt) What is the base of the triangle? 
> 20
(prompt) What is the height of the triangle? 
> 5
The area of the triangle is 50
{% endhighlight %}

<hr>

### min

Write a program that asks for two numbers and determines which one is smaller.  It will output the smaller one to the JavaScript console.

* using SublimeText, create a new file called __min.html__ in your repository directory: __~/Desktop/jversoza/lab-10-events/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* define a function called min
* it should have two parameters, a and b 
* your function should determine which number is smaller, a or b (either works if they're equal)
* it should __give back__ the smaller number (return)
* your program should ask for one number: "Number 1:""
* your program should ask for another number: "Number 2:""
* use the function you just created to determine the smaller of the two
* save the result of your function call in variable
* print out the result to the JavaScript console

{% highlight bash %}
(prompt) Number 1:
> 20
(prompt) Number 2: 
> 7
The smaller number is 7
{% endhighlight %}
