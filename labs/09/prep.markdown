---
layout: slides
title: MTEC1002 - Prep, Review
---

<section markdown="block" class="title-slide">

# Prep, Review

{% include title-slide-footer.html %}
</section>

<section markdown="block">
## Quick Rundown of Git Commands 
</section>

<section markdown="block">
### Git - Setting Up Repositories

__What are the commands that you would use to set up and link your repositories?__ &rarr;

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
### Git - Saving and Sharing Changes

__What's are the commands that you would use for making, saving and sharing changes?  Let's start with just making the change and prepping it to be saved.__ &rarr;

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
### Git - Saving and Sharing Continued...

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
### Showing and Getting Rid of Remote Repositories

How do you __show remote repository names and urls... and how do you get rid of remote repositories?__ &rarr;

<div class="incremental" markdown="block">
{% highlight bash %}
# show remote repositories
git remote -v

# The output should look something like...
# origin	https://jversoza@github.com/jversoza/lab-08-prep.git (fetch)
# origin	https://jversoza@github.com/jversoza/lab-08-prep.git (push)

# remove remote repository (assuming remote repository name is origin)
git remote remove origin
{% endhighlight %}

__And how do you add back a remote repository?__

{% highlight bash %}
git remote add origin https://jversoza@github.com/jversoza/lab-08-new.git
{% endhighlight %}
</div>
</section>

<section markdown="block">
## JavaScript
</section>


<section markdown="block">
### A Template

__What kind of file and what set up do we have write in order to start a new JavaScript program?__ &rarr;

<div class="incremental" markdown="block">
We have to create a bare bones web page, an __.html__ file:

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
### Data Types and Values

__What's a value and what's a data type?__ &rarr;

<div class="incremental" markdown="block">

* values are just data - for example: 3.14, "hello"
* a __type__ is just a kind or category of value.  
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

Numbers can be positive or negative rational numbers, like 23, -42 and 3.14.  __However, there are also some special values that are numbers.  What are they, and how do you get them?__ &rarr;

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
"Surrounded by quotes!"
{% endhighlight %}

__What's an empty string?__ &rarr;

* an __empty string__ is a string with nothing in it - just two consecutive quotes

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
### Booleans

__What's a boolean?__ &rarr; 

<div class="incremental" markdown="block">
A boolean value is a data type with only two possible values:

{% highlight js %}
true
false
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

__Name 5 binary arithmetic operators (they take two operands, one on either side), and their precedence__ &rarr;

<div class="incremental" markdown="block">

* __+__ - addition
* __-__ - subtraction
* __\*__ - multiplication
* __/__ - division
* __%__ - modulo (remainder operator)
* order of operations: parentheses, exponents, multiplication, division, (modulo),  addition, subtraction (PEMDAS)
</div>
</section>

<section markdown="block">
### String Operators

__We learned one operator that works on strings.  What was it?__ &rarr;

<div class="incremental" markdown="block">
__string concatenation__, or __+__, is an operator that takes two strings and joins them:

{% highlight html %}
"hello " + "there"
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Comparison Operators

Name some __comparison__ operators that __return__ boolean values... &rarr;

<div class="incremental" markdown="block">
* __===__ - equals - checks if both operands are the __same value and type__
	* gives back true if both are the same value and type
	* gives back false otherwise
* __!==__ - not equals - checks if the operands are __not the same value or type__
	* gives back true if both operands are not the same value or type
	* gives back false otherwise
</div>
</section>

<section markdown="block">
### Even More Comparison Operators

* __&lt;__ - less than
* __&gt;__ - greater than 
* __&lt;=__ - less than or equal to
* __&gt;=__ - greater than or equal to
</section>

<section markdown="block">
### Logical Operators

Name some __logical__ operators that allow you to __combine boolean values__. &rarr;

<div class="incremental" markdown="block">
* __and__ (represented as __&amp;&amp;__) - takes two operands.  
	* only gives back true when both operands are true.
	* gives back false otherwise
* __or__ (represented as __&#124;&#124;__) - takes two operands. 
	* returns true if either operand is true
	* it only gives back false when both operands are false.
* __and is evaluated before for__
</div>
</section>

<section markdown="block">
### Boolean Expressions

You can create boolean expressions with comparison and logical  operators.  __What is the value that results from the following expressions?  What type are they?__ &rarr;

{% highlight js %}
24 !== "hello"
5 === "5"
true && false
false || true
{% endhighlight %}


<div class="incremental" markdown="block">
{% highlight js %}
true
false
false
true
{% endhighlight %}
</div>
</section>

<section markdown="block">
### More Boolean Expressions

{% highlight js %}
true || false && false
5 < 2 || 8 > 20
{% endhighlight %}

{% highlight js %}
var login = 'albert';
var password = 'secret';
login === 'albert' || password == 'secret'
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight js %}
true
false
true
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Not

There's one more logical operator, __not__. 

