---
layout: lab
title: Animation
prefix: ../../
---
# Lab 11 - Part 2 - Animation

1. circle-animate
2. circle-bounce
3. circle-y-bounce
4. \*circle-xy
5. \*car-animate


## Instructions

Note that __ALL OF THESE FILES MUST BE SAVED IN THE LOCAL REPOSITORY THAT YOU CREATED FOR THIS LAB__.

### circle-animate

Write a program that draws a black circle that moves across the canvas horizontally

* using SublimeText, create a new file called __circle-animate.html__ in your repository directory: __~/Desktop/jversoza/lab-11-interaction/__
* setup an html file
* create a canvas element of at least 800 by 600
* add script tags
* add a listener to your document to handle onload events... set it to run your main function: document.addEventListener('DOMContentLoaded', main);
* create 5 variables:
	* sketch (don't set it to anything yet)
	* context (don't set it to anything yet)
	* circle ... an object that's equal to {'x':0, 'y':100, 'r':25 }
	* dx ... the velocity, which can be set to any value between 1 and 5
	* fps ... how often the screen redraws; 10 is a good value
* create a main function... and within this funciton:
	* assign values to sketch and context:
		* sketch = document.getElementById('sketch');
		* context = sketch.getContext("2d");
	* use setInterval to constantly call a function called animate (you'll create this later) 
		* pass in animate as the function to be called, and fps and the time interval
		* setInterval(animate, fps);
* create an animate function... and within this function:
	* clear the screen
		* use context.clearRect
		* use the arguments 0, 0 ... and the width and height of your canvas element
		* context.clearRect(0, 0, sketch.offsetWidth, sketch.offsetHeight);
		* use draw_circle to draw a shape, and use the circle object's x, y and radius values
		* draw_circle(circle.x, circle.y, circle.r);
		* increment the circle's x value
		* circle.x = circle.x + dx;
* bring in your draw_circle function from previous exercises
* use git status, add, commit, and push to save your file in version control and submit it
* send it to github by using git push
* example movie: [circle-animate](../../resources/mov/circle-animate.mov)


### circle-bounce

Make your circle bounce back and forth when it reaches the far left or far right side of the screen

* using SublimeText, create a new file called __circle-bounce.html__ in your repository directory: __~/Desktop/jversoza/lab-11-interaction/__
* setup an html file
* create a canvas element of at least 800 by 600
* add script tags
* add a listener to your document to handle onload events... set it to run your main function: document.addEventListener('DOMContentLoaded', main);
* this will be similar to the previous lab, circle-animate...
* create 5 variables:
	* sketch (don't set it to anything yet)
	* context (don't set it to anything yet)
	* circle ... an object that's equal to {'x':0, 'y':100, 'r':25 }
	* dx ... the velocity, which can be set to any value between 1 and 5
	* fps ... how often the screen redraws; 10 is a good value
* create a main function... and within this funciton:
	* assign values to sketch and context:
		* sketch = document.getElementById('sketch');
		* context = sketch.getContext("2d");
	* use setInterval to constantly call a function called animate (you'll create this later) 
		* pass in animate as the function to be called, and fps and the time interval
		* setInterval(animate, fps);
* create an animate function... and within this function:
	* clear the screen
		* use context.clearRect
		* use the arguments 0, 0 ... and the width and height of your canvas element
		* context.clearRect(0, 0, sketch.offsetWidth, sketch.offsetHeight);
		* use draw_circle to draw a shape, and use the circle object's x, y and radius values
		* draw_circle(circle.x, circle.y, circle.r);
		* increment the circle's x value
		* circle.x = circle.x + dx;
		* create a conditional that checks if your circle has reached the far left or far right of the canvase:
			* circle.x > sketch.offsetWidth - dx
			* circle.x < 0 + dx
		* use an if / else if to handle these conditions
		* the body of the condition should change the direction (by multiplying dx by -1)
		* ...as well as set the circle's x value to either 0 or sketch.offsetWidth:
			* circle.x = offsetWidth;
			* circle.x = 0;
* bring in your draw_circle function from previous exercises
* use git status, add, commit, and push to save your file in version control and submit it
* send it to github by using git push
* example movie: [circle-bounce](../../resources/mov/circle-bounce.mov)

<!--_ -->

### circle-y-bounce

Copy your program above, and modify it so that your circle travels vertically, instead of horizontally.  It should bounce in the opposite direction if it hits the top or bottom of the canvas.

* using SublimeText, create a new file called __circle-y-bounce.html__ in your repository directory: __~/Desktop/jversoza/lab-11-interaction/__
* copy your program above... and change it so that: 
	* the circle travels up and down
	* ...and bounces off of the top or bottom of the canvas.
	* use 0 for the top
	* use sketch.offsetHeight for the bottom
* use git status, add, commit, and push to save your file in version control and submit it
* send it to github by using git push
* example movie: [circle-y-bounce](../../resources/mov/circle-y-bounce.mov)

### \*circle-xy

Animate your circle so that it is travelling both horizontally and vertically (along the x and y axis).  Make sure it bounces off of the top, bottom, left and right of the canvas.

* using SublimeText, create a new file called __circle-xy.html__ in your repository directory: __~/Desktop/jversoza/lab-11-interaction/__
* using the programs above as a base
	* add both a dx and dy
	* make the circle move in both directions by adding the dx or dy to the circle object's x and y
	* add another if / else if ... so that top, bottom, left and right are handled appropriately
* send it to github by using git push
* use git status, add, commit, and push to save your file in version control and submit it
* example movie: [circle-xy](../../resources/mov/circle-xy.mov)

### \*car-animate

Animate your car! Make it move from left to right...

* using SublimeText, create a new file called __car-animate.html__ in your repository directory: __~/Desktop/jversoza/lab-11-interaction/__
* mimic the example movie: [car-animate](../../resources/mov/car-animate.mov)
* send it to github by using git push
* use git status, add, commit, and push to save your file in version control and submit it
