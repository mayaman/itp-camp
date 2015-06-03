---
layout: lab
title: JavaScript Basics
prefix: ../../
---
# Homework


1. shout
2. temperature
3. madlibs and madlibs with prompt

## Instructions


### shout

Write a program that takes user input and repeats the user input, but with three exclamation points afterwards. 

* create a new file called __shout.html__ 
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should ask for a word: "Give me a word, and I'll shout it out"
* the program should repeat the word, but with three exclamation points added to it
* the output should go to the __JavaScript console__ 
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
(prompt) Give me a word, and I'll shout it out
> yeah
yeah!!!
{% endhighlight %}

<hr>

### temperature

Write a program that calculates celsius to fahrenheit based on user input.

* create a new file called __temperature.html__ 
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should ask for the temperature in celsius
* find the formula for celsius to faahrenheit conversion online!
* translate that formula into javascript 
* the program should output to the __JavaScript console__: c degrees celsius is f degrees fahrenheit
* (obvs with f and c substituted with the appropriate calculated values)
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
(prompt) Please enter a temperature in celsius
> 37
37 degrees celsius is 98 degrees fahrenheit
{% endhighlight %}

<hr>

### madlibs

Write a program that simulates MadLibs!  It will ask your for words, and then it will print out a story (in this case lyrics), with the user entered words substituted for words in the story.

Part 1

* create a new file called __madlibs.html__ 
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* define 4 variables, set them each equal to a word: a noun, an adjective, an adverb and a verb
* name the variables after the part of speech of the word they are replacing, for example
{% highlight html %}
var noun = 'pizza';
var noun = 'ukulele';
{% endhighlight %}
* write program that __uses those 4 variables__ in these lyrics:
{% highlight bash %}
On a tropical island,
Underneath a molten lava moon.
Hangin' with the hula dancers,
Askin' questions cause' they got all the answers.
{% endhighlight %}
* substitute any words you'd like to change
* use string concatenation to stitch together the lyrics
* print out the new version of lyrics, each line on a separate line
* for example, the __JavaScript console__ may display:
{% highlight bash %}
On a tropical pizza,
Underneath a molten ...
{% endhighlight %}

Part 2

* modify your program so that it asks for user input for each variable (don't use hardcoded values anymore)
* this should result in 4 dialog boxes
* and the result of the new lyrics printed out to the __JavaScript console__

