---
layout: slides
title: MTEC1002 - JavaScript For Loop
---

<section markdown="block" class="title-slide">

# For Loops

{% include title-slide-footer.html %}
</section>


<section markdown="block">
### Counting

__Let's write a program that prints out the number 0 through 5 to the JavaScript Console.__ &rarr;

<div class="incremental" markdown="block">
{% highlight js %}
//start out with the surrounding html
console.log(0)
console.log(1)
console.log(2)
console.log(3)
console.log(4)
console.log(5)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Let's Spruce That Up a Bit

__How can we change this so that we print out a single variable that is incremented after each print.__ &rarr;

{% highlight js %}
// what if we just want to make multiple calls to the following line...
console.log(n);

// what's the missing code to make this count from 0 through 5?
{% endhighlight %}
</section>

<section markdown="block">
### Let's Spruce That Up a Bit Continued

{% highlight js %}
var n = 0;
var increment = 1;
console.log(n);
n = n + 1;
console.log(n);
n = n + 1;
console.log(n);
n = n + 1;
console.log(n);
n = n + 1;
console.log(n);
n = n + 1;
console.log(n);
{% endhighlight %}
</section>

<section markdown="block">
### A Closer Look...

__Is there a pattern here?__ &rarr;

{% highlight js %}
var n = 0;
var increment = 1;
console.log(n);
n = n + 1;
console.log(n);
n = n + 1;
console.log(n);
n = n + 1;
console.log(n);
n = n + 1;
console.log(n);
n = n + 1;
console.log(n);
{% endhighlight %}
</section>

<section markdown="block">
### A Closer Look Continued

__The following two lines were repeated 5 times!__ &rarr;

{% highlight js %}
console.log(n);
n = n + 1;
{% endhighlight %}

__That's a bit tedious, right?__
</section>

<section markdown="block">
### Some Motivation

__Wouldn't it be great if we could just tell the computer to repeat this block of code for us?__ &rarr;

{% highlight js %}
console.log(n);
n = n + 1;
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
###  Loops

JavaScript has a couple of structures that allow us to __repeat__ blocks of code!

* for loops - _count_ controlled (repeats code for a specific number of times)
* while loops - _condition_ controlled (repeats code as long as a condition is true)
</section>

<section markdown="block">
### Today, We're Using For Loops 

For now, we'll use for loops to repeat a block of code a specific number of times.  __The following code counts from 0 through 5.__ &rarr;

{% highlight js %}
for(var i = 0; i <= 5; i = i + 1) {
	console.log(i);
}
{% endhighlight %}
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
### For Loop Notes

{% highlight js %}
//    initialization
//    |        condition
//    |        |       afterthought/increment
//    |        |       |
for(var i = 0; i <= 5; i = i + 1) {
	console.log(i);
}
{% endhighlight %}

Notice that:

* we can use the variable created in the initialization
* the afterthought (3rd part) adds 1 to the variable on each iteration
</section>

<section markdown="block">
### Counting By 2's 

__How can we change our loop to count from 5 to 10 instead?__ &rarr;

<div class="incremental" markdown="block">
{% highlight js %}
for(var i = 5; i <= 10; i = i + 1) {
	console.log(i);
}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Counting By 2's 

__How can we change our loop to count by 2's from 0 to 10?__ &rarr;

<div class="incremental" markdown="block">
{% highlight js %}
for(var i = 0; i <= 10; i = i + 2) {
	console.log(i);
}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Backwards

__How can we change our loop to count backwards from 10 to 0?__ &rarr;

<div class="incremental" markdown="block">
{% highlight js %}
for(var i = 10; i >= 0; i = i - 1) {
	console.log(i);
}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Using Variables Outside of the Loop 

__Write a program that adds the numbers 1 through 100 together.  Try creating a variable outside of the for loop... and change that variable on each iteration.__ &rarr;

<div class="incremental" markdown="block">
{% highlight js %}
var total = 0;

for(var num = 1; num <= 100; num = num + 1) {
	total = total + num;
}
console.log(total)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Using Input in a For Loop 

__Write a program that asks for 4 numbers.  If the numbers is greater than 10, print out "That's a lot".  Use a for loop to do this.__ &rarr;

<div class="incremental" markdown="block">
{% highlight js %}
var total = 0;

for(var num = 1; num <= 100; num = num + 1) {
	total = total + num;
}
console.log(total)
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Controlling the Condition of a For Loop With a Variable

__Ask the user for a number... and use a for loop to count from 0 up to that number.__

<div class="incremental" markdown="block">
{% highlight js %}
var answer = prompt("Give me a number to count up to");
var end = parseInt(answer);

for(var num = 1; num <= end; num = num + 1) {
	console.log(num);
}
console.log(total)
{% endhighlight %}
</div>
</section>

