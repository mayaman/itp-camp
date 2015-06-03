---
layout: slides
title: MTEC1002 - JavaScript Basics
---

<section markdown="block" class="title-slide">

# JavaScript Basics

{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Source Material

See the first two chapters of the second edition of [Eloquent JavaScript](http://eloquentjavascript.net/2nd_edition/preview/) for more detailed information:

* [Chapter 1 - Values](http://eloquentjavascript.net/2nd_edition/preview/01_values.html)
* [Chapter 2 - Program Structure](http://eloquentjavascript.net/2nd_edition/preview/02_program_structure.html)
</section>

<section markdown="block">
### JavaScript

__What's JavaScript?__ &rarr; 

<div class="incremental" markdown="block">
* __JavaScript__ is a __widely used__, __high-level__ programming language that is __available on many platforms__
* it was originally created in 1995 as a way to add interactivity (through programming) to web pages in __Netscape Navigator__!
* __JavaScript__ and __Java__ are two entirely different programming languages
</div>
</section>

<section markdown="block">
### Rationale for Using JavaScript

__Why are we learning JavaScript?__ &rarr;
s
<div class="incremental" markdown="block">
* we need _something_ to put into version control
* some understanding of basic JavaScript will be helpful in other classes, specifically with classes geared towards web development
* JavaScript is a __widely used__, __high-level__ programming language that is __available on nearly every platform__
* some people (_me_) think it's __fun__
</div>
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
</section>

<section markdown="block">
### Values, Types and Operators

The most basic elements of a JavaScript program are:

* values
* types
* operators
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
// Statement
1 + 5;

// Even these are statements:
1;
"hi";
{% endhighlight  %}
</section>

<section markdown="block">
## All statements end in a semicolon (;) in JavaScript
</section>

<section markdown="block">
### Values

__What's a value, and what are some examples of values in JavaScript?__ &rarr;

<div class="incremental" markdown="block">

* values are just data
* some examples of values are numbers, like 3.14 and -273 and strings, like "hello" and "hi"
* there are also special values like:
	* __Infinity__ (and negative Infinity!)
	* __NaN__ - not-a-number
	* __null/undefined__ - _absence of a value_
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

A __type__ is just a kind or category of value.  Here are three data types in JavaScript:

* __numbers__ - numeric data (clearly!)
* __strings__ - an ordered sequence of characters (alphanumeric, punctuation, spaces, etc.)
* __boolean__ values - true / false

A values types sometimes determines what we can and can't do with that value!
</section>

<section markdown="block">
### Operators

__What's an operator?__ &rarr;

<div class="incremental" markdown="block">

* operators allow us to combine and transform values
* operators have __operands__, 
	* operands are the values that supply to operators
	* __binary__ operators have two operands
	* __unary__ operators have one operand
* operators give back values... 
	* using operators with values yields other values!
</div>
</section>

<section markdown="block">
### Numbers

* numbers are just _numbers_
* you can represent 
	* positive and negative whole numbers: 23, 42, -10
	* decimals (with a period): 2.3, 4.2
* no need for commas
* JavaScript uses a fixed number of bits to store numbers: _64 bits_
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

__What is the resulting value of this expression?__ &rarr;

{% highlight html %}
6 + 20 % 8
{% endhighlight %}

<div class="incremental" markdown="block">
* order of operations: parentheses, exponents, multiplication, division, addition, subtraction (PEMDAS)
* modulo is the same precedence as multiplication and division
* answer is 10
</div>
</section>

<section markdown="block">
### Some Special Numbers...

* __Infinity, -Infintity__ - positive and negative infinities (don't use these, they're not that useful, and not mathematically solid!)
* __NaN__ (not-a-number) - this results from any numeric operation that doesn't give back a meaniingful result... such as 0/0

</section>


<section markdown="block">
### Strings

__What's a string, and give an example of a string literal__ &rarr;

<div class="incremental" markdown="block">
A __string__ is an ordered sequence of characters.  You can tell that a value is a string if it is surrounded by single or double quotes:

{% highlight html %}
"I am a string"
"I'm a string"
{% endhighlight %}
</div>

</section>

<section markdown="block">
## Quoted text is a string!
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
* typeof - gives the _type_ of a value (Number, String, etc.)

__Let's try some of these.__ &rarr;

{% highlight html %}
+10
typeof "hi there"
{% endhighlight %}

</section>

<section markdown="block">
### typeof

Again, __typeof__ is:

* an operator that takes one operand
* gives back the type of value the operand

__What are the types that we know?  What would we get with this code:__  &rarr;

{% highlight html %}
typeof "five"
typeof 5
typeof "5"
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

Comments allow the programmer to write notes that the JavaScript interpreter will skip over / ignore

* these are meant for humans to read, not the computer.
* you can comment by starting a line with //
* or by stopping and starting a series of lines with /\* \*/

{% highlight html %}
// a comment
/*
a long
comment
*/
{% endhighlight  %}
</section>

<section markdown="block">
### A Sample Program

__What do you think this program does?__ &rarr;
{% highlight html %}
<!DOCTYPE html>
<html>
<body>
<script>
var answer = prompt("Give me something to say twice:");
console.log(answer + " " + answer);
</script>
</body>
</html>
{% endhighlight  %}

__Let's write it together.__ &rarr;
</section>

