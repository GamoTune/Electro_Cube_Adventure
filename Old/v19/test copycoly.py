#test copycoly
import shutil
import os
import distutils.dir_util

cwd = os.getcwd()
cwd = cwd.replace("\\", "/" )
cwd = cwd+str("/")

originalPath = str(cwd)+"assets/data/editeur/monde2"
copyPath = str(cwd)+"assets/data/solo/monde2"

shutil.copytree(originalPath, copyPath)