---
layout: slides
title: MTEC1002 - Drawing Revisited, Events
---

<section markdown="block" class="title-slide">

# Drawing Revisited, Events

{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Let's Draw

What HTML element do we use to draw on a web page?

<div class="incremental" markdown="block">
* a __canvas__ is an html element that be used for programmatic rendering of graphics on a web page
* think of it is a blank rectangle on your page that you can draw on
</div>

</section>

<section markdown="block">
### Setting up a Canvas 

Again, a __canvas__ is an html element - it's a tag.  You can draw on it by using JavaScript.  __How do we set it up?__ &rarr;

<div class="incremental" markdown="block">
1. create an html page
2. add your canvas tags
3. add your script tags
4. tell the page to _call your code_ once the whole page is loaded 
5. create a function that will do your drawing!
6. write some setup code so that you have access to the canvas
</div>
</section>

<section markdown="block">
### Our Usual Template

Let's start with our usual template....

{% highlight html %}
<html>
<head>
	<title></title>
</head>
<body>
<script>
</script>
</body>
</html>
{% endhighlight %}
</section>


<section markdown="block">
### A Canvas

Let's add a place to draw!.  Use a pair of opening and closing tags called canvas... with attributes, id, width, and height.

* __id__ will be used later in order to reference this particular canvas
* __width__ and __height__ are the dimensions of your drawing area
* place this tag before your JavaScript (for now... we'll see a more _correct_ way of doing it later)
* make sure to add an __id attribute__!

{% highlight html %}
<canvas id="sketch" width="800" height="600">
</canvas>
{% endhighlight %}
</section>


<section markdown="block">
### Script Tags

As usual, add your script tags:

* this can be done within the body
* you can place it before the closing body tag (after the canvas element)
{% highlight html %}
<script>
</script>
{% endhighlight %}
</section>

<section markdown="block">
### Events

We can have JavaScript run whenever a specific even happens.  We'll use __document.addEventListener__ to monitor for events.

* it takes two parameters...
* an event (as a string)
* the name of a function that should run when the event is triggered:

{% highlight js %}
document.addEventListener('DOMContentLoaded', main);
{% endhighlight %}
</section>

<section markdown="block">
### Events Continued

{% highlight js %}
document.addEventListener('DOMContentLoaded', main);
{% endhighlight %}

* the above runs a function called main when the page is loaded.
* we'll use this to start our drawing...
</section>

<section markdown="block">
### Define our Drawing Function

{% highlight js %}
function main() {
	// draw stuff here
}
{% endhighlight %}
</section>

<section markdown="block">
### A Template (Somewhat Updated)

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

function main() {
	// your code goes here
}
</script>
</body>
</html>
{% endhighlight %}
</section>

<section markdown="block">
### Drawing

About the canvas...

* the canvas origin is at 0, 0, and it's at the upper left hand corner
* positive y values go down, positive x values go right

Once you have your context, you can call _methods_ (or functions) from the context by using the dot and the function name:

{% highlight js %}
context.fillRect(30, 30, 50, 50);
{% endhighlight %}
</section>


<section markdown="block">
### A Rectangle

__fillRect__ creates a rectangle.  It takes 4 arguments:

* __x__ position
* __y__ position
* __width__ of rectangle
* __height__ of rectangle

{% highlight js %}
context.fillRect(x, y, width, height);
{% endhighlight %}

</section>

<section markdown="block">
### A Circle

A circle is a bit more complicated:

{% highlight js %}
context.beginPath();
context.arc(x, y, radius, start angle, end angle, clockwise);
context.closePath();
context.fill();
{% endhighlight %}

</section>

<section markdown="block">
### Circle Example

{% highlight js %}
context.beginPath();
context.arc(30, 10, 10, 0, 2 * Math.PI, true);
context.closePath();
context.fill();
{% endhighlight %}
</section>

<section markdown="block">
### Colors 

You can color your shapes by setting __fillStyle__:

{% highlight js %}
context.fillStyle = "#00ff00"
{% endhighlight %}

* this sets the fill color for all shapes drawn subsequently
* notice that it's not a function call
* rather... you set that property equal to a value
* the value is a _string_ representation of a hexadecimal color code
	* "#ff0000" - red
	* "#00ff00" - green
	* "#0000ff" - blue
	* "#000000" - black
</section>

<section markdown="block">
### More About Drawing
 
Each shape you create draws on top of all of your previous drawwings.  In this case, the green circle is drawn over the black square:

{% highlight js %}
context.fillRect(40, 30, 100, 100);

context.fillStyle = "#00ff00"
context.beginPath();
context.arc(50, 40, 40, 0, 2 * Math.PI, true);
context.closePath();
context.fill();
{% endhighlight %}

</section>

<section markdown="block">
### Let's Make Some Functions to Draw Stuff

* simplify making a circle by creating a function
* create a crescent using your circle function
</section>

<section markdown="block">
### A Circle Function

First... it's tough to make a circle.  __Lets try making a few functions to reduce our code.__ &rarr;

<div class="incremental" markdown="block">
{% highlight js %}
document.addEventListener('DOMContentLoaded', main);

function main() {
	var sketch = document.getElementById('sketch');
	var context = sketch.getContext("2d");
	draw_circle(context, 300, 300, 100);
}

function draw_circle(context, x, y, r) {
	context.beginPath();
	context.arc(x, y, r, 0, 2 * Math.PI, true);
	context.closePath();
	context.fill();
}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### A Crescent

<div class="incremental" markdown="block">
{% highlight js %}
document.addEventListener('DOMContentLoaded', main);

function main() {
	var sketch = document.getElementById('sketch');
	var context = sketch.getContext("2d");
	draw_moon(context, 300, 300, 100);
}

function draw_circle(context, x, y, r) {
	context.beginPath();
	context.arc(x, y, r, 0, 2 * Math.PI, true);
	context.closePath();
	context.fill();
}

function draw_moon(context, x, y, r) {
	draw_circle(context, x, y, r)
	context.fillStyle =	"#ffffff";	
	draw_circle(context, x + 50, y + 50, r)
}
{% endhighlight %}
</div>
</section>



<section markdown="block">
### The Full Program

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

function main() {
	var sketch = document.getElementById('sketch');
	var context = sketch.getContext("2d");
	draw_moon(context, 300, 300, 100);
}

function draw_circle(context, x, y, r) {
	context.beginPath();
	context.arc(x, y, r, 0, 2 * Math.PI, true);
	context.closePath();
	context.fill();
}

function draw_moon(context, x, y, r) {
	draw_circle(context, x, y, r)
	context.fillStyle =	"#ffffff";	
	draw_circle(context, x + 50, y + 50, r)
}

</script>
</body>
</html>
{% endhighlight %}
</section>

