from bs4 import BeautifulSoup
import os

fo = open('TableMSPath.txt', 'r')
path = fo.readline()
print(path)
file = path
print(file)
var1 = open(file)
xml = BeautifulSoup(var1, 'xml')
fo.close()

# for lst in xml.findAll('table',{'id':'UnderwritingRules'}):
#       print(lst)
