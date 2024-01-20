import os
import sys

BIG_FILE_NAME = "bigFile.tsv"

def sqrRoot(val):
    sqrRt = 1
    while sqrRt*sqrRt < val:
        sqrRt+=1
    sqrRt -= 1
    return sqrRt
def divideBigFile(bigFileName):
    with open(bigFileName,'r') as bigFile:
        bigFileLines = bigFile.readlines()
        size = len(bigFileLines)
        cnt = sqrRoot(size)
        i=0
        for i in range(cnt+1):
            filename = bigFileLines[cnt*i][:-1].replace("\t","_") + ".tsv"
            with open('subfiles/'+filename,'w+') as file:
                k = i*cnt
                while k < (i+1)*cnt:
                    file.write(bigFileLines[k])
                    k+=1
        if i*(cnt+1) < size:
            k=i*(cnt+1)
            filename = bigFileLines[k][:-1].replace("\t","_") + ".tsv"
            with open('subfiles/'+filename,'w+') as file:
                while k < size:
                    file.write(bigFileLines[k])
                    k+=1
def incLetter(letters, index):
    if letters[index]=='a':
        letters[index]='b'
    elif letters[index]=='b':
        letters[index]='c'
def createBigSortedTestFile():
    letters = ['a','a','a','a','a','a']
    with open(BIG_FILE_NAME,'w+') as bigFile:
        for i in range(1,3**6):
            for j in range(6):
                if i%(3**(5-j)) == 0:
                    incLetter(letters,j)
                    k=j+1
                    while k<6:
                        letters[k] = 'a'
                        k+=1
                    break
            line = "".join(letters[:3]) + "\t" + "".join(letters[3:]) + "\t" + str(i) + "\n"
            bigFile.write(line)

def getSearchStr(str1,str2):
    finalStr = "FAULT"
    if len(str1) > 3:
        print("Invalid str1 value")
        return ""
    elif len(str1) < 3 and len(str2) > 0:
        print("Invalid str1 value")
        return ""
    if len(str2) > 3:
        print("Invalid str2 value")
        return ""
    if len(str1) < 3:
        finalStr = str1
    else:
        finalStr = str1+"_"+str2
    return finalStr

def searchStartFile(flList, start, end, srcStr):
    if end - start < 2:
        if srcStr <= flList[start][:len(srcStr)]:
            return start-1
        else:
            return start
    mid = (end+start)//2
    if srcStr <= flList[mid][:len(srcStr)]:
        return searchStartFile(flList,start,mid, srcStr)
    else:
        return searchStartFile(flList,mid,end, srcStr)
def searchEndFile(flList, start, srcStr):
    end = start
    while srcStr >= flList[end][:len(srcStr)]:
        end +=1
    return end
def searchFile(flList, srcStr):
    start = searchStartFile(flList,0,len(flList),srcStr)
    end = searchEndFile(flList,start,srcStr)
    while start < end:
        with open("subfiles/"+flList[start],'r') as file:
            fileLines = file.readlines()
            if fileLines[-1][:len(srcStr)] < srcStr:
                start += 1
            else:
                break
    while end > start:
        with open("subfiles/"+flList[end],'r') as file:
            fileLines = file.readlines()
            if fileLines[0][:len(srcStr)] >srcStr:
                end-=1
            else:
                break
    return (start,end)

def searchInLines(lines,start,end, srcStr):
    if(end-start<2):
        if lines[start][:len(srcStr)] == srcStr:
            return start
        elif lines[start+1][:len(srcStr)] == srcStr:
            return start+1
        else:
            return -1
    mid = (start+end)//2
    if lines[mid][:len(srcStr)] == srcStr:
        return mid
    elif lines[mid][:len(srcStr)] < srcStr:
        return searchInLines(lines,mid,end,srcStr)
    else:
        return searchInLines(lines,start,mid,srcStr)
    
def searchInFile(filename, srcStr,foundList):
    with open("subfiles/"+filename, 'r') as file:
        fileLines = file.readlines()
        foundLine = searchInLines(fileLines,0,len(fileLines),srcStr)
        if foundLine == -1:
            return
        else:
            iter = foundLine
            while fileLines[iter][:len(srcStr)] == srcStr:
                foundList.append(fileLines[iter])
                iter-=1
                if iter == -1:
                    break
            iter = foundLine+1
            if iter == len(fileLines):
                return
            while fileLines[iter][:len(srcStr)] == srcStr:
                foundList.append(fileLines[iter])
                iter+=1
                if iter == len(fileLines):
                    break

def searchStr(str1,str2):
    srcStr = getSearchStr(str1,str2)
    if srcStr == "":
        print("INVALID INPUT")
        return
    srcStr = srcStr.replace("_","\t")
    fileList = os.listdir("subfiles/")
    fileList.sort()
    (startFlInd,endFlInd) = searchFile(fileList, srcStr)
    flInd = startFlInd
    foundList = []
    while flInd <= endFlInd:
        searchInFile(fileList[flInd], srcStr, foundList)
        flInd+=1
    foundList.sort()
    for fn in foundList:
        print(fn)

def start():
    if sys.argv[1] == "divide":
        divideBigFile(sys.argv[2])
    else:
        searchStr(sys.argv[1],sys.argv[2])


start()