from git import Repo
import os

dirfile = os.path.abspath('./') # code的文件位置，我默认将其存放在根目录下
repo = Repo(dirfile)

for i in range(2):
    os.system("echo 1 >> \"a.txt\"")
    g = repo.git
    g.add("--all")
    g.commit("-m test-1")
    g.push()
    print("Successful push!")
