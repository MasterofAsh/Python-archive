import shutil
import os

shutil.copy("testcopyDay87.txt", "testcopy2Day87.txt")
shutil.copytree("JunkFolderDay87", "testcopy2Day87.txt")
shutil.move("JunkFolderDay87", "testcopyDay87.txt")
shutil.rmtree("JunkFolderDay87")
os.remove("testcopyDay87.txt")