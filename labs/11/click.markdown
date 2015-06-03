---
layout: slides
title: MTEC1002 - JavaScript For Loop
---

<section markdown="block" class="title-slide">

# Click Events

{% include title-slide-footer.html %}
</section>

<section markdown="block">
### What Will This Code Output in the JavaScript Console?
{% highlight js %}
function greet() {
	return "hello";
}
print(typeof greet);
// gives us a function without a name
{% endhighlight %}

<div class="incremental" markdown="block">
* function
* remember ... functions are types
</div>
</section>


<section markdown="block">
### Anonymous Functions

We can create functions without names!

{% highlight js %}
function(event) {
		draw_exclamation(event.x, event.y);
}
// gives us a function without a name
{% endhighlight %}

...and we can pass these as arguments to another function.

</section>

<section markdown="block">
### A Click

In addition to detecting when a page loads, you can __listen for when an element is clicked__:

{% highlight js %}
sketch.addEventListener("click", function(event) {
	// your code here... event.x, event.y
});
{% endhighlight %}

* note that we pass in an _anonymous_ function as the second argument rather than a named argument
* it takes a single parameter, which contains the x and y values of where the click occurred
</section>

<section markdown="block">
### Event Objects

Note that we can access the event created from clicking!

This contains the x and y coordinates of where the click occurred.
</section>

<section markdown="block">
### Clicking Circles

<div class="incremental" markdown="block">
{% highlight html %}
<html>
<head>
    <title></title>
</head>
<body>
<canvas id="sketch" width="800" height="600">
</canvas>
<script>
document.addEventListener('DOMContentLoaded', main);

var sketch;
var context;

function main() {
	sketch = document.getElementById('sketch');
	context = sketch.getContext("2d");
	context.fillStyle = "#992255";
	sketch.addEventListener("click", function(event) {
		draw_circle(event.x, event.y, 75);
	});
}

function draw_circle(x, y, r) {
	context.beginPath();
	context.arc(x, y, r, 0, 2 * Math.PI, true);
	context.closePath();
	context.fill();
}
</script>
</body>
</html>
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Clearing the Screen

{% highlight js %}
context.clearRect(0, 0, sketch.offsetWidth, sketch.offsetHeight);
{% endhighlight %}
</section>

<section markdown="block">
### Two Items Relative to One Another

{% highlight js %}
document.addEventListener('DOMContentLoaded', main);
var sketch;
var context;
function main() {
	sketch = document.getElementById('sketch');
	context = sketch.getContext("2d");
	sketch.addEventListener("click", function(event) {
		draw_exclamation(event.x, event.y);
	});
}
function draw_exclamation(x, y) {
	context.fillRect(x, y, 50, 100);
	draw_circle(x + 25, y + 150, 25);
}
function draw_circle(x, y, r) {
	context.beginPath();
	context.arc(x, y, r, 0, 2 * Math.PI, true);
	context.closePath();
	context.fill();
}
{% endhighlight %}
</section>
