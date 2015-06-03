---
layout: slides
title: MTEC1002 - Prep, Review
---

<section markdown="block" class="title-slide">

# Prep, Review

{% include title-slide-footer.html %}
</section>

<section markdown="block">
## Quick Rundown of Git Commands 
</section>

<section markdown="block">
### Git - Setting Up Repositories

__What are the commands that you would use to set up and link your repositories?__ &rarr;

<div class="incremental" markdown="block">
{% highlight bash %}
# create a local repository
git init

# configure it with your name and email
git config user.name  "your name"
git config user.email "your@email.address"

# create a remote repository
curl -u 'your github user name' https://api.github.com/user/repos -d '{"name":"your repository name"}'

# link the two
git remote add origin "your username"@"the url to your repository on github"
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Git - Saving and Sharing Changes

__What's are the commands that you would use for making, saving and sharing changes?  Let's start with just making the change and prepping it to be saved.__ &rarr;

<div class="incremental" markdown="block">

{% highlight bash %}
# (make changes)

# show the exact, line-by-line changes that you've made
git diff --color

# check on the status of your changes
git status

# stage your changes / prep them to be saved
git add --all 

# check your staged changes using git status again
git status

# (continued...)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Git - Saving and Sharing Continued...

__Saving and sending to the remote repository__ &rarr;

<div class="incremental" markdown="block">
{% highlight bash %}

# save them, make sure you remember your comment by using -m!
git commit -m 'my message'

# show a history of your changes
git log --color (show your changes so far)

# send to your remote repository
git push origin master
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Showing and Getting Rid of Remote Repositories

How do you __show remote repository names and urls... and how do you get rid of remote repositories?__ &rarr;

<div class="incremental" markdown="block">
{% highlight bash %}
# show remote repositories
git remote -v

# The output should look something like...
# origin	https://jversoza@github.com/jversoza/lab-08-prep.git (fetch)
# origin	https://jversoza@github.com/jversoza/lab-08-prep.git (push)

# remove remote repository (assuming remote repository name is origin)
git remote remove origin
{% endhighlight %}

__And how do you add back a remote repository?__

{% highlight bash %}
git remote add origin https://jversoza@github.com/jversoza/lab-08-new.git
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Functions

__What's a function?  What's a function call?  What are arguments?__ &rarr;

<div class="incremental" markdown="block">
* a __function__ is a named sequence of statements that perform some useful action
* it can __optionally__ take __inputs__ and __return values__
* to __call__ a function is just to _run_ or _execute_ it
* the values passed to a function are called __arguments__
</div>
</section>

<section markdown="block">
###  Calling Functions

__How do you call _or execute_ a function?__ &rarr;

<div class="incremental" markdown="block">
* to call a function, use its name followed by parentheses... with an optional list of comma separated arguments between the parentheses
* an example of a function call is:

{% highlight html %}
prompt("hello") is a function call
{% endhighlight %}
</div>
</section>

<section markdown="block">
## When you see parentheses - ( )'s - after a function name, that function is being _called_ or _executed_
</section>

<section markdown="block">
### Built-in Functions

JavaScript comes with many built-in functions.  __We know three; what are they and what do they do?__ &rarr;

<div class="incremental" markdown="block">
* __prompt("some message")__ - asks the user for input and __returns__ that value to your program! ... takes a single argument, the message to display to a user (this usually requires the use of _variables_)
* __console.log("some message")__ - prints the argument that you pass to it... out to Chrome's JavaScript console 
* __parseInt("5")__ - converts a string to a number
</div>
</section>

<section markdown="block">
### Some Functions Return Values

__What type of value does prompt always return?  What type of value does parseInt always return?__  &rarr;

<div class="incremental" markdown="block">
* __prompt__ always gives back a __string__
* __parseInt__ always gives back a __number__
</div>
</section>


<section markdown="block">
### Using Prompt With Variables

Remember that the function prompt gives back a value.  To retain that value, you have to hold it in a variable:

{% highlight html %}
var answer = prompt("Yes or no!?");
{% endhighlight  %}

</section>



<section markdown="block">
## Conditionals
</section>

<section markdown="block">
### Blocks of Code

Curly braces denote statements of code that are grouped together.  Everything within the curly braces below is considered part of the if statement.  Blocks of code must __start and end__ with curly braces...

{% highlight js %}
... {
	// code wrapped by curly braces
} 
{% endhighlight %}

</section>

<section markdown="block">
### Conditionals...

__What kind of statement would we use to execute code if a condition is true?__ &rarr;

<div class="incremental" markdown="block">

An if statement...

{% highlight js %}
if (some_boolean_expression) {
	// do stuff here if expression is true
}
{% endhighlight %}

* [Diagram for if statements](../../resources/img/if.png)
* [Diagram for consecutive if statements](../../resources/img/if-consecutive.png)
</div>

</section>

<section markdown="block">
### Conditionals Continued

__What kind of statement would we use to execute code one branch of code if a condition is true and another branch of code otherwise?__ &rarr;

<div class="incremental" markdown="block">

* an if / else statement  
* an else must always have a preceding if!

{% highlight js %}
if (some_boolean_expression) {
	// do stuff here if expression is true
} else {
	// do stuff here if expression is false
}
{% endhighlight %}

* [Diagram for if / else statements](../../resources/img/if-else.png)
* else statements are always attached to an if!
</div>

</section>

<section markdown="block">
### If / Else If

__What kind of statement would we use to execute multiple branches of code based on multiple chained conditions?__ &rarr;


<div class="incremental" markdown="block">
Use if / else if statements

{% highlight js %}
if (boolean_expression_1) {
	// do stuff here if expression 1 is true
} else if (boolean_expression_2) {
	// do stuff here if expression 2 is true
} else if (boolean_expression_3) {
	// do stuff here if expression 3 is true
}
{% endhighlight %}

* [Diagram for if / else if statements](../../resources/img/if-else-if.png)
</div>
</section>

<section markdown="block">
### If / Else If

* once a condition is true, the if / else if executes the code in that block and the if / else if ends immediately (even if other later conditions are true)
* can end with else to handle all _other_ conditions
</section>


<section markdown="block">
### Usage

* use if statements if there's a single alternative path of execution
* use if/else  statements if there's a two possible alternative paths of execution
* use if/else if statements if there's more than two possible alternative paths of execution
</section>

<section markdown="block">
### Repeat That Again?

__What construct do we use if we want to execute a block of code multiple times without writing it multiple times?__ &rarr;

<div class="incremental" markdown="block">
* we use a for loop!
* __what does a for loop look like... what are its parts?__ &rarr;
</div>
</section>

<section markdown="block">
### For Loop Dissected

A for loop consists of the keyword, __for__, and three parts, separated by a semicolon,  contained within parentheses:

* initialization - declares a variable and value to start with
* condition - a condition for the loop to stop 
* _afterthought_ - a way to increment/decrement or change the variable on each iteration so that the condition is eventually met

You can use the variable that you declare in the initialization within your for loop!
</section>

<section markdown="block">
### For Loop Parts

{% highlight js %}
//    initialization
//    |        condition
//    |        |       afterthought/increment
//    |        |       |
for(var i = 0; i <= 5; i = i + 1) {
	console.log(i);
}
{% endhighlight %}
</section>

<section markdown="block">
### Square 1 Through 10

__Create a for loop that prints out the square of every number from 1 through 10__ &rarr;

<div class="incremental" markdown="block">
{% highlight js %}
for(var i = 1; i <= 10; i = i + 1) {
	console.log(i * i);
}

{% endhighlight %}
</div>
</section>
