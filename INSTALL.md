Installation
============

Stuff that you need to know to get a local dev machine working.


Ideal Environment
-----------------

Ubuntu 12.04 LTS


The Tools
---------

Let's install the essentials first:

```
# Install the applications we need.
$ sudo apt-get install python-setuptools git-core
$ sudo easy_install pip
$ sudo pip install virtualenv virtualenvwrapper

# Now, setup virtualenvwrapper
$ echo "WORKON_HOME=~/.envs" >> ~/.bashrc
$ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

# Refresh our current shell session to fetch our changes in ~/.bashrc
$ source ~/.bashrc
```

We're installing the standard python setuptools. That gives us easy_install.
With easy_install, we install pip. pip is just like easy_install, much modern.
We'll be using pip to install packages.

For the next part, we'll install virtualenv and virtualenvwrapper. What this
basically does is it creates an isolated space for packages in our project.

You'll get new shell commands:

```
$ pip
$ workon
$ mkvirtualenv
$ lsvirtualenv

# and more... You can read more about the following

http://virtualenvwrapper.readthedocs.org/en/latest/
http://www.pip-installer.org/en/latest/
```


The Application Environment
---------------------------

Now that we have the necessary tools to start working, let's make our project
environment.

```
# Let's check the current packages in our environment
$ pip freeze

# Let's try making that isolated environment
$ mkvirtualenv myproject --distribute

# Activate that environment
$ workon myproject

# Check that we're in a different environment. We should be see less packages.
$ pip freeze
```

Once we're sure that we can make environments, Let's start working on our 'real'
project, shall we?
