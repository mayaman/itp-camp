---
layout: slides
title: MTEC1002 - JavaScript For Loop
---

<section markdown="block" class="title-slide">

# Click Events

{% include title-slide-footer.html %}
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

function main() {
	var sketch = document.getElementById('sketch');
	var context = sketch.getContext("2d");
	context.fillStyle = "#992255";
	sketch.addEventListener("click", function(event) {
		context.beginPath();
		context.arc(event.x, event.y, 75, 0, 2 * Math.PI, true);
		context.closePath();
		context.fill();
	});
}
</script>
</body>
</html>
{% endhighlight %}
</div>
</section>

