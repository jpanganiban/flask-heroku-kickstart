Flask Kickstart Docs
====================

You'll find most of the things I've done with the application here.

Installation
------------

See `INSTALL.md` for more information on how to install the application locally.

Deployment
----------

See `DEPLOY` for more information on how to deploy the application to heroku (ie. push code).

Application Structure
---------------------

Our application structure:


```
application/
  controllers/
  forms/
  models/
  views/
config.py
development.env
Procfile
requirements.txt
runserver.py
```

###application/

This is where our application lives. You can find the application factory in
`__init__.py`.

####application/controllers/

This is where all the controllers go. The convention is to have a new module for
every main functionality (ie. /billing -> controllers/billing.py). We heavily
use the [Blueprints][blueprint] to make our application a lot more modular.

[blueprint]: [http://flask.pocoo.org/docs/blueprints/]


####application/models/

This is the directory where we store all the models. You can find the db object
in `__init__.py`. The idea is to create a new module for every model class (ie.
User -> user.py).

####application/forms/

This is where all the forms go. We are using flask-wtforms for our forms.

####application/views/

This is just basically the 'template' directory. Only that 'views' sounds much
more appropriate, IMO.

####config.py

This module contains the Config class where all the configurations go. Should
you need to pick-up something dynamically (ie. from the environment variables)
what you do is this:

```
import os

class Config(object):
  # Configs here...

  @property
  def SOME_CONFIG(self):
    return os.environ.get('SOME_VAR', 'DEFAULT VALUE')
```

####development.env

This file will contain the environment variables we will load during the
development. It should have the similar environment variables as the ones in
Heroku but points to something local.

ie.

```
DATABASE_URL=sqlite:///mydb.db

instead of

DATABASE_URL=postgresql://<something that points to heroku>
```

The way we use it:


```
$ foreman start --env development.env
```

This reads the Procfile and starts everything (similar the way Heroku does), and
reads the development.env and sets the variables in the file as the process environment
variable.

####Procfile

This is where we store the process we need to run. You can find more about it in
the heroku docs.

####requirements.txt

This is where we store all our python package requirements. Whenever we install
a new package via pip, We should make sure to update this file:

```
$ pip freeze > requirements.txt
```

####runserver.py

This is our main module where our flask application is contructed.


TODO
----

Setup SQLAlchemy migrations so we can properly update our database schema.
