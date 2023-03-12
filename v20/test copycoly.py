#test copycoly
import shutil
import os
import distutils.dir_util

cwd = os.getcwd()
cwd = cwd.replace("\\", "/" )
cwd = cwd+str("/")

originalPath = str(cwd)+"assets/data/origine"
copyPath = str(cwd)+"assets/data/solo/"
if os.path.exists(copyPath):
    shutil.rmtree(copyPath)
shutil.copytree(originalPath, copyPath)