App
======

Simple Flask based Python app

Install Dependencies::

    $ pip install -r requirements.txt

Run
---

::

    $ export FLASK_APP=app
    $ export FLASK_ENV=development
    $ flask init-db
    $ flask run

Open http://127.0.0.1:5000 in a browser.


Test
----

::

    $ pip install '.[test]'
    $ pytest

Run with coverage report::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser