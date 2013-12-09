#!/usr/bin/env python

import glob
import os
import sys
import time
from optparse import OptionParser


class FileWatcher(object):
    def __init__(self, basepath, watch_wildcard):
        self.basepath = basepath
        self.wildcard = watch_wildcard
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
    
    def _check_for_file_changes_in_dir(self, topdir):
        change_detected = False
        filenames = glob.glob(os.path.join(topdir, self.wildcard))
        for filename in filenames:
            if self.file_did_change(filename):
                change_detected = True
        return change_detected
    
    def _check_for_changes_in_subdirs(self, topdir):
        change_detected = False
        for item in os.listdir(topdir):
            itemname = os.path.join(topdir, item)
            if os.path.isdir(itemname):
                change_in_subdirectory = self.did_files_change(itemname)
                if change_in_subdirectory == True:
                    change_detected = True
        return change_detected
    
    def did_files_change(self, topdir=None):
        if topdir is None:
            topdir = self.basepath
        file_changed = self._check_for_file_changes_in_dir(topdir)
        subdir_changed = self._check_for_changes_in_subdirs(topdir)
        return (file_changed or subdir_changed)
    
    def execute_command_on_change(self, command):
        while True:
            if self.did_files_change():
                command.execute()
                print " -- done --"
            time.sleep(1)
    

class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
    
    def execute(self):
        os.system(self.cmd)

def option_parser():
    usage = "usage: %prog [options] command [arguments...]"
    parser = OptionParser(usage)
    parser.add_option("-b", "--basepath", dest="basepath", default=".",
                      help="base path to watch for changes")
    parser.add_option("-p", "--pattern", dest="watch_wildcard", default="*.py",
                      help="glob-style pattern for file names to watch")
    return parser

def parse_options_and_shell_command():
    parser = option_parser()
    (options, positional_arguments) = parser.parse_args()
    shell_command = " ".join(positional_arguments)
    if shell_command == "":
        parser.error("No command provided")
    
    return (options, shell_command)

def main(unused_argv=None):
    options, shell_command = parse_options_and_shell_command()
    watcher = FileWatcher(options.basepath, options.watch_wildcard)
    try:
        watcher.execute_command_on_change(Command(shell_command))
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main(sys.argv)
