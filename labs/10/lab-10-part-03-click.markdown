---
layout: lab
title: Click
prefix: ../../
---
# Lab 10 - Part 3 - Click

1. rectangles
2. \*faces

## Instructions

Note that __ALL OF THESE FILES MUST BE SAVED IN THE LOCAL REPOSITORY THAT YOU CREATED FOR THIS LAB__.

### rectangles

Write a program that draws a rectangle wherever you click.

* using SublimeText, create a new file called __rectangles-click.html__ in your repository directory: __~/Desktop/jversoza/lab-10-events/__
* setup an html file
* create a canvas element of at least 800 by 600
* add script tags
* add a listener to your document to handle onload events... set it to run your main function: document.addEventListener('DOMContentLoaded', main);
* create a main function within your script tags
* start writing your program in your main function
* get your sketch element: var sketch = document.getElementById('sketch');	
* create your context: var context = sketch.getContext("2d"); 
* create a listener for click events
* in the anonymous function, use event.x and event.y to draw a rectangle
* use git status, add, commit, and push to save your file in version control and submit it
* example image below

![rectangles](../../resources/img/lab-10-rectangle-click.png)

* send it to github by using git push
* modify your program so that the squares are horizontal instead of vertical!
* example image below

### \*faces

Write a program that draws a face wherever you click.

* using SublimeText, create a new file called __faces-click.html__ in your repository directory: __~/Desktop/jversoza/lab-10-events/__
* setup an html file
* create a canvas element of at least 800 by 600
* use your previous face function to draw faces whenever the canvas is clicked
* use git status, add, commit, and push to save your file in version control and submit it
* example image below

![faces](../../resources/img/lab-10-face-click.png)

