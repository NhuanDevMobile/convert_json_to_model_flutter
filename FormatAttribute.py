import numpy as np
import re
import datetime
import os
def FormatAttribute(arr):
    # readFile = open("FileAttribute.txt","r",encoding="UTF-8")
    arr = arr
    result = []
    try:
        for i in arr:
            find1 = i.find(":")
            sub1 = i[:find1].lower()
            res1 = re.findall(r'"([^"]*)"', sub1)
            find1 = [pos for pos, char in enumerate(res1[0]) if char == "_"]
            str = res1[0]
            for a in find1:
                fromReplace = res1[0][a:a+2]
                toReplace = res1[0][a+1:a+2].upper()
                str = str.replace(fromReplace, toReplace)
                # res1[0].replace()
            # attri2 = res[sub2-1:sub2]
            result.append(str)
            print(str)
    except:
        print("123")
    return result
def FormatAttributeUp(arr):
    # readFile = open("FileAttribute.txt","r",encoding="UTF-8")
    arr = arr
    result = []
    try:
        for i in arr:
            find1 = i.find(":")
            sub1 = i[:find1]
            res1 = re.findall(r'"([^"]*)"', sub1)
            print(res1)
            result.append(res1[0])
            print(str)
    except:
        print("123")
    return result
def FormatModel(arr,title):
    # readFile = open("FileAttribute.txt","r",encoding="UTF-8")
    arr = arr
    result = []
    if(title != ''):
        result.append("class " +title+"{")

    print(len(arr))
    resAttribute = FormatAttribute(arr)
    try:
        for i in range(0, len(arr)):
            print(resAttribute[i])
            find1 = arr[i].find(":")
            sub1 = (arr[i][find1+1:len(arr[i])-2].lower()).replace(' ','')
            checkInt = sub1.isdigit()
            checkID = resAttribute[i][len(resAttribute[i])-2 : len(resAttribute[i])]
            print(checkID)
            if checkInt == True:
                result.append("int? "+resAttribute[i]+";")
            elif  checkInt == False and checkID == "Id":
                result.append("int? " + resAttribute[i] + ";")
            elif  checkInt == False and sub1 == "true":
                result.append("bool? " + resAttribute[i] + ";")
            else:
                result.append("String? " + resAttribute[i] + ";")
        print(len(resAttribute[i]- 3))
        if (title != ''):
            result.append("}")
    except:
        print("err")
    return result
def FormatSuper(arr):
    # readFile = open("FileAttribute.txt","r",encoding="UTF-8")
    arr = arr
    result = []
    try:
        for i in arr:
            find1 = i.find(":")
            sub1 = i[:find1].lower()
            res1 = re.findall(r'"([^"]*)"', sub1)
            find1 = [pos for pos, char in enumerate(res1[0]) if char == "_"]
            str = res1[0]
            for a in find1:
                fromReplace = res1[0][a:a + 2]
                toReplace = res1[0][a + 1:a + 2].upper()
                str = str.replace(fromReplace, toReplace)
                # res1[0].replace()
            # attri2 = res[sub2-1:sub2]
            result.append(str +": "+str+",")
            print(str)
    except:
        print("123")
    return result
def FormatJson(arr):
    # readFile = open("FileAttribute.txt","r",encoding="UTF-8")
    arr = arr
    result = []
    print(len(arr))
    resJson = FormatAttributeUp(arr)
    resAttribute = FormatAttribute(arr)
    print(len(resJson))
    print(len(resAttribute))
    try:
        for i in range(0, len(arr)):
            # print(resAttribute[i]+": (json['"+resJson[i]+"'] as double? ?? -1.0).toInt(),")
            find1 = arr[i].find(":")
            sub1 = (arr[i][find1 + 1:len(arr[i]) - 2].lower()).replace(' ', '')
            checkInt = sub1.isdigit()
            checkID = resAttribute[i][len(resAttribute[i]) - 2: len(resAttribute[i])]
            print(checkID)
            if checkInt == True:
                result.append(resAttribute[i]+": (json['"+resJson[i]+"'] as double? ?? -1.0).toInt(),")
            elif checkInt == False and checkID == "Id":
                result.append(resAttribute[i] + ": (json['" + resJson[i] + "'] as double? ?? -1.0).toInt(),")
            elif checkInt == False and sub1 == "true":
                result.append(resAttribute[i] + ": json['" + resJson[i] + "'] as bool? ?? false,")
            else:
                result.append(resAttribute[i] + ": json['" + resJson[i] + "'] as String? ?? '',")
    except:
        print("err")
    return result

