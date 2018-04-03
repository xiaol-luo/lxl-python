from cppluabind.parse import do_parse
import os
import sys
import argparse


def main():
    curr_dir = os.path.dirname(__file__)
    file_path = os.path.abspath(os.path.join(curr_dir, "data/heads.h"))
    include_dir = os.path.abspath(os.path.join(curr_dir, "data")).replace('\\', '/')
    do_parse(file_path, 
        ['-x', 'c++', '-std=c++11', '-D__CODE_GENERATOR__', "-I{0}".format(include_dir)], 
        {
            os.path.abspath(os.path.join(include_dir, "AutoBind/AutoHead.h")).replace('\\', '/'),
            #os.path.abspath(os.path.join(include_dir, "AutoBind/AutoHeadOther.h")).replace('\\', '/'),
        },
        curr_dir)

if __name__ == "__main__":
    main()