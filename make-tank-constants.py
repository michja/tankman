#!/usr/bin/python

import os
import sys
from mako.template import Template

file = "tank_constants.php"

def template_to_string(file):
    string = ""
    with open(file, 'r') as f:
        string = f.read()
    return string


def exec_path():
    return os.path.realpath(os.getcwd())


def file_exists(file):
    return os.path.isfile(file)


def make_tank_constants(name=False):
    name = name if (name) else os.path.basename(exec_path())
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
    template = Template(template).render(site=name)
    with open(output, 'w') as f:
        f.write(template)


if __name__ == "__main__":
    name = sys.argv[1] if (len(sys.argv) > 1) else False
    make_tank_constants(name)