def FormatJson1(arr, title):
    # readFile = open("FileAttribute.txt","r",encoding="UTF-8")
    arr = arr
    result = []
    if(title != ''):
        result.append(title+".fromJson(dynamic json) {")
    print(len(arr))
    resJson = FormatAttributeUp(arr)
    resAttribute = FormatAttribute(arr)
    print(len(resJson))
    print(len(resAttribute))
    try:
        for i in range(0, len(arr)):
            # print(resAttribute[i]+": (json['"+resJson[i]+"'] as double? ?? -1.0).toInt(),")
            find1 = arr[i].find(":")
            sub1 = (arr[i][find1 + 1:len(arr[i]) - 2].lower()).replace(' ', '')
            checkInt = sub1.isdigit()
            checkID = resAttribute[i][len(resAttribute[i]) - 2: len(resAttribute[i])]
            print(checkID)
            if checkInt == True:
                result.append(resAttribute[i]+" = json['"+resJson[i]+"'] ?? 0;")
            elif checkInt == False and checkID == "Id":
                result.append(resAttribute[i] + " = json['" + resJson[i] + "'] ?? 0;")
            elif checkInt == False and sub1 == "true":
                result.append(resAttribute[i] + " = json['" + resJson[i] + "'] ?? false;")
            else:
                result.append(resAttribute[i] + " = json['" + resJson[i] + "'] ?? '';")
        if (title != ''):
            result.append("}")
    except:
        print("err")
    return result
def FormatToJson(arr):
    # readFile = open("FileAttribute.txt","r",encoding="UTF-8")
    arr = arr
    result = []
    result.append(" Map<String, dynamic> toJson() {")
    result.append(" final map = <String, dynamic>{};")
    print(len(arr))
    resJson = FormatAttributeUp(arr)
    resAttribute = FormatAttribute(arr)
    print(len(resJson))
    print(len(resAttribute))
    try:
        for i in range(0, len(arr)):
            # print(resAttribute[i]+": (json['"+resJson[i]+"'] as double? ?? -1.0).toInt(),")
            find1 = arr[i].find(":")
            sub1 = (arr[i][find1 + 1:len(arr[i]) - 2].lower()).replace(' ', '')
            checkInt = sub1.isdigit()
            checkID = resAttribute[i][len(resAttribute[i]) - 2: len(resAttribute[i])]
            print(checkID)
            result.append("map['" + resJson[i] + "'] = " +resAttribute[i] +";")

        result.append(" return map;")
        result.append("}")

    except:
        print("err")

    return result
def FormatFinal(arr):
    # readFile = open("FileAttribute.txt","r",encoding="UTF-8")
    arr = arr
    result = []
    print(len(arr))
    resAttribute = FormatAttribute(arr)
    try:
        for i in range(0, len(arr)):
            print(resAttribute[i])
            find1 = arr[i].find(":")
            sub1 = (arr[i][find1+1:len(arr[i])-2].lower()).replace(' ','')
            checkInt = sub1.isdigit()
            checkID = resAttribute[i][len(resAttribute[i])-2 : len(resAttribute[i])]
            print(checkID)
            if checkInt == True:
                result.append("final int? "+resAttribute[i]+";")
            elif  checkInt == False and checkID == "Id":
                result.append("final int? " + resAttribute[i] + ";")
            elif  checkInt == False and sub1 == "true":
                result.append("final bool? " + resAttribute[i] + ";")
            else:
                result.append("final String? " + resAttribute[i] + ";")
        print(len(resAttribute[i]- 3))

    except:
        print("err")
    return result
