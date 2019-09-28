import os
import glob
os.chdir("/Users/binggangliu")
for file in glob.glob("*.csv"):
    print(file)
