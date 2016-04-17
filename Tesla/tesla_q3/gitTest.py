__author__ = 'chenggu'

import os
import re
import subprocess
import time
from git import Repo
join = os.path.join

# A repo object provides high-level access to your data
repo = Repo('/Users/chenggu/myQt/')
# print len(list(repo.iter_commits()))

master = repo.head.reference
# print isinstance(repo.git.log(since = "2.weeks"), str)
list = repo.git.log(oneline = True, graph = True, pretty = "%h %s %cd").split('\n')
levelIndicator = ['*', '|', '\\', '/']
reGitInfo = re.compile('[*\s|\\/]+([0-9a-zA-Z]+)\s([0-9a-zA-Z\_\s]+?)\s([a-zA-Z0-9\s:]+)')

count = 0
subprocess.Popen(['python', 'gitTest.py'])

for item in list:
    # level = 0
    # for i in levelIndicator:
    #     level += str(item).count(i)
    # print str(item) + " ---- level: " + str(level)
    print str(item)
    count += 1
    # print isinstance(item, unicode)
    # if reGitInfo.match(str(item)):
        # count += 1
        # print reGitInfo.match(str(item)).groups()
print count