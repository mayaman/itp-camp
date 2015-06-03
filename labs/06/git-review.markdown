---
layout: slides
title: MTEC1002 - Version Control Review
---

<section markdown="block" class="title-slide">

# Version Control Review, Troubleshooting 

{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Version Control - Definition

__What is version control?__ &rarr;

<div class="incremental" markdown="block">

__Version control software__ allows you to record changes to a file or set of files over time. With version control, you can:
</div>
</section>

<section markdown="block">
### And Why!?

__Why use version control anyway?__ &rarr;


<div class="incremental" markdown="block">

* so that you can __review__ changes made over time, and track __who__ made those changes
* to document work by leaving __comments__ on changes that you've made
* __easily recover from accidentally breaking or deleting code__ by __revert__ing to a previous state
* it make sharing and collaborating with others easier through the ability to __send, receive and automatically merge__ changes
* __it's expected that you know this as a professional programmer__
* um ... it's how we submit assignments!
</div>

</section>

<section markdown="block">
### Tools

__What version control software are we using?  What is the website we use to store assignments?  What is the relationship between the two?__ &rarr;

<div class="incremental" markdown="block">

* __git__ is solely the __version control__ system that we're using
* __github__ is a __website__ that _hosts_ (stores) git repositories
	* that means it can store all versions of your files
	* (but only after you've sent changes to it)
* __git__ and __github__ are two totally separate things!
* we'll be using __git__ to submit our assignments by posting them to __github__
</div>
</section>

<section markdown="block">
### Vocabulary

What is a __repository__, __local repository__, __remote repository__, __commit__, and __diff__? &rarr;

<div class="incremental" markdown="block">

* __repository__ - the place where your version control system stores the snapshots that you _save_
* __local repository__ - the repository on your computer
* __remote repository__ - a copy of versions of your files on another computer
* __commit__ - save a snapshot of your work
* __diff__ - the line-by-line difference between two files or sets of files
</div>
</section>


<section markdown="block">
### More Vocabulary

In your __local repository__, describe what is contained in the: __working directory__, __index__ and __HEAD__. &rarr;

<div class="incremental" markdown="block">
* __the working directory / working copy__ - stuff you've changed but haven't saved
* __index__ - stuff that you're about to save (staging area)
* __HEAD__ - stuff that you've already saved
</div>
</section>

<section markdown="block">
### How Do We Use Git?

__What is the primary way that we use git?  That is, what is the root command, and what can we do with it? "Where" do you have to be to use git?__ &rarr;

<div class="incremental" markdown="block">
* we use __git__ through the __commandline__ 
* the base command is __git__ followed by a specific _git command_
* these commands/actions only work when __you're in a git repository__
* (that is, you have to cd to the directory that contains your repository)

</div>
</section>

<section markdown="block">
## All git commands must be run in your repository directory (where you ran git init)
</section>

<section markdown="block">
### Setting Up Repositories

__What's the workflow for setting up repositories for our assignments? (just the high level description, not the actual commands)__ &rarr;

<div class="incremental" markdown="block">
* create a __local repository__
* __configure it__ to use your name and email (for tracking purposes, comments)
* create a __remote repository__ (we'll use __github__ as our __remote repository__)
* _link_ the two
</div>
</section>

<section markdown="block">
### Commands for Setting Up Repositories

__What are the actual commands that you would use to set up and link your repositories?__ &rarr;

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
### One of These Is Not Like the Others

__One of the previous commands was not a git command?  Which one was it?  Explain what it does.__ &rarr;

<div class="incremental" markdown="block">

{% highlight bash %}
# creating a remote repository on github can be done with curl:
#     curl makes a request to github with the username and data you provide
# -u means your username:
#     replace 'your github user name' with your username
# -d means data: 
#    replace 'your repository name' with the name you'd like to 
#    call your new remote repository
# keep EVERYTHING ELSE as is
curl -u 'your github user name' https://api.github.com/user/repos -d '{"name":"your repository name"}'
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Dissecting git remote

__Explain what each part of the following command means__ &rarr;

{% highlight bash %}
git remote add origin "your username"@"the url to your repository on github"
{% endhighlight %}

<div class="incremental" markdown="block">
* you're using a bunch of git commands that deal with remote repositories
* you're making your local repository aware of a remote repository (adding a remote repository)
	* you're calling that remote repository origin
	* and you're associating it with a github url (which is hopefully a repository that you've created!)
</div>
</section>

<section markdown="block">
### Additional git remote Commands

Sometimes you need to troubleshoot your remote repository connection.

{% highlight bash %}
# show remote repositories
git remote -v

# or ...
cat .git/config

# remove / delete an associated remote repository
git remote remove name_of_remote

# change / set the url of a named remote
git remote set-url name_of_remote the_updated_url
{% endhighlight %}
</section>

<section markdown="block">
### Making, Saving, and Sharing Changes

__What's the workflow for making, saving and sharing changes?__ &rarr;

<div class="incremental" markdown="block">
* make changes, show your exact line-by-line changes... and check on their status
* put them aside so they can staged for saving / committing, check on your staged changes
* save / commit, check that your changes were saved
* send changes from local repository to remote repository
</div>
</section>


<section markdown="block">
### And...the Corresponding Commands

__What's are the actual commands that you use for making, saving and sharing changes?  Let's start with just making the change and prepping it to be saved.__ &rarr;

<div class="incremental" markdown="block">

{% highlight bash %}
# (make changes)

# show the exact, line-by-line changes that you've made
git diff --color

# check on the status of your changes
git status

# stage your changes / prep them to be saved
git add --all 

# (continued...)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Corresponding Commands Continued

__Saving and sending to the remote repository__ &rarr;

<div class="incremental" markdown="block">
{% highlight bash %}
# check your staged changes
git status

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
### Details on git status

__What does git status do?__ &rarr;

<div class="incremental" markdown="block">
__git status__ - show what changes are ready to be committed as well as changes that you are working on in your working directory that haven't been staged yet

</div>
</section>

<section markdown="block">
### Additional Notes on git add

__git add__ marks a file or files as ready to be saved.  

__There are two ways to use it:__ &rarr;

{% highlight bash %}
# add all
git add --all 

# add specific file
git add relative/path/to/myfile.txt
{% endhighlight %}
</section>

<section markdown="block">
### Commit Messages

When you commit (save) __remember to add a commit message__ using the __-m__ option.

{% highlight bash %}
# in the directory of your repository
git commit -m 'commit message goes here'
{% endhighlight %}
</section>

<section markdown="block">
### Some Troubleshooting

If you're having issues sending your changes to your remote repository (github)...

Show your remote repository names and urls:

{% highlight bash %}
git remote -v
{% endhighlight %}

The output should look something like...

{% highlight bash %}
origin	https://github.com/jversoza/lab-06-javascript-conditionals.git (fetch)
origin	https://github.com/jversoza/lab-06-javascript-conditionals.git (push)
{% endhighlight %}

If it's incorrect, try changing the associated url:

{% highlight bash %}
git remote set-url origin https://your_github_user_name@github.com/your_github_user_name/lab-06-javascript-conditionals.git 
{% endhighlight %}
</section>
