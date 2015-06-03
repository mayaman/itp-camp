---
layout: lab
title: Prep - Creating Local and Remote Repositories
prefix: ../../
---
# Lab 8 - Prep - Creating Local and Remote Repositories, Warm-Up Programs

In this lab, you'll be:

1. creating two repositories, one local and one remote
2. linking the two with each other so that they can be synchronized
3. associating a name and email address with your local repository
4. creating the following programs:
	1. password to pizza site
	2. ordered enough pizza? (remember to use parseint)
	3. price for pizza toppings
	4. \* tip (for pizza restaurant, of course)

## Instructions for Repository Set Up

### Set up Your Local Repository

This will create a local git repository to store your work for this lab.  The repository will be in ~/Desktop/yourname/lab-08-for.

* open terminal
* (if doesn't already exist) create a folder that consists of your first initial and last name on your Desktop
{% highlight bash %}
cd ~/Desktop
mkdir your_first_initial_last_name
{% endhighlight %}
* within that folder, create another folder called __lab-08-for__ and __change into it__
{% highlight bash %}
cd your_first_initial_last_name
mkdir lab-08-for
cd lab-08-for
{% endhighlight %}
* use pwd to verify that you're in the correct folder
	* you should be in __~/Desktop/your_first_initial_last_name/lab-08-for__
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
* in your lab-08-for folder, create your repository!
{% highlight bash %}
git init
{% endhighlight %}
* it should say:
{% highlight bash %}
Initialized empty Git repository in /Users/joe/Desktop/jversoza/lab-08-for/.git/
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

* log in to github; you should see the list of repositories on the right	
![Repository List](../../resources/img/repos-screen.png)
* you should have all of the previous lab related repositories 
* go back to terminal
* using the commandline, create a remote repository on github by using the command below...
* substitute your github username where it says "your github user name" (keep the single quotes and __KEEP "name":__ at the end of the line; don't change that!).  the name of the repository is lab-08-for (you can see that specified at the end of the command)
{% highlight bash %}
curl -u 'your github user name' https://api.github.com/user/repos -d '{"name":"lab-08-for"}'
{% endhighlight %}
* it should output a bunch of text!
{% highlight bash %}
Enter host password for user 'jversoza':
{
  "id": 17210769,
  "name": "lab-08-for",
  "full_name": "jversoza/lab-08-for",
  "owner": {
    "login": "jversoza",
	...
}
{% endhighlight %}
<!--_-->
* refresh your page on github
* you should see the new repository added
* go back to terminal
* make sure you're in your local repository folder for __lab-08-for__
	* use __pwd__ to do this
	* you should be in __~/Desktop/yourname/lab-08-for__
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
git remote add origin https://your_github_user_name@github.com/your_github_user_name/lab-08-for.git 
{% endhighlight %}
* (alternatively, if you click on your repo you can see your remote repository's url on the lower right hand side of the page...)
![Repository List](../../resources/img/repos-url.png)
* to check that you've linked properly, run the following command again:
{% highlight bash %}
git remote -v
{% endhighlight %}
* it should show origin ... and your repository url:
{% highlight bash %}
origin	https://jversoza@github.com/jversoza/lab-08-for.git (fetch)
origin	https://jversoza@github.com/jversoza/lab-08-for.git (push)
{% endhighlight %}

### Creating and Saving Changes Locally, Sending to Remote Repository

In this part of the lab, you will create a text file in your local repository, and then you'll send it to your remote repository.

* open terminal
* make sure you're in your local repository folder for lab-08-for
	* use __pwd__ to do this
	* you should be in __~/Desktop/yourname/lab-08-for__
	* if you're not in your lab folder, change your directory to it
	* if this doesn't exist yet... make sure you completed the beginning part of this lab
* use __git status__ to show that there aren't any changes yet
{% highlight bash %}
git status
{% endhighlight %}
* it should give the following output
{% highlight bash %}
# On branch master
#
# Initial commit
#
nothing to commit (create/copy files and use "git add" to track)
{% endhighlight %}
* create a file called __README.markdown__ using __SublimeText__ (see below...)
* go to Applications &rarr; SublimeText (or use Command+Spacebar to activate spotlight search, then start typing Sublime)
* once SublimeText is open, go to File &rarr; New (or Command+n) to create a new file
* save your file by going to File &rarr; Save As to save your files as __README.markdown__ in your __~/Desktop/yourname/lab-08-for__
![Save As](../../resources/img/sublime-save-as-menu.png)
* make sure you navigate to your __~/Desktop/yourname/lab-08-for__ before saving!
![Save As](../../resources/img/sublime-save-as.png)
* add text to your file: 
{% highlight bash %}
lab 8, for
{% endhighlight %}
* switch back to terminal
* use __git status__ to show that you've made changes
{% highlight bash %}
git status
{% endhighlight %}
* it should give the following output; notice that it contains README.markdown 
{% highlight bash %}
# On branch master
#
# Initial commit
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	README.markdown
nothing added to commit but untracked files present (use "git add" to track)
{% endhighlight %}
* if we want to save this file in the repository, we have _stage_ it (that is, mark it as something that we're ready to save / commit)
{% highlight bash %}
git add --all
{% endhighlight %}
* to check that you've staged your commit, use __git status__ again
{% highlight bash %}
git status
{% endhighlight %}
* it should output the following text (note that README.markdown moved from _untracked_ to _Changes to be committed_)
{% highlight bash %}
# On branch master
#
# Initial commit
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#
#	new file:   README.markdown
#
{% endhighlight %}
* now we're ready to commit (that is, save the file to the local repository); everything after the -m is the message that will be associated with the changes that you've made
{% highlight bash %}
git commit -m "added a README file"
{% endhighlight %}
* the output of the command should be:
{% highlight bash %}
[master (root-commit) 5b24d27] added readme
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.markdown
{% endhighlight %}
* check the status again 
{% highlight bash %}
git status
{% endhighlight %}
* notice that there is nothing staged and no more changes!
{% highlight bash %}
# On branch master
nothing to commit, working directory clean
{% endhighlight %}
* to show the changes that you've saved so far, use __git log__
{% highlight bash %}
git log --color
{% endhighlight %}
* it should show you the following...
{% highlight bash %}
commit 5b24d2777a602908978916ca8fe9c8dd2ed6036b
Author: joe <jversoza@citytech.cuny.edu>
Date:   Wed Mar 26 20:18:51 2014 -0500

    added readme

{% endhighlight %}
* you can share your changes / send them to a remote repository by using __git push__
{% highlight bash %}
git push origin master
{% endhighlight %}
* it should result in:
{% highlight bash %}
Counting objects: 3, done.
Writing objects: 100% (3/3), 242 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/jversoza/lab-08-for.git
 * [new branch]      master -> master
{% endhighlight %}
* go back to github and look in your repository.  you should see that file appear.

<hr>

## Instructions for Warm-Up Programs

Note that __ALL OF THESE FILES MUST BE SAVED IN THE LOCAL REPOSITORY THAT YOU CREATED FOR THIS LAB__.

<hr>

### password

Write a program for a pizza ordering site that asks for your user name and password.  The program will have a _hardcoded_ username and password of your choosing.  Ask the user for their username, then ask for their password.  Based on their input, display an appropriate message to the JavaScript console.

* using SublimeText, create a new file called __password.html__ in your repository directory: __~/Desktop/jversoza/lab-08-for/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* output - "Welcome to Pizza 4 U"
* create two variables, one for username and one for password
* set each to a value of your choosing
* ask for a username and assign it to a new variable: "What is your user name?"
* ask for a password and assign it to a new variable : "What is your password?"
* say "WELCOME!" if the user input matches the username and password that you set
* say "K THX BAI" if the user input does not match either the username or password that was set
* use logical operators and if / else to do this
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
# assuming that the hardcoded username and password are albert and secret respectively...

(prompt) What is your username?
> albert
(prompt) What is your password?
> secret
WELCOME!
{% endhighlight %}

* save your file in SublimeText
* use git status, add, commit, and push to save your file in version control and submit it

<hr>

### enough

Write a program that determines if you've ordered enough pizza.  It assumes 8 slices per pie, and 2 slices per person.  It will ask for how many people and how many pies... and based on the input, it will display an appropriate message.

* using SublimeText, create a new file called __enough.html__ in your repository directory: __~/Desktop/jversoza/lab-08-for/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* output - "Let's find out if you ordered enough pizza?"
* ask for number of slices and assign it to a new variable: "How many pies did you order?"
* ask for number of people and assign it to a new variable : "How many people are eating pizza?"
* calculate how many slices are needed based on the number of people (remember, 2 per person)
* calculate total slices there are based on the number of pies (remember, 8 per pie)
* use a conditional - an if / else - with a comparison operator to determine if there are enough pies
* say "x pies is equal to y slices" (with x and y substituted appropriately)
* say "x people need y slices" (with x and y substituted appropriately)
* say "U NEED MOAR 'ZA" if there are not enough slices
* (optional) - print out how many extra slices are needed...
* the program should say "ENOUGH!" if there are enough (or more) slices to accommodate the number of people specified
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}

Let's find out if you ordered enough pizza?
(prompt) How many pies did you order?
> 3 
(prompt) How many people are eating pizza?
> 15
3 pies are 24 slices
15 people need 30 slices
U NEED MOAR 'ZA
{% endhighlight %}

* save your file in SublimeText
* use git status, add, commit, and push to save your file in version control and submit it
<hr>

### toppings

Write a program that gives back the price of a topping based on user input...

* using SublimeText, create a new file called __toppings.html__ in your repository directory: __~/Desktop/jversoza/lab-08-for/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* say - "We have mushrooms, pepperoni, and anchovies."
* ask for a topping: "What topping would you like?"
* based on the input, say "That's an extra x dollars" with x substituted appropriately:
	* mushrooms - $2
	* pepperoni - $3
	* anchovies - $4
* if the topping that the user put in does not exist, say "Sorry, we don't have that"
* use an if / else if / else to do this
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}

We have mushrooms, pepperoni, and anchovies.
(prompt) What topping would you like?
> mushroom
That's an extra 2 dollars.
{% endhighlight %}

* save your file in SublimeText
* use git status, add, commit, and push to save your file in version control and submit it

<hr>


### tip

Create a tip calculator.

* using SublimeText, create a new file called __tip.html__ in your repository directory: __~/Desktop/jversoza/lab-08-for/__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should ask the following:
	* how many people?	
	* how much did it cost?
	* how was the service? 
		* the values for this can be: terrible, poor, ok, good, great
		* only ask about service if there are less than 6 people
* if the number of people are > 6 tip should always be 20%, regardless of service.
* otherwise, calculate the tip using the following table:
	* terrible = no tip (0%)
	* poor - 10%
	* ok - 15%
	* good - 20%
	* great - 25%
* output the calculated tip.
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
# Run 1: 
# -----
(prompt) How many people? > 2
(prompt) How much did it cost? > 25
(prompt) How was the service (terrible, poor, ok, good, great)? > great
You should probably tip $6.25!

 
# Run 2: 
# -----
(prompt) How many people? > 4
(prompt) How much did it cost? > 70
(prompt) How was the service (terrible, poor, ok, good, great)? > meh
Couldn't understand meh service; using default 15 percent.
You should probably tip $10.5!

# Run 3: 
# -----
(prompt) How many people? > 200
(prompt) How much did it cost? > 950
You should probably tip $190.0!
{% endhighlight %}

