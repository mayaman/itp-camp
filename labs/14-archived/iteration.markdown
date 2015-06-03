---
layout: slides
title: For Loops and While Loops
---

<section markdown="block" class="title-slide">
# While Loops 

{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Motivation for Loops

A program to count from 1 to 9:

{% highlight python %}
n, delta = 1, 1
print(n)
n = n + delta
print(n)
n = n + delta
print(n)
n = n + delta
print(n)
n = n + delta
print(n)
n = n + delta
print(n)
n = n + delta
print(n)
n = n + delta
print(n)
n = n + delta
print(n)
{% endhighlight %}
</section>

<section markdown="block">
### Motivation for Loops Continued

Um.  That was _kind of tedious_.  Can't we just tell the computer to repeat those two lines of code?  

__YES! ...using loops__

{% highlight python %}
n = 1
end = 9
delta = 1

while n <= end:
	print(n)
	n = n + delta
{% endhighlight %}
</section>

<section markdown="block">
### Iteration and Loops

Some formal definitions:

* __iteration__ - repeated execution of a set of programming statements.
* __loop__ - the construct that allows allows us to repeatedly execute a statement or a group of statements until a terminating condition is satisfied.
* sometimes these words are used interchangeably
</section>

<section markdown="block">
### While Loops

Using a __while__ loop allows us to:

* repeat a block of code
* until a condition is met
* looks similar to an if statement
</section>

<section markdown="block">
### While Loop Syntax

A template:

{% highlight python %}
# while <some sort of condition>:
#	<do stuff here>
{% endhighlight %}

Some _real_ code:

{% highlight python %}
a = 100
while a > -1:
	print(a)
{% endhighlight %}

__What does this output? &rarr;__

<div class="incremental">
{% highlight python %}
100
100
100
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Trivial Cases, Again

__What do these snippets of code print out?&rarr;__
{% highlight python %}
while True:
	print("I'm true!")
{% endhighlight %}
{% highlight python %}
while False:
	print("I'm false!")
{% endhighlight %}

<div class="incremental">
{% highlight python %}
I'm true!
I'm true!
I'm true!
{% endhighlight %}
{% highlight python %}
# nothing printed here
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Let's Step Through True
{% highlight python %}
while True:
	print("I'm true!")
{% endhighlight %}

1. condition is true
2. print "I'm true!"
3. go back to top
4. condition is true
5. print "I'm true!"
6. go back to top
7. you know the _deal_
</section>

<section markdown="block">
### Let's Step Through False
{% highlight python %}
while False:
	print("I'm false!")
{% endhighlight %}

1. condition is false

We never even get into the body of the loop!
</section>

<section markdown="block">
### Slightly More Complicated
<aside>Well, Not This One Exactly, But You'll See</aside>

__What does this print out? &rarr;__

{% highlight python %}
keep_on_going = True
while keep_on_going:
	print("I'm going!)"
{% endhighlight %}

<div class="incremental">
{% highlight python %}
I'm going
I'm going
I'm going
.
.
I'm going
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Slightly More Complicated Continued

__Let's add one line.  What does this print out? &rarr;__

{% highlight python %}
keep_on_going = True
while keep_on_going:
	print("I'm going!")
	keep_on_going = False
{% endhighlight %}

<div class="incremental">
{% highlight python %}
I'm going
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Slightly More Complicated Continued Continued

Going through each iteration

{% highlight python %}
keep_on_going = True
while keep_on_going:
	print("I'm going!")
	keep_on_going = False
{% endhighlight %}

* condition (keep_on_going) is true 
* print "I'm going!"
* set keep_on_going to false
* condition (keep_on_going) is false

Loop ends after one iteration.
</section>

<section markdown="block">
### What Happened There?

* we had some state __outside__ of the loop
* __within__ the loop we mutated / changed that state to eventually get out of the condition
* consequently, the loop _terminates_
* sometimes we call these kinds of variables __sentinel__ variables
* they only let certain conditions in!
</section>

<section markdown="block">
### Affecting the Outcome of the Condition

To change the outcome of your conditional:

* maintain state 
	* declare a variable __outside__ of the loop!
* mutate that state on loop iteration 
	* change that variable __inside__ the loop!
	* this will eventually cause the conditional to fail
* examples:
	* using operators to change a variable in your condition
	* using input to change a variable in your condition
</section>


<section markdown="block">
### Count From 2 Through 8 By 2's

__How would you implement this?&rarr;__

<div class="incremental">
{% highlight python %}
count = 2
while count <= 8:
	print(count)
	count = count + 2
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Stepping Through Counting By 2's
{% highlight python %}
count = 2
while count <= 8:
	print(count)
	count = count + 2
{% endhighlight %}
1. count is 2
2. condition is true because count (2) is less than 8
3. print count
4. add 2 to count... count is now 4
5. condition is true because count(4) is less than 8..
6. goes on until count gets to 10, at which point condition is no longer true

[Check out the fancy step through](http://www.pythontutor.com/visualize.html#code=count+%3D+0%0Awhile+count+%3C%3D+8%3A++++%0A++++print(count)%0A++++count+%3D+count+%2B+2&mode=display&cumulative=false&py=2&curInstr=0)
</section>

<section markdown="block">
### Odd Numbers Except 13

__Write a program that... &rarr;__

* prints all of the odd numbers from 1-99
* skips 13

There are a few ways to do this!  __What are some general strategies for solving this problem?&rarr;__

<div markdown="block" class="incremental">

* using modulo
* or incrementing by twos

</div>
</section>

<section markdown="block">
### Possible Solutions for Odd Numbers Except 13
 
[Increment by 2's](http://www.pythontutor.com/visualize.html#code=n+%3D+1%0Awhile+n+%3C%3D+99%3A%0A++++if+n+!%3D+13%3A%0A++++++++print(n)%0A++++n+%3D+n+%2B+2&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&py=3&curInstr=0)

{% highlight python %}
n = 1
while n <= 99:
    if n != 13:
        print(n)
    n = n + 2
{% endhighlight %}

[Using modulo to determine odds](http://www.pythontutor.com/visualize.html#code=n+%3D+1%0Awhile+n+%3C%3D+99%3A%0A++++if+n+!%3D+13%3A%0A++++++++print(n)%0A++++n+%3D+n+%2B+2&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&py=3&curInstr=0)

{% highlight python %}
n = 1
while n <= 99:
    if n % 2 == 1 and n != 13:
        print(n)
    n = n + 1
{% endhighlight %}
</section>

<section markdown="block">
### Do You Want Cake (Again)

__Repeatedy ask if user wants cake until user says yes or yeah.  How would you implement this?&rarr;__

{% highlight python %}
Do you want cake?
> no
Do you want cake?
> No
Do you want cake?
> yeah
Have some cake!
{% endhighlight %}

<div class="incremental">
{% highlight python %}
answer = 'no'
while answer != 'yes' and answer != 'yeah':
	answer = raw_input("Do you want cake?\n> ")
print("Have some cake!")
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Stepping Through Cake

Let's make an assumption that the user enters "no" first, and then "yeah" second.

{% highlight python %}
answer = 'no'
while answer != 'yes' and answer != 'yeah':
	answer = raw_input("Do you want cake?\n> ")
print("Have some cake!")
{% endhighlight %}

1. answer is set to no by default
2. condition is true, answer (no) is not 'yes' or 'yeah'
3. answer is set to user input of 'no'
4. condition is true, answer (no) is not 'yes' or 'yeah'
5. answer is set to user input of 'yes'
6. condition is false, answer != 'yeah' is now false!
7. have some cake is printed
</section>

<section markdown="block">
### Accumulating Values

__Write a program that will: &rarr;__ 

* continually ask the user for a number (__forever__)
* add that number to a running total
* print out the running total

{% highlight python %}
Give me a number to add
> 10
Current total is 10
Give me a number to add
> 15
Current total is 25
Give me a number to add
> 5
Current total is 30
Give me a number to add
> 
{% endhighlight %}

</section>

<section markdown="block">
### Potential Solution for Accumulating Values

{% highlight python %}
total = 0
while True:
    n = int(raw_input("Give me a number to add\n> "))
    total = total + n
    print("Current total is " + str(total))
{% endhighlight %}

</section>

<section markdown="block">
### A Difficult One... 

__Write a program that continually asks the user for numbers, and asks them if they'd like to keep going.  In the end, it should output the average of all of the numbers entered&rarr;__

{% highlight python %}
I'll calculate the average for you!
Current total: 0
Numbers summed: 0
Please enter a number to add
> 10
Do you want to continue adding numbers (yes/no)?
> yes
Current total: 10
Numbers summed: 1
Please enter a number to add
> 12
Do you want to continue adding numbers (yes/no)?
> no
The average is 11.0
{% endhighlight %}
</section>

<section markdown="block">
### Some Hints, Please?
Let's try keeping track of multiple variables:

* a user's answer to whether or not the program should continue
* the total (sum) of the numbers that a user has entered 
* the count of numbers input
</section>

<section markdown="block">
### An Average Solution

{% highlight python %}
total = 0
count = 0
answer = 'yes'
print("I'll calculate the average for you!")
while answer == 'yes':
        print("Current total: " + str(total))
        print("Numbers summed: " + str(count))
        total = total + int(raw_input("Please enter a number to add\n> "))
        count = count + 1
        answer = raw_input("Do you want to continue adding numbers (yes/no)?\n> ")
print("The average is "+ str(total / count))
{% endhighlight %}
</section>

<section markdown="block">
### Increment / Decrement

We've used the following syntax to increment or decrement a variable

{% highlight python %}
n = 0
n = n + 1

n = 100
n = n - 1
{% endhighlight %}

_Slightly_ tedious...
</section>

<section markdown="block">
### Increment / Decrement Continued

There's some _syntactic sugar_ that makes doing this less verbose:  use __+=__ or __-=__

* __n += 1__ is the same as n = n + 1
* __n -= 1__ is the same as n = n - 1

{% highlight python %}
n = 0
# adds one to n and binds the resulting value to n
n +=  1

n = 100
# subtracts one to n and binds the resulting value to n
n -= 1
{% endhighlight %}

</section>

<section markdown="block">
### More Syntactic Sugar

This works for other operators too.   __What does this code print out? &rarr;__

{% highlight python %}
n = 2
n *= 2
n *= 2
print(n)

n = 64
n /= 2
n /= 2
print(n)
{% endhighlight %}
<div class="incremental">
{% highlight python %}
8
16.0
{% endhighlight %}
</div>

</section>

<section markdown="block">
### What About Strings?

Also works with strings....   __What does this code print out? &rarr;__
{% highlight python %}
s = "h"
s += "e"
s += "y"
s *= 3
print(s)
{% endhighlight %}

<div class="incremental">
{% highlight python %}
heyheyhey
{% endhighlight %}
</div>

<!-- remove asterisk* -->
</section>

<section markdown="block">
### Other Exercises

* count the number of digits in an int
	* repeatedly use integer division
	* ...until the original number becomes 0
	* keep count of divisions
* continually add exclamation points to a word
	* ask for a word
	* ask for x number of exclamation points
	* print out resulting word and exclamation points
	* continue asking for another word and exclamation points
</section>

<section markdown="block" class="title-slide">
# For Loops

{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Two Kinds of Loops

The two kinds of loops in Python are:

* __while__ loops
* __for__ loops
</section>

<section markdown="block">
### Let's See What For Loops Can Do

__for loops__ repeat code by iterating over every item in some group / collection of items:

{% highlight python %}
# (we'll talk about range() in a second)
for i in range(5):
	print i
{% endhighlight %}

Outputs the following:

{% highlight python %}
0
1
2
3
4
{% endhighlight %}
</section>

<section markdown="block">
### For Loop Syntax

Syntax

{% highlight bash %}
# for <some variable name> in <iterable object>:
#	(<some variable name> can be used here)
{% endhighlight %}

Again, the same example:

{% highlight bash %}
# variable  an iterable object, like range
#     |      |
#     |      |
# for i in range(5):
# 	print i
{% endhighlight %}
</section>

<section markdown="block">
### For Loops

A more technical explanation is: __for loops__ iterate over every item in an __iterable object__.  

An _iterable object_:

* is a _thing_ (_object_) that contains other values / _members_
* is capable of returning each of its members __one at a time__
* examples of iterable objects include: 
	* strings
	* lists
	* __range objects__
* so... let's see about these __range objects__
</section>

<section markdown="block">
### Range and Range Objects

A __range__ object is another data type!  It represents an arithmetic sequence, such as 0, 1, 2, 3, 4.

* a __range__ object is created by calling the range() function.
* with one argument, it creates an arithmetic sequence from 0 up to but __not including__ that argument
* consequently, range(5) produces 0, 1, 2, 3, 4
* to see the elements in a range, you can use the __list()__ function
* (we'll learn more about lists later!)
</section>

<section markdown="block">
### This Makes Absolutely No Sense!
{% highlight python %}
numbers = range(5)
print(numbers)
print(type(numbers))
print(list(numbers))
{% endhighlight %}

{% highlight python %}
range(0, 5)
<class 'range'>
[0, 1, 2, 3, 4]
{% endhighlight %}
</section>

<section markdown="block">
### So... All of That Meant...

* there's a type called __range__
* the string representation of a range shows you the original arguments that you passed in
* you can call the list method to show the exact ints in the list
</section>

<section markdown="block">
### Quick Summary So Far...

We've learned two new built in functions

* __range__ returns a range _object_, a representation of an arithmetic sequence
* __list__ returns a list _object_
	* for now, we use list in combination with print  to show each number in a range object
	* we'll learn more about lists later
</section>

<section markdown="block">
### Range with 1 Parameter

As mentioned previously...

* with one argument, range(x) creates an arithmetic sequence from 0 up to but __not including__ that argument
* consequently, range(5) produces 0, 1, 2, 3, 4
</section>

<section markdown="block">
### Range Can Also Take 2 Parameters

With two arguments: range(5, 10)

* the first specifies the first element... 
* the second specifies the element that the sequence will go up to (but not include)
* 5, 6, 7, 8, 9
</section>

<section markdown="block">
### Oh Yeah, It Can Also Take 3 Parameters

With three arguments: range(3, 22, 6)

* the first specifies the first element...
* the second specifies the element that the sequence will go up to (but not include)
* the third is the _step_
* [3, 9, 15, 21]

__What do you think happens if the step is negative? Like range(10,0, -1) &rarr;__

<div class="incremental">
{% highlight python %}
print(list(range(10, 0, -1)))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
{% endhighlight %}
</div>

</section>

<section markdown="block">
### Using range in a Loop (2 Arguments)

__What would this print out?&rarr;__

{% highlight python %}
for i in range(5, 10):
	print(i)
{% endhighlight %}

<div class="incremental">
{% highlight python %}
5
6
7
8
9
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Using range in a Loop (3 Arguments)

__What would this print out?&rarr;__

{% highlight python %}
for i in range(10, 0, -1):
	print(i)
{% endhighlight %}
<div class="incremental">
{% highlight python %}
10
9
8
.
.
1
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Some Exercises!
* count to 100 starting from 1
* count to 100 by twos from 0
* count backwards starting from 100 down to and including 0
* sum the first 1-100 numbers (which, of course, [doesn't need a loop](http://betterexplained.com/articles/techniques-for-adding-the-numbers-1-to-100/))
</section>

<section markdown="block">
### Some More Exercises
* roll a die 1000 times; count how many times a one is rolled!
* [fizz buzz](http://c2.com/cgi/wiki?FizzBuzzTest)
* make me a ladder 
	* ask for a height, make a ladder with that rungs
	* can you do using a for loop?
	* or how about just string multiplication?

{% highlight python %}
 ========
 |      |
 ========
 |      |
 ========
 |      |
{% endhighlight %}
</section>

<section markdown="block" class="title-slide">
# While Loops vs For Loops

{% include title-slide-footer.html %}
</section>

<section markdown="block">
### For Loops...

__When should you use them? &rarr;__

<div class="incremental" markdown="block">
* you know ahead of time how many iterations you'll have to go through
* you have an _iterable_ structure that you have to traverse
	* a sequence of numbers
	* a list of _items_
</div>
</section>

<section markdown="block">
### While Loops

__When should you use them? &rarr;__

<div class="incremental" markdown="block">
* when you don't know how many iterations you'll have to go through!
* when you must repeat something until some condition is met
* generally not a great option for counting (need to keep track of counter separately)
	
</div>
</section>

<section markdown="block">
### Let's Try Using Both...
* count to 0 to 25 by 5's
	* implement using while
	* implement using for
* generate a series of numbers, each randomly chosen from (1 through 10) that add up to 50 (you can go over)
	* implement using while
	* implement using for
</section>

