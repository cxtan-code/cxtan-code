#!/usr/bin/python

import sys
import os
import time
git_list = {
        "git_add":"git add ",
        "git_commit":"git commit -m ",
        "git_push":"git push -u origin master",
        "git_pull":"git pull"
        }
if __name__ == '__main__':
    local_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    print local_time
    for cmd in sys.argv:
        os.system(git_list["git_add"] + cmd)
        os.system(git_list["git_commit"] + local_time)
    os.system(git_list["git_push"])
    pass































