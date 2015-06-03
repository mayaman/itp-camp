---
layout: lab
title: JavaScript Conditionals
prefix: ../../
---
# Lab 6 - JavaScript Conditionals

In this lab, you'll be creating several programs:

1. cake
2. spanish
3. \* guess 

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

### cake

Write a program that asks the user if they want cake.  Based on the response, it will output a different message to the JavaScript Console.

* using SublimeText, create a new file called __cake.html__ in your repository directory: __~/Desktop/jversoza/lab-06-javascript-conditionals/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should ask: "Do you want cake?"
* based on the user's input:
	* print out "Have some cake." if the user says exactly "yes"
	* print out "No cake for you" if the user says anything other than "yes"
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
# Run 1
(prompt) Do you want cake?
> yes
Have some cake.
# Run 2
(prompt) Do you want cake?
> maybe
No cake for you.
{% endhighlight %}
* save your file in SublimeText
* use status, add commit and push to save your file in version control and submit it
* modify your program so that the program accepts no as an answer, and says something different if it is not yes and not no:
	* print out "Have some cake." if the user says exactly "yes"
	* print out "No cake for you." if the user says exactly "no"
	* print out "I don't understand." if the user types anything else"
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
# Run 1
(prompt) Do you want cake?
> no
No cake for you
# Run 2
(prompt) Do you want cake?
> maybe
I don't understand
{% endhighlight %}
* save your file in SublimeText
* use status, add commit and push to save your file in version control and submit it

<hr>

### spanish

Write a program that translates english words to Spanish.

* using SublimeText, create a new file called __spanish.html__ in your repository directory: __~/Desktop/jversoza/lab-06-javascript-conditionals/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should ask for a word: "Give me a word in English..."
* based on the user's input:
	* output "gato" if the user says "cat"
	* output "pero" if the user says "dog"
	* output "caballo" if the user says "horse"
	* output "no se" if the user says anything else
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
# Run 1
(prompt) Give me a word in English...
> gato
cat
# Run 2
(prompt) Give me a word in English...
> bear
no se
{% endhighlight %}
* save your file in SublimeText
* use status, add commit and push to save your file in version control and submit it
`
<hr>

### guess

Write a number guessing game!  "Hardcode" a secret number.  Ask the user to guess the secret number.  If they are correct, say "You got it!".  If they are within 1, say "Close, but the number is (the secret number)".  Lastly, if they were totally incorrect, then say, "The number is (the secret number)".  Look up the parseInt function to convert the input into a number so that your comparisons work.

