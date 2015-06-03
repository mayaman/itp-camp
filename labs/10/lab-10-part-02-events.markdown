---
layout: lab
title: Events and Drawing Revisited
prefix: ../../
---
# Lab 10 - Part 2 - Events and Drawing Revisited

1. squares (vertical and horizontal)
2. \* size
3. grid 
4. \* diagonal 
5. face
6. \* multiface



## Instructions

Note that __ALL OF THESE FILES MUST BE SAVED IN THE LOCAL REPOSITORY THAT YOU CREATED FOR THIS LAB__.

### squares

Write a program that draws multiple squares using a for loop.

* using SublimeText, create a new file called __vertical.html__ in your repository directory: __~/Desktop/jversoza/lab-10-events/__
* setup an html file
* create a canvas element of at least 800 by 600
* add script tags
* add a listener to your document to handle onload events... set it to run your main function: document.addEventListener('DOMContentLoaded', main);
* create a main function within your script tags
* start writing your program in your main function
* get your sketch element: var sketch = document.getElementById('sketch');	
* create your context: var context = sketch.getContext("2d"); 
* create three variables, x and y (both equal to 0) and size (equal to 20)
* use a for loop to loop from 0 through (up-to and including) 4
* use your for loop variable to modify the variables you created, x, y and size
	*  size should be constant (20)
	*  y should be equal to loop variable, i * something larger than size (30)
	*  x should always be equal to 100
	* in the for loop, draw a rectangle using the variables you created: context.fillRect(x, y, size, size);
* example image below

![vertical](../../resources/img/lab-10-squares-1-vertical.png)

* use git status, add, commit, and push to save your file in version control and submit it
* send it to github by using git push
* modify your program so that the squares are horizontal instead of vertical!
* example image below


![horizontal](../../resources/img/lab-10-squares-2-horizontal.png)

<hr>

### \* size

Draw a series of squares that increase in size and change in color.

* using SublimeText, create a new file called __size.html__ in your repository directory: __~/Desktop/jversoza/lab-10-events/__
* setup an html file
* create a canvas element of at least 800 by 600
* add script tags
* add a listener to your document to handle onload events... set it to run your main function: document.addEventListener('DOMContentLoaded', main);
* create a main function within your script tags
* start writing your program in your main function
* get your sketch element: var sketch = document.getElementById('sketch');	
* create your context: var context = sketch.getContext("2d"); 
* again, use a for loop to create 5 squares, each an increasing size, and optionally, a lighter shade of green
* hint: you'll have to vary the size based on the loop variable (perhaps multiply the loop variable by 20)
* hint: you can use the loop variable to create a two digit number... that you can insert into the hex string
* hint: you can set x equal to whatever value x was previously, and add the size of the square plus some constant offset
* use git status, add, commit, and push to save your file in version control and submit it
* example image below

![size](../../resources/img/lab-10-squares-3-gradient.png)


<hr>

### grid

Draw a grid of squares.

* using SublimeText, create a new file called __grid.html__ in your repository directory: __~/Desktop/jversoza/lab-10-events/__
* setup an html file
* create a canvas element of at least 800 by 600
* add script tags
* add a listener to your document to handle onload events... set it to run your main function: document.addEventListener('DOMContentLoaded', main);
* create a main function within your script tags
* start writing your program in your main function
* get your sketch element: var sketch = document.getElementById('sketch');	
* create your context: var context = sketch.getContext("2d"); 
* create two variables, x and y - both set to 0
* use two for loops!
	* the outside for loop should have a loop variable called i
	* the inside for loop should have a loop variable called j
	* within the innermost for loop change x based on the loop variable i (maybe something like x = i * ...)
	* within the innermost for loop change y based on the loop variable j 
	* set your fill color to blue...
	* call context.fillRect with your new x and y values to create blue squares
* use git status, add, commit, and push to save your file in version control and submit it
* example image below

![grid](../../resources/img/lab-10-grid-1.png)

<hr>

### diagonal

Create a diagonal line in your grid of squares.

* modify the above program (grid.html) so that a diagonal line of squares from the upper left corner down to the lower right corner is yellow
* hint: use a conditional to do this ... base this conditional on the values of your loop variables (i and j)

![diagonal](../../resources/img/lab-10-grid-2-diagonal.png)


<hr>

### face

Draw a face!

* using SublimeText, create a new file called __face.html__ in your repository directory: __~/Desktop/jversoza/lab-10-events/__
* setup an html file
* create a canvas element of at least 800 by 600
* add script tags
* add a listener to your document to handle onload events... set it to run your main function: document.addEventListener('DOMContentLoaded', main);
* create a main function within your script tags
* start writing your program in your main function
* get your sketch element: var sketch = document.getElementById('sketch');	
* create your context: var context = sketch.getContext("2d"); 
* create a function that draws a circle - it should take a context, x, y, and r value...
* use that function to the draw circles that compose the face
* use git status, add, commit, and push to save your file in version control and submit it
* example image below

![face](../../resources/img/lab-10-face-1.png)

<hr>

### multiface

* modify your program above so that face can be drawn using a function call
* draw three faces
* hint: pass context in as a parameter... along with x and y coordinates
* use that function to draw a face
* use git status, add, commit, and push to save your file in version control and submit it
* example image below

![multiface](../../resources/img/lab-10-face-2-function.png)

