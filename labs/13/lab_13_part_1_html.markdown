---
layout: lab
title: Lab 13, Part 1 - HTML
prefix: ../../
---
# Lab 13, Part 1 - HTML 

In this lab, you'll be:

1. creating two repositories, one local and one remote
2. linking the two with each other so that they can be synchronized
3. associating a name and email address with your local repository
4. creating an html page

## Instructions for Repository Set Up

### Set up Your Local Repository

This will create a local git repository to store your work for this lab.  The repository will be in ~/Desktop/yourname/lab-13-html.

* open terminal
* (if doesn't already exist) create a folder that consists of your first initial and last name on your Desktop
{% highlight bash %}
cd ~/Desktop
mkdir your_first_initial_last_name
{% endhighlight %}
* within that folder, create another folder called __lab-13-html__ and __change into it__
{% highlight bash %}
cd your_first_initial_last_name
mkdir lab-13-html
cd lab-13-html
{% endhighlight %}
* use pwd to verify that you're in the correct folder
	* you should be in __~/Desktop/your_first_initial_last_name/lab-13-html__
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
* in your lab-13-html folder, create your repository!
{% highlight bash %}
git init
{% endhighlight %}
* it should say:
{% highlight bash %}
Initialized empty Git repository in /Users/joe/Desktop/jversoza/lab-13-html/.git/
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
* substitute your github username where it says "your github user name" (keep the single quotes and __KEEP "name":__ at the end of the line; don't change that!).  the name of the repository is lab-13-html (you can see that specified at the end of the command)
* __KEEP '{"name":"lab-13-html"}' as is__, but __change 'your github user name' appropriately__
{% highlight bash %}
# keep {"name" ...
# but change 'your github user name'
curl -u 'your github user name' https://api.github.com/user/repos -d '{"name":"lab-13-html"}'
{% endhighlight %}
* it should output a bunch of text!
{% highlight bash %}
Enter host password for user 'jversoza':
{
  "id": 17210769,
  "name": "lab-13-html",
  "full_name": "jversoza/lab-13-html",
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
* make sure you're in your local repository folder for __lab-13-html__
	* use __pwd__ to do this
	* you should be in __~/Desktop/yourname/lab-13-html__
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
git remote add origin https://your_github_user_name@github.com/your_github_user_name/lab-13-html.git 
{% endhighlight %}
* (alternatively, if you click on your repo you can see your remote repository's url on the lower right hand side of the page...)
![Repository List](../../resources/img/repos-url.png)
* to check that you've linked properly, run the following command again:
{% highlight bash %}
git remote -v
{% endhighlight %}
* it should show origin ... and your repository url:
{% highlight bash %}
origin	https://jversoza@github.com/jversoza/lab-13-html.git (fetch)
origin	https://jversoza@github.com/jversoza/lab-13-html.git (push)
{% endhighlight %}


### Create an HTML Page!

#### Basic Structure

* open up SublimeText (try Command+SPACEBAR to search for SublimeText)
* create a new file
* safe it...  browse to home&rarr;Desktop&rarr;usernamefolder&rarr;lab-13-game&rarr; and save as __index.html__
* create a skeleton page by using the following tags (don't use tab completion!)
	* &lt;!DOCTYPE html&gt; (note that this has no closing tag)
	* &lt;html lang="en"&gt;
	* &lt;head&gt;
	* &lt;body&gt;
* view your page by opening it in your browser (double click on the file from finder or option-click&rarr;Open With... your browser)
* add text between the body tags
* view your page (now just hit the refresh/reload button on your browser)
* add a title; it should go in head
* use git to check the __status__, __add__ to staging, and __commit__ (don't forget the __-m 'message'__ part)... and of course, __push origin master__

#### Paragraphs and Headings

* add another line of text
* view your page (note that there are no line breaks!)
* add paragraph tags around each line of text
* view your page (note that the text is now on separate lines!)
* add some emphasis and strong tags around some text in one of the paragraphs
	* &lt;em&gt; 
	* &lt;strong&gt; 
* view your page (look for italicized and bolded text!)
* add a header tag before each paragraph
	* add an &lt;h1&gt; first
	* add an &lt;h2&gt; next
* add one more header tag, an h1 again... and add another paragraph tag underneath it
* view your page (look for both headers)
* use git to check the __status__, __add__ to staging, and __commit__ (don't forget the __-m 'message'__ part)

#### Lists and Links

* add an ordered list after your headers and paragraphs
	* &lt;ol&gt;
	* &lt;li&gt;
* view your page (look for both headers)
* add an un-ordered list after your previous list
	* &lt;ul&gt;
	* &lt;li&gt;
* change one of your list items so that some of the text within it is a link
	* &lt;a&gt;
* do the same for some text within one of the paragraphs (perhaps link to largest island in a lake)
* add another link in one of your paragraphs (perhaps link to garfield without garfield)
* view your page and check that your links work
* use git to check the __status__, __add__ to staging, and __commit__ (don't forget the __-m 'message'__ part)

#### Images and Tables

* add an image somewhere on your page
	* &lt;img&gt; (no closing tag)
	* add a src attribute, set it equal to http://foureyes.github.io/mtec1002-spring2014/resources/img/lab-13-face.png 
* view your page 
* add a table
	* make it 2 columns, 3 rows
	* &lt;table&gt;, &lt;tr&gt;, &lt;td&gt;
	* add text into each table cell
* view your page 
* use git to check the __status__, __add__ to staging, and __commit__ (don't forget the __-m 'message'__ part)

### Submit Your Work Through GitHub

* use git to check the __status__, __add__, __commit__ (don't forget the __-m 'message'__ part)
* since you cloned, your repository is already aware of your remote repository...
* so, all you have to do is __push__ (don't forget __origin master__)
* check that your code is on github by refreshing the page
