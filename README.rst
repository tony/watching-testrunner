Why
---

Because unit testing is even more fun 

* when you don't have to switch out of your editor to get feedback from
  unit tests.
* the shorter the feedback period is till you get feedback from your
  tests.

I've seen the usefullness toying with rubys autotest command, so I
pestered Felix to build something like this, and after using it for about
a two years, I finally got around to packaging it. :-)

In addition to that it's brain dead simple, has no dependencies and is
_really_ small.

Usage
-----

.. code-block:: bash

    % watching_testrunner --help
    Usage: watching_testrunner [options] [--] command [arguments...]

    Options:
      -h, --help            show this help message and exit
      -b BASEPATH, --basepath=BASEPATH
                            base path to watch for changes
      -p WATCH_WILDCARD, --pattern=WATCH_WILDCARD
                            glob-style pattern for file names to watch

Examples
--------

.. code-block:: bash

    $ watching_testrunner nosetessts

This will run nosetests whenever any python file below the current
directory changes

.. code-block:: bash

    $ watching_testrunner -- nosetessts $NOSETESTS_ARGUMENTS

Will run nosetests all the same, but will not try to parse any of the
nosetests arguments.

.. code-block:: bash

    $ watching_testrunner --basepath foo/bar --pattern="*" nosetessts $NOSETESTS_ARGUMENTS

This will run nosetests whenever any file below ./foo/bar changes.

.. code-block:: bash

    $ watching_testrunner --basepath path/to/js_tests --pattern="*.js" jasmine --console
 
This will run jasmine --console whenever any js file below
``./path/to/js_tests`` changes (i.e. you can use the watching testrunner
to get auto test execution using any tool for any language)
