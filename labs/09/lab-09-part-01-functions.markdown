---
layout: lab
title: JavaScript For Loops
prefix: ../../
---
# Lab 9 - Part 2 - JavaScript Functions

In this lab, you'll be creating several programs:

1. greetings
2. pluralize 
3. \*factorial
4. \*prime


## Instructions

Note that __ALL OF THESE FILES MUST BE CREATED IN THE REPOSITORY THAT YOU CREATED FOR THIS LAB__.

### greetings

Write a program that says hello three times.

* using SublimeText, create a new file called __greetings.html__ in your repository directory: __~/Desktop/jversoza/lab-09-canvas/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should say "hello" three times in the JavaScript console
* do this by creating a function called greet
* greet will print out hello exactly once
* call the greet function three times
* use git status, add, commit, and push to save your file in version control and submit it
* example output below...

{% highlight bash %}
hello
hello
hello
{% endhighlight %}

<hr>

### pluralize

Write a program that creates a plural version of a word inputted by a user.

* using SublimeText, create a new file called __pluralize.html__ in your repository directory: __~/Desktop/jversoza/lab-09-canvas/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* define a function called pluralize
* it should have one parameter, word
* it should __give back__ a value - the plural version of the word passed in
* ask for a word: "Word please:"
* it should call your pluralize function
* pluralize will give back the word with an s appended to the end of it
* use the result of calling your pluralize function to print the plural version to the JavaScript console
* \*add an if-else-if statement to handle the following words: moose (moose), automaton (automata), mouse (mice)
* use git status, add, commit, and push to save your file in version control and submit it
* example interaction is below (everything after the greater than sign (&gt;) is user input using the prompt function):

{% highlight bash %}
(prompt) Word please:
> car
cars
{% endhighlight %}

<hr>

### factorial

Write a program that calculates the factorial of a number entered by the user.  Factorial is the product of all positive integers less than or equal to a number.  4! (or 4 factorial) = 4 * 3 * 2 * 1 = 24

* using SublimeText, create a new file called __factorial.html__ in your repository directory: __~/Desktop/jversoza/lab-09-canvas/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* define a function called factorial
* it should have one parameter, n
* it should __give back__ an number - the product of all positive numbers less than or equal to the user input
* ask for a word: "Number please::"
* it should then call your factorial function
* factorial will give back the result of the calculation
* use the result of calling your factorial function to print the factorial
* hint: use a for loop to do this
* example interaction is below (everything after the greater than sign (&gt;) is user input using the prompt function):

{% highlight bash %}
(prompt) Number please:
> 4
24
{% endhighlight %}
