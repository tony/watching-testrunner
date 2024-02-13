# Why

Because unit testing is way more fun

- when you don't have to switch out of your editor to get feedback from unit tests.
- when the feedback period from a change to feedback from your tests is shorter.

I've seen the usefullness of a tool like this when toying with rubys
autotest command, but didn't like the complications of getting that
highly optimized code to work with setups like VMs and Docker Containers
where file system notifications don't reliably work.

So this skips all the optimizations and just uses the simplest possible
algorithm - iterate all files and see what changed. And that works
surprisingly well.

In addition to that it's dead simple, has no dependencies and is
_really_ small.

# Usage

```bash
% watching_testrunner --help
Usage: watching_testrunner [options] [--] command [arguments...]

Options:
  -h, --help            show this help message and exit
  -b BASEPATH, --basepath=BASEPATH
                        base path to watch for changes
  -p WATCH_WILDCARD, --pattern=WATCH_WILDCARD
                        glob-style pattern for file names to watch
```

# Examples

```bash
$ watching_testrunner nosetests
```

This will run nosetests whenever any python file below the current directory changes

```bash
$ watching_testrunner -- nosetests $NOSETESTS_ARGUMENTS
```

Will run nosetests all the same, but will not try to parse any of the nosetests arguments.

```bash
$ watching_testrunner --basepath foo/bar --pattern="*" nosetests $NOSETESTS_ARGUMENTS
```

This will run nosetests whenever any file below ./foo/bar changes.

```bash
$ watching_testrunner --basepath path/to/js_tests --pattern="*.js" jasmine --console
```

This will run jasmine --console whenever any js file below `./path/to/js_tests` changes (i.e. you
can use the watching testrunner to get auto test execution using any tool for any language)

# Many thanks to
- [Felix Schwarz](https://github.com/FelixSchwarz) for the original implementation after me pestering him about this idea
- [Tony Narlock](https://github.com/tony) for prompting me to port this to python 3, hosting it on his account and caring for it's continued development
