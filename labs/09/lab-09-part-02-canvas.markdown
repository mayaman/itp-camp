---
layout: lab
title: Canvas
prefix: ../../
---
# Lab 9 - Part 2 - Canvas

In this lab, you'll be creating the following programs:

1. square
2. squarecircle
3. customcircle
4. five
5. \* car
6. \* alternating



## Instructions

Note that __ALL OF THESE FILES MUST BE SAVED IN THE LOCAL REPOSITORY THAT YOU CREATED FOR THIS LAB__.

### square

Write a program that draws a square.

* using SublimeText, create a new file called __square.html__ in your repository directory: __~/Desktop/jversoza/lab-09-canvas/__
* setup an html file
* create a canvas element of at least 300 by 300
* add an onload attribute to the body tag to call a function called draw
* add script tags
* create a draw function within your script tags
* start writing your program in your draw function
* draw a black square
* the square should be at least 100 pixels wide and 100 pixels high
* use git status, add, commit, and push to save your file in version control and submit it
* example image below

![square](../../resources/img/lab-09-square.png)

<hr>

### squarecircle

Write a program that draws a square and a circle next to each other.

* using SublimeText, create a new file called __squarecircle.html__ in your repository directory: __~/Desktop/jversoza/lab-09-canvas/__
* setup an html file
* create a canvas element of at least 300 by 300
* add an onload attribute to the body tag to call a function called draw
* add script tags
* create a draw function within your script tags
* start writing your program in your draw function
* draw a black square of any dimensions
* draw a black circle next to the square
* use git status, add, commit, and push to save your file in version control and submit it
* example image below

![squarecircle](../../resources/img/lab-09-squarecircle.png)

<hr>


### customcircle

Write a program that asks for a number and a color - red, green, or blue. It will draw a circle with that radius and color.

* using SublimeText, create a new file called __customcircle.html__ in your repository directory: __~/Desktop/jversoza/lab-09-canvas/__
* setup an html file
* create a canvas element of at least 300 by 300
* add an onload attribute to the body tag to call a function called draw
* add script tags
* create a draw function within your script tags
* start writing your program in your draw function
* the program should ask for a radius: "Enter a radius"
* the program should ask for a color: "Enter a color"
* use the parseInt function to convert input from a string to a number
* use a conditional (if, if-else, or if-else-if) to create a string of the hex color that represents the color entered by the user - red ("#ff0000"), green, or blue
* draw the circle in at the center of your canvas
* (if your canvase is 300 x 300, then the circle should be at 150 x 150)
* the program should use the input to draw a circle with that radius
* use git status, add, commit, and push to save your file in version control and submit it
* example images below

![customcircle1](../../resources/img/lab-09-customcircle-1.png)

![customcircle2](../../resources/img/lab-09-customcircle-2.png)

![customcircle3](../../resources/img/lab-09-customcircle-3.png)

<hr>

### five

Draw five squares using a for loop

* using SublimeText, create a new file called __five.html__ in your repository directory: __~/Desktop/jversoza/lab-09-canvas/__
* setup an html file
* create a canvas element of at least 300 by 300
* add an onload attribute to the body tag to call a function called draw
* add script tags
* create a draw function within your script tags
* start writing your program in your draw function
* draw five black squares, all adjacent to eachother using a for loop!
* use git status, add, commit, and push to save your file in version control and submit it
* example image below

![five](../../resources/img/lab-09-five.png)


<hr>

### \*car

Draw a car...

* using SublimeText, create a new file called __car.html__ in your repository directory: __~/Desktop/jversoza/lab-09-canvas/__
* setup an html file
* create a canvas element of at least 300 by 300
* add an onload attribute to the body tag to call a function called draw
* add script tags
* create a draw function within your script tags
* start writing your program in your draw function
* draw a car!
* use two rectangles and two circles
* make the color of the rectangles different from the color of the circles
* use git status, add, commit, and push to save your file in version control and submit it
* example image below

![car](../../resources/img/lab-09-car.png)

<hr>

### \*alternating

Draw a row of circles and squares.

* using SublimeText, create a new file called __alternating.html__ in your repository directory: __~/Desktop/jversoza/lab-09-canvas/__
* setup an html file
* create a canvas element of at least 300 by 300
* add an onload attribute to the body tag to call a function called draw
* add script tags
* create a draw function within your script tags
* start writing your program in your draw function
* draw a 10 shapes - 5 circles and 5 squares
* they should be alternating horizontally
* the squares and the circles should be colored differently
* hint: use a conditional for this
* hint: use modulo to switch between circles and squares (% 2 will give back 0 or 1)
* (optional) \*ask for a number, draw that many shapes
* use git status, add, commit, and push to save your file in version control and submit it
* example image below

![alternating](../../resources/img/lab-09-alternating.png)
