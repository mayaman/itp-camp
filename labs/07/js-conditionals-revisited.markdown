---
layout: slides
title: MTEC1002 - JavaScript Conditionals
---

<section markdown="block" class="title-slide">

# JavaScript Conditionals

{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Source Material

See the first two chapters of the second edition of [Eloquent JavaScript](http://eloquentjavascript.net/2nd_edition/preview/) for more detailed information:

* [Chapter 1 - Values](http://eloquentjavascript.net/2nd_edition/preview/01_values.html)
* [Chapter 2 - Program Structure](http://eloquentjavascript.net/2nd_edition/preview/02_program_structure.html)
</section>


<section markdown="block">
### Boolean Values

Besides numbers and strings, there is another type that we talked about briefly.  __They are booleans.  What are the possible values that a boolean can be?__ &rarr; 

<div class="incremental" markdown="block">
* a boolean value is __true__ or __false__
* a literal __true__ and __false__ is just:

{% highlight js %}
true
false
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Boolean Operators

__What are some operators that return boolean values?__ &rarr;

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
### Boolean Expressions

You can create boolean expressions with these operators.  __What is the value that results from the following expressions?  What type are they?__ &rarr;

{% highlight js %}
1 === "1"
12 !== "cat"
{% endhighlight %}


<div class="incremental" markdown="block">
{% highlight js %}
// boolean
false
true
{% endhighlight %}
</div>

</section>

<section markdown="block">
### Additional Comparison Operators

__Can you think of other comparison operators that JavaScript may have?__ &rarr;

<div class="incremental" markdown="block">
* these all return boolean values
* less than - __&lt;__
* greater than - __&gt;__
* less than or equal to - __&lt;=__
* greater than or equal to- __&gt;=__
</div>

</section>

<section markdown="block">
### Additional Comparison Operators Continued

{% highlight js %}
// false!
5 > 7

// true!
5 >= 5
{% endhighlight %}

</section>

<section markdown="block">
## Boolean Expressions Give Back Boolean Values!
</section>

<section markdown="block">
### Conditionals

[See Conditional Execution in Eloquent JavaScript](http://eloquentjavascript.net/2nd_edition/preview/02_program_structure.html)

A conditional is a way of allowing us to conditionally execute code based on a boolean expression.

</section>

<section markdown="block">
### If Statement

Conditionally execute a branch of code.

{% highlight js %}
if (some_boolean_expression) {
	// do stuff here if expression is true
}
{% endhighlight %}

* [Diagram for if statements](../../resources/img/if.png)
* [Diagram for consecutive if statements](../../resources/img/if-consecutive.png)

</section>

<section markdown="block">
### If / Else Statement

Execute one branch if condition is true, another branch if condition is false.  An else must have a preceding if!

{% highlight js %}
if (some_boolean_expression) {
	// do stuff here if expression is true
} else {
	// do stuff here if expression is false
}
{% endhighlight %}

* [Diagram for if / else statements](../../resources/img/if-else.png)
* else statements are always attached to an if!

</section>

<section markdown="block">
### If / Else If

Chain multiple conditions.  You can add else at the end as well.  Conditions are evaluated until the first true condition, at which point the if statement finishes immediately.


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
</section>


<section markdown="block">
### Usage

* use if statements if there's a single alternative path of execution
* use if/else  statements if there's a two possible alternative paths of execution
* use if/else if statements if there's more than two possible alternative paths of execution
</section>

<section markdown="block">
### Boolean Expressions

Note that within the parentheses is some expression that produces a boolean values (true or false).

{% highlight js %}
if (boolean_expression_1) {
	// do stuff here if expression 1 is true
} 
{% endhighlight %}

</section>

<section markdown="block">
### Blocks of Code

Curly braces denote statements of code that are grouped together.  Everything within the curly braces below is considered part of the if statement.

{% highlight js %}
if (boolean_expression_1) {
	// do stuff here if expression 1 is true
} 
{% endhighlight %}

</section>


<section markdown="block">
### Logical Operators

Logical operators allow you to combine boolean values!

* __and__ (represented as __&amp;&amp;__) - takes two operands.  
	* only gives back true when both operands are true.
	* gives back false otherwise
* __or__ (represented as __&#124;&#124;__) - takes two operands. 
	* returns true if either operand is true
	* it only gives back false when both operands are false.
</section>

<section markdown="block">
### Using Logical Operators

Examples

{% highlight js %}
// variable num is between 1 and 10
if(num >= 1 && num <=10) {
	print("it's between 1 and 10")
}

// answer is yeah or yes
if(answer === 'yes' || answer === 'yeah' ) {
	print("YUP!")
}
{% endhighlight %}
</section>

<section markdown="block">
### Converting from Numbers to Strings

Use the built-in function __parseInt__ to convert a number to a string.

* parseInt takes two arguments, the string to convert, and the radix (which will be 10 for us)
* we can use this when we get user input... __why would we need to do this?__...

{% highlight js %}
var num = parseInt(answer, 10);
{% endhighlight %}
</section>
