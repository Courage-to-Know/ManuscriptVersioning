import os
import fnmatch
import shutil
import datetime
import copy
import xml.etree.ElementTree as ET


def userInput():
    fo = open('Raj.txt', 'r')
    n = 1
    oldVersion = fo.readline()
    oldVersion = oldVersion[:-n]
    path = fo.readline()
    path = path[:-n]
    newVersion = fo.readline()
    newVersion = newVersion[:-n]
    nBDate = fo.readline()
    nBDate = nBDate[:-n]
    rNDate = fo.readline()
    rNDate = rNDate[:-n]
    # print(oldVersion)
    # print(path)
    # print(newVersion)
    # print(nBDate)
    # print(rNDate)
    fo.close()

    VersionFormat = oldVersion
    VersionFormat1 = oldVersion + ".xml"
    # print(VersionFormat1)
    MsPath = path
    # print(MsPath)
    FilePath = os.path.join(MsPath, VersionFormat1)
    # path check if file exists
    Check: bool = os.path.exists(FilePath)
    pathCheck = 0
    if Check:
        print("Hurray!Manuscript found in the given path.")
        VersionFormatNew = newVersion
        VersionFormatNew1 = VersionFormatNew + ".xml"
        FilePathNew = os.path.join(MsPath, VersionFormatNew1)
        print("Path of the Manuscript to be versioned:" + FilePathNew)
        pathCheck = 1

    else:
        print(
            "Sorry no Manuscript found in the given path" + MsPath + " with the name " + VersionFormat)

    if pathCheck == 1:

        effectiveDate = nBDate
        versionCaption = VersionFormatNew.replace('_', ' ')
        versionID = (versionCaption[-7:])
        version = versionID.replace(' ','.')
        if pathCheck == 1:

            try:
                datetime.datetime.strptime(effectiveDate, '%Y-%m-%d')
                X = 1
                if X == 1:
                    renewalDate = rNDate
                    try:
                        datetime.datetime.strptime(renewalDate, '%Y-%m-%d')
                        Y = 1
                        if X == 1 & Y == 1:
                            src = FilePath
                            des = FilePathNew
                            shutil.copy(src, des)

                        tree = ET.parse(FilePathNew)
                        Root = tree.getroot()
                        element = Root.findall('properties')
                        for iD in element:
                            iD.set("manuscriptID", VersionFormatNew)
                        for viD in element:
                            viD.set("versionID", VersionFormatNew)
                        for caption in element:
                            caption.set("caption", versionCaption)
                        for nBDate in element:
                            nBDate.set('versionDate', effectiveDate)
                        items = Root.findall('properties/keys/keyInfo')
                        for item in items:
                            if item.get('name') == "effectiveDateNew":
                                item.set("value", effectiveDate)
                            if item.get('name') == "effectiveDateRenewal":
                                item.set("value", renewalDate)
                            if item.get('name') == "version":
                                item.set("value", version)
                        tree.write(FilePathNew)
                        print("New version Manuscript created " + VersionFormatNew1 + " in the path:" + FilePathNew)

                        f = open('TableMSPath.txt', 'w')
                        f.write(FilePathNew)
                        f.close()

                    except ValueError:
                        print("Incorrect data format, should be YYYY-MM-DD")
                    Y = 0
            except ValueError:
                print("Incorrect data format, should be YYYY-MM-DD")

    def find(pattern, path):
        result = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
                    catalogPath = os.path.join(root, name)
                    print(catalogPath)
                    Check1: bool = os.path.exists(catalogPath)
                    if Check1 & pathCheck:
                        print("Manuscript Catalog update is in progress....")

                        from xml.etree import ElementTree as R
                        tree1 = R.parse(catalogPath)
                        Root1 = tree1.getroot()
                        # print(Root.attrib)
                        items1 = Root1.findall("entry")
                        for item1 in items1:
                            if item1.get('ID') == VersionFormat:
                                # print(item1)
                                # member1 = root.find(.//entry[@line = question1]
                                member1 = copy.deepcopy(item1)
                                # print(member1)

                                # if question2 == "Y":
                                member1.set("ID", VersionFormatNew)
                                member1.set("description", versionCaption)
                                # if question3 == "Y" and X == 1:
                                member1.set("versionDate", effectiveDate)
                                # if question4 == "Y":
                                member1.set("versionID", VersionFormatNew)
                                # if question5 == "Y" and Y == 1:
                                member1.set("effectiveDateNew", effectiveDate)
                                # if question6 == "Y" and Z == 1:
                                member1.set("effectiveDateRenewal", renewalDate)
                                member1.set("version", version)

                                Root1.append(member1)
                                # print(member1)
                                # print(item.get('Line'))
                            # print(element.attrib)
                            # ET.dump(entry)
                            tree1.write(catalogPath)
                            VersionStatus = 1

                        print("Manuscript Version is complete.")

        return result

    find('ManuScriptCatalog.xml', 'C:\Program Files')


userInput()

# def CheckPath():
#  Check: bool = os.path.exists(FilePath)
# If
# Check = bool(True)
# print('Manuscript found')
# return ()
# print("Manuscript to be versioned:" + FilePath)
# OldVersion = input('Which Manuscript do you want to version?')
# print(OldVersion)
# MsPath = input("Please provide the path of the Manuscript:")
# print(MsPath)
# FilePath = MsPath + "\\" + OldVersion
