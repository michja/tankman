#!/usr/bin/python

import os
import sys
import argparse
from mako.template import Template

file = "local.mak"


def template_to_string(file):
    string = ""
    with open(file, 'r') as f:
        string = f.read()
    return string


def exec_path():
    return os.path.realpath(os.getcwd())


def file_exists(file):
    return os.path.isfile(file)


def make_local_mak(**kwargs):
    name = kwargs['name'] if ('name' in kwargs and kwargs['name']) else os.path.basename(exec_path())
    url = kwargs['url'] if ('url' in kwargs and kwargs['url']) else raw_input("URL?: ")
    input = "{}/{}.mako".format(
        os.path.dirname(os.path.realpath(__file__)),
        file
    )

    # does the output file exist already?
    output = "{}/{}".format(exec_path(), file)
    if (file_exists(output) and
            raw_input("Overwrite {}? y/N: ".format(output)).upper() != "Y"):
        print "operation halted at user request"
        exit()

    template = template_to_string(input)
    template = Template(template).render(site=name, url=url)
    with open(output, 'w') as f:
        f.write(template)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a local.mak file')
    parser.add_argument('-n', '--name')
    parser.add_argument('-u', '--url')
    args = parser.parse_args()
    # name = sys.argv[1] if (len(sys.argv) > 1) else False
    make_local_mak(name=args.name, url=args.url)
