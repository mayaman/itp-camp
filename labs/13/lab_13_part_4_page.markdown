---
layout: lab
title: Lab 13, Part 4 - HTML
prefix: ../../
---
# Lab 13, Part 4 - HTML 

## Overview

* create a basic html page

## Instructions

### Create an Your Own Page!

#### Create Your Files

* use SublimeText to create two new files
* use save as to save both files under your lab-13-html folder that's in your ~/Desktop/username folder
	* use (Save As...)
	* one should be called mypage.html
	* one should be called mystyles.css
* view your page 
* use git to check the __status__, __add__ to staging, and __commit__ (don't forget the __-m 'message'__ part)

#### Lists and Headings

In mypage.html...

* create a heading (largest - h1), with text: Some Useful Information
* create a heading (second largest - h2), with text: Top 3 Cat Names 
* under the heading, create an ordered list of your top 3 cat names
	* maybe: chairman meow, katy purry, yo yo meow
* add another heading (second largest - h2), with text: Do Not Eat List
* under the heading, create an unordered list of foods that you refuse to eat
	* for each food, link to a relevant wikipedia article
* view your page 
* use git to check the __status__, __add__ to staging, and __commit__ (don't forget the __-m 'message'__ part)

#### A Table

In mypage.html...

* add a table containing 4 rows and 2 columns (use table, tr, td)
	* in the first row, first column type in: animal 
	* in the first row, second column type in: awesome
	* in each remaining row, add an animal and yes or no (for example: narwhale and YES!)
* view your page 
* use git to check the __status__, __add__ to staging, and __commit__ (don't forget the __-m 'message'__ part)

#### Paragraphs

In mypage.html...

* create three paragraphs (use p tags)
	* one should have the text: this is the first paragraph
	* the second should be: paragraph number two!!!
	* and the third should be: last one, really...
* in the third paragraph, make the word "really" a link to google

#### Styling

In mypage.html...

* include mystyles.css

In mystyles.css (and mypage.html for some)...

* make all links turn red when they're hovered over
* make all headers (both h1 and h2) uppercase through css
* give all paragraphs a border that's 2 pixels wide, dashed and black
* in the first paragraph, add an id called top (id="top") as an attribute
	* add 50 pixels of padding for a paragraph with an id of top
* add 25 pixels of margin for each paragraph
* double the size of links that are within an element that has an id of top
* choose one list item from the top 3 cat names and one list item from the do not eat list
	* add a class attribute named highlight to both of those list items (class="highlight")
	* add a style that makes all text that has that class have a yellow background
* use git to check the __status__, __add__ to staging, and __commit__ (don't forget the __-m 'message'__ part)

### Upload Your Files!

* open your SFTP client, CyberDuck
* connect to foureyes.in using your account
* navigate to public_html
* open finder... go to ~/Desktop/username/lab_13_part_4
* drag your files to the your sftp client
* check [http://foureyes.in/~username/mypage.html](http://foureyes.in/~username/mypage.html)
* (replace username with your username, of course!)
