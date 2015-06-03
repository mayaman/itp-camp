---
layout: slides
title: JavaScript Basics
---

<section markdown="block" class="title-slide">

# JavaScript Basics

{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Some Readings

Most of the material in these slides is based on the frist two chapters of the second edition of [Eloquent JavaScript](http://eloquentjavascript.net/2nd_edition/preview/):

* [Chapter 1 - Values](http://eloquentjavascript.net/2nd_edition/preview/01_values.html)
* [Chapter 2 - Program Structure](http://eloquentjavascript.net/2nd_edition/preview/02_program_structure.html) (up to control flow)
</section>

<section markdown="block">
### A Quick Note on Writing JavaScript

* our primary mode of writing JavaScript for this lab will be in a text editor
* the JavaScript that we create will run in a web page, so they'll have to live in __an html file__ 
* your code goes __within the script tags__ of that file
* here's a sample file again... (note that all of the tags are boilerplate for now)
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

</section>

<section markdown="block">
### Running Your Programs

__We'll run our programs in our web browser!__

* because we're running JavaScript within a web page, we'll need a browser to run our programs
* we're using __Chrome__... so just go to File &rarr; Open File ... &rarr; browse to the html file you create
* you'll see output and errors pop up in the JavaScript console
* (you can get to this by going to View &rarr; Developer &rarr; JavaScript Console)
* if you make changes to your original file, save it and refresh the page (Command + r)

__Let's see how that works.__ &rarr;
</section>

<section markdown="block">
### Trying One Line at a Time

The JavaScript console also lets you try out lines of JavaScript one line at a time interactively.

* you can use this to experiment with code
* it has access to everything else in the page (we'll see this later)
* it will give you instant feedback with each line you type

__Let's check out the interactive part of the JavaScript console.__ &rarr;

</section>

<section markdown="block">
### The JavaScript Console

As you can see, Chrome's JavaScript console is multi-purpose.  __What are the ways that we can use it?__ &rarr;

<div class="incremental" markdown="block">
* shows the output of your program
* displays errors from your program
* allows you to interactively execute single lines of code on the page that you're on
* ...and later, we'll see that we can use it to debug our programs
</div>

</section>


<section markdown="block">
### Ok.  On to JavaScript...

* values
* types
* operations
* variables
* calling functions 
* input/output
* \*comments
</section>

<section markdown="block">
### Values

__Values__ are just data.  Some examples of data we'll see in JavaScript are:

* numbers, like <code>42</code>, <code>3.0</code>, <code>-1</code>
* sequences of characters, like <code>"Hi there!"</code>
* ...and other special values:
	* __true__ and __false__
	* __Infinity__ (and negative Infinity!)
	* __NaN__ - not-a-number
	* __null/undefined__ - _absence of a value_
</section>


<section markdown="block">
### Values in Programs

* examples of values in programs include 42 and "hello there"...
* to create values, just write them!
* writing 42 in the console magically creates a value in memory!
* values that are written plainly like this are called __literals__
* this is also sometimes called __hardcoding__ values
</section>

<section markdown="block">
### Types

So, values can be categorized by the _kind_ of value that they are. For example, <code>42</code> and <code>3.14</code> are numeric values.

We'll look at these 3 __data types__ to begin with (JavaScript has more, and we'll look at those later)

* __numbers__ - numeric data (surprise!)
* __strings__ - an ordered sequence of characters (alphanumeric, punctuation, spaces, etc.)
* __boolean__ values - true / false
</section>

<section markdown="block">
### Numbers

* unsurprisingly, numbers are just _numbers_
* you can represent 
	* positive and negative whole numbers: 23, 42, -10
	* decimals (with a period): 2.3, 4.2
* no need for commas
* JavaScript uses a fixed number of bits to store numbers: _64 bits_
</section>

<section markdown="block">
### 64 Bits?

__What format do computers use to deal with data?__ &rarr;

<div class="incremental" markdown="block">
Binary (or base 2) numbers!

A __bit__ is a single binary digit.  __How many values do you think a single bit can hold, and what are those possible values?__ &rarr;

A single bit can hold 2 values: __0__ or __1__

</div>
</section>

<section markdown="block">
### 64 Bits? Continued

__How many values can we _encode_ into 2 bits?__ &rarr;

<div class="incremental" markdown="block">
4 values... or 2 to the 2nd power: 00, 01, 10, 11.  __How about 3 bits?__ &rarr;

8 values... or 2 to the 3rd power: 000, 001, 010, 011, 100, 101, 110, 111.  __See a pattern?__ &rarr;
</div>
</section>

<section markdown="block">
### 64 Bits? Finale

__So how many values can 64 bits hold?__ (Um... a lot?) &rarr;

<div class="incremental" markdown="block">
2 the power of 64!  Which is about 18 with 18 0's after it. __However, this doesn't necessarily mean we can use 2 to the 64 as a number...__ &rarr;

This just means that number of possible values.  This has to include negative numbers, decimals, etc...
</div>
</section>

<section markdown="block">
### Operators

* Using operators with values yield values!
* We're familiar with some numeric operators... __what are they?__ &rarr;
</section>

<section markdown="block">
### Numeric Operators

Some binary arithmetic operators (they take two operands, one on either side)

* __+__ - addition
* __-__ - subtraction
* __\*__ - multiplication
* __/__ - division
* __%__ - modulo (remainder operator)

__Let's try some of these out.__ &rarr;
</section>

<section markdown="block">
### Numeric Operators, Precedence

__What order would I evaluate this in?  What is the resulting value?__ &rarr;

{% highlight html %}
4 + 1 * 5
{% endhighlight %}

<div class="incremental" markdown="block">
* remember PEMDAS? (modulo is the same precedence as multiplication)
* multiplication first
* then addition
* result is 9
</div>
</section>

<section markdown="block">
### Strings

A __string__ is an ordered sequence of characters.  You can tell that a value is a string if it is surrounded by single or double quotes:

{% highlight html %}
"I am a string"
"I'm a string"
{% endhighlight %}

</section>

<section markdown="block">
## Quoted text is a string!
</section>

<section markdown="block">
### Strings Continued

A __string__ can be composed of _any_ characters: numbers, letters, punctuation, spaces, etc.

The following is a string with nothing in it... or an __empty string__:
{% highlight html %}
""
{% endhighlight %}


</section>

<section markdown="block">
### Escape Characters

If there is a backslash in a string (\\), that means:

* the next character has a special meaning
* the initial backslash will not be printed out

For example, __\\n__ is a newline
{% highlight html %}
"\n"
{% endhighlight %}

For example, __\\t__ is a tab
{% highlight html %}
"\t" 
{% endhighlight %}

</section>


<section markdown="block">
### I Heard You Like Backslashes

__How would we put a double quote in a double quoted string?__ &rarr;

<div class="incremental" markdown="block">
{% highlight html %}
"\""
{% endhighlight %}

__And what about an _actual_ backslash?__ &rarr;

{% highlight html %}
"\\"
{% endhighlight %}
</div>

</section>

<section markdown="block">
### String Operators

__string concatenation__, or __+__, is an operator that takes two strings and joins them:

{% highlight html %}
"hello " + "there"
{% endhighlight %}
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
### Some Special Numbers...

* __Infinity, -Infintity__ - positive and negative infinities (don't use these, they're not that useful, and not mathematically solid!)
* __NaN__ (not-a-number) - this results from any numeric operation that doesn't give back a meaningful result... such as 0/0

__Let's try these out__ &rarr;
</section>

<section markdown="block">
### Expressions and Statements

* An __expression__ is just a fragment of code that produces (_gives back_ or _yields_) a value
	* Even a single value, such as <code>42</code> is an expression.
	* You can piece together expressions to compose arbitrarily complex expressions.
* A __statement__ is a full instruction; it's _an action_
	* __All statements end in a semicolon__
	* An expression can be a statement
* A __program__ is a sequence of statements that specify to a computer actions to perform.

There's actually quite a bit more complexity to this -- enough to [warrant a very lengthy explanation](http://www.2ality.com/2012/09/expressions-vs-statements.html) (but we'll stick with our hand-wavey explanation). 

</section>

<section markdown="block">
### Expressions and Statements Continued

{% highlight html %}
// Expression (no semicolon)
1 + 5

// Statement
1 + 5;

// Even these are statements:
1;
"hi";
{% endhighlight  %}
</section>

<section markdown="block">
## All statements end in a semicolon in JavaScript
</section>

<section markdown="block">
### Functions

__What's a function?__ &rarr;

<div class="incremental" markdown="block">
* a __function__ is a named sequence of statements that perform some useful action.
* it can take inputs, and it can return values, but it doesn't have to do either
* to __call__ (or execute) a function, just call it by name, with parentheses after (with an optional list of commas separated inputs within the parentheses)
* the values passed to a function are called __arguments__
* for example: prompt("hello") is a function call
</div>
</section>

<section markdown="block">
## To call a function, use its name followed by parentheses.
</section>

<section markdown="block">
### Some Built-in Functions

* __prompt("some message")__ - asks the user for input and __returns__ that value to your program! ... takes a single argument, the message to display to a user (this usually requires the use of _variables_)
* __console.log("some message")__ - prints the argument that you pass to it... out to Chrome's JavaScript console 

__Let's try these out.__ &rarr;
</section>



<section markdown="block">
### "Catching" Values

Ok... so when we type in a value or just write a literal value, __how can we refer to that value again__? &rarr;

<div class="incremental" markdown="block">
We can use variables!

* variables hold values
* they allow our programs to remember or save the results of expressions
</div>

</section>

<section markdown="block">
### Variables

__Variables__ are names that refer to values:  

* you can use a variable's name wherever you want to use that value.
* to create a variable, use the special word, var, followed by =, then the value, and finally a semicolon
* this is _declaring_ or _defining_ a variable:

{% highlight html %}
var x = 23;

// using that variable
console.log(x + 7);
{% endhighlight %}

__What will the above output?__ &rarr;
</section>

<section markdown="block">
### Prompt Revisited

Remember that the function prompt gives back a value.  To retain that value, you have to hold it in a variable:

{% highlight html %}
var answer = prompt("Yes or no!?");
{% endhighlight  %}

</section>

<section markdown="block">
### You Can Put All of These Together!

__Let's write a small program that echoes back whatever is written in a prompt.__ &rarr;

<div class="incremental" markdown="block">
{% highlight html %}
var answer = prompt("Say something!");
console.log(answer);
{% endhighlight  %}

__Of course, you have to embed that in script tags in HTML for it to run (or just use the interactive console).__ &rarr;
</div>
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
