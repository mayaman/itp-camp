---
layout: lab
title: Lab 14, Part 4 - Markdown
prefix: ../../
---

# Lab 14, Part 4 - Markdown

## Overview

* use [markdown](http://daringfireball.net/projects/markdown/basics) on your [github pages](http://pages.github.com/)
* __we won't be forking and cloning another lab__; we'll be using the same repository as we did in part 1

## Instructions

### Prep Work

* in terminal 
* use pwd to make sure you're in your __~/Desktop/username/lab-14-remote__ folder
* (we're using the same repository as we did in part 1)
* if you're not in that folder, cd into it

### Creating a Page Without HTML!

#### Create a Page That Will be Interpreted as Markdown by Github

* in the same folder that index.html page is in... (your lab-14-remote folder)
* using sublime text, create a new file called __about.markdown__
* in the beginning of the file write the following code:
{% highlight html %}
---
title: About
---
{% endhighlight %}
* this has to be at the very top of the page (including the 3 dashes)
* this will cause the html page to be generated with the title "About"

#### Write Some Headings and Lists in Markdown!

* create a heading called "About"
{% highlight html %}
# A Large Header
{% endhighlight %}
* create a smaller heading called "Topics"
{% highlight html %}
## Slightly Smaller Header
{% endhighlight %}
* under this heading create a bulleted list with the following elements
	* GitHub pages
	* CSS Frameworks
	* More Noise from the Ceiling
{% highlight html %}
* one list item
* another list item
{% endhighlight %}
* under GitHub pages, include a sub list with the following elements:
	* HTML
	* Markdown
{% highlight html %}
* one list item
* another list item
	* a sub list
	* that's a tab, btw!
{% endhighlight %}
* create another smaller heading called "Labs"
{% highlight html %}
## Slightly Smaller Header
{% endhighlight %}
* create an ordered list under that, with the following elements
	* github page
	* markdown
	* bootstrap
{% highlight html %}
# first item
# next item
{% endhighlight %}
* use git __status__, __add__, and __commit__ to save your work
* ...then __push__ to __origin__ __gh-pages__
* -------- when you do git push, __git push origin gh-pages__ -------- 
* check your __about__ page: 
	* open http://yourusername.github.io/lab-14-remote/__about.html__ in your browser (replace yourusername with your actual username)
	* or follow the link to about from your homepage
* view source  to see the HTML that was generated!
	* you know how to do this in Chrome!
	* in Firefox: View &rarr; Page Source
	* in Safari
		* Safari &rarr; Preferences, Advanced Tab - Check Show Develop Menu  
		* Develop &rarr; Show Page Source	

#### Add Bold, Italicized, a Link and an Image

* Make GitHub a link to http://github.com
{% highlight html %}
[link text](link url)
{% endhighlight %}
* Make Noise italicized
{% highlight html %}
_italicized_
{% endhighlight %}
* Make HTML and CSS Bold
{% highlight html %}
__bold!__
{% endhighlight %}
* Find an image of a robot and use markdown to _hotlink_ to it
{% highlight html %}
![alt text](/path/to/image.jpg)
{% endhighlight %}
* use git __status__, __add__, and __commit__ to save your work
* ...then __push__ to __origin__ __gh-pages__
* -------- when you do git push, __git push origin gh-pages__ -------- 
* check your __about__ page: 
	* open http://yourusername.github.io/lab-14-remote/__about.html__ in your browser (replace yourusername with your actual username)
	* or follow the link to about from your homepage
* view source  to see the HTML that was generated!
	* you know how to do this in Chrome!
	* in Firefox: View &rarr; Page Source
	* in Safari
		* Safari &rarr; Preferences, Advanced Tab - Check Show Develop Menu  
		* Develop &rarr; Show Page Source	
