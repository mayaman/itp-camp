---
layout: slides
title: MTEC1002 - Version Control Review
---

<section markdown="block" class="title-slide">

# Submitting Assignments, JavaScript Review

{% include title-slide-footer.html %}
</section>

<section markdown="block">
## Version Control!
</section>

<section markdown="block">
### About Repositories

What is a __repository__, __local repository__, __remote repository__, __commit__, and __diff__? &rarr;

<div class="incremental" markdown="block">

* __repository__ - the place where your version control system stores the snapshots that you _save_
* __local repository__ - the repository on your computer
* __remote repository__ - a copy of versions of your files on another computer
* __commit__ - save a snapshot of your work
* __diff__ - the line-by-line difference between two files or sets of files
</div>
</section>

<section markdown="block">
### Changing and Saving Files

In your __local repository__, describe what is contained in the: __working directory__, __index__ and __HEAD__. &rarr;

<div class="incremental" markdown="block">
* __the working directory / working copy__ - stuff you've changed but haven't saved
* __index__ - stuff that you're about to save (staging area)
* __HEAD__ - stuff that you've already saved
</div>
</section>

<section markdown="block">
### How Do We Use Git?

__What is the primary way that we use git?  That is, what is the root command, and what can we do with it? "Where" do you have to be to use git?__ &rarr;

<div class="incremental" markdown="block">
* we use __git__ through the __commandline__ 
* the base command is __git__ followed by a specific _git command_
* these commands/actions only work when __you're in a git repository__
* (that is, you have to cd to the directory that contains your repository)

</div>
</section>

<section markdown="block">
## All git commands must be run in your repository directory (where you ran git init)
</section>

<section markdown="block">
### Commands for Setting Up Repositories

__What are the actual commands that you would use to set up and link your repositories?__ &rarr;

<div class="incremental" markdown="block">
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
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Commands for Saving and Sharing Changes

__What's are the actual commands that you use for making, saving and sharing changes?  Let's start with just making the change and prepping it to be saved.__ &rarr;

<div class="incremental" markdown="block">

{% highlight bash %}
# (make changes)

# show the exact, line-by-line changes that you've made
git diff --color

# check on the status of your changes
git status

# stage your changes / prep them to be saved
git add --all 

# check your staged changes using git status again
git status

# (continued...)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Saving and Sharing Continued...

__Saving and sending to the remote repository__ &rarr;

<div class="incremental" markdown="block">
{% highlight bash %}

# save them, make sure you remember your comment by using -m!
git commit -m 'my message'

# show a history of your changes
git log --color (show your changes so far)

# send to your remote repository
git push origin master
{% endhighlight %}
</div>
</section>





<section markdown="block">
### git status

__What does git status do?__ &rarr;

<div class="incremental" markdown="block">
__git status__ - show what changes are ready to be committed as well as changes that you are working on in your working directory that haven't been staged yet

</div>
</section>

<section markdown="block">
### git add

__What does git add do? Does it take any arguments or does it have flags?__ &rarr;

<div class="incremental" markdown="block">
__git add__ marks a file or files as ready to be saved.  

{% highlight bash %}
# add all to stage all of your changes
git add --all 

# add a path to a file to add a specific file
git add relative/path/to/myfile.txt
{% endhighlight %}
</div>
</section>

<section markdown="block">
### git commit

__What does git commit do? Does it take any arguments or does it have flags?__ &rarr;


<div class="incremental" markdown="block">
__git commit__ _saves_ your changes to your local repository.

{% highlight bash %}
# in the directory of your repository
git commit -m 'commit message goes here'
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Showing and Getting Rid of Remote Repositories

How do you... __Show your remote repository names and urls?__ __...and how do you  get rid of remote repositories?__ &rarr;

<div class="incremental" markdown="block">
{% highlight bash %}
# show remote repositories
git remote -v

# The output should look something like...
# origin	https://jversoza@github.com/jversoza/lab-07-javascript-conditionals.git (fetch)
# origin	https://jversoza@github.com/jversoza/lab-07-javascript-conditionals.git (push)

