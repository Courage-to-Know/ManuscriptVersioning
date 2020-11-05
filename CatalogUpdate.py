import lxml as lxml

oldVersion = fo.readline()
path = fo.readline()
newVersion = fo.readline()
nBDate = fo.readline()
rNDate = fo.readline()
print(oldVersion)
print(path)
print(newVersion)
print(nBDate)
print(rNDate)


data = fo.readlines()
print(data)
data[1] =
for line in data[1]:
    a = line.strip()
    data1 = fo.readline()
    print(data1)
fo.close()





include_dirs = lxml.get_include() + [find_libxml2_include()]

import os
import fnmatch
import shutil
import datetime
import copy
import xml.etree.ElementTree as ET
from UserInput import userInput
# pip install django==3.0
#pip install libxml2-python3
#pip install django-import-data
#pip install -U pip wheel setuptools
#manage.py runserver

userInput()

os.remove('TableMSPath.txt')


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
                catalogPath = os.path.join(root, name)
                print(catalogPath)
                Check1: bool = os.path.exists(catalogPath)
                if Check1:
                    print('YES')
                    from UserInput import userInput
                    from xml.etree import ElementTree as R
                    tree1 = R.parse(catalogPath)
                    Root1 = tree1.getroot()
                    # print(Root.attrib)
                    items = root.findall("entry")
                    for item in items:
                        if item.get('ID') == :
                            # print("Y")
                            # member1 = root.find(.//entry[@line = question1]
                            member1 = copy.deepcopy(item)

                            # if question2 == "Y":
                            member1.set("description", user_input2)
                            # if question3 == "Y" and X == 1:
                            member1.set("versionDate", user_input3)
                            # if question4 == "Y":
                            member1.set("versionID", user_input4)
                            # if question5 == "Y" and Y == 1:
                            member1.set("effectiveDateNew", user_input5)
                            # if question6 == "Y" and Z == 1:
                            member1.set("effectiveDateRenewal", user_input6)

                            root.append(member1)
                            print(member1)
                            # print(item.get('Line'))
                        # print(element.attrib)
                        # ET.dump(entry)
                tree1.write(catalogPath)
    return result


find('ManuScriptCatalog.xml', 'C:\Program Files')
