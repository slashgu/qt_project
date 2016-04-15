__author__ = 'chenggu'

import os
import time
from git import Repo
join = os.path.join

# A repo object provides high-level access to your data
repo = Repo('/Users/chenggu/myQt/')

commits = list(repo.iter_commits())
print commits