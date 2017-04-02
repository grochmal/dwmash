#!/usr/bin/env python3

import sys, os, configparser
from getopt import getopt, GetoptError
from collections import OrderedDict
import logging as lg

from . import config


config = configparser.ConfigParser(dict_type=OrderedDict)


def dwmash():
    pass


def dwmash_util():
    pass


def cmd_line():
    usage_args = '[-hv] [-c <config>] <matches.csv> <input.csv> [<output.csv>]'
    usage = ' '.join([sys.argv[0], usage_args])
    try:
        opts, args = getopt(sys.argv[1:], 'hvc:')
    except GetoptError as e:
        print(e)
        print(usage)
        sys.exit(1)
    configfd = '~/.fstitch.ini'
    verbose = 0
    out_file = None
    for o, a in opts:
        if '-h' == o:
            print(usage)
            sys.exit(0)
        elif '-v' == o:
            verbose += 1
        elif '-c' == o:
            configfd = a
        else:
            assert False, o + ': unhandled option'
    format = '%(asctime)s:%(levelname)s:%(funcName)s:%(message)s'
    if 0 >= verbose:
        lg.basicConfig(format=format, level=lg.WARNING)
    elif 1 == verbose:
        lg.basicConfig(format=format, level=lg.INFO)
    elif 1 < verbose:
        lg.basicConfig(format=format, level=lg.DEBUG)
    if 2 > len(args):
        print(usage)
        sys.exit(1)
    matchfd = args[0]
    inputfd = args[1]
    if 2 < len(args):
        out_file = args[2]
    def readable(f):
        if os.path.isfile(f) and os.access(f, os.R_OK):
            return True
        print(f, ': bas permissions on (does it exist?)')
        return False
    if not all(map(readable, [configfd, matchfd, inputfd])):
        sys.exit(1)
    try:
        config.read(configfd)
    except configparser.MissingSectionHeaderError as e:
        print(e)
        print(configfd, ': does not appear to be an INI file')
    except configparser.ParsingError as e:
        print(e)
        print(configfd, ': cannot be parsed')
    if out_file:
        try:
            outfpt = open(out_file, 'w')
            lg.info('Output will go to: %s', out_file)
        except Exception as e:
            print(e)
            sys.exit(1)
    lg.info('Config: %s, Match %s, Input %s', configfd, matchfd, inputfd)
    loader(matchfd, inputfd)


if '__main__' == __name__:
    # hack to be able to inject the program state into an interactive session
    if 'ipython' == sys.argv[0]:
        arg = sys.argv.pop(0)
        while '--' != arg and 1 < len(sys.argv):
            arg = sys.argv.pop(0)
    main()

