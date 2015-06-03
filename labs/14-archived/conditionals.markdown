---
layout: slides
title: Boolean Logic and Conditionals
---

<section markdown="block" class="title-slide">
# Boolean Logic

{% include title-slide-footer.html %}
</section>

<section markdown="block">
## Some Computer Science History...
</section>

<section markdown="block">
### For Context - What's this Boolean Stuff About?
<aside>It's This Guy...</aside>

<div class="img-container" markdown="block">
![George Boole](../../resources/img/boole.jpeg)
</div>
</section>

<section markdown="block">
### George Boole

<aside markdown='block'>
The _Father_ of Computer Science!  SCIENCE!
</aside>

* English Mathematician, Philosopher and Logician in the 1800's
* Proposed that logical propositions can be expressed by algebraic equations (mathematical logic - AND, OR, NOT)
* This idea, now called __Boolean logic__, is the basis of computer science!
</section>

<section markdown="block">
### In Python...
As we talked about in the review, Python has a __bool__ type to represent Boolean values

* True or False
* just like other values, can be assigned to variables
* __comparison operators__ (we learned the equality operator) return Boolean values
* Boolean values can be combined into expressions using __logical operators__
</section>

<section markdown="block">
## Comparison Operators
</section>

<section markdown="block">
### Comparison Operators
__Can you guess what some of the comparison operators are?  Like I said, you already know one!__ 

There are six comparison operators:

<div class="incremental" markdown="block"> 
* __==__ - equals (can be called logical equivalence or equality operator)
* __!=__ - not equal
* __>__ - greater than
* __<__ - less than
* __>=__ - greater than / equal
* __<=__ - less than / equal
</div>
</section>

<section markdown="block">
### Comparison Operators Continued
* again - these operators always return a bool
* these operators do what you would expect 
	* __==__ - returns True if both sides are equal &rarr;
	* __!=__ - returns True if both sides are not equal &rarr;
	* __>__, __<__, __>=__, __<=__ - returns True if value on the left is greater than, less than, greater than / equal, or less than equal to the value on the right &rarr;
* never put equals first on >=, <=
</section>

<section markdown="block">
### Comparison Operators Have Feelings Too
<aside>Just as Sensitive to Type Mismatches as Numeric or String Operators.  Well... At Least Some Are</aside>

__What do you think will happen if we compare 8 >= "four"?__ &rarr;

<div class="incremental" markdown="block"> 

{% highlight pycon %}
>>> 8 >= "four"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: int() >= str()
{% endhighlight %}
</div>

</section>

<section markdown="block">
### Comparison Operators and Different Types
* objects of different types, except different numeric types, are never equal
	* equals (__==__) will always return False for different types &rarr;
	* not equals (__!=__) will always return True for different types &rarr;
