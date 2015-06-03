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

{% highlight html %}
true
false
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Boolean Operators

There are a couple of operators that return boolean values!

* __===__ - equals - checks if both operands are the __same value and type__
	* gives back true if both are the same value and type
	* gives back false otherwise
* __!==__ - not equals - checks if the operands are __not the same value or type__
	* gives back true if both operands are not the same value or type
	* gives back false otherwise

</section>

<section markdown="block">
### Boolean Expressions

You can create boolean expressions with these operators:

{% highlight html %}
1 === "1"
12 !== "cat"
{% endhighlight %}

__By the way... what is the type of value given back by these, and how do we find out what the type actually is?__ &rarr;

<div class="incremental" markdown="block">
{% highlight html %}
# boolean
var result =  1 === "1"
typeof result
{% endhighlight %}
</div>

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

{% highlight html %}
if (some_boolean_expression) {
	// do stuff here if expression is true
}
{% endhighlight %}

</section>

<section markdown="block">
### If / Else Statement

Execute one branch if condition is true, another branch if condition is false.  An else must have a preceding if!

{% highlight html %}
if (some_boolean_expression) {
	// do stuff here if expression is true
} else {
	// do stuff here if expression is false
}
{% endhighlight %}

</section>

<section markdown="block">
### If / Else If

Chain multiple conditions.  You can add else at the end as well.  Conditions are evaluated until the first true condition, at which point the if statement finishes immediately.


{% highlight html %}
if (boolean_expression_1) {
	// do stuff here if expression 1 is true
} else if (boolean_expression_2) {
	// do stuff here if expression 2 is true
} else if (boolean_expression_3) {
	// do stuff here if expression 3 is true
}
{% endhighlight %}

</section>
<section markdown="block">
### Boolean Expression

Note that within the parentheses is some expression that produces a boolean values (true or false).

{% highlight html %}
if (boolean_expression_1) {
	// do stuff here if expression 1 is true
} 
{% endhighlight %}

</section>

<section markdown="block">
### Blocks of Code

Curly braces denote statements of code that are grouped together.  Everything within the curly braces below is considered part of the if statement.

{% highlight html %}
if (boolean_expression_1) {
	// do stuff here if expression 1 is true
} 
{% endhighlight %}

</section>

