---
layout: lab
title: Lab 14, Part 5 - Even More Markdown
prefix: ../../
---

# Lab 14, Part 5 - Even More Markdown

## Overview

* use [markdown](http://daringfireball.net/projects/markdown/basics) on your [github pages](http://pages.github.com/)

## Instructions

### Prep Work

* in terminal 
* use pwd to make sure you're in your __~/Desktop/username/lab-14-remote__ folder
* if you're not in that folder, cd into it

### Creating One More Markdown Page

* in the same folder that index.html page is in... (your lab-14-remote folder)
* using sublime text, create a new file called __practice.markdown__
* in the beginning of the file write the following code:

{% highlight html %}
---
title: Practice
---
{% endhighlight %}

* this has to be at the very top of the page (including the 3 dashes)
* this will cause the html page to be generated with the title "Practice"
* create a heading called "This is a Header!"
* under that, create an unordered list with the following elements
	* the word "plain"
		* under plain, create a sub list with three elements: "one", "two" and "three"
	* the word "bold" in bold
	* the word "italicized" in italics
* create a smaller heading called "Another Header"
* under this header create an bulleted list with the following elements
	* a link to the wikipedia article on your 1st favorite movie
	* a link to the wikipedia article on your 2nd favorite movie
* add an image to an animal that starts with the letter 'a' the end of your page 
* use git __status__, __add__, and __commit__ to save your work
* ...then __push__ to __origin__ __gh-pages__
* check your __practice__ page: 
	* open http://yourusername.github.io/lab-14-remote/__practice.html__ in your browser (replace yourusername with your actual username)
	* or follow the link to practice from your homepage
* view source to see the HTML that was generated!
	* you already know how to do this in Chrome!
	* in Firefox: View &rarr; Page Source
	* in Safari
		* Safari &rarr; Preferences, Advanced Tab - Check Show Develop Menu  
		* Develop &rarr; Show Page Source	
