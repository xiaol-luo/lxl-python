

import sys
import os


search_dirs = sys.argv[1:]

for dir_path in search_dirs:
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            file_path = os.path.abspath(os.path.join(root, f)).replace('\\', '/')
            if not file_path.endswith(".meta"):
                continue
            with open(file_path, 'r') as f:
                f.readline()
                line_content = f.readline()
                guid = line_content[6:].strip(" \n")
                # print(file_path)
                ret = "<Asset Guid=\"{0}\" AssetBundleName=\"ui_card2\" />".format(guid)
                print(ret)
