#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
PATENTS = "ipgb20060117.xml"

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def split_file(filename):
   

    output = []
    data = {}
    
    result = {}

    f = open(filename)
    print(filename)
    count = 0
    file_number = 0

    # import pprint
    # pprint.pprint(f.readlines())


    output.append(f.readline())

    for line in f.readlines():

        if line.startswith("<?xml"):
            data["ipgb20060117.xml-{}".format(file_number)] = output



            root = ET.fromstringlist(output)
            # print ""
            # print root.tag
            # print root.attrib
            #
            # for child in root:
            #     print(child.tag, child.attrib)

            tree = ET.ElementTree(root)
            tree.write("\ipgb20060117.xml-{}".format(file_number), encoding = 'UTF-8')
            output = []
            file_number += 1
        output.append(line)


    data["\ipgb20060117.xml-{}".format(file_number)] = output
    root = ET.fromstringlist(output)
    tree = ET.ElementTree(root)
    tree.write("\ipgb20060117.xml-{}".format(file_number), encoding = 'UTF-8')

    #import pprint
    #pprint.pprint(data)
    # return data
    pass


def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print ("You have not split the file {} in the correct boundary!".format(fname))
            f.close()
        except:
            print ("Could not find file {}. Check if the filename is correct!".format(fname))
    print ("Passed.")


test()
