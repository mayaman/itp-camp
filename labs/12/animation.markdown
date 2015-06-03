---
layout: slides
title: MTEC1002 - Animation
---

<section markdown="block" class="title-slide">

# Animation Template

{% include title-slide-footer.html %}
</section>



<section markdown="block">
### General Overview

1. use setInterval to continually call animate
2. create an animate function to draw!
</section>

<section markdown="block">
### Animation Part 1

Variables.

{% highlight js %}
document.addEventListener('DOMContentLoaded', main);

var sketch;
var context;
var circle;
var dx = 2;
var fps = 10;

{% endhighlight %}
</section>

<section markdown="block">
### Animation Part 2

__main__ and __animate__ function.

{% highlight js %}
function main() {
	sketch = document.getElementById('sketch');
	context = sketch.getContext("2d");

	// store x and y values here... as well as radius or width and height
	my_object = {'x':25, 'y':100};
	animation = setInterval(animate, fps);
}

function animate() {
	// clear the screen
	context.clearRect(0, 0, sketch.offsetWidth, sketch.offsetHeight);

	// draw something ... draw_circle or context.fillRect

	// move the position by changing the x or y value based on velocity (dx or dy)
	my_object.y += dy
}

{% endhighlight %}
</section>

<section markdown="block">
### Draw Circle Function

__draw_circle__ function.

{% highlight js %}
function draw_circle(x, y, r) {
	context.beginPath();
	context.arc(x, y, r, 0, 2 * Math.PI, true);
	context.closePath();
	context.fill();
}
{% endhighlight %}
</section>
