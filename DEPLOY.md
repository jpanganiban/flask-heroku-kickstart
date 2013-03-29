Deployment
==========

Stuff that you need to know on how to deploy the application.

Ideal Environment
-----------------

Ubuntu 12.04

The Tools
---------

Let's install the  essentials:

```
# Install the heroku toolchain
$ sudo apt-get install heroku heroku-toolbelt
````

The command above installs the essential tools to deploy a heroku application.


Update Our Deployment
---------------------

To update our deployment

```
$ git push heroku master
```

This pushes the changes in branch `master` to our heroku app.

Also, don't forget to update our git repository

```
$ git push origin master
```


Restarting the Database
-----------------------

Suppose that there were changes in the scheme we do the following:

```
$ heroku pg:reset DATABASE
```

This recreates our postgres database. It will be empty though, so to get
our schema loaded in the databse, we do the following:

We open a browser and navigate to:

```
http://<our-application-url>/db-reset
```

You will see the code that corresponds to the db-reset in `runserver.py`.


Scaling Our Application
-----------------------

Right now, we have 1 worker that handles our heroku application. Should we need
more, we need to increase its capacity.

To increase the capacity of our application, what we do is:

```
$ heroku ps:scale web=2
```
