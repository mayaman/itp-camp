---
layout: slides
title: MTEC1002 - Canvas
---

<section markdown="block" class="title-slide">

# Canvas Preview

{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Our Usual Template

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

{% highlight html %}
<canvas id="sketch" width="300" height="225">
</canvas>
{% endhighlight %}
</section>

<section markdown="block">
### A Canvas in Context

Here's everything put together.

{% highlight html %}
<html>
<head>
	<title></title>
</head>
<body>
<canvas id="sketch" width="300" height="225">
</canvas>
<script>
</script>
</body>
</html>
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
### Drawing

About the canvas...

* the canvas origin is at 0, 0, and it's at the upper left hand corner
* positive y values go down, positive x values go right

Once you have your context, you can call _methods_ (or functions) from the context by using the dot and the function name:

{% highlight html %}
<script>
context.fillRect(30, 30, 50, 50);
</script>

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

<!--
fill example
context.fillStyle = "#00ff00";
hex colors
whole example
-->