* the <, <=, > and >= operators... 
	* will raise a TypeError if the objects are of different types that cannot be compared &rarr;
	* will happily compare numeric types (for example comparing floats and ints works as you'd expect)! &rarr;
</section>

<section markdown="block">
## Logical Operators
</section>

<section markdown="block">
### What are Logical Operators?

__Logical Operators are operators that combine Boolean values.__  

* these operators always return another Boolean value.  
* furthermore, these operators can be used to create more complex Boolean expressions. 
</section>

<section markdown="block">
###  Three Logical Operators:
1. __and__ - 
	* takes two operands, one on each side 
	* to return True, both sides of the operator must be True &rarr;
2. __or__ - 
	* takes two operands, one on each side
	* to return True,at least one side of the operator must be True &rarr;
3. __not__ - 
	* only takes one operand to the right
	* to return True, the original value on the right must evaluate to False &rarr;
	* two nots cancel eachother out (fun!) &rarr;
</section>

<section markdown="block">
###  Logical Operators _in Action_
{% highlight pycon %}
>>> True and False
False
>>> True and True
True
>>> True or False
True
>>> not True
False
>>> not not True
True
{% endhighlight %}
</section>

<section markdown="block">
### That Can Get Complicated!

<aside>Is There a Way to Show All Operands and Results?</aside>

__Yes__.  We'll use __truth tables__ to show what each operator will return.

* a __truth table__ is a concise table of Boolean values that describes the semantics of an operator
* it will go through each possible operands and specify the resulting Boolean value
* each row will represent a combination of operands
* each column will represent a value of one operand
* ...with the exception of the last column, which represents the resulting value
</section>

<section markdown="block">
### Truth Table - AND

__and__ takes two operands.  Each operand can be True or False (or will evaluate to True or False!).  

__Can you guess how many possible combinations there are for these two operands?__  __What will the Truth Table look like?__ &rarr;

<div class="incremental" markdown="block"> 
{% highlight python %}
"""
(using p and q to represent the operands
...and t and f for true and false)
 p | q | p and q
----------------
 f | f | f
 f | t | f
 t | f | f
 t | t | t
"""
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Truth Table - OR

Let's fill out a truth table for __or__! &rarr;

<div class="incremental" markdown="block"> 
{% highlight python %}
"""
(using p and q to represent the operands
...and t and f for true and false)
 p | q | p and q
----------------
 f | f | f
 f | t | t
 t | f | t
 t | t | t
"""
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Truth Table - NOT

Let's fill out a truth table for __not__! &rarr;

<div class="incremental" markdown="block"> 
{% highlight python %}
"""
(using p and q to represent the operands
...and t and f for true and false)
 p | not p
-----------
 t | f 
 f | t 
"""
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Let's Evaluate Some Simple Boolean Expressions

* True and False &rarr;
* True and not False &rarr;
* True or False &rarr;
* True or not False &rarr;
* False or False &rarr;
* not False and not False &rarr;

</section>

<section markdown="block">
### Chaining Boolean, Comparison, and Other Operators
You can chain together operators to make complex Boolean expressions!  

* Boolean expressions can involve Boolean, comparison, and other operators
* they can be arbitrarily complex!  (don't do that)

__What do you think this evaluates to?__ &rarr;
{% highlight python %}
100 > 1 and -10 ** 2 <= -100 or "foo" == "bar" and 100 >= 100
{% endhighlight %}

<div class="incremental" markdown="block"> 
{% highlight python %}
True
{% endhighlight %}

__How can we make it False?  And why does that work?__ &rarr;
</div>

</section>

<section markdown="block">
### Chaining Boolean, Comparison, and Other Operators
<aside>Let's Go Back to That Original Expression...</aside>

{% highlight python %}
100 > 1 and -10 ** 2 <= -100 or "foo" == "bar" and 100 >= 100
{% endhighlight %}

* what order will the operations be evaluated in?
* both THINKSCI and QUICKSTART have order of operations for logical operators
* however, there's an overall order of operations that exists
* [A summary can be found in the official documentation for Python 3]( http://docs.python.org/py3k/reference/expressions.html#summary)
</section>

<section markdown="block">
### Order of Operations / Operator Precedence
The previous summary, but even more _summar-ied_

* parentheses are evaluated first (obv)
* numeric / string operations (in turn, are also ordered)
* comparison operations (==, !=, >, <, >=, >=)
* not
* and
* or
</section>

<section markdown="block">
### A Quick Note About Boolean Operators and Style
<aside>Because This is Crazy...</aside>
{% highlight python %}
True and True or False and True and 10 * 10 + 10 == 110 and not False
{% endhighlight %}
* it's usually a good idea to use parentheses, at the very least, for readability 
* ...unless you're chaining the same operator (for example True and True and True)
</section>

<section markdown="block">
### Some Exercises
* not (8 != 8) or not True  
* "hello" == "world" or 5 + 5 > 5 and 5 + 5 < 55 and 28 != 0
* not True or not True or not True and False
* ((True or False) and not True) or 801 >= 801 and -1 * 1 < 0
</section>

<section markdown="block">
### Short Circuit Evaluation
* if left hand side of boolean decides the outcome, no need to deal with the remainder of expression
	* saves some processin' time!
	* for example: (false and (true and true and true or false))
	* can stop at false!
* can be applied internally to a larger more complex boolean expression
* generally, just language implementation details, right?
	* but it's a concept you should be aware of 
	* (perhaps if there's a function on the right side that doesn't get called!)
</section>

<section markdown="block">
### Short Circuit Evaluation Continued
__Can you think of some comparison or logical operators where short circuit evaluation wouldn't make sense?__

* obv __not__ - nothing to short circuit!
* == equivalence operations - both sides must be evaluated to test equality
</section>

<section markdown="block">
### Review
* comparison operators
	* ==, !=, >, <, >=, <=
	* comparing different types
* logical operators
	* and, or, not
	* truth tables
* operator precedence
</section>

<section markdown="block" class="title-slide">
# If Statements / Conditionals

{% include title-slide-footer.html %}
</section>

<section markdown="block">
## Back to the Lecture at Hand?
</section>

<section markdown="block">
### Anatomy of an If Statement

__Write an if statement testing if a and b are _not_ equal.  If they're not equal, print the value of a and b twice.__ &rarr;
{% highlight python %}
a, b = "foo", "bar"
{% endhighlight %}

<div class="incremental" markdown="block">
* begin with keyword __if__
* condition
* colon - ends the condition / marks that a block of code is about to come up
* if + condition + colon usually is considered the _if-statement header_
* body of if statement ends when indentation goes back one level
* blank lines don't count as ending a block of code!
</div>
</section>

<section markdown="block">
### Let's See That Again
<aside>Now With More Blank Lines</aside>

{% highlight python %}
a, b = "foo", "bar"
if a != b:
	# totally ok?  yes!
	# but why?
	# perhaps when done more reasonably, readability
	print a
	print a


	print b

	print b
{% endhighlight %}
</section>

<section markdown="block">
### Oh Yeah, Else What?

We can use __else__ to execute code if the original condition was not met

* go back one level of indentation to mark that the previous code block has ended
* keyword __else__
* body - indented, body ends when indentation goes back one level
* not required, obvs
</section>

<section markdown="block">
### What About Multiple Chained Conditions?
What if __else__ is not fine-grained enough?  For example, how about a program that asks for cake and handles a yes, no, or anything other than...

{% highlight python %}
"""
Do you want cake?
> yes
Here, have some cake.

Do you want cake?
> no
No cake for you.

Do you want cake?
> blearghhh
I do not understand.
"""
{% endhighlight %}
</section>

<section markdown="block">
### Consecutive Ifs
__One way to do it is consecutive if statements...__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
answer = raw_input("Do you want cake?\n> ")
if answer == 'yes':
        print("Here, have some cake.")
if answer == 'no':
        print("No cake for you.")
if answer != 'yes' and answer != 'no':
        print("I do not understand.")
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Else If (elif)

We can use __elif__ to chain a series of conditions, where only one path of code will be executed

* if statement like usual
* go back one level of indentation to mark that the previous code block has ended
* keyword __elif__
* condition
* colon
* body - indented, body ends when indentation goes back one level
* not required obv
* even if more than one true, only the first true executes!
* can add an else at the end
</section>

<section markdown="block">
### elif Example
<aside>Let's have some more cake...</aside>
__How would we redo the cake exercise with elif?__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
answer = raw_input("Do you want cake?\n> ")
if answer == 'yes':
        print("Here, have some cake.")
elif answer == 'no':
        print("No cake for you.")
else:
        print("I do not understand.")
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Nesting If Statements

* it behaves as you'd expect
* remember to get indentation right
* if there are multiple elif's or else's,  you can use indentation to see which initial if statement they belong to
* this works for any combination of if, elif and else
* note that sometimes nested if statements are equivalent to and
* best to simplify - that is, less nesting, better
</section>

<section markdown="block" class="title-slide">
# How to (Un)Complicate Things With If Statements

{% include title-slide-footer.html %}
</section>

<section markdown="block">
## elif
<aside>Like Smashing Together Your Two Favorite Keywords</aside>
</section>

<section markdown="block">
### elif Is the New _Else If_

We can use __elif__ to chain together a series of conditions.  This allows us to create multiple flows of execution (more than two), but - at most - only one path will be executed (even if more than one condition is true). 

* each condition is checked in order
* if the first is false, the next condition is checked
* this continues until the first true condition
* the body of code associated with that condition is executed
* the statement ends even if there are more conditions left
</section>

<section markdown="block">
### elif Syntax

* if statement like usual
* go back one level of indentation to mark that the previous code block has ended
* keyword __elif__
* condition
* colon
* body - indented, body ends when indentation goes back one level
* not required obv
* even if more than one true, only the first true executes!
* can add an else at the end
</section>

<section markdown="block">
### A Trivial elif Example

__Translate an athlete's finishing placement (1st, 2nd and 3rd) into its Olympic medal value: 1 for gold, 2 for silver, 3 for bronze and anything else means no medal &rarr;__.  Do this by asking for user input.  For example:

{% highlight python %}
What number should I translate into a medal?
>1
gold

What number should I translate into a medal?
>3
bronze

What number should I translate into a medal?
>23
no medal for you!
{% endhighlight %}
</section>

<section markdown="block">
### Medals... Solution!

{% highlight python %}
"""Translate place number into Olympic medal.  FTW!"""

place = int(input('What number should I translate into a medal?\n>'))
if place == 1:
    medal = "gold"
elif place == 2:
    medal = "silver"
elif place == 3:
    medal = "bronze"
else:
    medal = "no medal for you!"
print(medal)
{% endhighlight %}

</section>

<section markdown="block">
### Another elif Example
<aside>Let's have some more cake...</aside>
__Let's do the cake exercise (ask the user if they want cake) again with elif...__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
"""Ask me if I want cake, I *dare* you to."""
answer = input("Do you want cake?\n> ")
if answer == 'yes':
    print("Here, have some cake.")
elif answer == 'no':
    print("No cake for you.")
else:
    print("I do not understand.")
{% endhighlight %}
</div>
</section>

<section markdown="block">
### And How Did That Compare To Consecutive If Statements?

__We could have impemented this using consecutive if statements.__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
answer = input("Do you want cake?\n> ")
if answer == 'yes':
    print("Here, have some cake.")
if answer == 'no':
    print("No cake for you.")
if answer != 'yes' and answer != 'no':
    print("I do not understand.")
{% endhighlight %}
</div>
</section>

<section markdown="block">
### And How Did That Compare To Consecutive Nested If Statements?

__We could have impemented this using nested if statements.__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
answer = input("Do you want cake?\n> ")
if answer == 'yes':
    print("Here, have some cake.")
else:
    if answer == 'no':
        print("No cake for you.")
    else:
        print("I do not understand.")
{% endhighlight %}
</div>
</section>

<section markdown="block">
### And How Did That Compare To Consecutive Nested If Statements?

__What do you think the decision trees look like?.__ &rarr; (Oh, and BTW, what's a decision tree? ...It's a graph that shows all possible decisions and the outcomes of those decisions.)

<div class="incremental" markdown="block">
<div class="img-container" markdown="block">
![trees](../../resources/img/cake-decision-trees.png)
</div>
</div>
</section>

<section markdown="block">
### And How About Speed?

__We could make an educated guess.__ &rarr;

<div class="incremental" markdown="block">
* elif skips conditions if one of the early conditions is true!
* that means, best case, there are less instructions for the computer to execute when using elif
	* compared to nested ifs
	* or consecutive ifs
* not sure what the interpreter/compiler does behind the scenes when it translates, though
	* could optimize things 
	* produce similar machine code for both kinds of code
</div>
</section>

<section markdown="block">
### We're Not Finished Yet...
<aside>I'm bad at making decisions...</aside>

* __Add "maybe" as a potential answer?__ &rarr;  
* __Handle different ways of saying yes (like "yeah")?__ &rarr;

{% highlight python %}
Do you want cake?
> maybe
So, call me.

Do you want cake?
> yes
Here, have some cake.

Do you want cake?
> yeah
Here, have some cake.

{% endhighlight %}
</section>

<section markdown="block">
### Adding 'yeah' and 'maybe'...

{% highlight python %}
"""Ask me if I want cake, I *dare* you to."""
answer = input("Do you want cake?\n> ")
if answer == 'yes' or answer == 'yeah':
    print("Here, have some cake.")
elif answer == 'no':
    print("No cake for you.")
elif answer == 'maybe':
    print("So, call me.")
else:
    print("I do not understand.")
{% endhighlight %}
</section>

<section markdown="block">
### Lastly, Everything Together

__Write a program that names the rolls of two dice in a dice game called craps...__ &rarr;

* ask the user for the values of two dice rolls.  
* output the [name of the roll](http://en.wikipedia.org/wiki/Craps#Rolling) using Wikipedia's article on Craps
* only check for the following rolls:
	* _Snake Eyes_
	* _Hard Four_ 
	* _Easy Four_  
* print out "I don't know yet" for any other rolls.  Example output:
* example interaction on next page
</section>

<section markdown="block">
### Craps - Example Interaction

{% highlight python %}
What roll did you get for the first die?
> 1
What roll did you get for the second die?
> 1
Snake Eyes!

Press ENTER or type command to continue
What roll did you get for the first die?
> 1
What roll did you get for the second die?
> 3
Easy Four
{% endhighlight %}
</section>

<section markdown="block">
### Name That Craps Roll

{% highlight python %}
""" Name that craps roll! (well, at least four of them)
http://en.wikipedia.org/wiki/Craps#Rolling"""

d1 = int(input("What roll did you get for the first die?\n> "))
d2 = int(input("What roll did you get for the second die?\n> "))
if d1 == 1 and d2 ==1:
    print("Snake Eyes!")
elif d1 == 1 and d2 == 3 or d1 == 3 and d2 == 1:
    print("Easy Four")
elif d1 == 2 and d2 == 2:
    print("Hard Four")
else:
    print("I don't know that roll yet")
{% endhighlight %}
</section>

<section markdown="block">
### Nesting If Statements

* we saw this above to motivate our __elif__ example
* it behaves as you'd expect
* remember to get indentation right
* if there are multiple elif's or else's,  you can use indentation to see which initial if statement they belong to
* this works for any combination of if, elif and else
* note that sometimes nested if statements are equivalent to and
* best to simplify - that is, less nesting, better
</section>

<section markdown="block">
### Nesting If Statements Example

The coffee shop has a special for half price pastries on Fridays after 4 (16:00... or 16).  __Ask for day and time, and make a recommendation (buy now, wait x hours or don't buy).__ &rarr;

{% highlight python %}
What day is it (ex Thursday, Friday, etc.)?
> Friday
What time is it (in 24 hour time)?
> 17
Go ahead, you deserve a treat

Press ENTER or type command to continue
What day is it (ex Thursday, Friday, etc.)?
> Friday
What time is it (in 24 hour time)?
> 12
Just wait 4 more hours
{% endhighlight %}

</section>

<section markdown="block">
### Pastry Buying Guide

{% highlight python %}
""" pastry buying guide """

day = input("What day is it (ex Thursday, Friday, etc.)?\n> ")
time = int(input("What time is it (in 24 hour time)?\n> ")) # not adventure
delicious_time = 16
if day == 'Friday':
	if time >= delicious_time:
		print("Go ahead, you deserve a treat") 
	else:
		print("Just wait %s more hours" % (delicious_time - time)) 
else:
	print("Don't do it!  Just don't.")
{% endhighlight %}
</section>


<section markdown="block">
### How to Order Conditions

* if more than one condition in a series of elif's is true 
	* only the first true condition is executed!
	* other are skipped, including else
* be careful of conditions that never get evaluated 
	* an above condition may already account for it
	* here's an example...
</section>

<section markdown="block">
### Ordering Conditions Continued!

The intention of the following code is to:

* determine if a number is 101 or greater than 100
* if it's 101, it should only print out "exactly 101" (it should not print out greater than 100)

__What gets printed if n = 200?  What if n = 101?__   &rarr;

{% highlight python %}
if n > 100:
	print("more than 100")
elif n == 101:
	print("exactly 101")
{% endhighlight %}

<div class="incremental" markdown="block">
200 &rarr; more than 100, 101 &rarr; more than 100
</div>

</section>

<section markdown="block">
### How to Order Conditions Continued Some More!

__Of course, we could fix this.  There are a few ways...__ &rarr;

<div class="incremental" markdown="block">
* reordering
* using and
{% highlight python %}
if n == 101:
	print("exactly 101")
elif n > 100:
	print("more than 100")

if n > 100 and n != 101:
	print("more than 100")
elif n == 101:
	print("exactly 101")
{% endhighlight %}
</div>
</section>

<section markdown="block">
## Equivalent Conditions
</section>

<section markdown="block">
### Logical Opposites 
A way to get rid of not operators is to use the opposite logical operator:

[Logical Opposites from {{ site.bookt }} ](http://openbookproject.net/thinkcs/python/english3e/conditionals.html)

* for example... the logical opposite of &gt; is &lt;=
* the logical opposite of &lt; is &gt;=

</section>

<section markdown="block">
### Logical Opposites Continued
__How can we rewrite this without the not?__&rarr;

{% highlight python %}
if not (age >= 17):
    print("Hey, you're too young to get a driving licence!")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
if age < 17:
    print("Hey, you're too young to get a driving licence!")
{% endhighlight %}
</div>
</section>

<section markdown="block">
### De Morgan's Law
* not (x and y)  ==  (not x) or (not y)
* not (x or y)   ==  (not x) and (not y)
* {{ site.bookt }} example
	* uses combination of logical opposites and De Morgan's Law
	* clarity / closeness to original 

__Let's try truth tables for these!__ &rarr;
</section>

<section markdown="block">
### De Morgan's Law Truth Tables

{% highlight bash %}
x | y | not (x and y)   x | y | (not x) or (not y)
=====================   =========================
t | t | f               t | t | f
t | f | t               t | f | t
f | t | t               f | t | t
f | f | t               f | f | t

x | y | not (x or y)   x | y | (not x) and (not y)
====================   ===========================
t | t | f              t | t | f
t | f | t              t | f | t
f | t | t              f | t | t
f | f | t              f | f | t
{% endhighlight %}
</section>

<section markdown="block">
### De Morgan's Law 
__How can we rewrite this fragment of code from {{ site.bookt }}?__&rarr; 

{% highlight python %}
# "suppose we can slay the dragon only if our magic lightsabre sword 
# is charged to 90% or higher, and we have 100 or more energy units 
# in our protective shield." 

if not ((sword_charge >= 0.90) and (shield_energy >= 100)):
    print("Your attack has no effect, the dragon fries you to a crisp!")
else:
    print("The dragon crumples in a heap. You rescue the gorgeous princess!")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
# first... demorgan's: 
if not (sword_charge >= 0.90) or not (shield_energy >= 100):
	# ...
{% endhighlight %}

{% highlight python %}
# next... logical opposites:
if (sword_charge < 0.90) or (shield_energy < 100):
	# ...
{% endhighlight %}
</div>
</section>

<section markdown="block">
## Truthiness and Style
</section>

<section markdown="block">
### Truthiness

See this [crazy chart](http://docs.python.org/py3k/library/stdtypes.html#truth-value-testing) on the _intrinsic_ boolean value of various types.  The following values are considered false:

* None
* False
* 0 of any numeric type (0.0, 0)
* empty mapping or sequence type (We'll look at these later) - this includes the empty string '', "", etc.
</section>

<section markdown="block">
### Truthiness Examples

{% highlight python %}
a = ""
if a:
	print("true!")

a = 0
if a:
	print("true!")

a = "foo"
if a:
	print("true!")
{% endhighlight %}

</section>

<section markdown="block">
### Another Note About Style
* remember idioms?
* http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#testing-for-truth-values
* more elegant to test intrinsic truth values than using equality operator
{% highlight python %}
b = True
# instead of if b == True
if b:
	print("b")

s = "catz!"
# to test if the value is not empty string 
# (rather than s != "")
if s:
	print(s)

{% endhighlight %}

</section>

<section markdown="block">
### Let's Write a Mini Quiz Game!

__Write a program to ask a couple of questions about the book, Dune.__ &rarr;

{% highlight python %}
#  ______            _        _______ 
# (  __  \ |\     /|( (    /|(  ____ \
# | (  \  )| )   ( ||  \  ( || (    \/
# | |   ) || |   | ||   \ | || (__    
# | |   | || |   | || (\ \) ||  __)   
# | |   ) || |   | || | \   || (      
# | (__/  )| (___) || )  \  || (____/\
# (______/ (_______)|/    )_)(_______/
# 
# What is the name of the desert planet that's informally called Dune?
# > Arrakis
# You got it right!
# What valuable resource is only found on Dune?
# > cheese?
# Nope, the answer is: spice
# You got 1 questions right! 
{% endhighlight %}
</section>

<section markdown="block">
### Let's Write a Mini Quiz Game (Continued)!

Let's get some requirements down:

* ask two questions sequentially
* keep track of the number of questions that the player got right
* output the number of questions right
* (optional) keep track of the number of questions wrong, and output that as well
* (optional) ask for the player's name and greet the player

</section>

<section markdown="block">
### We Don't Have To Jump Right Into Code!

__So, first, what's our plan?__ &rarr;

* flow chart?
* pseudocode?
</section>

<section markdown="block">
### Let's Write a Mini Quiz Game! (Continued Some More)!

What are some ways that we can be more tolerant about capitalization?  That is... what if we wanted to accept these answers:

1. Arrakis / arrakis
2. spice / the spice / the spice melange

Another wrinkle might be to have different output based on which version of the _right_ answer was chosen.  For example, if someone puts in spice, it might say, "oh, you mean, _the spice melange_".
</section>

<section markdown="block">
## [Built-In Modules Are Up Next!](built-in-modules.html)
</section>

<section markdown="block" class="title-slide">
# Built-In Modules
</section>

<section markdown="block">
### Built-In Functions

So... again, we learned a few built-in functions.  These are all available by default.

* print
* type
* int
* str
* float
* bool
* input
</section>

<section markdown="block">
### Modules

__module__

* a file containing Python definitions and statements intended for use in other Python programs
* the contents of a module are made available to the other program by using the import statement.
</section>

<section markdown="block">
### Modules Continued

So... what does that actually mean?

* there are other functions that are not automatically loaded when you run python
* these functions (and other definitions, such as variables and constants like pi) are grouped together in files called modules
* you can bring them in to your program by using the __import__ statement
* simply use the keyword __import__ followed by the module name (with no quotes)

{% highlight python %}
import math
import random
{% endhighlight %}
</section>

<section markdown="block">
### So... What Can These Modules Do?

* math
	* __pi__ &rarr;
	* __floor__ &rarr;
	* __sqrt__ &rarr;
* random
	* __random__ &rarr;
	* __randint__ &rarr;

</section>

<section markdown="block">
### We Know How to Call Functions
<aside>But How Do You Do It From Modules?</aside>

Call or use these definitions by using the module name as the prefix and dot (__.__)... and then the function name

* math.pi()
* math.sqrt(25)
</section>

<section markdown="block">
### Let's See math and random in Use

{% highlight python %}
import math
a = math.cos(math.pi)
print(a)
b = math.sqrt(4)
print(b)

import random
a = random.randint(10)
print(a)
b = random.randint(5,10)
print(b)
{% endhighlight %}
</section>

<section markdown="block">
### Let's Simulate Rolling a Six Sided Die Twice

__Use random to "roll" two six sided dice; print out the two die rolls, as well as their sum.__&rarr;  

Try running this multiple times.

<div class="incremental" markdown="block"> 
{% highlight python %}
d1 = random.randint(1,6)
print(d1)
d2 = random.randint(1,6)
print(d2)
print('sum is: ' + str(d1 + d2))
{% endhighlight %}
</div>
</section>
