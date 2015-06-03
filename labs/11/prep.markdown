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
### Another Template

{% highlight html %}
<html>
<head>
    <title></title>
</head>
<body>
<canvas id="sketch" width="800" height="600">
</canvas>
<script>
document.addEventListener('DOMContentLoaded', main);

var sketch;
var context;

function main() {
	sketch = document.getElementById('sketch');
	context = sketch.getContext("2d");
	// draw here... for example:
	// draw_circle(100, 200, 25);
	// context.fillRect(20, 30, 70, 50);
}
</script>
</body>
</html>
{% endhighlight %}

</section>

<section markdown="block">
### Drawing a Circle

{% highlight html %}

function draw_circle(x, y, r) {
	context.beginPath();
	context.arc(x, y, r, 0, 2 * Math.PI, true);
	context.closePath();
	context.fill();
}
{% endhighlight %}

</section>
