#!/usr/bin/env python
# -*- coding: utf8 - *-
"""Command line tool for watching files and re-running shell commands.

watching_testrunner
~~~~~~~~~~~~~~~~~~~

"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    with_statement,
    unicode_literals,
)

import argparse
import glob
import os
import sys
import time


class FileWatcher(object):
    def __init__(self, basepaths, patterns):
        self.basepaths = basepaths
        self.patterns = patterns
        self.existing_files = {}

    def file_did_change(self, filename):
        change_detected = False

        current_mtime = os.path.getmtime(filename)
        if filename in self.existing_files:
            known_mtime = self.existing_files[filename]
            if known_mtime < current_mtime:
                change_detected = True
        else:
            # TODO: Currently there is no handling of deleted files.
            change_detected = True

        self.existing_files[filename] = current_mtime
        return change_detected

    def _glob(self, topdir):
        for pattern in self.patterns:
            for file in glob.iglob(os.path.join(topdir, pattern)):
                yield file

    def _check_for_file_changes_in_dir(self, topdir):
        did_change = False
        # Iterating over all files, to record all changes
        for filename in self._glob(topdir):
            if self.file_did_change(filename):
                did_change = True
        return did_change

    def _check_for_changes_in_subdirs(self, topdir):
        change_detected = False
        for item in os.listdir(topdir):
            itemname = os.path.join(topdir, item)
            if os.path.isdir(itemname):
                change_in_subdirectory = self.did_files_change(itemname)
                if change_in_subdirectory:
                    change_detected = True
        return change_detected

    def did_files_change(self, topdir=None):
        if topdir is None:
            # not using a generator to ensure all file changes are recorded
            return any([self.did_files_change(topdir) for topdir in self.basepaths])

        file_changed = self._check_for_file_changes_in_dir(topdir)
        subdir_changed = self._check_for_changes_in_subdirs(topdir)
        return file_changed or subdir_changed

    def execute_command_on_change(self, command):
        while True:
            if self.did_files_change():
                command.execute()
                print(" -- done --")
            time.sleep(1)


class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd

    def execute(self):
        os.system(self.cmd)


def option_parser():
    parser = argparse.ArgumentParser(description='Execute command on file changes')
    parser.add_argument(
        "-b",
        "--basepath",
        action='append',
        metavar="BASEPATH",
        dest="basepaths",
        help="base paths to watch for changes. Default: .",
    )
    parser.add_argument(
        "-p",
        "--pattern",
        action='append',
        metavar="PATTERN",
        dest="patterns",
        help="glob-style patterns for file names to watch. Default: *.py",
    )
    parser.add_argument(
        metavar="COMMAND",
        dest='command',
        nargs='+',
        help="shell command to invoke on each chanege. Separate with -- from other arguments if neccessary",
    )
    return parser


def parse_options_and_shell_command():
    parser = option_parser()
    options = parser.parse_args()
    if options.basepaths is None:
        options.basepaths = ["."]

    if options.patterns is None:
        options.patterns = ["*.py"]

    # REFACT remove concatenation and switch to subprocess.run
    options.command = " ".join(options.command)

    return options


def main(unused_argv=None):
    options = parse_options_and_shell_command()
    watcher = FileWatcher(options.basepaths, options.patterns)
    try:
        watcher.execute_command_on_change(Command(options.command))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main(sys.argv)
