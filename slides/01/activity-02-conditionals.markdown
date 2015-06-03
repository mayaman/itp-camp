---
layout: lab
title: JavaScript Conditionals
prefix: ../../
chrome: 0
---
# JavaScript Conditionals

Let's write a couple of programs that require the use of conditionals....

1. cake
2. \* guess 

### cake

Write a program that asks the user if they want cake.  Based on the response, it will output a different message to the JavaScript Console.

* create a new file called __cake.html__
* setup an html file, and add script tags... start writing your JavaScript between the script tags
* the program should ask: "Do you want cake?"
* based on the user's input:
	* print out "Have some cake." if the user says exactly "yes"
	* print out "No cake for you" if the user says anything other than "yes"
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
// Run 1
(prompt) Do you want cake?
> yes
Have some cake.
// Run 2
(prompt) Do you want cake?
> maybe
No cake for you.
{% endhighlight %}
* save your file in SublimeText
* use status, add commit and push to save your file in version control and submit it
* modify your program so that the program accepts no as an answer, and says something different if it is not yes and not no:
	* print out "Have some cake." if the user says exactly "yes"
	* print out "No cake for you." if the user says exactly "no"
	* print out "I don't understand." if the user types anything else"
* example interaction is below (everything after the greater than sign (&gt; is user input using the prompt function):
{% highlight bash %}
// Run 1
(prompt) Do you want cake?
> no
No cake for you
// Run 2
(prompt) Do you want cake?
> maybe
I don't understand
{% endhighlight %}

<hr>

### guess

Write a number guessing game!  "Hardcode" a secret number.  Ask the user to guess the secret number.  If they are correct, say "You got it!".  If they are within 1, say "Close, but the number is (the secret number)".  Lastly, if they were totally incorrect, then say, "The number is (the secret number)".  

* You can look up the parseInt function to convert the input into a number so that your comparisons work.
* (or use == instead of ===)

{% highlight bash %}
// In the examples below, assume 5 was hardcoded as the secret number
// Run 1
(prompt) Guess what number I'm thinking of!
> 5
You got it!
// Run 2
(prompt) Guess what number I'm thinking of!
> 6
Close, but the number is 5.
// Run 3
(prompt) Guess what number I'm thinking of!
> 7
The number is 5.
{% endhighlight %}