def FormatThis(arr, title):
    # readFile = open("FileAttribute.txt","r",encoding="UTF-8")
    arr = arr
    result = []
    if (title != ""):
        result.append(title +"({")
    try:
        for i in arr:
            find1 = i.find(":")
            sub1 = i[:find1].lower()
            res1 = re.findall(r'"([^"]*)"', sub1)
            find1 = [pos for pos, char in enumerate(res1[0]) if char == "_"]
            str = res1[0]
            for a in find1:
                fromReplace = res1[0][a:a+2]
                toReplace = res1[0][a+1:a+2].upper()
                str = str.replace(fromReplace, toReplace)
                # res1[0].replace()
            # attri2 = res[sub2-1:sub2]
            result.append('this.'+str+',')
            print(str)
        if (title != ""):
            result.append("});")
    except:
        print("123")
    return result

def FormatRequiredThis(arr):
    # readFile = open("FileAttribute.txt","r",encoding="UTF-8")
    arr = arr
    result = []
    try:
        for i in arr:
            find1 = i.find(":")
            sub1 = i[:find1].lower()
            res1 = re.findall(r'"([^"]*)"', sub1)
            find1 = [pos for pos, char in enumerate(res1[0]) if char == "_"]
            str = res1[0]
            for a in find1:
                fromReplace = res1[0][a:a+2]
                toReplace = res1[0][a+1:a+2].upper()
                str = str.replace(fromReplace, toReplace)
                # res1[0].replace()
            # attri2 = res[sub2-1:sub2]
            result.append('required this.'+str+',')
            print(str)
    except:
        print("123")
    return result
def FormatAttributeCT(arr):
    # readFile = open("FileAttribute.txt","r",encoding="UTF-8")
    arr = arr
    result = []
    try:
        for i in arr:
            find1 = i.find(":")
            sub1 = i[:find1].lower()
            res1 = re.findall(r'"([^"]*)"', sub1)
            find1 = [pos for pos, char in enumerate(res1[0]) if char == "_"]
            str = res1[0]
            for a in find1:
                fromReplace = res1[0][a:a+2]
                toReplace = res1[0][a+1:a+2].upper()
                str = str.replace(fromReplace, toReplace)
                # res1[0].replace()
            # attri2 = res[sub2-1:sub2]
            result.append(str+"!,")
            print(str)
    except:
        print("123")
    return result

def FormatHoaThuong(arr):
    # readFile = open("FileAttribute.txt","r",encoding="UTF-8")
    arr = arr
    result = []
    try:
        for i in arr:
            sub1 = i.lower()
            # res1 = re.findall(r'"([^"]*)"', sub1)
            find1 = [pos for pos, char in enumerate(sub1) if char == "_"]
            str = sub1
            for a in find1:
                fromReplace = sub1[a:a+2]
                toReplace = sub1[a+1:a+2].upper()
                str = str.replace(fromReplace, toReplace)
                # res1[0].replace()
            # attri2 = res[sub2-1:sub2]
            result.append(str)
            print(str)
    except:
        print("123")
    return result
def AutoModel(arr, title):
    # readFile = open("FileAttribute.txt","r",encoding="UTF-8")
    arr = arr
    result = []
    if (title != ''):
        result.append("class " + title + "{")

    print(len(arr))
    resAttribute = FormatAttribute(arr)
    try:
        for i in range(0, len(arr)):
            print(resAttribute[i])
            find1 = arr[i].find(":")
            sub1 = (arr[i][find1 + 1:len(arr[i]) - 2].lower()).replace(' ', '')
            checkInt = sub1.isdigit()
            checkID = resAttribute[i][len(resAttribute[i]) - 2: len(resAttribute[i])]
            if checkInt == True:
                result.append("int? " + resAttribute[i] + ";")
            elif checkInt == False and checkID == "Id":
                result.append("int? " + resAttribute[i] + ";")
            elif checkInt == False and sub1 == "true":
                result.append("bool? " + resAttribute[i] + ";")
            else:
                result.append("String? " + resAttribute[i] + ";")
        if(title != ''):
            result1 = FormatThis(arr, title)
            result += result1
            result2 = FormatJson1(arr, title)
            result += result2
            result3 = FormatToJson(arr)
            result += result3
            result.append("}")
    except:
        print("error")
    return result
