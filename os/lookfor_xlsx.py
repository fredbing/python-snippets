import os
import glob
os.chdir("/Users/binggangliu")
for file in glob.glob("*.xlsx"):
    print(file)
