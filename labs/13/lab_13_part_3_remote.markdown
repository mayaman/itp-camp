---
layout: lab
title: Lab 13, Part 3 - Remote Server
prefix: ../../
---
# Lab 13, Part 3 - Remote 

## Overview

* connect to a remote server
* run commands on remote server
* upload files to remote server

## Instructions

### Cleaning Up

* close terminal

### Running Commands on a Remote Server

* open terminal
* use ssh to connect to a remote server using your username and foureyes.in as the host
{% highlight bash %}
ssh yourusername@foureyes.in
{% endhighlight %}
* you'll be asked for a password... and once you're authenticated, you will have a prompt on the remote server
* use ls to list all of the files (there should be none!)
* use mkdir to create a directory called public\_html
* chmod 755 public_html
* try running the following commands on the remote server:
	* whoami
	* who
* type CONTROL+D to log out


### Use an FTP Client to Transfer Files

* on your local workstation...
* download this SFTP client: [https://update.cyberduck.io/Cyberduck-4.4.4.zip](https://update.cyberduck.io/Cyberduck-4.4.4.zip)
* unzip it (it might automatically be extracted for you)
* move the CyberDuck up to the desktop
* double click on it to run it
* click on open connection
![sftp-open.png](../../resources/img/sftp-open.png)
* look for the drop down that says __FTP__
![sftp-ftp.png](../../resources/img/sftp-ftp.png)
* change it so that it is __SFTP__
![sftp-sftp.png](../../resources/img/sftp-sftp.png)
* uncheck add to keychain
![sftp-keychain.png](../../resources/img/sftp-keychain.png)
* put in the domain (foureyes.in), username and password
![sftp-login.png](../../resources/img/sftp-login.png)
* once you've contected, you should see the public\_html folder that you created
![sftp-public.png](../../resources/img/sftp-public.png)
* click into the public\_html folder; it should be empty
![sftp-in-public.png](../../resources/img/sftp-in-public.png)
* open up finder and browse to Desktop &rarr; username &rarr; lab_13_part1 
* with finder and CyberDuck side-by-side...
![sftp-finder.png](../../resources/img/sftp-finder.png)
* drag and drop both your .html file and your .css file
![sftp-transfer.png](../../resources/img/sftp-transfer.png)
* if you do this more than once, you may be asked to overwrite (just choose continue):
![sftp-overwrite.png](../../resources/img/sftp-overwrite.png)
* check [http://foureyes.in/~username/mypage.html](http://foureyes.in/~username/index.html)
