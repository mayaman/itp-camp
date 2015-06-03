---
layout: lab
title: Animation
prefix: ../../
---
# Lab 12 - Part 2 - Keyboard

1. rectangle-key
2. rectangle-key-2
3. \*rectangle-key-2-boundary


## Instructions

Note that __ALL OF THESE FILES MUST BE SAVED IN THE LOCAL REPOSITORY THAT YOU CREATED FOR THIS LAB__.

### rectangle-key

Write a program that allows a user to move a rectangle up and down on the canvas using the up and down arrow keys.

* using SublimeText, create a new file called __rectangle-key.html__ in your repository directory: __~/Desktop/jversoza/lab-12-game/__
* setup an html file
* add a style tag in insides the head tag - add the following code to give your canvas element a border:

{% highlight html %}
<style>
#sketch {
	border:1px solid #000;
}
</style>
{% endhighlight %}

* create a canvas element that is 480 by 720
* add script tags
* add a listener to your document to handle onload events... set it to run your main function: document.addEventListener('DOMContentLoaded', main);
* declare the following variables: 
	* sketch - your canvas element
	* context - your drawing instrument
	* rectangle - an object that contains your rectangles x, y position as well as width and height (w and h) 
	* two boolean values - go_up and go_down... both set equal to false
	* fps (set this equal to 10) - the delay in ms before your animate function is called
	* start writing your program in your main function
	* get your sketch element: sketch = document.getElementById('sketch');	
	* create your context: context = sketch.getContext("2d"); 
	* create your rectangle object: rectangle = {'x':200, 'y':200, 'w':80, 'h':20};
	* add an event listener for keydown:  document.addEventListener('keydown', ...
	* the second argument is an anonymous function
	* in the anonymous function check if the keycode is 38 or 40 (up or down), and change the go_up variable accordingly: event.keyCode === 38 ... event.keyCode === 40 
	* your main function is finished!
* use git status, add, commit, and push to save your file in version control and submit it
* send it to github by using git push
* example image below

[rectangle-key](../../resources/mov/12/rectangle-key.mov)

### rectangle-key-2

Modify the previous program so that instead of moving up and down, the rectangle moves side-to-side:

[rectangle-key-2](../../resources/mov/12/rectangle-key-2.mov)

### \*rectangle-key-2-boundary

Finally - modify your program to prevent the rectangle from going off screen:

[rectangle-key-2-boundary](../../resources/mov/12/rectangle-key-2-boundary.mov)
