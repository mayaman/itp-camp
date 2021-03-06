---
layout: slides
title: MTEC1002 - Canvas
---

<section markdown="block" class="title-slide">

# Canvas 

{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Let's Draw

Tired of text?  We can actually __draw__ with JavaScript using a __canvas__.

* a __canvas__ is an html element that be used for programmatic rendering of graphics on a web page
* think of it is a blank rectangle on your page that you can draw on
</section>

<section markdown="block">
### Setting up a Canvas 

again, a __canvas__ is an html element - it's a tag.  You can draw on it by using JavaScript.  Here's how you set it up:

1. create an html page
2. tell the page to _call your code_ once the whole page is loaded (right now, we'll do this by adding an onload attribute to the body tag)
3. add your canvas tags
4. add your script tags
5. create a function that will do your drawing!
6. write some setup code so that you have access to the canvas


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
### Telling Your Page to Draw Something

We'll have to let the page know that it should start drawing once the entire page is loaded.  

* we do this by adding an onclick event handler to the body tag... 
* that calls a function called draw()that we'll define later
* note that there are better ways to do this, but we'll go with this technique for now

{% highlight html %}
<body onclick="draw()">
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
<canvas id="sketch" width="300" height="300">
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
### Draw Function

Within your script tags, define the function that you specified in your body tag.

{% highlight html %}
<script>
function draw() {
 // your drawing goes here
}
</script>
{% endhighlight %}
</section>

<section markdown="block">
### Using Your Canvas in JavaScript

In order to draw on your canvas, you have to:

1. _retrieve_ the canvas element from your page using the id
2. get the context from your canvas element (which is what we'll be using to draw)
{% highlight html %}

<script>
var sketch = document.getElementById('sketch');
var context = sketch.getContext("2d");
</script>
{% endhighlight %}

</section>

<section markdown="block">
### All Together Now...

Here's everything put together.

{% highlight html %}
<html>
<head>
	<title></title>
</head>
<body onload="draw()">
<canvas id="sketch" width="300" height="300">
</canvas>
<script>
function draw() {
	var sketch = document.getElementById('sketch');
	var context = sketch.getContext("2d");
	// draw stuff here!
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
### An Example Program:

{% highlight html %}
<body onload="draw()">
<canvas id="sketch" width="300" height="300">
</canvas>
<script>
function draw() {
        var sketch = document.getElementById('sketch');
        var context = sketch.getContext("2d");

        context.fillRect(40, 30, 100, 100);

        context.fillStyle = "#00ff00"
        context.beginPath();
        context.arc(50, 40, 40, 0, 2 * Math.PI, true);
        context.closePath();
        context.fill();
}
</script>
</body>
{% endhighlight %}
</section>
