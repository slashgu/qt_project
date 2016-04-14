__author__ = 'chenggu'

import os
import time
from git import Repo
join = os.path.join

# A repo object provides high-level access to your data
repo = Repo('/Users/chenggu/myQt/')

# index = repo.index
# print repo.head.commit.parents

headCommit = repo.head.commit

# headCommit = headCommit.parents[0].parents[0].parents[0]
# commitTime = headCommit.committed_date
# print time.asctime(time.gmtime(commitTime))

tree = headCommit.tree

# file_count = 0
# tree_count = 0
# for item in tree.traverse():
#     file_count += item.type == 'blob'
#     tree_count += item.type == 'tree'

