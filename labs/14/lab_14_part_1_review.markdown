---
layout: lab
title: Lab 14, Part 1 - HTML and CSS Review
prefix: ../../
---
# Lab 14, Part 1 - HTML and CSS Review

## Overview

* review HTML and CSS

## Instructions for Repository Set Up

### Set up Your Local Repository

This will create a local git repository to store your work for this lab.  The repository will be in ~/Desktop/yourname/lab-14-remote.

* open terminal
* (if doesn't already exist) create a folder that consists of your first initial and last name on your Desktop
{% highlight bash %}
cd ~/Desktop
mkdir your_first_initial_last_name
{% endhighlight %}
* within that folder, create another folder called __lab-14-remote__ and __change into it__
{% highlight bash %}
cd your_first_initial_last_name
mkdir lab-14-remote
cd lab-14-remote
{% endhighlight %}
* use pwd to verify that you're in the correct folder
	* you should be in __~/Desktop/your_first_initial_last_name/lab-14-remote__
	* if you're not, cd into it
* to prove that this is not yet a repository, list __all__ files in your current directory 
{% highlight bash %}
ls -al
{% endhighlight %}
* it should mostly be empty
{% highlight bash %}
total 0
drwxr-xr-x  2 joe  staff   68 Mar 26 19:21 .
drwxr-xr-x  3 joe  staff  102 Mar 26 19:21 ..
{% endhighlight %}
* in your lab-14-remote folder, create your repository!
{% highlight bash %}
git init
{% endhighlight %}
* it should say:
{% highlight bash %}
Initialized empty Git repository in /Users/joe/Desktop/jversoza/lab-14-remote/.git/
{% endhighlight %}
* show that this worked by listing __all__ files in your current directory
{% highlight bash %}
ls -al
{% endhighlight %}
* check that this shows __.git__ 
* use ls .git to show the contents of your repository (it should contain a configuration file, for example)
{% highlight bash %}
ls .git
{% endhighlight %}
* configure your name and email for your commits (these do not have to be the same as your github account)
{% highlight bash %}
# in the directory of your repository
git config user.name  "my first and last name"
git config user.email "my@email.address"
{% endhighlight %}
* finally, use git config again to see if this worked:
{% highlight bash %}
git config -l
{% endhighlight %}
* (use should see your name and email appear in the configuration)

### Create Your Remote Repository

This will create a remote git repository on github.  It will also link your local repository with this remote repository.  In order to submit your work, you will send your files / changes from your local repository to the remote repository on github.

* using the commandline, create a remote repository on github by using curl
* substitute your github username where it says "your github user name" (keep the single quotes and __KEEP "name":__ at the end of the line; don't change that!).  the name of the repository is lab-14-remote (you can see that specified at the end of the command)
* __KEEP '{"name":"lab-14-remote"}' as is__, but __change 'your github user name' appropriately__
{% highlight bash %}
# keep {"name" ...
# but change 'your github user name'
curl -u 'your github user name' https://api.github.com/user/repos -d '{"name":"lab-14-remote"}'
{% endhighlight %}
* it should output a bunch of text!
{% highlight bash %}
Enter host password for user 'jversoza':
{
  "id": 17210769,
  "name": "lab-14-remote",
  "full_name": "jversoza/lab-14-remote",
  "owner": {
    "login": "jversoza",
	...
}
{% endhighlight %}
<!--_-->
* log in to github; you should see the list of repositories on the right	
![Repository List](../../resources/img/repos-screen.png)
* you should have this new repository
* go back to terminal
* make sure you're in your local repository folder for __lab-14-remote__
	* use __pwd__ to do this
	* you should be in __~/Desktop/yourname/lab-14-remote__
	* if you're not in your lab folder, change your directory to it
* run this command to show that you have not linked your local repository to any remote repository yet
{% highlight bash %}
git remote -v
{% endhighlight %}
* it should _do nothing_
* now, link your local repository to your remote repository on github by using git remote add 
* make sure to substitute the two spots where it says "your_github_user_name" with your github username
<!--_-->
{% highlight bash %}
# change your_github_user_name in two places!
git remote add origin https://your_github_user_name@github.com/your_github_user_name/lab-14-remote.git 
{% endhighlight %}
* (alternatively, if you click on your repo you can see your remote repository's url on the lower right hand side of the page...)
![Repository List](../../resources/img/repos-url.png)
* to check that you've linked properly, run the following command again:
{% highlight bash %}
git remote -v
{% endhighlight %}
* it should show origin ... and your repository url:
{% highlight bash %}
origin	https://jversoza@github.com/jversoza/lab-14-remote.git (fetch)
origin	https://jversoza@github.com/jversoza/lab-14-remote.git (push)
{% endhighlight %}




## Create a Two Page Site!

### Home Page

* with SublimeText create a page called __home.html__ in your lab-14-remote folder
* start with the [basic structure](http://www.htmldog.com/guides/html/beginner/tags/) needed for an html5 document
* put in a [title](http://www.htmldog.com/guides/html/beginner/titles/) called: Lab 14 Home
* create a [heading](http://www.htmldog.com/guides/html/beginner/headings/), h1, with text: Lab 14, Part 2 - Review
* create a smaller [heading](http://www.htmldog.com/guides/html/beginner/headings/), h2, with text: Home
* create a [list](http://www.htmldog.com/guides/html/beginner/lists/) under the heading
* in that list put two list items that are [links](http://www.htmldog.com/guides/html/beginner/links/):
	* home links to home.html
		* add a class to this list item called 'active'
	* about links to about.html
* create a [paragraph](http://www.htmldog.com/guides/html/beginner/paragraphs/) under that list
* in your paragraph tag, write in: Welcome to lab 14!!!!  That's a lot of exclamation points!!!!!  Have some more!!!!
* add an [image](http://www.htmldog.com/guides/html/beginner/images/) at the end of your page
	* &lt;img&gt; (no closing tag)
	* add a src attribute, set it equal to an image of a pizza
* use git to check the __status__, __add__ to staging, and __commit__ (don't forget the __-m 'message'__ part)... you can wait to use git push at the end of the lab


### About Page

* with SublimeText create a page called __about.html__ in your lab-14-remote folder
* start with the [basic structure](http://www.htmldog.com/guides/html/beginner/tags/) needed for an html5 document
* put in a [title](http://www.htmldog.com/guides/html/beginner/titles/) called: Lab 14 About
* create a [heading](http://www.htmldog.com/guides/html/beginner/headings/), h1, with text: Lab 14, Part 2 - Review
* create a smaller [heading](http://www.htmldog.com/guides/html/beginner/headings/), h2, with text: About
* create a [paragraph](http://www.htmldog.com/guides/html/beginner/paragraphs/) under that list
* in your paragraph tag, write in: This is for MTEC1002
* use git to check the __status__, __add__ to staging, and __commit__ (don't forget the __-m 'message'__ part)... you can wait to use git push at the end of the lab

### Style Your Pages

* with SublimeText create a stylesheet called __mystyles.css__ in your lab-14-remote folder
* edit __about.html__ so that [it uses your stylesheet](http://www.htmldog.com/guides/css/beginner/applyingcss/)
* edit __home.html__ so that [it uses your stylesheet](http://www.htmldog.com/guides/css/beginner/applyingcss/)
* in your stylesheet, make sure that the entire page uses sans-serif fonts
* make your largest headers red
* put a black border around every element with a class of active
* put in [this](http://images.wikia.com/adventuretimewithfinnandjake/images/3/3a/S1e1_flip_out.png) as a repeating background image!
* make the margins around your paragraphs 20px
* use git to check the __status__, __add__ to staging, and __commit__ (don't forget the __-m 'message'__ part)
* git push origin master!

