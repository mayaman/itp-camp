---
layout: slides
title: MTEC1002 - JavaScript For Loop
---

<section markdown="block" class="title-slide">

# Functions Revisited

{% include title-slide-footer.html %}
</section>




<section markdown="block">
## We can write our own functions!
</section>

<section markdown="block">
### Creating Functions

__How do we write our own functions?__ &rarr;

<div class="incremental" markdown="block">

1. start with the keyword, __function__
2. followed by the name of your function
3. followed by parentheses
4. followed by an _optional_ list of comma separated parameters (input)
5. close parentheses
6. a block of code between curly braces
</div>
</section>

<section markdown="block">
### An Example

{% highlight js %}
function foo() {
	console.log("FOO!");
}
{% endhighlight %}
</section>

<section markdown="block">
### A Function With Parameters (Input)

__How do we create a function that has parameters or inputs?__ &rarr;

<div class="incremental" markdown="block">
{% highlight js %}
function foo(s) {
	console.log(s + "!");
}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Giving Back Values (Output)

__How do we create a function that gives back values?__ &rarr;

<div class="incremental" markdown="block">
{% highlight js %}
// use the keyword, return
function foo(s) {
	return s + "!";
}
console.log(foo("hi"));
{% endhighlight %}
</div>
</section>

<section markdown="block">
### A Few Notes About Functions

* can be defined anywhere (that is, you can use them even if they are defined later in your file)
* inputs and outputs are __optional__
* a functions is another type!
* let's define a function... and prove this (__how do we show type?__)
</section>

<section markdown="block">
## A Function is Another Type!
</section>

<section markdown="block">
### Demos

* factorial function
* sum of three numbers function
</section>