* only takes one operand, a boolean
* gives back the opposite boolean value
* __not__ is represented by an exclamation point - __!__

{% highlight js %}
! true
! (5 > 10)
! (true && true)
{% endhighlight %}
</section>

<section markdown="block">
## Boolean Expressions Give Back Boolean Values!
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
typeof -12
typeof "98.6"
typeof (20 === 20)
typeof NaN
{% endhighlight %}

<div class="incremental" markdown="block">
* we know three types: strings, numbers, and booleans
* number, string, boolean, number
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
## When you see parentheses - ( )'s - after a function name, that function is being _called_ or _executed_
</section>

<section markdown="block">
### Built-in Functions

JavaScript comes with many built-in functions.  __We know three; what are they and what do they do?__ &rarr;

<div class="incremental" markdown="block">
* __prompt("some message")__ - asks the user for input and __returns__ that value to your program! ... takes a single argument, the message to display to a user (this usually requires the use of _variables_)
* __console.log("some message")__ - prints the argument that you pass to it... out to Chrome's JavaScript console 
* __parseInt("5")__ - converts a string to a number
</div>
</section>

<section markdown="block">
### Some Functions Return Values

__What type of value does prompt always return?  What type of value does parseInt always return?__  &rarr;

<div class="incremental" markdown="block">
* __prompt__ always gives back a __string__
* __parseInt__ always gives back a __number__
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
## Conditionals
</section>

<section markdown="block">
### Blocks of Code

Curly braces denote statements of code that are grouped together.  Everything within the curly braces below is considered part of the if statement.  Blocks of code must __start and end__ with curly braces...

{% highlight js %}
... {
	// code wrapped by curly braces
} 
{% endhighlight %}

</section>

<section markdown="block">
### Conditionals...

__What kind of statement would we use to execute code if a condition is true?__ &rarr;

<div class="incremental" markdown="block">

An if statement...

{% highlight js %}
if (some_boolean_expression) {
	// do stuff here if expression is true
}
{% endhighlight %}

* [Diagram for if statements](../../resources/img/if.png)
* [Diagram for consecutive if statements](../../resources/img/if-consecutive.png)
</div>

</section>

<section markdown="block">
### Conditionals Continued

__What kind of statement would we use to execute code one branch of code if a condition is true and another branch of code otherwise?__ &rarr;

<div class="incremental" markdown="block">

* an if / else statement  
* an else must always have a preceding if!

{% highlight js %}
if (some_boolean_expression) {
	// do stuff here if expression is true
} else {
	// do stuff here if expression is false
}
{% endhighlight %}

* [Diagram for if / else statements](../../resources/img/if-else.png)
* else statements are always attached to an if!
</div>

</section>

<section markdown="block">
### If / Else If

__What kind of statement would we use to execute multiple branches of code based on multiple chained conditions?__ &rarr;


<div class="incremental" markdown="block">
Use if / else if statements

{% highlight js %}
if (boolean_expression_1) {
	// do stuff here if expression 1 is true
} else if (boolean_expression_2) {
	// do stuff here if expression 2 is true
} else if (boolean_expression_3) {
	// do stuff here if expression 3 is true
}
{% endhighlight %}

* [Diagram for if / else if statements](../../resources/img/if-else-if.png)
</div>
</section>

<section markdown="block">
### If / Else If

* once a condition is true, the if / else if executes the code in that block and the if / else if ends immediately (even if other later conditions are true)
* can end with else to handle all _other_ conditions
</section>


<section markdown="block">
### Usage

* use if statements if there's a single alternative path of execution
* use if/else  statements if there's a two possible alternative paths of execution
* use if/else if statements if there's more than two possible alternative paths of execution
</section>

<section markdown="block">
### Repeat That Again?

__What construct do we use if we want to execute a block of code multiple times without writing it multiple times?__ &rarr;

<div class="incremental" markdown="block">
* we use a for loop!
* __what does a for loop look like... what are its parts?__ &rarr;
</div>
</section>

<section markdown="block">
### For Loop Dissected

A for loop consists of the keyword, __for__, and three parts, separated by a semicolon,  contained within parentheses:

* initialization - declares a variable and value to start with
* condition - a condition for the loop to stop 
* _afterthought_ - a way to increment/decrement or change the variable on each iteration so that the condition is eventually met

You can use the variable that you declare in the initialization within your for loop!
</section>

<section markdown="block">
### For Loop Parts

{% highlight js %}
//    initialization
//    |        condition
//    |        |       afterthought/increment
//    |        |       |
for(var i = 0; i <= 5; i = i + 1) {
	console.log(i);
}
{% endhighlight %}
</section>

<section markdown="block">
### Counting By 3's 

__Create a for loop that counts from 0 up to and including 9 by 3's?__ &rarr;

<div class="incremental" markdown="block">
{% highlight js %}
for(var i = 0; i <= 9; i = i + 3) {
	console.log(i);
}

{% endhighlight %}
</div>
</section>


