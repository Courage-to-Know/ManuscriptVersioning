import xml.etree.ElementTree as ET
import os
fo = open('TableMSPath.txt', 'r')

path = fo.readline()
print(path)
file1 = path
tree = ET.parse(file1)
root = tree.getroot()
lst = root.findall('model/object/table')
x = 1
if x == 1:
    ID = []
    for item in lst:
        id1 = item.get('id')
        ID.append(id1)
    print(ID)

fo.close()


