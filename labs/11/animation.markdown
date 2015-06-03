---
layout: slides
title: MTEC1002 - JavaScript For Loop
---

<section markdown="block" class="title-slide">

# Animation

{% include title-slide-footer.html %}
</section>

<section markdown="block">
## We Can Actually Make Our Drawings Move!
</section>

<section markdown="block">
### Animation

1. Clear canvas
2. Draw image
3. Move position of image
4. Go back to step #1

(think of a flip book!)
</section>

<section markdown="block">
### Clearing the Canvas

* context.clearRect will blank out the canvas
* pass it the following arguments: 0, 0, the width and heigh of the canvas
	* we can access our canvas element, called sketch
	* use the variables offsetWidth and offsetHeight

{% highlight js %}
context.clearRect(0, 0, sketch.offsetWidth, sketch.offsetHeight);
{% endhighlight %}
</section>



<section markdown="block">
### Repeatedly Drawing

To repeatedly draw and clear out images, we can use a built-in function called __setInterval__  - it takes two parameters:

* the function to call
* the time to call it in

{% highlight js %}

// will repeatedly call animate every 10ms
setInterval(animate, 10);

{% endhighlight %}
</section>

<section markdown="block">
### Velocity and Position

In order to keep track of how our drawing moves, will need to use a few variables:

* velocity (dx or dy)
* the drawings position (we can use a javascript object!)

</section>

<section markdown="block">
### An Object

* an object is basically a container for arbitrary properties
* example: circle = {'x':5, 'y':2};
* each property and value is separated by a colon
* each set of property/value pairs are separated by commas
* the entire object is surrounded by curly braces
* properties can be accessed using the dot operator: circle.x
</section>

<section markdown="block">
### The Animate Function 

* on each call of animate, we will draw based on the object's position
* ...then ... we'll modify the position by adding the velocity (dx or dy)
</section>

<section markdown="block">
## Let's create a rectangle that travels across the screen horizontally.
</section>

<section markdown="block">
### Animating a Rectangle

{% highlight js %}
document.addEventListener('DOMContentLoaded', main);

var sketch;
var context;
var rectangle = {'x':0, 'y':100};
var dx = 1;
var fps = 10;

function main() {
	sketch = document.getElementById('sketch');
	context = sketch.getContext("2d");
	setInterval(animate, fps);
}

function animate() {
	context.clearRect(0, 0, sketch.offsetWidth, sketch.offsetHeight);
	context.fillRect(rectangle.x, rectangle.y, 120, 40);
	rectangle.x = rectangle.x + dx;
}
{% endhighlight %}
</section>

<section markdown="block">
### Boundaries

We can use sketch.offsetWidth and sketch.offsetHeight to determine horizontal and vertical boundaries.

If the position of our drawing reaches these boundaries, change its velocity by multiplying by -1... and setting the position appropiately...
</section>



<section markdown="block">
## Let's create a rectangle that bounces back and forth horizontally.
</section>

<section markdown="block">
### Rectangle Bounce

{% highlight js %}
document.addEventListener('DOMContentLoaded', main);

var sketch;
var context;
var rectangle = {'x':0, 'y':100, 'w':120, 'h':40};
var dx = 3;
var fps = 10;

function main() {
	sketch = document.getElementById('sketch');
	context = sketch.getContext("2d");
	setInterval(animate, fps);
}

function animate() {
	context.clearRect(0, 0, sketch.offsetWidth, sketch.offsetHeight);
	context.fillRect(rectangle.x, rectangle.y, 120, 40);

	rectangle.x = rectangle.x + dx;
	if (rectangle.x > sketch.offsetWidth - rectangle.w - dx) {
		dx = dx * -1;
		rectangle.x = offsetWidth;
	} else if (rectangle.x < 0 + dx) {
		dx = dx * -1;
		rectangle.x = 0;
	}
}
{% endhighlight %}
</section>
