import os

CURR_DIR = os.path.curdir
REPOS_DIR = os.path.join(CURR_DIR,'repos')
GIT_ROOT = os.path.join(REPOS_DIR, 'git')
CC_ROOT = os.path.join(REPOS_DIR, 'cc')
FILE_TYPES = ['cpp','h','c','gpj']
PROJECTS = {
    'common':[os.path.join(GIT_ROOT,'common_files'),os.path.join(CC_ROOT,'common_files_view')],
    'prj2':['git_root','cc_root'],
}


def getCRC(file):
    sum = 0
    with open(file, 'r') as f:
        data = f.read()
        for chr in data:
            sum += ord(chr)
    return sum

def calculateCrcInRepo(repo_root, crc_of):
    for root, dirs, files in os.walk(repo_root):
        for file in files:
            if file.split('.')[-1] in FILE_TYPES:
                if file not in crc_of.keys():
                    crc_of[file] = []
                crc_of[file].append(getCRC(os.path.join(root,file)))

def getDiffFilesInPrj(prj):
    diff_files = []
    git_root = PROJECTS[prj][0]
    cc_root = PROJECTS[prj][1]
    if not os.path.exists(git_root) or not os.path.exists(cc_root):
        print('given roots in PROJECTS NOT exist for '+prj)
        return diff_files
    crc_of = {'temp':[]}
    calculateCrcInRepo(git_root, crc_of)
    calculateCrcInRepo(cc_root,crc_of)
    for file in crc_of.keys():
        if len(crc_of[file]) == 2:
            if crc_of[file][0] != crc_of[file][1]:
                diff_files.append(file)
    diff_files.sort()
    return diff_files

def printDiffFiles(diff_files_of):
    for prj in diff_files_of.keys():
        if len(diff_files_of[prj]) > 0:
            print('-----------------------')
            print('--------'+prj+'--------')
            for file in diff_files_of[prj]:
                print(file)

def getDiffFiles():
    diff_files_of = {'temp':[]}
    for prj in PROJECTS:
        if prj not in diff_files_of.keys():
            diff_files_of[prj] = getDiffFilesInPrj(prj)
    
    printDiffFiles(diff_files_of)

getDiffFiles()
