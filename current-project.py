#!/usr/bin/python

import os
import sys
import subprocess
import json

filename = "{}/current-project.json".format(os.path.dirname(os.path.realpath(__file__)))
if not os.path.isfile(filename):
    exit("no file")


def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


def get_json():
    with open(filename, "r") as json_file:
        data = byteify(json.loads(json_file.read()))
    return data


def write_json(data):
    with open(filename, "w") as json_file:
        json.dump(data, json_file)


def get(field):
    json_data = get_json()
    return json_data['project'][field] if 'project' in json_data and field in json_data['project'] else False


def write(field, data):
    json_data = get_json()
    json_data['project'][field] = data
    write_json(json_data)
    refresh_widget()


def update(name):
    data = get_json()
    data['project']['name'] = name
    write_json(data)
    refresh_widget()


def refresh_widget():
    subprocess.Popen("xfce4-panel --plugin-event=genmon-9:refresh:bool:true", shell=True)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        write('name', sys.argv[1])
    txt = get('directory')
    xml = "<img>/home/michael/Pictures/icons/code-white.png</img><txt>  {}</txt>"
    print xml.format(txt) if txt else False
    # print current_project()
