---
layout: lab
title: Lab 13, Part 2 - CSS
prefix: ../../
---
# Lab 13, Part 1 - CSS 

## Overview

* style a page using CSS

## Instructions

### Prep Work

* __WE'LL USE THE SAME HTML FILE THAT WE USED IN THE PREVIOUS LAB AS OUR STARTING POINT!__
* in terminal change to your __~/Desktop/username/lab-13-html__ folder
* use __pwd__ to make sure you're in the right directory!

### Style Your Page With CSS

#### Include an External CSS File

* open up SublimeText (try Command+SPACEBAR to search for SublimeText)
* if you don't have __index.html__ already open, go to the top menu bar, click on File&rarr;Open
* browse to home&rarr;Desktop&rarr;usernamefolder&rarr;lab-13-html&rarr;index.html
* create a new file by going to File&rarr;New 
* immediately save your new file by going to File&rarr;Save As
	* browse to home&rarr;Desktop&rarr;usernamefolder&rarr;lab-13-html
	* name your file __style.css__
* add this to __style.css__
{% highlight css %}
p {
    color: red;
}
{% endhighlight %}

* add your external css file to your page
	* in your &lt;head&gt; tag
	* add...  &lt;link rel="stylesheet" href="style.css"&gt;
* view your page by opening it in your browser (double click on the file from finder or Option-click&rarr;Open With)
* you should see your paragraph tags in red

#### Changing Color and Text

(view your page after each modification)

* using the color property:
	* change your largest header (h1) to green using hex values
	* change your paragraphs so that they're blue using hex values
* change the background color on all headers (h1 and h2) so that they're gray (maybe something like #888888)
* use font-family on body to change all of your text to sans-serif
* use font-size on body to make all your text twice the normal size
* use text-decoration on all paragraphs ... try strike-through
* use text-decoration on your second largest header (h2) ... try underline
* use text-transform on your largest header (h1) to change to uppercase
* view your page 
* use git to check the __status__, __add__ to staging, and __commit__ (don't forget the __-m 'message'__ part)

#### Margins, Padding and Border

* add 20px margin to your largest header (h1)
* add 40px padding to your largest header (h1)
* add a 5 pixel wide, dashed, red border around your largest header (h1)
* use git to check the __status__, __add__ to staging, and __commit__ (don't forget the __-m 'message'__ part)

#### Using Chrome Inspector or Firebug

#### Classes, IDs, Grouped Selectors

In __index.html__...

* add an id to your first paragraph called intro
* add an class to your first header (h1) called spotlight

In __style.css__...

* add a selector for #intro
	* set the border to one pixel, solid, black
* add a selector for .spotlight
	* set the background-color to yellow (try #FEFE22)
* remove any color properties from your h2 and paragraph selectors
* group h2 and p so that their color is dark green
* use git to check the __status__, __add__ to staging, and __commit__ (don't forget the __-m 'message'__ part)

#### Nesting, Pseudo Classes, Background

* create a selector that through all of the link text within a paragraph (p a)
* create a selector that changes link text to uppercase when hovered over (a:hover)
* add a repeating image to the background
{% highlight css %}
body {
    background: white url(http://foureyes.github.io/mtec1002-spring2014/resources/img/lab-13-face.png) repeat top right;
}
{% endhighlight %}

* use git to check the __status__, __add__ to staging, and __commit__ (don't forget the __-m 'message'__ part)
