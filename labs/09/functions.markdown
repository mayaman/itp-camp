---
layout: slides
title: MTEC1002 - JavaScript For Loop
---

<section markdown="block" class="title-slide">

# Functions

{% include title-slide-footer.html %}
</section>


<section markdown="block">
### Built-in Functions

__What are some functions that we know?__

<div class="incremental" markdown="block">
{% highlight js %}
prompt("number please...");
console.log("hi");
parseInt("5");
{% endhighlight %}

</div>
</section>

<section markdown="block">
## We can write our own functions!
</section>

<section markdown="block">
### Creating Functions

1. start with the keyword, __function__
2. followed by the name of your function
3. followed by parentheses
4. followed by an _optional_ list of comma separated parameters (input)
5. close parentheses
6. a block of code between curly braces
</section>

<section markdown="block">
### Basic Functions

Here's a bare bones function....

{% highlight js %}
function foo() {
	console.log("FOO!");
}
{% endhighlight %}
</section>

<section markdown="block">
### A Function With Parameters

To create a function that has an input, and executes some code...

{% highlight js %}
function foo(s) {
	console.log(s + "!");
}
{% endhighlight %}
</section>

<section markdown="block">
### A Function With Parameters That Returns a Value

To create a function that has an inputs, and returns a value....

{% highlight js %}
function foo(s) {
	return s + "!";
}
console.log(foo("hi"));
{% endhighlight %}
</section>
