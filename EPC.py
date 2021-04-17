from git import Repo
import os

dirfile = os.path.abspath('') # code的文件位置，我默认将其存放在根目录下
repo = Repo(dirfile)

for i in range(500):
    g = repo.git
    g.add("--all")
    g.commit("-m ")
    g.push()
    print("Successful push!")
