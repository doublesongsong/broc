#!/usr/bin/env python
# -*- coding: utf-8 -*- 

################################################################################
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
    Description : analyse command line option
    Authors     : zhousongsong(doublesongsong@gmail.com)
                  liruihao(liruihao01@gmail.com)
    Date        : 2015-09-18 10:28:23
"""

import os
import sys
import getopt

broc_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
sys.path.insert(0, broc_dir)
from util import Log

def Help(bin_name, subcommand=None):
    """
    Show help imformation
    Args:
        bin_name : executable file name
        subcommand : executable file subcommand. In broc, it's in [""]
    Return:
        0 : success
    """
    if subcommand is None:
        Log.colorprint("DEFAULT", "Usage: %s <subcommand> [option] [args]" % (bin_name), False)
        Log.colorprint("DEFAULT",
                "Type %s help <subcommand> for help on a specific subcommand" % (bin_name),
                False)
        Log.colorprint("DEFAULT", "Available subcommands:", False)
        Log.colorprint("DEFAULT", "    build      : Build the specified targets", False)
        Log.colorprint("DEFAULT", "    test       : Build and runs the specified targets",
                False)
        Log.colorprint("DEFAULT", "    show-deps  : Print the dependency graph", False)
        Log.colorprint("DEFAULT", "    clean      : Remove output files", False)
        Log.colorprint("DEFAULT", "    scratch    : Create a BROC template", False)
        Log.colorprint("DEFAULT", "    version    : Display the version", False)
        Log.colorprint("DEFAULT", "    config     : Display broc's config items", False)
        Log.colorprint("DEFAULT", "    help       : Print the help commands", False)
        return 0

    if subcommand == "build" or subcommand == "test":
        if subcommand == "build":
            Log.colorprint("DEFAULT", "build: Builds the specified targets", False)
        else:
            Log.colorprint("DEFAULT", "test: Builds and runs the specified targets", False)
        Log.colorprint("DEFAULT", "Usage: %s %s [option] <path>" % (bin_name, subcommand), False)
        Log.colorprint("DEFAULT", "Valid options:", False)
        Log.colorprint("DEFAULT",
            "\t--mode=[release|debug]  : Set build mode, default mode is debug",
            False)
        Log.colorprint("DEFAULT",
            "\t--jobs=num\t\t: Set the number of build threads",
            False)
        Log.colorprint("DEFAULT", "\t --all-log\t\t: Show all build log infomation", False)
        Log.colorprint("DEFAULT", "\t --auto-includet\t: Add include directory of dependent modules", False)
        Log.colorprint("DEFAULT", "\t --auto-lib\t\t: Add static library files of dependent modules", False)
        return 0

    if subcommand == "show-deps":
        Log.colorprint("DEFAULT", "show-deps: Print the dependency graph", False)
        Log.colorprint("DEFAULT", "Usage: %s %s <path>" % (bin_name, subcommand), False)
        return 0

    if subcommand == "clean":
        Log.colorprint("DEFAULT", "clean: Remove output files", False)
        Log.colorprint("DEFAULT", "Usage: %s clean" % (bin_name), False)
        return 0

    if subcommand == "scratch":
        Log.colorprint("DEFAULT", "scratch: Create a BROC template", False)
        Log.colorprint("DEFAULT", "Usage: %s scratch" % (bin_name), False)
        return 0

    if subcommand == "version":
        Log.colorprint("DEFAULT", "version: Display the version", False)
        Log.colorprint("DEFAULT", "Usage: %s version" % (bin_name), False)
        return 0

    if subcommand == "help":
        Log.colorprint("DEFAULT", "help: Print the for commands", False)
        Log.colorprint("DEFAULT", "Usage: %s help <subcommand>" % (bin_name), False)
        return 0
    
    Log.colorprint("DEFAULT", "%s unknow commmand" % subcommand, False)
    return 0


def OptionBuild(argv):
    """
    Get build or test options.
    Args:
        argv : command line argv
    Return:
        None : fail
        options : build or test options
        options["all_log"] : show all build log
        options["mode"] : debug or release
        options["path"] : modular path
        options["jobs"] : the number of build threads
        options["auto_include"] : add directory include of dependent modules automatically
        options["auto_lib"] : add .a files of dependent modules automatically
    """
    options = dict()
    options["all_log"] = False
    options["path"] = ""
    options["mode"] = "debug"
    options["jobs"] = 4
    options["auto_include"] = False
    options["auto_lib"] = False

    try:
        opts, args = getopt.gnu_getopt(argv, "", ["all-log", "mode=", "jobs="])
    except getopt.GetoptError as ex:
        Log.colorprint("DEFAULT", "%s\nType '%s help' for usage" % \
                (str(ex), os.path.basename(sys.argv[0])), False)
        return None

    if len(args) <= 0:
        options["path"] = os.getcwd()
    elif len(args) == 1:
        options["path"] = args[0]
    else:
        Log.colorprint("RED", "invalid arguments %s\nType '%s help' for usage" % \
                (str(args), os.path.basename(sys.argv[0])), False)
        return None
    
    for opt, arg in opts:
        if opt == "--all-log":
            options["all_log"] = True
            continue
        if opt == "--mode":
            if arg != "debug" and arg != "release":
                Log.colorprint("RED", "invalid mode %s. Please use debug or release" % arg, False)
                return None
            options["mode"] = arg
            continue
        if opt == "--jobs":
            options["jobs"] = int(arg)
            continue
        if opt == "--auto-inlcude":
            options["auto_include"] = True
            continue
        if opt == "--auto-lib":
            options["auto_lib"] = True
            continue
        return None

    return options


if __name__ == "__main__":
    Help('xxxx', 'build')
