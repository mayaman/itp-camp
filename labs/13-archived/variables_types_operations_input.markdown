---
layout: slides
title: Variables, Types, Operations, and, Input
---
<section markdown="block" class="title-slide">
# print("hi")

{% include title-slide-footer.html %}
</section>

<section markdown="block">
### A First Program
<aside>"Hello world!"</aside>
* "Hello world!" is traditionally the [first program you write when learning a new language](http://en.wikipedia.org/wiki/List_of_Hello_world_program_examples)
* simply outputs "Hello world!"

Follow these steps:

1. create a new file in sublime text 2 called hello.__py__
2. type in:	__print("Hello world!")__
3. run your program through terminal
	* open terminal
	* navigate to your file
	* type in python hello.py

</section>

<section markdown="block">
### SPACE!
* notice there's no space prior to __print__
* Python is __whitespace significant__
	* whitespace matters
	* it mostly matters at the beginning of lines
	* indentation specifies the beginning and end of a group of lines of code
	* interior spacing usually doesn't matter
* this will work &rarr;
{% highlight python %}
print  (      "Hello world!")
{% endhighlight %}
* this won't &rarr;
{% highlight python %}
        print("Hello world!")
{% endhighlight %}
* we'll see more about spacing in our next class
</section>

<section markdown="block">
### Print

* print is a built-in __function__
* __what's a function?__

<div class="incremental" markdown="block">
* a function is a bunch of code that gets executed whenever the name of the function is _called_
* it's a black box that does _something_
* similar to functions you've seen in math
	* it can take parameters (inputs)
	* it can return a value (output)
	* though it doesn't necessarily have to take parameters or return values
</div>
</section>

<section markdown="block">
### Print Continued
* print is a built in function... that will output whatever you give it to the console followed by a __new line__
* you can tell it's a built-in function because it's highlighted (purple)
* if you start typing it and open parentheses, you get a hint &rarr;
	* notice - it can take more than one parameter or argument!
	* you can give print multiple parameters by separating them with a comma; all parameters will be printed out separated by a space &rarr; 
{% highlight python %}
print("Hi", "there")
{% endhighlight %}
</section>

<section markdown="block">
### A Quick Note About Functions
* we will go into the rest of the hint when we cover functions
* for now we're just interested in calling functions
* you call a function by 
	* typing the function's name 
	* open parentheses 
	* any arguments (separated by commas)
	* close parentheses
{% highlight python %}
a_function_name("argument 1", 2, 3.0)
{% endhighlight %}
</section>

<section markdown="block">
### A String
* the one argument that we pass to the __print__ function  is __"Hello world!"__
* this is called a __string__...
* it's just a sequence of characters
* note that it's surrounded by quotes!
</section>

<section markdown="block">
### One Last Look...
* a function named print
* being called with exactly one argument
* the one argument is a string &rarr;
{% highlight python %}
print("Hello world!")
{% endhighlight %}
</section>

<section markdown="block">
### Some More New Stuff
<aside>For the remainder of this class:</aside>
* we'll talk a little more about strings and other __types__ of __values__
* comments
* the operations that you can use on those types
* variables
</section>

<section markdown="block" class="title-slide">
# Values, Types, and Comments

{% include title-slide-footer.html %}
</section>

<section markdown="block">
## Values
</section>

<section markdown="block">
### What are Values?
* __values__ are just data
	* for now, a __value__ is a number or a string (we'll see more __types__ of values later) 
	* it can be stored in a variable 
	* it can be computed in an expression
	* it can't be _evaluated_ further (2 + 3 is not a value, because it can be evaluated further)
* some examples of values:
	* -123456
	* "a string is a value"
	* 1.00000001 
</section>

<section markdown="block">
### A Note on Values in Code
The representation of a bare value in code is called a __literal__.

* "a string " a __string literal__
* 254 - an __integer literal__
* we'll go over these types in the next few slides
</section>

<section markdown="block">
## Data Types
</section>

<section markdown="block">
### Values can be Classified by Data Type
A __data type__ is a set of values.  The type of a value determines how it can be used in expressions.  Sometimes __data type__ is also referred to as just __type__... or __class__.  

__Today, we'll go over the following 4 types__

1. __str__ (string)
2. __int__ (integer)
3. __float__ (floating point)
4. __complex__ (complex numbers)

The last 3 are  __numeric types__.
</section>

<section markdown="block">
## Strings
</section>

<section markdown="block">
### What's a String Again?
<div class="incremental" markdown="block">
A __string__ is a sequence of characters.

* any characters
* including spaces and punctuation
* are __delimited__ by quotes - must __start and end__ with quotes!
</div>
</section>


<section markdown="block">
### Unbalanced Quotes
__What do you think will happen if you have an extra quote?__ 

Let's give it a try: &rarr;

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> "oops " I quoted again"
SyntaxError: invalid syntax
{% endhighlight %}

If you don't have matching start and end quotes (__unbalanced quotes__) or if you forget to close your quotes (you have a start quote, but no end), you'll also get a syntax error.
</div>
</section>

<section markdown="block">
### Alternate String Delimiters
<aside>You Don't Have to Stick to Double Quotes...</aside>
You can use three different types of quotation marks:

* double quotes - "
* single quotes - '
* triple double quotes __for multiline strings__ - """

<p markdown="block">

{% highlight python %}
"double quoted string"
'single quoted string'
"""more than
one line.  omg!"""
{% endhighlight %}
</p>
</section>

<section markdown="block">
### Multiline Strings?
* triple double quotes allow you to span multiple lines 
* single or double quotes do not

__What do you think will happen if you try spanning multiple lines with single or double quotes?__ &rarr;

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> "spanning multiple
SyntaxError: EOL while scanning string literal
{% endhighlight %}
</div>
</section>

<section markdown="block">
### A Quick Aside on Comments
A __comment__ is text in a program that is meant for the human reader; it isn't used by the interpreter.  A comment can be:

* prefixed with the # token
* __or__ surrounded by triple double quotes as a bare string literal

These are both comments: &rarr;
{% highlight python %}
# this is a comment
"""
so
is
this
"""
{% endhighlight %}
</section>

<section markdown="block">
###A Hasty Escape
What if I want to put in a character that has special meaning in a string?  Say, for example... a single or double quote?

* you can use the backslash character before the special character
* for quotes, you can use mixed quotes (embed single quotes in a double quoted string)!
* let's give it a try... &rarr;

<div markdown="block">
{% highlight python %}
print("escaping using \"backslash\"")
print("single  quotes ''''") 
print("""some "double quotes"""")
{% endhighlight %}
</div>
</section>

<section markdown="block">
###I Heard You Like Backslashes
<aside>So I...</aside>

__What if you want an _actual_ backslash in your string?__ &rarr;

<div class="incremental" markdown="block">
You can use backslashes to escape backslashes 
{% highlight python %}
print("I heard you like \\'s, So I put a \\ before your \\")
{% endhighlight %}
</div>
</section>


<section markdown="block">
###On a Tropical Island
<aside>A Quick Activity</aside>

![jake](../../resources/img/jake.jpeg)
</section>
<section markdown="block">
###On a Tropical Island Lyrics

These are lyrics to a song called ["On a Tropical Island"](http://www.youtube.com/watch?v=ewDWEXxu99o)... from a cartoon called Adventure Time.  It has a bunch of new lines in it, as well as single quotes.

__How would you get Python to print out these lyrics?  Let's find 2 different ways to print this out.__&rarr;

{% highlight pycon %}
On a tropical island,
Underneath a molten lava moon.
Hangin' with the hula dancers,
Askin' questions cause' they got all the answers.
{% endhighlight %}
</section>

<section markdown="block">
##Numeric Types
<aside>Integers, Floating Point Numbers and Complex Numbers</aside>
</section>

<section markdown="block">
###Three Numeric Types
The following types are all closely related; most of the same operations can be applied to all of them:

1. __int__ (integer)
2. __float__ (floating point)
3. __complex__ (complex numbers)
</section>

<section markdown="block">
### int (integer)

__What's an integer?__

<div class="incremental" markdown="block">
* __integer__ - whole number, can be negative
* "int" is the name of the integer type
* 24, -25 &rarr;
* no size limit (well, as much as your computer can handle)!
* for example: 1337 ** 20 &rarr;
</div>
</section>

<section markdown="block">
### __float__ (floating point)

__What's floating point number?__

<div class="incremental" markdown="block">
* __floating point__ represents real numbers (well really rational numbers, since there's a limit)
* ...but what's a real number?

<p markdown="block">				
* a quantity across a continuous line, like fractions or irrational numbers like pi or square root of two
* floating point numbers are __indicated by a decimal point__: 5.55555, 5.0 &rarr;
</p>
</div>
</section>

<section markdown="block">
### Really Big or Really Small Numbers
Very large or small numbers are expressed in scientific notation

* 5555 ** 5.0 gives back 5.289569361832972e+18 &rarr;
* __What do you think  2e+2 gives you?__ &rarr;

<div class="incremental" markdown="block">
* 200.0
</div>
</section>

<section markdown="block">
### Uh-oh - That's Too Much
<aside>Overflow</aside>

* unlike integers, floats have min and max values... if you have a value that's too big or too small
* sys.float_info.max &rarr;
* 5555**55555.0 &rarr;

{% highlight pycon %}
>>> 5555**55555.0
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    5555**55555.0
OverflowError: (34, 'Result too large')
>>> 
{% endhighlight %}

<!-- _nomd -->
</section>

<section markdown="block">
###Complex Numbers
<aside>Um - Does anyone remember these?  I don't</aside>

For completeness... __Python supports complex numbers__

* numbers with squareroot of 1 / imaginary numbers
* 1j * 1j &rarr;
</section>

<section markdown="block">
###Don't, Use, That, Comma
Clearly, symbols have special meanings in numeric types

* a decimal point signifies a floating point number
* scientific notation is represented by e and a plus or minus
* j is the imaginary part of a complex number

__However - Don't use commas!  They don't mean what you expect.__ &rarr;
{% highlight pycon %}
>>> 3,000
(3, 0)
>>> # huh???
>>> # it's something called a tuple
{% endhighlight %}
</section>

<section markdown="block">
###So You Don't Know What Type You Have
* There's a function called __type__
* Let's look at it in the interactive shell &rarr;
* Notice the arrow... it says it returns the "type" of the parameter passed in...
* Here's how you would use it:
* type(1.0) &rarr;
</section>

<section markdown="block">
###A Guessing Game
<aside>What type is it?</aside>

1. __1__
2. __1.0__
3. __"1"__
4. __"""1.0"""__
5. __1.111__
6. __'1,111'__

<div class="incremental" markdown="block">
1 is an __int__. 2 and 5 are __floats__.  Everything else is a string.
</div>
</section>

<section markdown="block">
### Reeeeeewind
<aside>A Quick Recap</aside>
* What do we call a bare value in code... like "foo" or 5?
* Name three ways to delimit a string
* Name two ways to put a double quote in a string
* How about a backslash
* Which type can be affected by really large or small numbers - float or int?
* How can I tell if a number is a float?
* What function could I use to determine the type of a value or variable?
* What are two ways of representing comments?
</section>

<section markdown="block" class="title-slide">
# Operations and Variables

{% include title-slide-footer.html %}
</section>

<section markdown="block">
##  Operations on Strings and Numeric Types
</section>

<section markdown="block">
### int operations 
<aside>The Usual...</aside>

As you'd expect: addition, subtraction and multiplication &rarr;

* add - __+__ 
* subtract - __-__
* multiply __\*__
</section>

<section markdown="block">
### Division is Special

* the division operator is __/__
* __what do you think 5/2 gives__ &rarr;			
* __what type is the result?__ &rarr;

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> 5/2
2.5
>>> type(5/2)
<class 'float'>
>>> 
{% endhighlight %}
</div>
</section>

<section markdown="block">
### We Don't Need No Decimal Points
<aside>Integer Division</aside>

* the integer division operator is __//__ (double forward slash)
* it will always give back an integer - for example 21//10 gives back 2
* if the result is a float, it will go to the nearest integer to the left of the number line!
* __what will 5//2 give back__
* __what will -5//2 give back__

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> 5//2
2
>>> -5//2
-3
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Modulus Operator (Remainder)
<aside>What's Left Over?</aside>
* the remainder operator is % (the percent symbol)
* __what would 5%2 give back?__ &rarr;

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> 5%2
1
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Exponentiation 
<aside>We NEED MORE STARS</aside>
* the exponentiation operator is __\*\*__ (two asterisks)
* __what do we get for 2**2__? &rarr;

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> 2**2
4
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Order of Operations
<aside>Too Many Operators!  What To Do First?</aside>

* as you would expect (remember PEMDAS?)
* __what does 12 + 10 / 5  give?

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> 12 + 10 / 5
14.0
{% endhighlight %}

__BTW, what type did we get back?__

float! (division, even with integers, gives back floats)
</div>
</section>


<section markdown="block">
### ((Parentheses))
<aside>(I Use Them A Lot</aside>
* you can use parentheses to group expressions...
* this will affect odrer of operations
* __what will (6 + 4) * 5 return?__ &rarr;

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> 12 + 10 / 5
14.0
{% endhighlight %}
</div>
</section>

<section markdown="block">
### You Could Always Use It As a Calculator
<aside>A Quick Activity</aside>

__Translate this formula__ &rarr;

* 9 divided by 5 * C + 32
* use 37 for C
* do you recognize the forumla?
</section>

<section markdown="block">
## str Operations
</section>

<section markdown="block">
### Multiplication!?
* the multiplication operator is __*__
* it returns a new string with the original string duplicated the number of times specified by the operand on the right side
* __what would "hey" * 3 return?__ &rarr;

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> "hey" * 3
'heyheyhey'
{% endhighlight %}
</div>
</section>

<section markdown="block">
### String Concatenation
* use the __+__ to stitch together strings
* it's basically just adding strings together
* for example: print("this" + "knocked " + "my" + "socks" + "off") &rarr;
* why are the words all smashed together? 
* how would we fix it? 
* __let's try different types! - does it work?__ &rarr;
	* with an int? try: 3 + " blind mice" &rarr;
	* with a float?
	* what kind of error are we getting?
</section>

<section markdown="block">
### Let's Fix It!
<aside>Type Conversion...</aside>

You can change from one type to another using functions of the same name as the type.  Let's look at what autocomplete says about the following functions and demo them.  &rarr;

* __int__
* __str__
* __float__

A few notes:

* unlike print, these functions return a value!
* sometimes this is called __casting__.
</section>

<section markdown="block">
###And This Helps... How? 
__Let's fix our previous string concatenation__ &rarr;

{% highlight pycon %}
3 + " blind mice"
{% endhighlight %}

<div class="incremental" markdown="block">

{% highlight pycon %}
>>> str(3) + " blind mice"
'3 blind mice'
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Review
* what operators do we use for exponentiation and integer division?
* what does -10//3 give back?
* what's an easy way of creating a string that has 100 exclamation points in it? 
* what's string concatenation?
</section>


<section markdown="block">
## Variables
</section>

<section markdown="block">
### What's a Variable?
* __variable__ - name that refers to a value
* this terminology is important; very specific... __name__ and __value__
* we can now use that name instead of the explicit value
* sometimes you'll hear me say the string "literal" - representation of a value within a program... i mean... the thing in quotes
</section>

<section markdown="block">
### So How Do Variables Actually Work?
{% highlight pycon %}
some_variable_name = "a value"
{% endhighlight %}

* this is an __assignment statement__ - binds a value to a name
* the equals sign __assignment token__ - the "operator" that we use to bind a name to a value
	* name on left
	* value on right
	* eeezy.... just like maths
</section>

<section markdown="block">
### Another Aside - Interactive Shell
Whenever you type something in the interactive shell, it will always return a value. &rarr;

* a value returns a value
* a variable returns a value
* a function can return a value
* if a function doesn't actually return a value, like print, the resulting value will be None (NoneType)
</section>

<section markdown="block">
### Some More Miscellaneous Comments
* how can I tell if it printed something vs just return?
	* kind of confusing... strings, you can tell... because it shows a representation of the value that's returned
	* well, almost every line returns a value... unless it starts a new block of code (with a colon) or it's a continued line.
* another btw,__metasyntactic variable__ - typical to use foo, bar, baz as placeholders for real values - meant to represent arbitrary name
</section>

<section markdown="block">
### Variables That Aren't Defined Yet
* __what happens when you use a variable that doesn't exist?__ &rarr;	

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> foo
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    foo
NameError: name 'foo' is not defined
>>> 
{% endhighlight %}
</div>
</section>

<section markdown="block">
### More About Reassignment

* you can reassign or rebind
* __let's see that in action__ &rarr;
{% highlight pycon %}
>>> a = 23
>>> a
23
>>> a = "foo"
{% endhighlight %}
</section>

<section markdown="block">
### Naming Variables
* you can make them as long as you want... though I suppose it could crash your computer
	* __what's an easy way to create a long variable name?__ &rarr;
	* __btw, you can autocomplete in the shell by using tab__ &rarr;
* names can only be alphanumeric (numbers and letters) or the underscore
* the first character has to be a letter or an underscore
* __case sensitive__ - case matters
* the name can't be a keyword or reserved word
</section>

<section markdown="block">
### Am I a Valid Name?
* _foo
* 1_foo
* foo
* 1foo
* $foo
* foo$
</section>

<section markdown="block">
### Let's Actually Use Some Variables
* exclaim = "!!!" 
* add a string to a variable that has a string in it
* 9 / 5 * c + 32
* let's convert 37...
</section>

<section markdown="block" class="title-slide">
# User Input

{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Getting Input From the Shell

* we can prompt the user through the console / terminal / shell / command prompt
* the user enters input through the same mechanism
</section>

<section markdown="block">
### The input() Function
* what parameter's does it take? &rarr;
* what does it return? &rarr;
* what if the user input is a number? &rarr;

<div class="incremental" markdown="block">
* input takes one parameter - the prompt that is displayed
* it returns a string representing the user's input
* it will always return a string - even if the user inputs a number
</div>
</section>

<section markdown="block">
### Let's Try Some Examples of input()
{% highlight python %}
>>> s = input(">")
>foo
>>> type(s)
<class 'str'>
>>> x = input(">")
>5
>>> type(x)
<class 'str'>
>>> x = int(input(">"))
>5
>>> type(x)
<class 'int'>
{% endhighlight %}

</section>

<section markdown="block">
### Write a Program That Asks For a Name
Here's the sample output; the text after the &gt; is user input.

{% highlight python %}
What's your name?
>Joe
Hi Joe
{% endhighlight %}
<div class="incremental" markdown="block">
__A potential solution...__ &rarr;

{% highlight python %}
print("What's your name?")
name = input(">")
print("Hi %s" % name)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Write a Program That Adds Exclamation Points
Here's the sample output; the text after the &gt; is user input.

{% highlight python %}
How loudly?
>4
This is really loud!!!!
{% endhighlight %}
<div class="incremental" markdown="block">
__A potential solution...__ &rarr;

{% highlight python %}
loudly = input("How loudly?\n>")
print("This is really loud" + "!" * int(loudly))
{% endhighlight %}
</div>
</section>