# remove remote repository (assuming remote repository name is origin)
git remote remove origin
{% endhighlight %}
</div>

</section>

<section markdown="block">
### Troubleshooting

If you have trouble sending your changes to github, make sure your remote repository url is correct...

{% highlight bash %}
# show remote repositories
git remote -v

# should give back something like...
# origin	https://jversoza@github.com/jversoza/lab-07-javascript-conditionals.git (fetch)
# origin	https://jversoza@github.com/jversoza/lab-07-javascript-conditionals.git (push)

# remove remote repository (assuming remote repository name is origin)
git remote remove origin

# add new remote
git remote add origin https://jversoza@github.com/jversoza/lab-07-javascript-conditionals.git
{% endhighlight %}
</section>

<section markdown="block">
## JavaScript!
</section>

<section markdown="block">
### Running JavaScript Programs

__What application / tool do we use to run our programs?__ &rarr; 

<div class="incremental" markdown="block">
* we'll be using our web browser to run JavaScript programs!
* specifically, we'll be using Chrome and Chrome's __JavaScript Console__
</div>
</section>

<section markdown="block">
### JavaScript Programs - File Format

__What kind of file will we save our programs in (as in, what extension should we use, what's the file type)?__ &rarr;

<div class="incremental" markdown="block">
* because we're targeting Chrome and Chrome's __JavaScript Console__ to run our programs, we'll be writing our JavaScript in web pages
* that means editing plain text files 
* specifically,files that that end in __.html__ (web pages)
	* it's actually not good practice to have JavaScript code interspersed with your html, but for our purposes of getting started it's ok
</div>
</section>

<section markdown="block">
### A Template for Our Programs

__What do we have to put in our .html file before we can write our JavaScript__ &rarr;

<div class="incremental" markdown="block">
We'll have to create a bare bones web page:

{% highlight html %}
<!DOCTYPE html>
<html>
<body>
<script>
// your JavaScript goes here!
</script>
</body>
</html>
{% endhighlight  %}

__Your code goes within the script tags!__
</div>
</section>

<section markdown="block">
### Creating JavaScript Programs

__What tool do we use to write our JavaScript programs?__ &rarr;

<div class="incremental" markdown="block">

* we use a text editor called __SublimeText__
* if we save the file as some_file_name.html (note the __.html__ extension) before writing...
* we can use TAB to automplete:
	* start typing html... and hit TAB
	* you'll still need to fill in the script tags
* (again, your code goes between the script tags)
</div>
</section>

<section markdown="block">
### Running a Program in Chrome

__How do we actually run our JavaScript programs in Chrome?  Where does the output (and errors) from your program show up?__ &rarr;

<div class="incremental" markdown="block">

* In __Chrome__... go to File &rarr; Open File ... &rarr; browse to the html file you created in SublimeText
* you'll see output and errors pop up in __Chrome's JavaScript Console__
* (you can get to this by going to View &rarr; Developer &rarr; JavaScript Console)
* if you make changes to your original file, just refresh the page (Command + r)

</div>
</section>


<section markdown="block">
### Trying One Line at a Time

__How do we try out single lines of JavaScript without writing an entire html file?__ &rarr;

<div class="incremental" markdown="block">

* once again, we can use Chrome's JavaScript console; it lets you try out lines of JavaScript one line at a time interactively
* you can use this to experiment with code
* it has access to everything else in the page (we'll see this later)
* it will give you instant feedback with each line you type
</div>
</section>

<section markdown="block">
### The JavaScript Console

Chrome's JavaScript Console is multi-purpose.  __What are the ways that we can use it?__ &rarr;

<div class="incremental" markdown="block">
* shows the output of your program
* displays errors from your program
* allows you to interactively execute single lines of code on the page that you're on
* ...and later, we'll see that we can use it to debug our programs
</div>

</section>

<section markdown="block">
## JavaScript Basics...

<!--
* what types do we know
	* what are some examples of each?
* what operators do we know
* put together expressions using variables, values and operators
* put together  statements
* built in functions
	* console.log
	* prompt()
* sample program.... double a number that's entered... using a temporary variable
-->
</section>


<section markdown="block">
### Data Types and Values

__What's a value and what's a data type?__ &rarr;

<div class="incremental" markdown="block">

* values are just data - for example: 3.14, "hello"
* a __type__ is just a kind or category of value.  
</div>
</section>

<section markdown="block">
### Creating Values

__How do we create a value in our program?__ &rarr;

<div class="incremental" markdown="block">

* to create values, just write them!
* for example: 7 ... or "hello there"
* values that are written plainly like this are called __literals__
</div>
</section>

<section markdown="block">
### Data Types


__What are some data types that we know?__ &rarr;

<div class="incremental" markdown="block">
* __number__ - numeric data (clearly!)
* __string__ - an ordered sequence of characters (alphanumeric, punctuation, spaces, etc.)
* __boolean__ values - true / false
* there's also __undefined__... when we try to use a variable that hasn't been created yet
</div>

</section>

<section markdown="block">
### Data Types

A value's data __type__ determines how that value behaves when used in functions or transformed/combined with __operators__.

</section>

<section markdown="block">
### Numbers

* numbers are, of course,  _numbers_
* including... positive and negative whole numbers: 23, 42, -10
* as well as decimals (with a period): 2.3, 4.2
* no need for commas
* JavaScript uses a fixed number of bits to store numbers: _64 bits_
</section>


<section markdown="block">
### Some Special Numbers...

__Are there any special values for numbers other than actual integer and floating point numbers?__ &rarr;

<div class="incremental" markdown="block">
* __Infinity, -Infintity__ - positive and negative infinities (don't use these, they're not that useful, and not mathematically solid!)
* __NaN__ (not-a-number) - this results from any numeric operation that doesn't give back a meaniingful result... such as 0/0
</div>

</section>

<section markdown="block">
### Strings

__What's a string, and give an example of a string literal__ &rarr;

<div class="incremental" markdown="block">
A __string__ is an ordered sequence of characters.  You can tell that a value is a string if it is surrounded by single or double quotes:

{% highlight html %}
"I'm a string"
'I\'m a string'
{% endhighlight %}
</div>

</section>


<section markdown="block">
### Empty Strings

__What's an empty string?__ &rarr;

<div class="incremental" markdown="block">
* a __string__ can be composed of _any_ characters: numbers, letters, punctuation, spaces, etc. ... and it can even be empty
* string with nothing in it is an __empty string__:

{% highlight html %}
""
{% endhighlight %}
</div>

</section>

<section markdown="block">
### Escape Characters

__How do we write a backslash, quote, tab or a new line in a string?__ &rarr;


<div class="incremental" markdown="block">
* use the escape character, backslash (\\)
* if there is a backslash in a string (\\), it means:
	* the next character has a special meaning
	* the initial backslash will not be printed out
* for example, backslash, quote, tab and newline:

{% highlight html %}
"\\"
"\""
"\t" 
"\n"
{% endhighlight %}
</div>

</section>


<section markdown="block">
### Operators

__What's an operator and what are some examples of operators?__ &rarr;

<div class="incremental" markdown="block">

* operators allow us to combine and transform values
* operators have __operands__, 
	* __operands__ are the values that supplied to operators
	* __binary__ operators have two operands
	* __unary__ operators have one operand
* __operators give back values__ 
	* using operators with values yields other values!
</div>
</section>

<section markdown="block">
### Numeric Operators

__Name 5 binary arithmetic operators (they take two operands, one on either side)__ &rarr;

<div class="incremental" markdown="block">

* __+__ - addition
* __-__ - subtraction
* __\*__ - multiplication
* __/__ - division
* __%__ - modulo (remainder operator)
</div>

</section>

<section markdown="block">
### Numeric Operators and Precedence

* order of operations: parentheses, exponents, multiplication, division, addition, subtraction (PEMDAS)
* modulo is the same precedence as multiplication and division
</section>



<section markdown="block">
### String Operators

__We learned about one operator that works on strings.  What was it?__ &rarr;

<div class="incremental" markdown="block">
__string concatenation__, or __+__, is an operator that takes two strings and joins them:

{% highlight html %}
"hello " + "there"
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Unary Operators

Unary Operators only have a single operand to the right:

* __+__ - convert to positive number
* __-__ - convert to negative number

__What's the operator that gives back the type of a value?__ &rarr;

<div class="incremental" markdown="block">
__typeof__ - gives the _type_ of a value (Number, String, etc.)
</div>

</section>

<section markdown="block">
### typeof

Again, __typeof__ is:

* an operator that takes one operand
* gives back the type of value the operand

__What are the types that we know?  What would we get with this code:__  &rarr;

{% highlight html %}
typeof true
typeof "10"
{% endhighlight %}

<div class="incremental" markdown="block">
* we know three types: strings, numbers, and booleans)
* string, number and string
</div>

</section>

<section markdown="block">
### Functions

__What's a function?  What's a function call?  What are arguments?__ &rarr;

<div class="incremental" markdown="block">
* a __function__ is a named sequence of statements that perform some useful action
* it can __optionally__ take __inputs__ and __return values__
* to __call__ a function is just to _run_ or _execute_ it
* the values passed to a function are called __arguments__
</div>
</section>

<section markdown="block">
###  Calling Functions

__How do you call _or execute_ a function?__ &rarr;

<div class="incremental" markdown="block">
* to call a function, use its name followed by parentheses... with an optional list of comma separated arguments between the parentheses
* an example of a function call is:

{% highlight html %}
prompt("hello") is a function call
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Built-in Functions

JavaScript comes with several built in functions.  We learned two of them.  __What are they and what do they do?__ &rarr;

<div class="incremental" markdown="block">
* __prompt("some message")__ - asks the user for input and __returns__ that value to your program! ... takes a single argument, the message to display to a user (this usually requires the use of _variables_)
* __console.log("some message")__ - prints the argument that you pass to it... out to Chrome's JavaScript console 
</div>
</section>


<section markdown="block">
## Values, Operators and Functions can be Combined to Make Expressions
</section>

<section markdown="block">
### What Exactly is a Program?

__What's a program?  What's a statement?  What's an expression?__ &rarr;

<div class="incremental" markdown="block">

* __program__ - a sequence of statements that specify to a computer actions to perform
* __statement__ - corresponds to a sentence... it's a full instruction for the computer... __all statements end in a semicolon__ in JavaScript (;)
* __expression__ - a fragment of code that produces a value; it's not a statement by itself
</div>
</section>

<section markdown="block">
### Expressions and Statements Continued

{% highlight html %}
# the entire line below is a statement
var x = 1 + 5;

# 1 + 5 in the statement above is just an expression... that produces a value
{% endhighlight  %}
</section>

<section markdown="block">
## All statements end in a semicolon (;) in JavaScript
</section>


<section markdown="block">
### Variables

__What are variables and how do you use them in JavaScript?__ &rarr;

<div class="incremental" markdown="block">
* __variables__ are names bound to values:  
* you can use a variable's name wherever you want to use that value.
* to create a variable, use the special word, var, followed by =, then the value, and finally a semicolon

{% highlight html %}
var x = 23;

// using that variable
console.log(x + 7);
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Using Prompt With Variables

Remember that the function prompt gives back a value.  To retain that value, you have to hold it in a variable:

{% highlight html %}
var answer = prompt("Yes or no!?");
{% endhighlight  %}

</section>

<section markdown="block">
### Comments

Comments allow the programmer to write notes that the JavaScript interpreter will skip over / ignore.  __How do you specify a comment in your program?__ &rarr;

<div class="incremental" markdown="block">
{% highlight html %}
// a comment
/*
a long
comment
*/
{% endhighlight  %}
</div>

</section>

<section markdown="block">
### Let's Write a Program That...

* asks the user for a number
* doubles the number and saves it in a variable
* prints out the new number to the JavaScript console

</section>

<section markdown="block">
### A Potential Solution

{% highlight html %}
<!DOCTYPE html>
<html>
<body>
<script>
var num = prompt("Give me a number; I'll double it");
var twice_the_num = num * 2;
console.log(twice_the_num);
</script>
</body>
</html>
{% endhighlight  %}
</section>
