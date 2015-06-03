---
layout: lab
title: JavaScript Basics
prefix: ../../
---
# Lab 6 - JavaScript Basics

In this lab, you'll be creating several programs:

1. say twice
2. shout
3. temperature
4. miles
5. \* ...and a couple of challenging ones: numbers and tree

## Summary of Commands:

__THESE ARE NOT LAB INSTRUCTIONS.__

The following is just a reference.  The lab instructions are below.

{% highlight bash %}
# create a local repository
git init

# configure it with your name and email
git config user.name  "your name"
git config user.email "your@email.address"

# create a remote repository
curl -u 'your github user name' https://api.github.com/user/repos -d '{"name":"your repository name"}'

# link the two
git remote add origin "your username"@"the url to your repository on github"

# two ways to show all remote repositories
git remote -v
cat .git/config

# removing a remote repository by name (usually origin)
git remote remove name_of_remote

# changing / setting the url of a named remote repository (usually origin)
git remote set-url name_of_remote new_remote_url

# look at the differences between your last save and your current changes (line by line)
git diff --color

# check on the status of your changes
git status

# "stage" or mark your changes as ready to be saved
git add --all

# save!
git commit -m 'my message'

# show a log of your changes so far
git log --color (show your changes so far)

# send to a remote repository (to submit an assignment)
git push origin master 
{% endhighlight %}

## Instructions

Note that __ALL OF THESE FILES MUST BE CREATED IN THE REPOSITORY THAT YOU CREATED FOR THIS LAB__.

### say twice

Write a program that takes user input and repeats the user input twice (both words on the same lin) in the JavaScript console.

* using SublimeText, create a new file called __saytwice.html__ in your repository directory: __~/Desktop/jversoza/lab-06-javascript-conditionals/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should ask for a word: "Give me a word to say twice"
* the program should repeat the input twice on the same line with a space inbetween...  back to the __JavaScript console__ 
	* for example, if someone enters "hello" in the prompt dialog
	* the output in the console would be "hello hello"
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
(prompt) Give me a word to say twice
> hello
hello hello
{% endhighlight %}
* save your file in SublimeText
* use status, add commit and push to save your file in version control and submit it

<hr>

### shout

Write a program that takes user input and repeats the user input, but with three exclamation points afterwards. 

* using SublimeText, create a new file called __shout.html__ in your repository directory: __~/Desktop/jversoza/lab-06-javascript-conditionals/__
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
* save your file in SublimeText
* use status, add commit and push to save your file in version control and submit it
<hr>

### temperature

Write a program that calculates celsius to fahrenheit based on user input.

* using SublimeText, create a new file called __temperature.html__ in your repository directory: __~/Desktop/jversoza/lab-06-javascript-conditionals/__
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
* save your file in SublimeText
* use status, add commit and push to save your file in version control and submit it

<hr>

### miles

Write a program that calculates miles-per-gallon based on user input for miles driven and gallons of gas used.

* using SublimeText, create a new file called __miles.html__ in your repository directory: __~/Desktop/jversoza/lab-06-javascript-conditionals/__
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
* save your file in SublimeText
* use status, add commit and push to save your file in version control and submit it

<hr>

### \*numbers
(This one's hard!) Write a program that outputs the number in the thousands, hundreds, tens and ones places of a number. 

* using SublimeText, create a new file called __numbers.html__ in your repository directory: __~/Desktop/jversoza/lab-06-javascript-conditionals/__
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
* save your file in SublimeText
* use status, add commit and push to save your file in version control and submit it

<hr>

### \*tree

(This one's slightly hard... try doing it in just one line!) Print out a tree!

* using SublimeText, create a new file called __tree.html__ in your repository directory: __~/Desktop/jversoza/lab-06-javascript-conditionals/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* print out an ascii art tree to the JavaScript console
<pre>
   /\
  /  \
  /  \
 /____\
   ||
</pre>
* save your file in SublimeText
* use status, add commit and push to save your file in version control and submit it
