---
layout: lab
title: Animation
prefix: ../../
---
# Lab 12 - Part 1 - Animation

1. circle-animate
2. circle-boundary
3. circle-boundary-all
4. \*circle-bounce
5. \*circle-bounce-2
6. \*circle-bounce-3

## Instructions

Note that __ALL OF THESE FILES MUST BE SAVED IN THE LOCAL REPOSITORY THAT YOU CREATED FOR THIS LAB__.

### circle-animate

Write a program that draws a circle that moves horizontally from left to right.

* using SublimeText, create a new file called __circle-animate.html__ in your repository directory: __~/Desktop/jversoza/lab-12-game/__
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
	* circle - an object that contains your circles x, y position and radius
	* dx (set this equal to 2) - the velocity
	* fps (set this equal to 10) - the delay in ms before your animate function is called
	* animation - a variable to keep track of your animation
* create a main function
	* start writing your program in your main function
	* get your sketch element: sketch = document.getElementById('sketch');	
	* create your context: context = sketch.getContext("2d"); 
	* create your circle object: circle = {'x':25, 'y':sketch.offsetHeight / 2, 'r':25};
	* specifiy a function to be called repeatedly at a specific interval: animation = setInterval(animate, fps);
	* note that the animate function will be defined immediately after... outside of the main function
	* your main function is finished!
* create another function, outside of main, called animate (this will be called repeatedly, and it will be responsible for clearing the screen and drawing your shapes)
	* clear the screen: context.clearRect(0, 0, sketch.offsetWidth, sketch.offsetHeight);
	* draw circle at current position of circle object (this function will be defined later): draw_circle(circle.x, circle.y, circle.r);
	* move the circle's position by adding velocity: circle.x = circle.x + dx;
	* that should finish your animate function
* finally, define your circle function; you can copy and paste from previous slides or programs
* use git status, add, commit, and push to save your file in version control and submit it
* send it to github by using git push
* example movie below

[circle-animate](../../resources/mov/12/circle-animate.mov)


### circle-boundary

Write a program that draws a circle that moves horizontally from left to right, but whenever it hits the right or left wall, it changes direction.

* using SublimeText, create a new file called __circle-boundary.html__ in your repository directory: __~/Desktop/jversoza/lab-12-game/__
* copy your code from your previous program
* at the end of your animate function, add a conditional or conditionals to check if your circle is at either end of the canvas:
	* check that the circle's x value is beyond the left side by seeing if it's greater than the canvas sidth minus velocity minus radius: circle.x > sketch.offsetWidth - dx - circle.r 
	* check that the circle's x value is beyond the right side by seeing if it's less than the circle's radius minus the velocity: circle.x < circle.r - dx 
	* if these conditions are set, change direction by changing the sign on velocity: dx = dx * -1
* use git status, add, commit, and push to save your file in version control and submit it
* send it to github by using git push
* example movie below

[circle-boundary](../../resources/mov/12/circle-boundary.mov)

### circle-boundary-all

Write a program that draws a circle that moves horizontally __and__ vertically, but whenever it hits the right, left, top, or bottom wall, it changes direction.

* using SublimeText, create a new file called __circle-boundary-all.html__ in your repository directory: __~/Desktop/jversoza/lab-12-game/__
* copy your code from your previous program
* add a velocity for y ... call it dy and set it to some value... so that the ball moves up and down as well as left and right
* in your animate function... change your circle's y position by adding velocity: circle.y = circle.y + dy;
* check your top and bottom boundaries (you can based this off of your left and right boundaries) 
* if the boundaries are encountered, flip the sign on dy (your vertical velocity)
* use git status, add, commit, and push to save your file in version control and submit it
* send it to github by using git push
* example movie below

[circle-boundary-all](../../resources/mov/12/circle-boundary-all.mov)

### circle-bounce

Write a program that draws a circle that falls vertically by using velocity and acceleration... and bounces after it hits the bottom boundary.  Eventually, the circle will stop bouncing. 

* using SublimeText, create a new file called __circle-bounce.html__ in your repository directory: __~/Desktop/jversoza/lab-12-game/__
* base this program off of previous programs
* you won't need to move horizontally for this (so, you can remove dx)
* however, you'll need acceleration (probably around 0.1 or 0.2), and some sort of number to dampen the velocity after a bounce (probably 0.8 or 0.9)
* in your animate function, along with changing the y position, you'll also modify dy, the velocity, by using acceleration (for example... adding acceleration)
* when your code checks for a bounce, instead of just flipping the sign on velocity, dampen the velocity by multiplying it by a number smaller than one (again, probably 0.8 or 0.9)
* if you want to stop bouncing at a certain threshhold, this code may come in handy:

{% highlight js %}
// if your velocity is less than some minimum value
if (Math.abs(dy) < min_dy_val) {
	// zero out acceleration and velocity
	dy = 0
	acc = 0
}
{% endhighlight %}

* use git status, add, commit, and push to save your file in version control and submit it
* send it to github by using git push
* example movie below

[circle-bounce](../../resources/mov/12/circle-bounce.mov)

### circle-bounce-2

* modify your previous program to have a horizontal velocity as well!
* use git status, add, commit, and push to save your file in version control and submit it
* send it to github by using git push
* example movie below

[circle-bounce-2](../../resources/mov/12/circle-bounce-2.mov)
