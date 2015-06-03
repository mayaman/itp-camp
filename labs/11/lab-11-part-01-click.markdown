---
layout: lab
title: Click
prefix: ../../
---
# Lab 11 - Part 2 - Click

1. rectangles-click
2. car
3. \*face 

## Instructions

Note that __ALL OF THESE FILES MUST BE SAVED IN THE LOCAL REPOSITORY THAT YOU CREATED FOR THIS LAB__.

### rectangles

Write a program that draws a rectangle wherever you click.

* using SublimeText, create a new file called __rectangles-click.html__ in your repository directory: __~/Desktop/jversoza/lab-11-interaction/__
* setup an html file
* create a canvas element of at least 800 by 600
* add script tags
* add a listener to your document to handle onload events... set it to run your main function: document.addEventListener('DOMContentLoaded', main);
* declare two variables - sketch and context
* create a main function
* start writing your program in your main function
* get your sketch element: sketch = document.getElementById('sketch');	
* create your context: context = sketch.getContext("2d"); 
* create a listener for click events: sketch.addEventListener ...
* create an anonymous function (do this as an argument to addEventListener)
* in the anonymous function, use event.x and event.y to draw a rectangle
* use git status, add, commit, and push to save your file in version control and submit it
* send it to github by using git push
* example image below

![rectangles](../../resources/img/lab-11-rectangle-click.png)


### car

Write a program that draws a car wherever you click.  It will clear the screen on each click so that there is only one car on the canvas.

* using SublimeText, create a new file called __car-click.html__ in your repository directory: __~/Desktop/jversoza/lab-11-interaction/__
* setup an html file
* create a canvas element of at least 800 by 600
* add script tags
* add a listener to your document to handle onload events... set it to run your main function: document.addEventListener('DOMContentLoaded', main);
* declare two variables - sketch and context
* create a main function
* start writing your program in your main function
* get your sketch element: sketch = document.getElementById('sketch');	
* create your context: context = sketch.getContext("2d"); 
* create a listener for click events: sketch.addEventListener ...
* create an anonymous function (do this as an argument to addEventListener)
* in the anonymous function, use event.x and event.y to draw a car
	* clear the canvas (see slides)
	* this will use a function you define later (called draw_car)
* copy in the draw_circle function from the slides
* create a new function called draw_car... that utilizes the draw_circle function
	* it should have two parameters, x and y
	* draw all of your shapes relative to these values... for example: 
		* context.fillRect(x, y, 120, 40);
		* context.fillRect(x + somevalue, y - anothervalue, 80, 30);
		* draw_circle(x + somevalue, y + anothervalue, 20)
			* (fill in somevalue and anothervalue with numbers)
* draw_car will be used in the anonymous function in event handler...
* use git status, add, commit, and push to save your file in version control and submit it
* send it to github by using git push
* example image below
	
![car](../../resources/img/lab-11-car-click.png)

### \*faces

Write a program that draws a face wherever you click.

* using SublimeText, create a new file called __faces-click.html__ in your repository directory: __~/Desktop/jversoza/lab-11-interaction/__
* setup an html file
* create a canvas element of at least 800 by 600
* use the code in the previous labs to set up a click interaction
* bring in your draw_circle function 
* create a function to draw a face... and parameterize it appropriately
* the program should draw a face wherever the mouse is clicked
* use git status, add, commit, and push to save your file in version control and submit it
* example image below

![faces](../../resources/img/lab-11-face-click.png)

