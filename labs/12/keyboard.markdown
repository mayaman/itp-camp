---
layout: slides
title: MTEC1002 - Keyboard
---

<section markdown="block" class="title-slide">

# Keyboard

{% include title-slide-footer.html %}
</section>

<section markdown="block">
### General Overview

1. use boolean variables to determine if position should change
2. use keyboard events to set these variables
</section>

<section markdown="block">
### Keyboard and Circle Example Part 1

Variables and document loaded.

{% highlight js %}
document.addEventListener('DOMContentLoaded', main);
var sketch;
var context;
var circle;
var fps = 10;
var go_up = false;
var go_down = false;

{% endhighlight %}
</section>

<section markdown="block">
### Part 2 - main

{% highlight js %}
function main() {
	sketch = document.getElementById('sketch');
	context = sketch.getContext("2d");

	// start circle at left edge, centered vertically
	circle = {'x':sketch.offsetWidth / 2, 'y':sketch.offsetHeight / 2, 'r':25};
	animation = setInterval(animate, fps);

	// keyboard events
	document.addEventListener('keydown', function(event) {
		if(event.keyCode === 38) {
			go_up = true;
		}

		if(event.keyCode === 40) {
			go_down = true;
		}
	});
	document.addEventListener('keyup', function(event) {
		if(event.keyCode === 38) {
			go_up = false;
		}

		if(event.keyCode === 40) {
			go_down = false;
		}
	});
}
{% endhighlight %}
</section>

<section markdown="block">
### Part 3 - animate

{% highlight js %}
function animate() {
	
	// clear the screen
	context.clearRect(0, 0, sketch.offsetWidth, sketch.offsetHeight);

	if(go_up) {
		circle.y = circle.y - 5;
	}

	if(go_down) {
		circle.y = circle.y + 5;
	}

	// draw circle at current position of circle object
	draw_circle(circle.x, circle.y, circle.r);
}
// draw circle function below
{% endhighlight %}
</section>
